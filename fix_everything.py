import os
import glob

# 1. Fix app.js
app_js_path = 'app.js'
with open(app_js_path, 'a', encoding='utf-8') as f:
    f.write("\n\n// Mobile Sidebar Toggle\n")
    f.write("document.addEventListener('DOMContentLoaded', () => {\n")
    f.write("    const menuBtn = document.getElementById('menu-btn');\n")
    f.write("    const sidebar = document.querySelector('.sidebar');\n")
    f.write("    if(menuBtn && sidebar) {\n")
    f.write("        menuBtn.addEventListener('click', () => {\n")
    f.write("            sidebar.classList.toggle('open');\n")
    f.write("        });\n")
    f.write("    }\n")
    f.write("});\n")

# 2. Fix styles.css
styles_path = 'styles.css'
with open(styles_path, 'r', encoding='utf-8') as f:
    styles = f.read()

# Add z-index to sidebar and menu button display block to media query
styles = styles.replace('.sidebar { transform: translateX(-280px); transition: transform 0.3s; }',
                        '.sidebar { transform: translateX(-280px); transition: transform 0.3s; z-index: 1000; box-shadow: 10px 0 30px rgba(0,0,0,0.5); }\n  #menu-btn { display: inline-block !important; }')
with open(styles_path, 'w', encoding='utf-8') as f:
    f.write(styles)

# 3. Fix HTML files
for file in glob.glob("*.html"):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add Menu Button
    btn_str = '<button class="theme-btn" id="theme-btn">☀️ Light Mode</button>'
    menu_btn = '<button class="menu-btn" id="menu-btn" style="margin-left:10px; background:var(--surface2); color:var(--text); border:1px solid var(--border); padding:0.55rem 1rem; border-radius:99px; font-weight:600; cursor:pointer; display:none;">☰ Menu</button>'
    if 'menu-btn' not in content:
        content = content.replace(btn_str, btn_str + '\n    ' + menu_btn)
        # Some files might have spaces:
        content = content.replace('<button class="theme-btn" id="theme-btn">☀️  Light Mode</button>', '<button class="theme-btn" id="theme-btn">☀️ Light Mode</button>\n    ' + menu_btn)

    # Fix index.html broken links
    if file == 'index.html':
        content = content.replace('<li><a href="practice.html">🎯&nbsp;&nbsp;Assignment Q1–Q12</a></li>', '<li><a href="practice.html">🎯&nbsp;&nbsp;Unit 1 &amp; 2 Practice</a></li>')
        content = content.replace('<li><a href="u1_practice.html">🏋️&nbsp;&nbsp;Unit 1 Practice Sheet</a></li>', '')
        content = content.replace('<li><a href="u2_practice.html">🏋️&nbsp;&nbsp;Unit 2 Practice Sheet</a></li>', '<li><a href="assignment.html">🚀&nbsp;&nbsp;ODE Assignment</a></li>')
        
    # Potential MathJax Syntax Fixes:
    # Change \begin{vmatrix} ... \end{vmatrix} inside $...$ to \[...\]
    content = content.replace('$\begin{vmatrix}', '\\[\\begin{vmatrix}')
    content = content.replace('\end{vmatrix}$', '\\end{vmatrix}\\]')
    
    # Change \begin{pmatrix} ... \end{pmatrix} inside $...$ to \[...\]
    content = content.replace('$\\begin{pmatrix}', '\\[\\begin{pmatrix}')
    content = content.replace('\\end{pmatrix}$', '\\end{pmatrix}\\]')
    
    # Fix Wronskian in assignment.html specifically
    content = content.replace('$W(y_1, y_2) = \\begin{vmatrix} x & x e^x \\\\ 1 & e^x + x e^x \\end{vmatrix} = x(e^x + x e^x) - x e^x = x e^x + x^2 e^x - x e^x = x^2 e^x$.',
                              '\\[ W(y_1, y_2) = \\begin{vmatrix} x & x e^x \\\\ 1 & e^x + x e^x \\end{vmatrix} = x^2 e^x \\]')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

# Now, commit to git and push
import subprocess
subprocess.run(['git', 'add', '.'], check=True)
subprocess.run(['git', 'commit', '-m', 'Fix mobile layout, resolve index.html links, and improve MathJax matrix syntax'], check=True)
subprocess.run(['git', 'push', 'origin', 'main'], check=True)

print("All fixes applied, committed, and pushed successfully!")
