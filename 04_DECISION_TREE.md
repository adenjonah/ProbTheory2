# Decision Tree for Problem Identification

**Generated:** December 16, 2025
**Purpose:** Diagnostic decision tree for rapid question type identification and solution routing

---

## 🎯 HOW TO USE THIS DECISION TREE

1. **Start at ROOT**
2. **Answer each question** (Yes/No)
3. **Follow the path** to terminal node
4. **Terminal nodes show:**
   - Section reference in cheat sheet
   - Key formula reminder
   - 2-3 keyword indicators
   - Common professor phrasing

---

## 🌳 MASTER DECISION TREE

```
ROOT: EXAMINE THE PROBLEM
│
├─[Q1] Does problem involve PROBABILITY CALCULATIONS?
│  │
│  ├─YES─>[Q1.1] Is it about CONDITIONAL probability?
│  │      │
│  │      ├─YES─>[Q1.1.1] Need to UPDATE beliefs/Use evidence?
│  │      │      │
│  │      │      ├─YES──►【BAYES' THEOREM】Section 1.3
│  │      │      │       Formula: P(H|E) = P(E|H)P(H)/P(E)
│  │      │      │       Keywords: "update", "given evidence", "posterior"
│  │      │      │       Prof says: "How does new information change probability?"
│  │      │      │
│  │      │      └─NO───►【CONDITIONAL PROBABILITY】Section 1.2
│  │      │              Formula: P(A|B) = P(A∩B)/P(B)
│  │      │              Keywords: "given that", "if we know", "conditional on"
│  │      │              Prof says: "What's the probability given..."
│  │      │
│  │      └─NO──>[Q1.1.2] Multiple scenarios/cases?
│  │              │
│  │              ├─YES──►【TOTAL PROBABILITY】Section 1.3
│  │              │       Formula: P(A) = ΣP(A|Bi)P(Bi)
│  │              │       Keywords: "different cases", "partition"
│  │              │       Prof says: "Consider all possible scenarios"
│  │              │
│  │              └─NO───►【BASIC PROBABILITY】Section 1.1
│  │                      Formula: P(A) = |A|/|S| (if equally likely)
│  │                      Keywords: "probability", "chance", "likelihood"
│  │                      Prof says: "Find the probability..."
│  │
│  └─NO──>[Q1.2] Is it about COUNTING/COMBINATIONS?
│         │
│         ├─YES─>[Q1.2.1] Does ORDER matter?
│         │      │
│         │      ├─YES──►【PERMUTATIONS】Section 1.1
│         │      │       Formula: P(n,k) = n!/(n-k)!
│         │      │       Keywords: "arrangements", "order matters", "sequence"
│         │      │       Prof says: "How many ways to arrange..."
│         │      │
│         │      └─NO───►【COMBINATIONS】Section 1.1
│         │              Formula: C(n,k) = n!/[k!(n-k)!]
│         │              Keywords: "choose", "select", "order doesn't matter"
│         │              Prof says: "How many ways to select..."
│         │
│         └─NO──>Continue to Q2
│
├─[Q2] Does problem involve RANDOM VARIABLES?
│  │
│  ├─YES─>[Q2.1] DISCRETE or CONTINUOUS?
│  │      │
│  │      ├─DISCRETE─>[Q2.1.1] Named distribution mentioned?
│  │      │          │
│  │      │          ├─BINOMIAL──►【BINOMIAL】Section 2.2
│  │      │          │            Formula: P(X=k) = C(n,k)p^k(1-p)^(n-k)
│  │      │          │            Keywords: "n trials", "success probability p"
│  │      │          │            Prof says: "Repeated independent trials..."
│  │      │          │
│  │      │          ├─POISSON───►【POISSON】Section 2.3
│  │      │          │            Formula: P(X=k) = e^(-λ)λ^k/k!
│  │      │          │            Keywords: "rate λ", "rare events", "per unit time"
│  │      │          │            Prof says: "Events occurring at rate..."
│  │      │          │
│  │      │          ├─GEOMETRIC─►【GEOMETRIC】Section 2.4
│  │      │          │            Formula: P(X=k) = p(1-p)^k
│  │      │          │            Keywords: "first success", "waiting time"
│  │      │          │            Prof says: "Number of trials until..."
│  │      │          │
│  │      │          └─OTHER─────►【DISCRETE RV】Section 2.1
│  │      │                       PMF, CDF, Expectation formulas
│  │      │                       Keywords: "PMF", "discrete", "countable"
│  │      │
│  │      └─CONTINUOUS─>[Q2.1.2] Named distribution mentioned?
│  │                   │
│  │                   ├─NORMAL────►【NORMAL】Section 3.2 🔥
│  │                   │           Formula: Z = (X-μ)/σ, use Φ(z)
│  │                   │           Keywords: "normal", "Gaussian", "N(μ,σ²)"
│  │                   │           Prof says: "Approximately normal..."
│  │                   │
│  │                   ├─EXPONENTIAL►【EXPONENTIAL】Section 3.3
│  │                   │           Formula: f(x) = λe^(-λx)
│  │                   │           Keywords: "waiting time", "memoryless"
│  │                   │           Prof says: "Time until event..."
│  │                   │
│  │                   ├─UNIFORM───►【UNIFORM】Section 3.1
│  │                   │           Formula: f(x) = 1/(b-a)
│  │                   │           Keywords: "equally likely", "uniform on [a,b]"
│  │                   │           Prof says: "Uniformly distributed..."
│  │                   │
│  │                   └─OTHER─────►【CONTINUOUS RV】Section 3.1
│  │                               PDF, CDF, Integration
│  │                               Keywords: "density", "continuous"
│  │
│  └─NO──>Continue to Q3
│
├─[Q3] Does problem involve MULTIPLE VARIABLES? 🔥
│  │
│  ├─YES─>[Q3.1] What aspect of multiple variables?
│  │      │
│  │      ├─JOINT DISTRIBUTION──>[Q3.1.1] Need marginals/conditionals?
│  │      │                     │
│  │      │                     ├─YES──►【MARGINAL/CONDITIONAL】Section 4.2
│  │      │                     │       Marginal: fx(x) = ∫f(x,y)dy
│  │      │                     │       Conditional: f(y|x) = f(x,y)/fx(x)
│  │      │                     │       Keywords: "marginal", "given X=x"
│  │      │                     │
│  │      │                     └─NO───►【JOINT DISTRIBUTIONS】Section 4.1
│  │      │                             Joint PDF/PMF properties
│  │      │                             Keywords: "joint", "bivariate"
│  │      │
│  │      ├─INDEPENDENCE TEST──►【INDEPENDENCE】Section 4.3
│  │      │                    Check: f(x,y) = fx(x)fy(y)
│  │      │                    Keywords: "independent?", "affect each other?"
│  │      │                    Prof says: "Are X and Y independent?"
│  │      │
│  │      ├─CORRELATION───────►【COVARIANCE/CORRELATION】Section 4.4
│  │      │                    Cov(X,Y) = E[XY] - E[X]E[Y]
│  │      │                    ρ = Cov(X,Y)/(σX·σY)
│  │      │                    Keywords: "covariance", "correlation", "ρ"
│  │      │
│  │      ├─BIVARIATE NORMAL──►【BIVARIATE NORMAL】Section 4.5 🔥
│  │      │                    Special properties, ρ = 0 ⟺ independent
│  │      │                    Keywords: "jointly normal", "bivariate normal"
│  │      │                    Prof says: "X and Y are jointly normal..."
│  │      │
│  │      └─TRANSFORMATIONS───►【TRANSFORMATIONS】Section 4.6 🔥
│  │                          Jacobian: |∂(x,y)/∂(u,v)|
│  │                          Keywords: "transform", "change variables"
│  │                          Prof says: "Find distribution of U=g(X,Y)"
│  │
│  └─NO──>Continue to Q4
│
├─[Q4] Does problem involve EXPECTATIONS/MOMENTS?
│  │
│  ├─YES─>[Q4.1] What type of expectation?
│  │      │
│  │      ├─BASIC E[X]────────►【EXPECTATION】Section 5.1
│  │      │                    Discrete: ΣxP(X=x)
│  │      │                    Continuous: ∫xf(x)dx
│  │      │                    Keywords: "expected value", "mean", "E[X]"
│  │      │
│  │      ├─VARIANCE──────────►【VARIANCE】Section 5.2
│  │      │                    Var(X) = E[X²] - (E[X])²
│  │      │                    Keywords: "variance", "Var(X)", "spread"
│  │      │
│  │      ├─CONDITIONAL E[X|Y]►【CONDITIONAL EXPECTATION】Section 5.3 🔥
│  │      │                    E[X] = E[E[X|Y]] (Total Expectation)
│  │      │                    Keywords: "E[X|Y]", "conditional expectation"
│  │      │                    Prof says: "Expected value given..."
│  │      │
│  │      ├─MGF──────────────►【MGF】Section 5.4 🔥
│  │      │                    M(t) = E[e^(tX)]
│  │      │                    Keywords: "MGF", "moment generating"
│  │      │                    Prof says: "Use the MGF to find..."
│  │      │
│  │      └─MOMENTS───────────►【MOMENTS】Section 5.5
│  │                          E[X^k], central moments
│  │                          Keywords: "k-th moment", "E[X²]"
│  │
│  └─NO──>Continue to Q5
│
├─[Q5] Does problem involve LARGE SAMPLES/APPROXIMATIONS? 🔥
│  │
│  ├─YES─>[Q5.1] What type of limit theorem?
│  │      │
│  │      ├─CLT APPLICATION───►【CENTRAL LIMIT THEOREM】Section 6.1 🔥
│  │      │                    Z = (X̄-μ)/(σ/√n) ~ N(0,1)
│  │      │                    Keywords: "large n", "approximate", "CLT"
│  │      │                    Prof says: "For large samples..."
│  │      │
│  │      ├─NORMAL APPROX────►【NORMAL APPROXIMATION】Section 6.2 🔥
│  │      │                    Continuity correction: ±0.5
│  │      │                    Keywords: "approximate using normal"
│  │      │                    Prof says: "Use normal approximation..."
│  │      │
│  │      ├─LLN──────────────►【LAW OF LARGE NUMBERS】Section 6.3
│  │      │                    X̄n → μ as n → ∞
│  │      │                    Keywords: "converges", "as n→∞"
│  │      │
│  │      └─CONFIDENCE INT───►【CONFIDENCE INTERVALS】Section 6.4
│  │                          X̄ ± zα/2·(σ/√n)
│  │                          Keywords: "confidence interval", "margin"
│  │                          Prof says: "95% confidence..."
│  │
│  └─NO──>Continue to Q6
│
├─[Q6] Does problem involve BAYESIAN STATISTICS? 🔥
│  │
│  ├─YES─>[Q6.1] What type of Bayesian problem?
│  │      │
│  │      ├─BASIC UPDATE─────►【BAYESIAN UPDATE】Section 7.1 🔥
│  │      │                    Posterior ∝ Likelihood × Prior
│  │      │                    Keywords: "update", "posterior", "prior"
│  │      │                    Prof says: "Update your belief..."
│  │      │
│  │      ├─CONJUGATE PRIOR──►【CONJUGATE PRIORS】Section 7.2 🔥
│  │      │                    Beta-Binomial, Gamma-Poisson
│  │      │                    Keywords: "conjugate", "Beta prior"
│  │      │                    Prof says: "Use conjugate prior..."
│  │      │
│  │      └─PREDICTIVE───────►【PREDICTIVE DISTRIBUTION】Section 7.3
│  │                          Integrate over posterior
│  │                          Keywords: "predict next", "predictive"
│  │
│  └─NO──>Continue to Q7
│
└─[Q7] Does problem involve FINANCE APPLICATIONS? 🔥
   │
   ├─YES─>[Q7.1] What finance concept?
   │      │
   │      ├─LOGNORMAL────────►【LOGNORMAL】Section 8.1 🔥
   │      │                    Stock price S = S₀e^X
   │      │                    E[S] = S₀exp(μ + σ²/2)
   │      │                    Keywords: "stock price", "lognormal"
   │      │                    Prof says: "Stock follows lognormal..."
   │      │
   │      ├─PORTFOLIO────────►【PORTFOLIO THEORY】Section 8.2
   │      │                    Risk, diversification
   │      │                    Keywords: "portfolio", "risk", "diversify"
   │      │
   │      └─OPTIONS──────────►【OPTIONS】Section 8.3
   │                          Black-Scholes concepts
   │                          Keywords: "call", "put", "option"
   │
   └─NO──►【REVIEW PROBLEM】
          Check: Combination of above?
          Multi-step problem?
          See Section 9: Practice Problems
```

