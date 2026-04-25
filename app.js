document.addEventListener('DOMContentLoaded', () => {

  /* ─── Theme ─── */
  const themeBtn = document.getElementById('theme-btn');
  const savedTheme = localStorage.getItem('math-hub-theme') || 'dark';
  document.documentElement.setAttribute('data-theme', savedTheme);
  updateThemeBtn(savedTheme);

  themeBtn?.addEventListener('click', () => {
    const next = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('math-hub-theme', next);
    updateThemeBtn(next);
  });

  function updateThemeBtn(t) {
    if (themeBtn) themeBtn.textContent = t === 'dark' ? '☀️ Light Mode' : '🌙 Dark Mode';
  }

  /* ─── Navigation (multi-page) ─── */
  const page = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links li').forEach(li => {
    const href = li.querySelector('a')?.getAttribute('href');
    li.classList.toggle('active', href === page);
  });

  /* ─── Progress Tracker ─── */
  const TOTAL_TOPICS = 40;
  const fillEl  = document.getElementById('overall-progress');
  const textEl  = document.getElementById('progress-text');
  const resetEl = document.getElementById('reset-progress');

  let progress = JSON.parse(localStorage.getItem('math-hub-progress') || '{}');

  function renderProgress() {
    const done = Object.values(progress).filter(Boolean).length;
    const pct  = Math.min(100, Math.round(done / TOTAL_TOPICS * 100));
    if (fillEl) fillEl.style.width = pct + '%';
    if (textEl) {
      textEl.textContent = pct < 100 ? `${done}/${TOTAL_TOPICS} topics done` : '🎉 Exam Ready!';
      textEl.style.color = pct === 100 ? '#22d3a0' : '';
    }
  }

  document.querySelectorAll('.syllabus-check').forEach(cb => {
    const id = cb.dataset.id;
    if (progress[id]) cb.checked = true;
    cb.addEventListener('change', () => {
      progress[id] = cb.checked;
      localStorage.setItem('math-hub-progress', JSON.stringify(progress));
      renderProgress();
    });
  });

  resetEl?.addEventListener('click', () => {
    localStorage.removeItem('math-hub-progress');
    progress = {};
    document.querySelectorAll('.syllabus-check').forEach(cb => cb.checked = false);
    renderProgress();
  });

  renderProgress();
});
