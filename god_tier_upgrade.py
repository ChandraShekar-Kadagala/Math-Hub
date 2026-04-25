import os
import glob
import subprocess

# 1. Update CSS
css_additions = """
/* ── God-Tier UI Polish ── */
::selection { background: var(--accent); color: white; }

body, .sidebar, .card, .qa-block, .topbar {
  transition: background-color 0.4s ease, border-color 0.4s ease, color 0.4s ease !important;
}

/* In-Page Search Bar */
.search-container {
  padding: 0 1.5rem 1rem;
}
.search-input {
  width: 100%;
  padding: 0.6rem 1rem;
  border-radius: 8px;
  border: 1px solid var(--border);
  background: var(--surface2);
  color: var(--text);
  font-family: inherit;
  font-size: 0.85rem;
  transition: all 0.2s;
}
.search-input:focus {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 2px rgba(124,109,250,0.25);
}

/* Highlight matches */
.highlight {
  background-color: rgba(255, 235, 59, 0.4);
  border-radius: 3px;
}
[data-theme="light"] .highlight {
  background-color: rgba(255, 235, 59, 0.8);
}
"""

with open('styles.css', 'a', encoding='utf-8') as f:
    f.write(css_additions)

# 2. Add Search HTML to Sidebar
search_html = """
  <div class="search-container">
    <input type="text" id="page-search" class="search-input" placeholder="Search page (Press '/')">
  </div>
"""

for file in glob.glob("*.html"):
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
        
    if 'search-container' not in html:
        # Insert search box after sidebar logo
        html = html.replace('</p></div>', '</p></div>\n' + search_html)
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

# 3. Update app.js for Search, Confetti, and Keyboard shortcuts
js_additions = """
// ── God-Tier JS Upgrades ──

document.addEventListener('DOMContentLoaded', () => {
    // 1. In-Page Search Filtering
    const searchInput = document.getElementById('page-search');
    const searchTargets = document.querySelectorAll('.card, .qa-block');
    
    if (searchInput && searchTargets.length > 0) {
        searchInput.addEventListener('input', (e) => {
            const query = e.target.value.toLowerCase().trim();
            
            searchTargets.forEach(target => {
                const text = target.innerText.toLowerCase();
                if (query === '' || text.includes(query)) {
                    target.style.display = '';
                } else {
                    target.style.display = 'none';
                }
            });
        });
        
        // Shortcut '/' to focus search
        document.addEventListener('keydown', (e) => {
            if (e.key === '/' && document.activeElement !== searchInput) {
                e.preventDefault();
                searchInput.focus();
                // Open sidebar on mobile if hidden
                const sidebar = document.querySelector('.sidebar');
                if(window.innerWidth <= 900 && sidebar && !sidebar.classList.contains('open')) {
                    sidebar.classList.add('open');
                }
            } else if (e.key === 'Escape' && document.activeElement === searchInput) {
                searchInput.value = '';
                searchInput.blur();
                searchInput.dispatchEvent(new Event('input')); // trigger reset
            }
        });
    }

    // 2. Confetti on 100% Progress
    const TOTAL_TOPICS = 40; // Assuming max topics across all pages
    const currentProgress = JSON.parse(localStorage.getItem('math-hub-progress') || '{}');
    const doneCount = Object.values(currentProgress).filter(Boolean).length;
    
    // Add listener to checkboxes to trigger confetti exactly when hitting 100%
    document.querySelectorAll('.syllabus-check').forEach(cb => {
        cb.addEventListener('change', () => {
            // Recalculate dynamically
            const prog = JSON.parse(localStorage.getItem('math-hub-progress') || '{}');
            const done = Object.values(prog).filter(Boolean).length;
            if (cb.checked && done >= TOTAL_TOPICS) {
                triggerConfetti();
            }
        });
    });
});

function triggerConfetti() {
    // Load canvas-confetti dynamically if not loaded
    if (!window.confetti) {
        const script = document.createElement('script');
        script.src = 'https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js';
        script.onload = shootConfetti;
        document.body.appendChild(script);
    } else {
        shootConfetti();
    }
}

function shootConfetti() {
    var duration = 3000;
    var end = Date.now() + duration;

    (function frame() {
        confetti({
            particleCount: 5,
            angle: 60,
            spread: 55,
            origin: { x: 0 },
            colors: ['#7c6dfa', '#38bdf8', '#22d3a0']
        });
        confetti({
            particleCount: 5,
            angle: 120,
            spread: 55,
            origin: { x: 1 },
            colors: ['#7c6dfa', '#38bdf8', '#22d3a0']
        });

        if (Date.now() < end) {
            requestAnimationFrame(frame);
        }
    }());
}
"""

with open('app.js', 'a', encoding='utf-8') as f:
    f.write(js_additions)

# 4. Commit and Push
subprocess.run(['git', 'add', '.'], check=True)
subprocess.run(['git', 'commit', '-m', 'Add God-Tier UI/UX: In-page search, keyboard shortcuts, smooth transitions, and confetti rewards'], check=True)
subprocess.run(['git', 'push', 'origin', 'main'], check=True)

print("God-Tier Upgrade Complete!")
