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


// Mobile Sidebar Toggle
document.addEventListener('DOMContentLoaded', () => {
    const menuBtn = document.getElementById('menu-btn');
    const sidebar = document.querySelector('.sidebar');
    if(menuBtn && sidebar) {
        menuBtn.addEventListener('click', () => {
            sidebar.classList.toggle('open');
        });
    }
});

// ── 30-Year Expert Level JS Upgrades ──

document.addEventListener('DOMContentLoaded', () => {
    // 1. Scroll to Top
    const fab = document.createElement('button');
    fab.className = 'fab';
    fab.innerHTML = '↑';
    document.body.appendChild(fab);
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) fab.classList.add('visible');
        else fab.classList.remove('visible');
    });
    
    fab.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    // 2. Active Recall Mode
    const activeRecallBtn = document.getElementById('recall-btn');
    if(activeRecallBtn) {
        let recallMode = localStorage.getItem('recallMode') === 'true';
        
        const updateRecallUI = () => {
            if(recallMode) {
                document.body.classList.add('active-recall-mode');
                activeRecallBtn.innerHTML = '🧠 Recall: ON';
                activeRecallBtn.style.background = 'var(--accent)';
                activeRecallBtn.style.color = 'white';
            } else {
                document.body.classList.remove('active-recall-mode');
                activeRecallBtn.innerHTML = '🧠 Recall: OFF';
                activeRecallBtn.style.background = 'var(--surface2)';
                activeRecallBtn.style.color = 'var(--text)';
            }
        };
        
        updateRecallUI();
        
        activeRecallBtn.addEventListener('click', () => {
            recallMode = !recallMode;
            localStorage.setItem('recallMode', recallMode);
            updateRecallUI();
        });
        
        // Reveal on click
        document.querySelectorAll('.qa-body').forEach(body => {
            body.addEventListener('click', () => {
                if(document.body.classList.contains('active-recall-mode')) {
                    body.classList.add('revealed');
                }
            });
        });
    }

    // 3. Pomodoro Timer
    const minDisplay = document.getElementById('t-min');
    const secDisplay = document.getElementById('t-sec');
    const playBtn = document.getElementById('t-play');
    const resetBtn = document.getElementById('t-reset');
    
    if(minDisplay && secDisplay && playBtn && resetBtn) {
        let timeLeft = 25 * 60;
        let timerId = null;
        let isRunning = false;
        
        const updateTimerUI = () => {
            const m = Math.floor(timeLeft / 60).toString().padStart(2, '0');
            const s = (timeLeft % 60).toString().padStart(2, '0');
            minDisplay.textContent = m;
            secDisplay.textContent = s;
        };
        
        playBtn.addEventListener('click', () => {
            if(isRunning) {
                clearInterval(timerId);
                playBtn.textContent = '▶️';
            } else {
                playBtn.textContent = '⏸️';
                timerId = setInterval(() => {
                    if(timeLeft > 0) {
                        timeLeft--;
                        updateTimerUI();
                    } else {
                        clearInterval(timerId);
                        alert("Pomodoro Session Complete! Take a 5 minute break.");
                        playBtn.textContent = '▶️';
                        isRunning = false;
                    }
                }, 1000);
            }
            isRunning = !isRunning;
        });
        
        resetBtn.addEventListener('click', () => {
            clearInterval(timerId);
            isRunning = false;
            timeLeft = 25 * 60;
            updateTimerUI();
            playBtn.textContent = '▶️';
        });
    }
});
