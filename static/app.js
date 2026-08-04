(() => {
  const body = document.body;
  const menuButton = document.querySelector('#menu-button');
  const backdrop = document.querySelector('#sidebar-backdrop');
  const progress = document.querySelector('#reading-progress');
  const article = document.querySelector('#book-content');

  const closeMenu = () => {
    body.classList.remove('menu-open');
    menuButton?.setAttribute('aria-expanded', 'false');
  };

  menuButton?.addEventListener('click', () => {
    const isOpen = body.classList.toggle('menu-open');
    menuButton.setAttribute('aria-expanded', String(isOpen));
  });
  backdrop?.addEventListener('click', closeMenu);
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') closeMenu();
  });

  const updateProgress = () => {
    if (!article || !progress) return;
    const articleTop = article.offsetTop;
    const distance = article.offsetHeight - window.innerHeight;
    const percentage = distance > 0
      ? Math.min(100, Math.max(0, ((window.scrollY - articleTop) / distance) * 100))
      : 100;
    progress.style.width = `${percentage}%`;
  };

  updateProgress();
  window.addEventListener('scroll', updateProgress, { passive: true });
  window.addEventListener('resize', updateProgress);

  const tocLinks = [...document.querySelectorAll('.toc a[href^="#"]')];
  const linksById = new Map(tocLinks.map((link) => [decodeURIComponent(link.hash.slice(1)), link]));
  const headings = [...document.querySelectorAll('.book-content h2[id], .book-content h3[id]')];

  if ('IntersectionObserver' in window && headings.length) {
    const observer = new IntersectionObserver((entries) => {
      const visible = entries.filter((entry) => entry.isIntersecting).at(-1);
      if (!visible) return;
      tocLinks.forEach((link) => link.classList.remove('current-section'));
      linksById.get(visible.target.id)?.classList.add('current-section');
    }, { rootMargin: '-15% 0px -72% 0px' });
    headings.forEach((heading) => observer.observe(heading));
  }
})();
