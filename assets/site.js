(() => {
  'use strict';
  const root = document.documentElement;
  const body = document.body;
  const phrase = key => body.dataset[key] || '';
  const switcher = document.getElementById('language-select');
  switcher?.addEventListener('change', () => {
    const suffix = location.hash || '';
    location.assign(switcher.value + suffix);
  });
  const themeBtn = document.getElementById('theme-toggle');
  const storedTheme = (() => { try { return localStorage.getItem('lectura-theme'); } catch { return null; } })();
  const preferredDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const initialTheme = storedTheme === 'light' || storedTheme === 'dark' ? storedTheme : (preferredDark ? 'dark' : 'light');
  function setTheme(theme) {
    root.dataset.theme = theme;
    if (themeBtn) {
      themeBtn.setAttribute('aria-label', theme === 'dark' ? phrase('light') : phrase('dark'));
      themeBtn.setAttribute('aria-pressed', String(theme === 'dark'));
      themeBtn.textContent = (theme === 'dark' ? '☀ ' + phrase('light') : '☾ ' + phrase('dark'));
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
  addEventListener('scroll', updateProgress, {passive:true});
  addEventListener('resize', updateProgress);
  updateProgress();
  const copyBtn = document.getElementById('copy-link');
  copyBtn?.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(location.href);
      copyBtn.textContent = '✓ ' + phrase('copy');
      setTimeout(() => { copyBtn.textContent = '↗ ' + phrase('share'); }, 2200);
    } catch { window.prompt(phrase('copyPrompt'), location.href); }
  });
})();
