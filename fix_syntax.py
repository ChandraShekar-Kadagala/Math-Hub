import glob
import re
import subprocess

for file in glob.glob("*.html"):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Use regex to find $ \begin{vmatrix} ... \end{vmatrix} $ and replace with \[ ... \]
    # Also for pmatrix
    content = re.sub(r'\$(\s*\\begin\{vmatrix\}.*?\\end\{vmatrix\}\s*)\$', r'\\[\1\\]', content, flags=re.DOTALL)
    content = re.sub(r'\$(\s*\\begin\{pmatrix\}.*?\\end\{pmatrix\}\s*)\$', r'\\[\1\\]', content, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

subprocess.run(['git', 'add', '.'], check=True)
subprocess.run(['git', 'commit', '-m', 'Fix MathJax syntax errors for matrices by ensuring display mode'], check=True)
subprocess.run(['git', 'push', 'origin', 'main'], check=True)
print("Syntax fixed and pushed!")
