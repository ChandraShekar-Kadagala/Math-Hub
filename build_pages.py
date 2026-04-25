import os

def write_html(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

# Base template
def get_base(title, active_page, body_content):
    return f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | MAT 223 Hub</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700;800&display=swap" rel="stylesheet">
<script>MathJax={{tex:{{inlineMath:[['$','$'], ['\\\\(','\\\\)']],displayMath:[['\\\\[','\\\\]']]}},options:{{skipHtmlTags:['script','noscript','style','textarea']}}}}</script>
<script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
<link rel="stylesheet" href="styles.css">
<style>
.main {{ width: calc(100% - var(--sidebar-w)); overflow-x: hidden; }}
@media (max-width: 900px) {{ .main {{ width: 100%; }} }}
mjx-container {{ overflow-x: auto; overflow-y: hidden; max-width: 100%; display: block; }}
</style>
</head>
<body>
<nav class="sidebar">
  <div class="sidebar-logo"><h1>MAT 223 Hub</h1><p>Engineering Mathematics Sem 2</p></div>
  <div class="nav-section-label">Units</div>
  <ul class="nav-links">
    <li class="{'active' if active_page == 'index' else ''}"><a href="index.html">🏠 Home &amp; Overview</a></li>
    <li class="{'active' if active_page == 'unit1' else ''}"><a href="unit1.html">📐 Unit 1 — Linear Algebra</a></li>
    <li class="{'active' if active_page == 'unit2' else ''}"><a href="unit2.html">🔄 Unit 2 — Transformations</a></li>
    <li class="{'active' if active_page == 'unit3' else ''}"><a href="unit3.html">📘 Unit 3 — First Order ODE</a></li>
    <li class="{'active' if active_page == 'unit4' else ''}"><a href="unit4.html">📕 Unit 4 — Higher Order ODE</a></li>
  </ul>
  <div class="nav-section-label">Practice</div>
  <ul class="nav-links">
    <li class="{'active' if active_page == 'cla1' else ''}"><a href="cla1.html">📝 CLA I Solutions</a></li>
    <li class="{'active' if active_page == 'practice' else ''}"><a href="practice.html">🎯 Practice &amp; Assignment</a></li>
  </ul>
  <div class="progress-widget">
    <p>📊 Global Progress</p>
    <div class="progress-bar"><div class="progress-fill" id="overall-progress"></div></div>
    <span id="progress-text">0/40 topics done</span>
    <button class="reset-btn" id="reset-progress">Reset Progress</button>
  </div>
</nav>
<div class="main">
  <div class="topbar">
    <div><h2>{title}</h2></div>
    <button class="theme-btn" id="theme-btn">☀️ Light Mode</button>
  </div>
  <div class="page-content">
{body_content}
  </div>
</div>
<script src="app.js"></script>
</body>
</html>"""

unit1_content = """
    <div class="section-label">Unit 1</div>
    <h1 class="page-title"><span>Linear Algebra</span> Foundations</h1>
    <p class="page-subtitle">Comprehensive coverage of Matrices, Systems, Determinants, and Vector Spaces.</p>

    <div class="section-label">1. Matrices & Properties</div>
    <div class="card">
        <div class="card-title">📦 Algebraic Properties & Special Types</div>
        <p><strong>Diagonal:</strong> $a_{ij} = 0$ for $i \\neq j$. <strong>Scalar:</strong> Diagonal with $a_{ii} = k$. <strong>Identity ($I$):</strong> Scalar with $k=1$.</p>
        <p><strong>Upper/Lower Triangular:</strong> $a_{ij} = 0$ for $i > j$ / $i < j$.</p>
        <p><strong>Symmetric:</strong> $A^T = A$. <strong>Skew-Symmetric:</strong> $A^T = -A$ (diagonals must be 0).</p>
        <p><strong>Idempotent:</strong> $A^2 = A$. <strong>Nilpotent:</strong> $A^k = 0$. <strong>Involutory:</strong> $A^2 = I$. <strong>Orthogonal:</strong> $A^T A = I$.</p>
        <div class="formula">
            <strong>Transpose Properties:</strong> $(A^T)^T = A$, $(A+B)^T = A^T+B^T$, $(AB)^T = B^TA^T$
        </div>
        <div class="check-item"><input type="checkbox" class="syllabus-check" data-id="u1-1"><label>Mastered Special Types of Matrices</label></div>
        <div class="check-item"><input type="checkbox" class="syllabus-check" data-id="u1-2"><label>Mastered Algebraic Properties</label></div>
    </div>

    <div class="section-label">2. Rank & Echelon Form</div>
    <div class="card">
        <div class="card-title">📊 Row Echelon Form (REF) & Rank</div>
        <p><strong>REF:</strong> 1) All zero rows are at the bottom. 2) Leading entry is strictly to the right of the leading entry above it. 3) Entries below leading entry are zero.</p>
        <p><strong>Reduced REF (RREF):</strong> REF + 1) Leading entries are 1. 2) Entries above leading entries are zero.</p>
        <p><strong>Rank(A):</strong> Number of pivots in REF = Dimension of column space = Number of linearly independent rows.</p>
        <div class="qa-block"><div class="qa-header"><h4>Example: Rank of $A$</h4></div><div class="qa-body">
            $A = \\begin{pmatrix} 1 & 1 & 1 \\\\ 2 & 0 & 4 \\\\ 3 & 2 & 4 \\\\ 0 & 5 & -5 \\end{pmatrix}$. $R_2 \\to R_2-2R_1$, $R_3 \\to R_3-3R_1$ gives $\\begin{pmatrix} 1 & 1 & 1 \\\\ 0 & -2 & 2 \\\\ 0 & -1 & 1 \\\\ 0 & 5 & -5 \\end{pmatrix}$. Rows 2,3,4 are multiples. RREF has 2 non-zero rows. Rank = 2.
        </div></div>
        <div class="check-item"><input type="checkbox" class="syllabus-check" data-id="u1-3"><label>Can reduce to REF / RREF</label></div>
        <div class="check-item"><input type="checkbox" class="syllabus-check" data-id="u1-4"><label>Can calculate Rank of a Matrix</label></div>
    </div>

    <div class="section-label">3. Systems of Linear Equations</div>
    <div class="card">
        <div class="card-title">⚙️ Solving $Ax = b$</div>
        <p><strong>Rouché-Capelli Theorem:</strong> Let $n$ be number of unknowns.</p>
        <ul>
            <li><strong>No Solution (Inconsistent):</strong> $Rank(A) < Rank([A|b])$</li>
            <li><strong>Unique Solution:</strong> $Rank(A) = Rank([A|b]) = n$</li>
            <li><strong>Infinite Solutions:</strong> $Rank(A) = Rank([A|b]) < n$</li>
        </ul>
        <p><strong>Homogeneous Systems ($Ax=0$):</strong> Always consistent (trivial solution $x=0$). Non-trivial solution exists if $Rank(A) < n$ (or $\\det(A)=0$).</p>
        <div class="check-item"><input type="checkbox" class="syllabus-check" data-id="u1-5"><label>Mastered Consistency Analysis (Rouché-Capelli)</label></div>
    </div>

    <div class="section-label">4. Inverse & Elementary Matrices</div>
    <div class="card">
        <div class="card-title">🔀 Gauss-Jordan & Elementary Matrices</div>
        <p><strong>Elementary Matrix $E$:</strong> Obtained from $I$ by a single row operation. $E$ is always invertible.</p>
        <p><strong>Gauss-Jordan Method:</strong> Augment $[A|I]$, apply row operations to get $[I|A^{-1}]$.</p>
        <p><strong>Properties of Inverse:</strong> $(A^{-1})^{-1} = A$, $(AB)^{-1} = B^{-1}A^{-1}$, $(A^T)^{-1} = (A^{-1})^T$.</p>
        <div class="check-item"><input type="checkbox" class="syllabus-check" data-id="u1-6"><label>Can calculate inverse using Gauss-Jordan</label></div>
    </div>

    <div class="section-label">5. Determinants & Cramer's Rule</div>
    <div class="card">
        <div class="card-title">🔢 Properties of Determinants</div>
        <p>$\\det(AB)=\\det(A)\\det(B)$, $\\det(A^T)=\\det(A)$, $\\det(A^{-1})=1/\\det(A)$, $\\det(cA)=c^n\\det(A)$.</p>
        <p>Row swap: sign change. Add multiple of row: no change. Multiply row by $c$: determinant multiplied by $c$. Identical rows: $\\det=0$.</p>
        <p><strong>Cramer's Rule:</strong> $x_i = \\det(A_i) / \\det(A)$ for $Ax=b$ where $\\det(A) \\neq 0$.</p>
        <div class="check-item"><input type="checkbox" class="syllabus-check" data-id="u1-7"><label>Mastered Determinant Properties & Cramer's Rule</label></div>
    </div>

    <div class="section-label">6. Vector Spaces</div>
    <div class="card">
        <div class="card-title">🧭 Subspaces, Independence, Basis</div>
        <p><strong>Subspace Test:</strong> A subset $W$ is a subspace if it contains 0, is closed under addition, and closed under scalar multiplication.</p>
        <p><strong>Linear Independence:</strong> $c_1v_1 + ... + c_nv_n = 0 \\implies c_1=...=c_n=0$. Or $\\det(V) \\neq 0$.</p>
        <p><strong>Span:</strong> Set of all linear combinations. <strong>Basis:</strong> Independent set that spans the space. <strong>Dimension:</strong> Number of vectors in a basis.</p>
        <div class="check-item"><input type="checkbox" class="syllabus-check" data-id="u1-8"><label>Can test for Vector Spaces & Subspaces</label></div>
        <div class="check-item"><input type="checkbox" class="syllabus-check" data-id="u1-9"><label>Can determine Linear Independence & Basis</label></div>
    </div>