---

## 🎯 QUICK REFERENCE BRANCHES

### Branch A: PROBABILITY FUNDAMENTALS
```
START → Probability? → Conditional? → Update? 
    → YES: Bayes (Sec 1.3)
    → NO: Basic Conditional (Sec 1.2)
```

### Branch B: DISTRIBUTIONS
```
START → Random Variable? → Discrete/Continuous?
    → DISCRETE → Which? → [Binomial/Poisson/Geometric]
    → CONTINUOUS → Which? → [Normal/Exponential/Uniform]
```

### Branch C: MULTIVARIATE 🔥
```
START → Multiple Variables? → What aspect?
    → Joint/Marginal (Sec 4.1-4.2)
    → Independence (Sec 4.3)
    → Correlation (Sec 4.4)
    → Bivariate Normal (Sec 4.5)
```

### Branch D: LIMIT THEOREMS 🔥
```
START → Large Sample? → What type?
    → CLT (Sec 6.1)
    → Normal Approximation (Sec 6.2)
    → Confidence Interval (Sec 6.4)
```

### Branch E: BAYESIAN 🔥
```
START → Bayesian? → What type?
    → Basic Update (Sec 7.1)
    → Conjugate Prior (Sec 7.2)
```

---

## 📋 TERMINAL NODE QUICK LOOKUP

