from __future__ import annotations

import os
import re
from dataclasses import dataclass
from pathlib import Path

import markdown
from flask import Flask, abort, redirect, render_template, send_from_directory, url_for


BASE_DIR = Path(__file__).resolve().parent
BOOK_DIR = BASE_DIR / "MATERIAL_CURSOS" / "Libro"
URL_PREFIX = "/libro_ds_ia"
CHAPTER_PATTERN = re.compile(r"^Capitulo_(\d+)_")
MARKDOWN_LINK_PATTERN = re.compile(
    r"(?P<prefix>\]\()(?P<target>(?:\./)?[^\s()]+)\.md(?P<anchor>#[^\s()]*)?\)"
)
IMAGE_PATTERN = re.compile(
    r"(?P<prefix>!\[[^]]*\]\()(?P<path>(?:\./)?imagenes/[^)\s]+)(?P<suffix>\))"
)
PLACEHOLDER_PATTERN = re.compile(r"<([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑ0-9_]*)>")

app = Flask(__name__, static_url_path=f"{URL_PREFIX}/static")


@dataclass(frozen=True)
class Document:
    slug: str
    title: str
    nav_title: str
    path: Path
    kind: str


def document_sort_key(path: Path) -> tuple[int, int, str]:
    if path.stem == "00_Indice":
        return (0, 0, path.name)

    chapter_match = CHAPTER_PATTERN.match(path.stem)
    if chapter_match:
        return (1, int(chapter_match.group(1)), path.name)
    if path.stem == "Laboratorios_integradores":
        return (2, 0, path.name)
    if path.stem == "Apendices":
        return (3, 0, path.name)
    return (4, 0, path.name)


def is_book_document(path: Path) -> bool:
    return (
        path.stem == "00_Indice"
        or CHAPTER_PATTERN.match(path.stem) is not None
        or path.stem == "Laboratorios_integradores"
        or path.stem == "Apendices"
        or path.stem.startswith("Apendice_")
    )


def extract_title(path: Path) -> str:
    with path.open(encoding="utf-8") as source:
        for line in source:
            if line.startswith("# "):
                return line[2:].strip()
    return path.stem.replace("_", " ")


def discover_documents() -> list[Document]:
    paths = sorted(
        (path for path in BOOK_DIR.glob("*.md") if is_book_document(path)),
        key=document_sort_key,
    )
    documents = []
    for path in paths:
        chapter_match = CHAPTER_PATTERN.match(path.stem)
        if chapter_match:
            kind = "chapter"
        elif path.stem == "00_Indice":
            kind = "index"
        else:
            kind = "supplement"
        title = extract_title(path)
        nav_title = re.sub(r"^Cap[ií]tulo \d+\.\s*", "", title, flags=re.IGNORECASE)
        documents.append(Document(path.stem, title, nav_title, path, kind))
    return documents


def prepare_markdown(source: str) -> str:
    def replace_link(match: re.Match[str]) -> str:
        slug = Path(match.group("target")).name
        anchor = match.group("anchor") or ""
        return f'{match.group("prefix")}{URL_PREFIX}/capitulo/{slug}{anchor})'

    source = MARKDOWN_LINK_PATTERN.sub(replace_link, source)
    source = IMAGE_PATTERN.sub(
        lambda match: (
            f'{match.group("prefix")}{URL_PREFIX}/media/'
            f'{match.group("path").removeprefix("./")}{match.group("suffix")}'
        ),
        source,
    )
    # Markdown treats placeholders such as <URL> as empty HTML elements.
    return PLACEHOLDER_PATTERN.sub(r"&lt;\1&gt;", source)


def render_markdown(path: Path) -> tuple[str, str]:
    renderer = markdown.Markdown(
        extensions=[
            "extra",
            "sane_lists",
            "toc",
            "pymdownx.arithmatex",
        ],
        extension_configs={
            "toc": {"permalink": True, "toc_depth": "2-3"},
            "pymdownx.arithmatex": {"generic": True},
        },
        output_format="html5",
    )
    html = renderer.convert(prepare_markdown(path.read_text(encoding="utf-8")))
    return html, renderer.toc


@app.get("/")
def root():
    return redirect(url_for("home"))


@app.get(f"{URL_PREFIX}/")
def home():
    return redirect(url_for("show_document", slug="00_Indice"))


@app.get(f"{URL_PREFIX}/capitulo/<slug>")
def show_document(slug: str):
    documents = discover_documents()
    position = next(
        (index for index, document in enumerate(documents) if document.slug == slug),
        None,
    )
    if position is None:
        abort(404)

    current = documents[position]
    content, chapter_toc = render_markdown(current.path)
    response = app.make_response(
        render_template(
            "book.html",
            documents=documents,
            current=current,
            content=content,
            chapter_toc=chapter_toc,
            previous=documents[position - 1] if position > 0 else None,
            following=documents[position + 1] if position + 1 < len(documents) else None,
        )
    )
    response.headers["Cache-Control"] = "no-store, max-age=0"
    return response


@app.get(f"{URL_PREFIX}/media/<path:asset_path>")
def book_media(asset_path: str):
    if not asset_path.startswith("imagenes/"):
        abort(404)
    response = send_from_directory(BOOK_DIR, asset_path, conditional=True)
    response.headers["Cache-Control"] = "no-cache"
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "7000")))