"""

unit2_content = """
    <div class="section-label">Unit 2</div>
    <h1 class="page-title"><span>Transformations</span> & Eigenvalues</h1>
    <p class="page-subtitle">Comprehensive coverage of Linear Mappings, Kernel, Eigenvalues, and Diagonalization.</p>

    <div class="section-label">1. Linear Transformations</div>
    <div class="card">
        <div class="card-title">🔄 Definitions & Properties</div>
        <p>A mapping $T: V \\to W$ is linear if $T(u+v) = T(u) + T(v)$ and $T(cu) = cT(u)$. Implies $T(0) = 0$.</p>
        <p>Every matrix defines a linear transformation $T(x) = Ax$.</p>
        <div class="check-item"><input type="checkbox" class="syllabus-check" data-id="u2-1"><label>Mastered Linear Transformation definitions</label></div>
    </div>

    <div class="section-label">2. Kernel and Range</div>
    <div class="card">
        <div class="card-title">🎯 Nullity and Rank</div>
        <p><strong>Kernel $\\text{Ker}(T)$:</strong> Set of $v \\in V$ such that $T(v) = 0$. Solved by finding Null Space of matrix $A$ ($Ax=0$).</p>
        <p><strong>Range $\\text{Range}(T)$:</strong> Set of $T(v)$ for $v \\in V$. Spanned by columns of $A$.</p>
        <div class="formula">
            <strong>Rank-Nullity Theorem:</strong> $\\text{dim}(\\text{Ker}(T)) + \\text{dim}(\\text{Range}(T)) = \\text{dim}(V)$
        </div>
        <div class="check-item"><input type="checkbox" class="syllabus-check" data-id="u2-2"><label>Can calculate Kernel and Range</label></div>
    </div>

    <div class="section-label">3. Eigenvalues & Eigenvectors</div>
    <div class="card">
        <div class="card-title">📈 Finding $\\lambda$ and $v$</div>
        <p><strong>Equation:</strong> $Av = \\lambda v$ for $v \\neq 0$.</p>
        <p><strong>Characteristic Equation:</strong> $\\det(A - \\lambda I) = 0$. Solve for eigenvalues $\\lambda$.</p>
        <p><strong>Eigenvectors:</strong> For each $\\lambda$, solve $(A - \\lambda I)v = 0$ to find the basis of the eigenspace.</p>
        <p><strong>Properties:</strong> Sum of eigenvalues = Trace(A). Product of eigenvalues = $\\det(A)$. Eigenvalues of $A^k$ are $\\lambda^k$.</p>
        <div class="check-item"><input type="checkbox" class="syllabus-check" data-id="u2-3"><label>Can calculate Eigenvalues & Eigenvectors</label></div>
    </div>

    <div class="section-label">4. Diagonalization & Similar Matrices</div>
    <div class="card">
        <div class="card-title">⬜ $P^{-1}AP = D$</div>
        <p><strong>Similar Matrices:</strong> $A$ is similar to $B$ if $P^{-1}AP = B$. Similar matrices have same eigenvalues, trace, and determinant.</p>
        <p><strong>Diagonalization:</strong> $A$ is diagonalizable if it has $n$ linearly independent eigenvectors (Geometric Multiplicity = Algebraic Multiplicity for all $\\lambda$).</p>
        <p><strong>Method:</strong> $D$ has eigenvalues on diagonal. $P$ has eigenvectors as columns. Then $A = PDP^{-1}$.</p>
        <p><strong>Symmetric Matrices:</strong> Always diagonalizable. Eigenvectors for distinct eigenvalues are orthogonal. $P$ can be made orthogonal ($P^T = P^{-1}$).</p>
        <div class="check-item"><input type="checkbox" class="syllabus-check" data-id="u2-4"><label>Mastered Diagonalization technique</label></div>
    </div>

    <div class="section-label">5. Advanced Decompositions</div>
    <div class="card">
        <div class="card-title">✨ Spectral & Singular Value Decomposition (SVD)</div>
        <p><strong>Spectral Decomposition:</strong> For a symmetric matrix $A$, it can be decomposed as $A = \\lambda_1 u_1 u_1^T + \\lambda_2 u_2 u_2^T + \\dots + \\lambda_n u_n u_n^T$, where $\\lambda_i$ are eigenvalues and $u_i$ are normalized orthogonal eigenvectors.</p>
        <p><strong>Singular Value Decomposition (SVD):</strong> Any $m \\times n$ matrix $A$ can be factored as $A = U \\Sigma V^T$.</p>
        <ul>
            <li>$U$ is an $m \\times m$ orthogonal matrix (Left singular vectors, eigenvectors of $AA^T$).</li>
            <li>$V$ is an $n \\times n$ orthogonal matrix (Right singular vectors, eigenvectors of $A^TA$).</li>
            <li>$\\Sigma$ is an $m \\times n$ diagonal matrix of singular values $\\sigma_i = \\sqrt{\\lambda_i}$, where $\\lambda_i$ are non-zero eigenvalues of $A^TA$.</li>
        </ul>
        <div class="formula">
            <strong>Key insight:</strong> SVD generalizes diagonalization to non-square matrices and is a fundamental tool for data compression and PCA.
        </div>
        <div class="check-item"><input type="checkbox" class="syllabus-check" data-id="u2-5"><label>Understands SVD and Spectral Decomposition</label></div>
    </div>