| Terminal Node | Section | Key Formula | Recognition |
|--------------|---------|-------------|-------------|
| **Bayes' Theorem** | 1.3 | P(H\|E) = P(E\|H)P(H)/P(E) | "update", "evidence" |
| **Conditional Prob** | 1.2 | P(A\|B) = P(A∩B)/P(B) | "given that" |
| **Total Probability** | 1.3 | P(A) = ΣP(A\|Bi)P(Bi) | "cases", "partition" |
| **Permutations** | 1.1 | P(n,k) = n!/(n-k)! | "order matters" |
| **Combinations** | 1.1 | C(n,k) = n!/[k!(n-k)!] | "choose", "select" |
| **Binomial** | 2.2 | P(X=k) = C(n,k)p^k(1-p)^(n-k) | "n trials" |
| **Poisson** | 2.3 | P(X=k) = e^(-λ)λ^k/k! | "rate λ" |
| **Geometric** | 2.4 | P(X=k) = p(1-p)^k | "first success" |
| **Normal** 🔥 | 3.2 | Z = (X-μ)/σ | "N(μ,σ²)" |
| **Exponential** | 3.3 | f(x) = λe^(-λx) | "waiting time" |
| **Joint Dist** | 4.1 | ∫∫f(x,y)dxdy = 1 | "joint", "bivariate" |
| **Marginal** | 4.2 | fx(x) = ∫f(x,y)dy | "marginal" |
| **Independence** | 4.3 | f(x,y) = fx(x)fy(y) | "independent?" |
| **Correlation** | 4.4 | ρ = Cov(X,Y)/(σX·σY) | "correlation" |
| **Bivariate Normal** 🔥 | 4.5 | Complex | "jointly normal" |
| **Jacobian** 🔥 | 4.6 | \|∂(x,y)/∂(u,v)\| | "transform" |
| **Expectation** | 5.1 | E[X] = ∫xf(x)dx | "expected value" |
| **Variance** | 5.2 | Var(X) = E[X²] - (E[X])² | "variance" |
| **Conditional E** 🔥 | 5.3 | E[X] = E[E[X\|Y]] | "E[X\|Y]" |
| **MGF** 🔥 | 5.4 | M(t) = E[e^(tX)] | "MGF" |
| **CLT** 🔥 | 6.1 | Z = (X̄-μ)/(σ/√n) | "large n" |
| **Normal Approx** 🔥 | 6.2 | Continuity: ±0.5 | "approximate" |
| **Confidence Int** | 6.4 | X̄ ± zα/2·(σ/√n) | "confidence" |
| **Bayesian** 🔥 | 7.1 | Post ∝ Like × Prior | "update" |
| **Conjugate** 🔥 | 7.2 | Beta-Binomial | "conjugate" |
| **Lognormal** 🔥 | 8.1 | S = S₀e^X | "stock price" |

