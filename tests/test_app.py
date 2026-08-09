import unittest
from pathlib import Path

from app import BASE_DIR, BOOK_DIR, app, discover_documents


class BookAppTestCase(unittest.TestCase):
    def setUp(self):
        app.config.update(TESTING=True)
        self.client = app.test_client()

    def test_root_redirects_to_book_entrypoint(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.location.endswith("/libro_ds_ia/"))

    def test_book_directory_uses_material_courses(self):
        self.assertEqual(
            BOOK_DIR.relative_to(BASE_DIR), Path("MATERIAL_CURSOS") / "Libro"
        )
        self.assertTrue(BOOK_DIR.is_dir())

    def test_book_entrypoint_redirects_to_index(self):
        response = self.client.get("/libro_ds_ia/")
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.location.endswith("/libro_ds_ia/capitulo/00_Indice"))

    def test_chapter_is_rendered_with_math_and_navigation(self):
        response = self.client.get(
            "/libro_ds_ia/capitulo/Capitulo_05_Probabilidad_incertidumbre_e_inferencia_bayesiana"
        )
        page = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('class="arithmatex"', page)
        self.assertIn("MathJax", page)
        self.assertIn(
            "/libro_ds_ia/media/imagenes/distribuciones_probabilidad.png", page
        )
        self.assertIn("/libro_ds_ia/static/styles.css", page)
        self.assertEqual(response.headers["Cache-Control"], "no-store, max-age=0")

    def test_first_chapter_formulas_are_rendered_as_math(self):
        response = self.client.get(
            "/libro_ds_ia/capitulo/Capitulo_01_Ciencia_de_Datos_e_IA"
        )
        page = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(page.count('class="arithmatex"'), 30)
        self.assertIn(r"\operatorname*{arg\,min}_{\theta}", page)
        self.assertIn(r"\prod_{t=2}^{T}", page)
        self.assertNotIn("<code>a_t = pi(h_t)</code>", page)

    def test_second_chapter_metric_notation_is_rendered_as_math(self):
        response = self.client.get(
            "/libro_ds_ia/capitulo/Capitulo_02_Ciclo_de_vida_de_un_proyecto_de_datos"
        )
        page = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(r"\operatorname{Precision@12}", page)
        self.assertIn(r"\operatorname{Recall@12}", page)
        self.assertNotIn("<code>precision@12</code>", page)

    def test_internal_markdown_links_use_application_routes(self):
        response = self.client.get("/libro_ds_ia/capitulo/00_Indice")
        page = response.get_data(as_text=True)
        self.assertIn(
            "/libro_ds_ia/capitulo/Capitulo_01_Ciencia_de_Datos_e_IA", page
        )
        self.assertNotIn("Capitulo_01_Ciencia_de_Datos_e_IA.md", page)

    def test_unknown_document_returns_404(self):
        self.assertEqual(
            self.client.get("/libro_ds_ia/capitulo/no-existe").status_code, 404
        )

    def test_media_route_only_exposes_book_images(self):
        response = self.client.get(
            "/libro_ds_ia/media/imagenes/ciclo_vida_datos.png"
        )
        self.assertEqual(response.status_code, 200)
        response.close()
        self.assertEqual(
            self.client.get("/libro_ds_ia/media/README.md").status_code, 404
        )

    def test_book_documents_are_discovered_in_order(self):
        documents = discover_documents()
        self.assertEqual(documents[0].slug, "00_Indice")
        self.assertEqual(documents[1].slug, "Capitulo_01_Ciencia_de_Datos_e_IA")
        self.assertGreaterEqual(len(documents), 20)


if __name__ == "__main__":
    unittest.main()
