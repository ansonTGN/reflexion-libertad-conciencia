(() => {
  const root = document.documentElement;
  const themeBtn = document.getElementById('theme-toggle');
  const storedTheme = (() => { try { return localStorage.getItem('lectura-theme'); } catch { return null; } })();
  const preferredDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const initialTheme = storedTheme === 'light' || storedTheme === 'dark' ? storedTheme : (preferredDark ? 'dark' : 'light');
  function setTheme(theme) {
    root.dataset.theme = theme;
    if (themeBtn) {
      themeBtn.setAttribute('aria-label', theme === 'dark' ? 'Activar tema claro' : 'Activar tema oscuro');
      themeBtn.setAttribute('aria-pressed', String(theme === 'dark'));
      themeBtn.textContent = theme === 'dark' ? '☀ Tema claro' : '☾ Tema oscuro';
    }
  }
  setTheme(initialTheme);
  themeBtn?.addEventListener('click', () => {
    const theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
    setTheme(theme);
    try { localStorage.setItem('lectura-theme', theme); } catch {}
  });
  const progress = document.getElementById('reading-progress');
  const updateProgress = () => {
    const doc = document.documentElement;
    const max = doc.scrollHeight - innerHeight;
    const value = max > 0 ? (scrollY / max) * 100 : 0;
    if (progress) progress.style.width = `${Math.min(100, Math.max(0, value))}%`;
  };
  addEventListener('scroll', updateProgress, { passive: true });
  addEventListener('resize', updateProgress);
  updateProgress();
  const copyBtn = document.getElementById('copy-link');
  copyBtn?.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(location.href);
      copyBtn.textContent = '✓ Enlace copiado';
      setTimeout(() => { copyBtn.textContent = '↗ Compartir'; }, 2200);
    } catch { window.prompt('Copia este enlace:', location.href); }
  });
})();