---

## 🔄 SPECIAL BRANCHES FOR COMPLEX PROBLEMS

### Multi-Step Problems Branch
```
If problem has multiple parts (a), (b), (c)...
│
├─Build on previous parts?
│  └─YES → Solve sequentially, carry forward results
│  └─NO → Can solve in parallel
│
├─Mixed concepts?
│  └─YES → Identify each concept, apply in order
│  └─NO → Single concept, multiple applications
│
└─Check: Do later parts verify earlier?
```

### Combination Problems Branch
```
If problem combines multiple concepts:
│
├─[Probability + Distribution]
│  → Find distribution first, then probability
│
├─[Expectation + CLT]
│  → Find E[X], Var(X), then apply CLT
│
├─[Joint + Independence + Correlation]
│  → Find joint, check independence, compute correlation
│
└─[Bayesian + Prediction]
   → Update posterior, then predict
```

---

## 📊 PROBLEM RECOGNITION PATTERNS

### Pattern 1: Word Clues
- **"Given that"** → Conditional probability
- **"Update"** → Bayesian
- **"Large n"** → CLT
- **"Jointly"** → Multivariate
- **"Rate"** → Poisson/Exponential
- **"Trials"** → Binomial
- **"First"** → Geometric
- **"Stock"** → Lognormal

