import glob
import re
import subprocess

for file in glob.glob("*.html"):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace any $ ... \begin{pmatrix} ... $ with \[ ... \]
    # This catches things like $A = \begin{pmatrix}...\end{pmatrix}$
    
    # We do this carefully. If it starts with $ and contains \begin{vmatrix} or pmatrix, up to the next $, replace with \[ \]
    content = re.sub(r'\$([^$]*?\\begin\{(p|v)matrix\}.*?\\end\{(p|v)matrix\}[^$]*?)\$', r'\\[\1\\]', content, flags=re.DOTALL)
    
    # Also fix any remaining malformed ones like $A = \begin{pmatrix}...\end{pmatrix}\]
    # which might have been caused by previous script
    content = re.sub(r'\$([^$]*?\\begin\{(p|v)matrix\}.*?\\end\{(p|v)matrix\}[^$]*?)\\\]', r'\\[\1\\]', content, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

subprocess.run(['git', 'add', '.'], check=True)
subprocess.run(['git', 'commit', '-m', 'Fix broken MathJax inline syntax where matrices were cut off'], check=True)
subprocess.run(['git', 'push', 'origin', 'main'], check=True)
print("Matrix MathJax fixed and pushed!")