"""

practice_content = """
    <div class="section-label">Master Problem Bank</div>
    <h1 class="page-title"><span>Unit 1 & Unit 2</span> Practice Problems</h1>
    <p class="page-subtitle">Fully solved practice sheets covering ALL required questions, transcribed directly from the FIC 117 Practice Problem PDFs.</p>

    <!-- UNIT 1 PRACTICE -->
    <div class="section-label" style="margin-top:2rem; font-size:1.2rem; color:white;">UNIT 1 - CHAPTER 1: MATRICES</div>

    <div class="qa-block">
        <div class="qa-header"><h4>Q1. Find RREF and Rank of: (i) $\\begin{pmatrix} 2 & 1 & 1 \\\\ 4 & 2 & 2 \\\\ 2 & 1 & 1 \\end{pmatrix}$, (ii) $\\begin{pmatrix} 1 & 2 & 1 \\\\ 2 & 4 & 2 \\\\ 3 & 6 & 3 \\end{pmatrix}$, (iii) $\\begin{pmatrix} 1 & 2 & 3 \\\\ 2 & 4 & 6 \\end{pmatrix}$</h4><span class="tag tag-blue">RREF & Rank</span></div>
        <div class="qa-body">
            <p><strong>(i)</strong> $R_2 \\to R_2 - 2R_1$, $R_3 \\to R_3 - R_1$. Matrix becomes $\\begin{pmatrix} 2 & 1 & 1 \\\\ 0 & 0 & 0 \\\\ 0 & 0 & 0 \\end{pmatrix}$. $R_1 \\to R_1/2$: $\\begin{pmatrix} 1 & 1/2 & 1/2 \\\\ 0 & 0 & 0 \\\\ 0 & 0 & 0 \\end{pmatrix}$ (RREF). Rank = 1.</p>
            <p><strong>(ii)</strong> $R_2 \\to R_2 - 2R_1$, $R_3 \\to R_3 - 3R_1$. Matrix becomes $\\begin{pmatrix} 1 & 2 & 1 \\\\ 0 & 0 & 0 \\\\ 0 & 0 & 0 \\end{pmatrix}$ (RREF). Rank = 1.</p>
            <p><strong>(iii)</strong> $R_2 \\to R_2 - 2R_1$. Matrix becomes $\\begin{pmatrix} 1 & 2 & 3 \\\\ 0 & 0 & 0 \\end{pmatrix}$ (RREF). Rank = 1.</p>
            <div class="answer-box">✅ Rank is 1 for all three matrices since all rows are proportional.</div>
        </div>
    </div>

    <div class="qa-block">
        <div class="qa-header"><h4>Q2. Find three $2 \\times 2$ matrices A, B, C such that $AB=AC$ with $B \\neq C$ and $A \\neq 0$.</h4><span class="tag tag-purple">Matrix Properties</span></div>
        <div class="qa-body">
            <p>We need A to be a non-invertible matrix (zero divisor). Let $A = \\begin{pmatrix} 1 & 0 \\\\ 0 & 0 \\end{pmatrix}$.</p>
            <p>Let $B = \\begin{pmatrix} 0 & 0 \\\\ 1 & 0 \\end{pmatrix}$ and $C = \\begin{pmatrix} 0 & 0 \\\\ 0 & 1 \\end{pmatrix}$. Note $B \\neq C$.</p>
            <p>Then $AB = \\begin{pmatrix} 1 & 0 \\\\ 0 & 0 \\end{pmatrix}\\begin{pmatrix} 0 & 0 \\\\ 1 & 0 \\end{pmatrix} = \\begin{pmatrix} 0 & 0 \\\\ 0 & 0 \\end{pmatrix}$.</p>
            <p>And $AC = \\begin{pmatrix} 1 & 0 \\\\ 0 & 0 \\end{pmatrix}\\begin{pmatrix} 0 & 0 \\\\ 0 & 1 \\end{pmatrix} = \\begin{pmatrix} 0 & 0 \\\\ 0 & 0 \\end{pmatrix}$.</p>
            <div class="answer-box">✅ A, B, C chosen such that $AB=AC=0$ despite $B \\neq C$. This demonstrates matrix multiplication lacks the cancellation property when $A$ is not invertible.</div>
        </div>
    </div>

    <div class="qa-block">
        <div class="qa-header"><h4>Q3. If $3 \\times 3$ matrix $A^2 = A$, what are the possible values for the rank of A?</h4><span class="tag tag-purple">Idempotent Rank</span></div>
        <div class="qa-body">
            <p>An idempotent matrix $A$ has eigenvalues either 0 or 1. Since $A$ is diagonalizable, its rank is equal to the sum of its eigenvalues (Trace).</p>
            <p>For a $3 \\times 3$ matrix, the number of eigenvalues that are 1 can be 0, 1, 2, or 3.</p>
            <div class="answer-box">✅ Possible ranks are 0, 1, 2, 3.</div>
        </div>
    </div>

    <div class="qa-block">
        <div class="qa-header"><h4>Q4. (i) Is upper triangular A invertible if all diagonal entries are non-zero? (ii) If some are zero?</h4><span class="tag tag-purple">Invertibility</span></div>
        <div class="qa-body">
            <p>The determinant of an upper triangular matrix is the product of its diagonal entries: $\\det(A) = a_{11}a_{22}...a_{nn}$.</p>
            <p>(i) If all $a_{ii} \\neq 0$, then $\\det(A) \\neq 0$, so **YES**, it is invertible.</p>
            <p>(ii) If any $a_{ii} = 0$, then $\\det(A) = 0$, so **NO**, it is not invertible.</p>
        </div>
    </div>

    <div class="qa-block">
        <div class="qa-header"><h4>Q5. If $A^k = 0$, show $I-A$ is invertible.</h4><span class="tag tag-purple">Nilpotent Inverse</span></div>
        <div class="qa-body">
            <p>Consider the identity: $(I-A)(I + A + A^2 + ... + A^{k-1}) = I - A^k$.</p>
            <p>Since $A^k = 0$, this becomes $(I-A)(I + A + A^2 + ... + A^{k-1}) = I$.</p>
            <div class="answer-box">✅ Thus, $(I-A)^{-1} = I + A + A^2 + ... + A^{k-1}$, proving $I-A$ is invertible.</div>
        </div>
    </div>

    <div class="qa-block">
        <div class="qa-header"><h4>Q6. Let $R = \\begin{pmatrix} \\cos\\theta & -\\sin\\theta \\\\ \\sin\\theta & \\cos\\theta \\end{pmatrix}$. Find $R^2, R^3, R^n$.</h4><span class="tag tag-purple">Rotation Matrix</span></div>
        <div class="qa-body">
            <p>$R$ represents a counter-clockwise rotation by $\\theta$. Applying it twice rotates by $2\\theta$.</p>
            <p>$R^2 = \\begin{pmatrix} \\cos(2\\theta) & -\\sin(2\\theta) \\\\ \\sin(2\\theta) & \\cos(2\\theta) \\end{pmatrix}$.</p>
            <p>By mathematical induction, applying it $n$ times rotates by $n\\theta$.</p>
            <div class="answer-box">✅ $R^n = \\begin{pmatrix} \\cos(n\\theta) & -\\sin(n\\theta) \\\\ \\sin(n\\theta) & \\cos(n\\theta) \\end{pmatrix}$.</div>
        </div>
    </div>

    <div class="section-label" style="margin-top:2rem; font-size:1.2rem; color:white;">UNIT 1 - CHAPTER 2: SYSTEMS OF EQUATIONS</div>

    <div class="qa-block">
        <div class="qa-header"><h4>Q1. For which values of k does $kx + y = 1, x + ky = 1$ have no solution, one, or infinite?</h4><span class="tag tag-red">Consistency</span></div>
        <div class="qa-body">
            <p>Determinant of coefficient matrix: $\\det = k^2 - 1 = (k-1)(k+1)$.</p>
            <p>1) If $\\det \\neq 0 \\implies k \\neq 1, k \\neq -1$: **Unique solution**.</p>
            <p>2) If $k=1$: equations are $x+y=1, x+y=1$. Same line. **Infinite solutions**.</p>
            <p>3) If $k=-1$: equations are $-x+y=1, x-y=1 \\implies -x+y=1, -x+y=-1$. Parallel lines. **No solution**.</p>
        </div>
    </div>

    <div class="qa-block">
        <div class="qa-header"><h4>Q2. For which values of a is there a whole line of solutions for $ax+2y=0, 2x+ay=0$?</h4><span class="tag tag-red">Homogeneous</span></div>
        <div class="qa-body">
            <p>For a homogeneous system to have infinite solutions (a line of solutions), the determinant must be 0.</p>
            <p>$\\det = a^2 - 4 = 0 \\implies a^2 = 4 \\implies a = 2$ or $a = -2$.</p>
            <div class="answer-box">✅ $a = 2$ or $a = -2$.</div>
        </div>
    </div>

    <div class="qa-block">
        <div class="qa-header"><h4>Q5. Values of a for no/unique/infinite solutions: $x+y+z=2, 2x+3y+2z=5, 2x+3y+(a^2-1)z=a+1$</h4><span class="tag tag-red">Consistency</span></div>
        <div class="qa-body">
            <p>Augmented matrix: $\\left(\\begin{array}{ccc|c} 1 & 1 & 1 & 2 \\\\ 2 & 3 & 2 & 5 \\\\ 2 & 3 & a^2-1 & a+1 \\end{array}\\right)$</p>
            <p>$R_2 \\to R_2-2R_1, R_3 \\to R_3-2R_1$: $\\left(\\begin{array}{ccc|c} 1 & 1 & 1 & 2 \\\\ 0 & 1 & 0 & 1 \\\\ 0 & 1 & a^2-3 & a-3 \\end{array}\\right)$</p>
            <p>$R_3 \\to R_3-R_2$: $\\left(\\begin{array}{ccc|c} 1 & 1 & 1 & 2 \\\\ 0 & 1 & 0 & 1 \\\\ 0 & 0 & a^2-3 & a-4 \\end{array}\\right)$</p>
            <p>Analysis on bottom row $0x + 0y + (a^2-3)z = a-4$:</p>
            <ul>
                <li><strong>No solution:</strong> $a^2-3 = 0 \\implies a = \\pm\\sqrt{3}$ (since RHS $a-4 \\neq 0$).</li>
                <li><strong>Unique solution:</strong> $a^2-3 \\neq 0 \\implies a \\neq \\pm\\sqrt{3}$.</li>
                <li><strong>Infinite solutions:</strong> Never! (Since $a^2-3=0$ and $a-4=0$ cannot be true simultaneously).</li>
            </ul>
        </div>
    </div>

    <div class="section-label" style="margin-top:2rem; font-size:1.2rem; color:white;">UNIT 2 - CHAPTER 3: VECTOR SPACES</div>

    <div class="qa-block">
        <div class="qa-header"><h4>Q3. Which are subspaces of $\\mathbb{R}^3$? (i) $b_1 = 0$, (ii) $b_1 = 1$, (iii) $b_1b_2 = 0$, (iv) $b_1+b_2+b_3 = 0$</h4><span class="tag tag-blue">Subspaces</span></div>
        <div class="qa-body">
            <p>(i) $b_1 = 0$: Contains 0. Closed under addition $(0+0=0)$ and scalar mult $(k\\cdot0=0)$. **YES, it is a subspace (yz-plane)**.</p>
            <p>(ii) $b_1 = 1$: Does not contain the zero vector $(0,0,0)$. **NO**.</p>
            <p>(iii) $b_1b_2 = 0$: Union of yz-plane and xz-plane. Not closed under addition: $(1,0,0) + (0,1,0) = (1,1,0)$, but $1\\cdot1 \\neq 0$. **NO**.</p>
            <p>(iv) $b_1+b_2+b_3 = 0$: Contains 0. $(a_1+a_2+a_3) + (b_1+b_2+b_3) = 0+0=0$. $k(b_1+b_2+b_3) = k(0)=0$. **YES, subspace (plane through origin)**.</p>
        </div>
    </div>

    <div class="qa-block">
        <div class="qa-header"><h4>Q5. Are the sets linearly independent? (i) $(1,1,0), (0,1,1), (1,0,1)$</h4><span class="tag tag-blue">Independence</span></div>
        <div class="qa-body">
            <p>Form matrix and find determinant: $\\det \\begin{pmatrix} 1 & 0 & 1 \\\\ 1 & 1 & 0 \\\\ 0 & 1 & 1 \\end{pmatrix} = 1(1) - 0 + 1(1) = 2$.</p>
            <div class="answer-box">✅ Since $\\det \\neq 0$, the vectors are Linearly Independent.</div>
        </div>
    </div>

    <div class="qa-block">
        <div class="qa-header"><h4>Q6. Find basis and dimension spanned by $v_1=(1,2,3), v_2=(2,3,4), v_3=(3,4,5)$.</h4><span class="tag tag-blue">Basis</span></div>
        <div class="qa-body">
            <p>Form matrix with vectors as rows and reduce: $\\begin{pmatrix} 1 & 2 & 3 \\\\ 2 & 3 & 4 \\\\ 3 & 4 & 5 \\end{pmatrix}$</p>
            <p>$R_2 \\to R_2-2R_1, R_3 \\to R_3-3R_1$: $\\begin{pmatrix} 1 & 2 & 3 \\\\ 0 & -1 & -2 \\\\ 0 & -2 & -4 \\end{pmatrix}$</p>
            <p>$R_3 \\to R_3-2R_2$: $\\begin{pmatrix} 1 & 2 & 3 \\\\ 0 & -1 & -2 \\\\ 0 & 0 & 0 \\end{pmatrix}$</p>
            <p>Two non-zero rows remain. **Dimension = 2**.</p>
            <div class="answer-box">✅ Basis: $\{(1,2,3), (0,-1,-2)\}$. Dimension = 2.</div>
        </div>
    </div>
"""

os.makedirs('C:\\Users\\k.chandra shekar\\.gemini\\antigravity\\scratch\\math_study_hub', exist_ok=True)
write_html('C:\\Users\\k.chandra shekar\\.gemini\\antigravity\\scratch\\math_study_hub\\unit1.html', get_base('Unit 1 — Linear Algebra', 'unit1', unit1_content))
write_html('C:\\Users\\k.chandra shekar\\.gemini\\antigravity\\scratch\\math_study_hub\\unit2.html', get_base('Unit 2 — Transformations', 'unit2', unit2_content))
write_html('C:\\Users\\k.chandra shekar\\.gemini\\antigravity\\scratch\\math_study_hub\\practice.html', get_base('Practice Solutions', 'practice', practice_content))
print("HTML Pages Generated successfully.")