### Pattern 2: Mathematical Notation
- **P(A|B)** → Conditional
- **f(x,y)** → Joint distribution
- **E[X|Y]** → Conditional expectation
- **N(μ,σ²)** → Normal
- **ψ(t)** or **M(t)** → MGF
- **π(θ|x)** → Bayesian posterior

### Pattern 3: Professor's Favorite Phrases
- **"Consider all scenarios"** → Total probability
- **"For large samples"** → CLT
- **"Update your belief"** → Bayesian
- **"Are they independent?"** → Independence test
- **"Find the distribution"** → Full analysis needed
- **"Approximate using"** → Normal approximation
- **"In finance"** → Lognormal/Portfolio

---

## 🚀 SPEED TIPS FOR EXAM

### Quick Identification (< 10 seconds)
1. **Scan for keywords** first
2. **Check notation** (f(x,y)? P(A|B)? E[X]?)
3. **Count variables** (one or multiple?)
4. **Note distribution names** (Normal? Binomial?)
5. **Look for "large n"** → CLT territory

### When Stuck
1. **Check problem type** against this tree
2. **Identify all given information**
3. **Match to terminal node**
4. **Apply formula from that section**

### Time Management
- **2-3 min:** Basic probability (Branch A)
- **3-5 min:** Single distribution (Branch B)
- **5-10 min:** Joint distributions (Branch C)
- **10-15 min:** Multi-step/CLT (Branches D-E)
- **10-15 min:** Bayesian complete (Branch F)

---

## 🎨 VISUAL DECISION MAP

### High-Level Overview
```
                    PROBLEM
                       │
        ┌──────────────┼──────────────┐
        │              │              │
   PROBABILITY    DISTRIBUTIONS   ADVANCED
   (Sections 1-2)  (Sections 3-4)  (Sections 5-8)
        │              │              │
   [Quick: 2-5min] [Med: 5-10min] [Long: 10-15min]
```

### Exam Strategy Flow
```
Read Problem
    ↓
Identify Keywords (10 sec)
    ↓
Navigate Tree (20 sec)
    ↓
Find Terminal Node (10 sec)
    ↓
Apply Formula (2-15 min)
    ↓
Check Answer
```

---

## 🔥 POST-MIDTERM 2 FAST TRACK

For post-midterm-2 emphasis, prioritize these paths:

1. **Q3 → Bivariate Normal** (Section 4.5)
2. **Q4 → Conditional Expectation** (Section 5.3)
3. **Q4 → MGF** (Section 5.4)
4. **Q5 → CLT** (Section 6.1)
5. **Q5 → Normal Approximation** (Section 6.2)
6. **Q6 → Bayesian Update** (Section 7.1)
7. **Q6 → Conjugate Priors** (Section 7.2)
8. **Q7 → Lognormal** (Section 8.1)

These represent 80% of post-midterm-2 exam content!

---

## 📝 PRACTICE NAVIGATION

### Example 1: "Find P(X+Y > 0) where X,Y are jointly normal"
```
Path: Q3 → YES → Bivariate Normal → Section 4.5
Time: 10 min
Key: Linear combinations of jointly normal
```

### Example 2: "400 games, each win $3 with p=0.25, approximate P(win > $240)"
```
Path: Q5 → YES → CLT Application → Section 6.1
Time: 8 min
Key: CLT with continuity correction
```

### Example 3: "Update probability after observing evidence"
```
Path: Q6 → YES → Basic Update → Section 7.1
Time: 5 min
Key: Bayes' theorem
```

### Example 4: "Stock price S = S₀e^X, find E[S]"
```
Path: Q7 → YES → Lognormal → Section 8.1
Time: 5 min
Key: E[e^X] = exp(μ + σ²/2)
```

---

_End of Decision Tree_
