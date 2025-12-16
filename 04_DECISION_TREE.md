# COMPREHENSIVE DECISION TREE FOR PROBABILITY PROBLEM IDENTIFICATION

**Generated:** December 16, 2025
**Version:** 2.0 - Massively Expanded
**Purpose:** Exhaustive decision tree covering ALL question types and terminology variations

---

# PAGE 1: LEVEL 0 - INITIAL CLASSIFICATION

## 🎯 START HERE: Read the problem completely, then answer these questions

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                              ROOT: EXAMINE THE PROBLEM                        ║
╚══════════════════════════════════════════════════════════════════════════════╝
                                        │
    ┌───────────────────────────────────┼───────────────────────────────────┐
    │                                   │                                   │
    ▼                                   ▼                                   ▼
┌────────────────┐            ┌────────────────┐            ┌────────────────┐
│ Does problem   │            │ Does problem   │            │ Does problem   │
│ mention a      │            │ describe a     │            │ ask about      │
│ DISTRIBUTION   │            │ PROCESS or     │            │ MULTIPLE       │
│ NAME?          │            │ SCENARIO?      │            │ VARIABLES?     │
└───────┬────────┘            └───────┬────────┘            └───────┬────────┘
        │                             │                             │
        ▼                             ▼                             ▼
   See BRANCHES               See BRANCHES                   See BRANCHES
      A-H (Page 2)              I-J (Page 5)                   K-O (Page 6)


    ┌───────────────────────────────────┼───────────────────────────────────┐
    │                                   │                                   │
    ▼                                   ▼                                   ▼
┌────────────────┐            ┌────────────────┐            ┌────────────────┐
│ Does problem   │            │ Does problem   │            │ Does problem   │
│ ask about      │            │ involve LIMITS │            │ involve        │
│ MOMENTS or     │            │ or APPROX-     │            │ BAYESIAN       │
│ MGF?           │            │ IMATIONS?      │            │ STATISTICS?    │
└───────┬────────┘            └───────┬────────┘            └───────┬────────┘
        │                             │                             │
        ▼                             ▼                             ▼
   See BRANCHES               See BRANCH S                   See BRANCH T
     P-R (Page 9)               (Page 10)                      (Page 11)


                    ┌────────────────────────────────┐
                    │ Problem involves MULTIPLE      │
                    │ concepts from above?           │
                    └───────────────┬────────────────┘
                                    │
                                    ▼
                          See BRANCH U (Page 12-15)
                          MULTI-CONCEPT PROBLEMS
```

---

# PAGE 2: BRANCH A - NORMAL/GAUSSIAN PROBLEMS 🔥🔥🔥

## SYNONYM RECOGNITION:
- **"Normal"** = **"Gaussian"** = **"N(μ,σ²)"** = **"Bell curve"**
- **"Gaussian vector"** = **"Multivariate normal"** = **"Jointly normal"** = **"MVN"**
- **"Standard normal"** = **"N(0,1)"** = **"Z"**
- **"Independent components"** in Gaussian context = **diagonal covariance matrix**

```
╔══════════════════════════════════════════════════════════════════════════════╗
║           BRANCH A: NORMAL/GAUSSIAN DISTRIBUTION PROBLEMS                     ║
║                      (Section 3.3, 4.5, 6.1-6.2)                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

You identified: Normal/Gaussian mentioned or implied

┌─────────────────────────────────────────────────────────────────────────────┐
│ [A1] Is it a SINGLE Gaussian random variable?                                │
└────────────────────────────────────────────┬────────────────────────────────┘
                                             │
        ┌────────────────┬───────────────────┼───────────────────┬────────────────┐
        │                │                   │                   │                │
        ▼                ▼                   ▼                   ▼                ▼
┌───────────────┐┌───────────────┐┌───────────────┐┌───────────────┐┌───────────────┐
│"Find P(X>a)" ││"Find E[g(X)]"││"Find dist of ││"Find P(|X|>a)"││"Find quantile"│
│or P(a<X<b)   ││               ││ Y = aX + b"   ││               ││or percentile  │
└───────┬───────┘└───────┬───────┘└───────┬───────┘└───────┬───────┘└───────┬───────┘
        │                │                │                │                │
        ▼                ▼                ▼                ▼                ▼
┌───────────────────────────────────────────────────────────────────────────────────┐
│ SOLUTION A1a:           SOLUTION A1b:           SOLUTION A1c:                      │
│ Standardize:            If g linear:            Y ~ N(aμ+b, a²σ²)                  │
│ Z = (X-μ)/σ             E[aX+b] = aμ+b          Linear transform of                │
│ Use Φ(z) table          E[X²] = μ² + σ²        normal is normal                   │
│ P(X>a) = 1-Φ((a-μ)/σ)  Otherwise integrate     Sec 3.3.2                          │
│ Sec 3.3.1              Sec 3.3.3                                                   │
│                                                                                     │
│ SOLUTION A1d:           SOLUTION A1e:                                               │
│ P(|Z|>a) = 2[1-Φ(a)]   Find z_p where Φ(z_p)=p                                     │
│ (for standard normal)   x_p = μ + σ·z_p                                            │
│ Sec 3.3.4              Sec 3.3.5                                                    │
└───────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ [A2] Is it MULTIPLE independent Gaussians (i.i.d.)?                          │
└────────────────────────────────────────────┬────────────────────────────────┘
                                             │
        ┌────────────────┬───────────────────┼───────────────────┬────────────────┐
        │                │                   │                   │                │
        ▼                ▼                   ▼                   ▼                ▼
┌───────────────┐┌───────────────┐┌───────────────┐┌───────────────┐┌───────────────┐
│"Find dist of ││"Find dist of ││"Find P(max   ││"Sum of        ││"Sample mean   │
│ X̄ = (1/n)ΣXᵢ"││ X₁+X₂"       ││ Xᵢ > a)"     ││ X₁-X₂"        ││ X̄ₙ"          │
└───────┬───────┘└───────┬───────┘└───────┬───────┘└───────┬───────┘└───────┬───────┘
        │                │                │                │                │
        ▼                ▼                ▼                ▼                ▼
┌───────────────────────────────────────────────────────────────────────────────────┐
│ SOLUTION A2a:           SOLUTION A2b:           SOLUTION A2c:                      │
│ X̄ ~ N(μ, σ²/n)         X₁+X₂ ~ N(μ₁+μ₂,       P(max>a)=1-P(all≤a)                 │
│                         σ₁²+σ₂²)               = 1-[Φ((a-μ)/σ)]ⁿ                   │
│ Sec 3.3.6              Sec 3.3.7               Sec 3.3.8                           │
│                                                                                     │
│ SOLUTION A2d:           SOLUTION A2e:                                               │
│ X₁-X₂ ~ N(μ₁-μ₂,       X̄ₙ ~ N(μ, σ²/n)                                            │
│ σ₁²+σ₂²)               Standard error = σ/√n                                       │
│ Sec 3.3.9              Sec 6.1.1                                                    │
└───────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ [A3] Is it a GAUSSIAN VECTOR (multivariate/bivariate normal)?                │
│      Keywords: "Gaussian vector", "jointly normal", "bivariate normal"       │
│                "independent components"                                       │
└────────────────────────────────────────────┬────────────────────────────────┘
                                             │
        ┌────────────────┬───────────────────┼───────────────────┬────────────────┐
        │                │                   │                   │                │
        ▼                ▼                   ▼                   ▼                ▼
┌───────────────┐┌───────────────┐┌───────────────┐┌───────────────┐┌───────────────┐
│"Independent  ││"Find marginal││"Find          ││"Linear combo  ││"Find P(X+Y>0)"│
│ components"  ││ distribution"││ conditional"  ││ aX+bY"        ││               │
└───────┬───────┘└───────┬───────┘└───────┬───────┘└───────┬───────┘└───────┬───────┘
        │                │                │                │                │
        ▼                ▼                ▼                ▼                ▼
┌───────────────────────────────────────────────────────────────────────────────────┐
│ SOLUTION A3a: "Independent components" means:                                      │
│ • Covariance matrix Σ is DIAGONAL                                                  │
│ • Components are independent (for MVN, ρ=0 ⟺ independent!)                         │
│ • Joint PDF factors: f(x₁,...,xₙ) = ∏ fᵢ(xᵢ)                                      │
│ Sec 4.5.1                                                                          │
│                                                                                     │
│ SOLUTION A3b: Marginals of MVN are univariate normal                               │
│ If (X,Y) ~ BVN(μ_X, μ_Y, σ²_X, σ²_Y, ρ), then X ~ N(μ_X, σ²_X)                   │
│ Sec 4.5.2                                                                          │
│                                                                                     │
│ SOLUTION A3c: Conditional of MVN                                                   │
│ Y|X=x ~ N(μ_Y + ρ(σ_Y/σ_X)(x-μ_X), (1-ρ²)σ²_Y)                                    │
│ Sec 4.5.3                                                                          │
│                                                                                     │
│ SOLUTION A3d: Linear combination of jointly normal is normal                       │
│ aX + bY ~ N(aμ_X + bμ_Y, a²σ²_X + b²σ²_Y + 2abρσ_Xσ_Y)                           │
│ Sec 4.5.4                                                                          │
│                                                                                     │
│ SOLUTION A3e: For P(X+Y>0), use A3d then standardize                               │
│ Z = (X+Y - E[X+Y])/√Var(X+Y), find P(Z > -E[X+Y]/√Var(X+Y))                       │
│ Sec 4.5.5                                                                          │
└───────────────────────────────────────────────────────────────────────────────────┘

**KEY FORMULAS FOR BRANCH A:**
• Standardization: Z = (X-μ)/σ
• Standard normal CDF: Φ(z) = P(Z ≤ z)
• Complement: P(X > a) = 1 - Φ((a-μ)/σ)
• Symmetry: Φ(-z) = 1 - Φ(z)
• Sum of normals: N(μ₁,σ₁²) + N(μ₂,σ₂²) = N(μ₁+μ₂, σ₁²+σ₂²) if independent
• For MVN only: ρ = 0 ⟺ independent
```

---

# PAGE 3: BRANCH B - EXPONENTIAL PROBLEMS

## SYNONYM RECOGNITION:
- **"Exponential"** = **"Exp(λ)"** = **"Exp(β)"** (careful: λ=1/β sometimes!)
- **"Memoryless"** (continuous) = **Exponential**
- **"Waiting time"** = often Exponential
- **"Time between arrivals"** = Exponential
- **"Service time"** = often Exponential
- **"Mean θ"** for Exponential means λ = 1/θ

```
╔══════════════════════════════════════════════════════════════════════════════╗
║           BRANCH B: EXPONENTIAL DISTRIBUTION PROBLEMS                         ║
║                      (Section 3.4)                                            ║
╚══════════════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────────────────────────┐
│ [B1] What are you asked to find?                                             │
└────────────────────────────────────────────┬────────────────────────────────┘
                                             │
        ┌────────────────┬───────────────────┼───────────────────┬────────────────┐
        │                │                   │                   │                │
        ▼                ▼                   ▼                   ▼                ▼
┌───────────────┐┌───────────────┐┌───────────────┐┌───────────────┐┌───────────────┐
│"Find P(X>t)" ││"Find E[X],   ││"Memoryless   ││"Sum of Exp   ││"Min of Exp   │
│or P(X<t)     ││ Var(X)"      ││ property"    ││ = Gamma"     ││ variables"   │
└───────┬───────┘└───────┬───────┘└───────┬───────┘└───────┬───────┘└───────┬───────┘
        │                │                │                │                │
        ▼                ▼                ▼                ▼                ▼
┌───────────────────────────────────────────────────────────────────────────────────┐
│ SOLUTION B1:                                                                       │
│ P(X > t) = e^(-λt)      E[X] = 1/λ         P(X > s+t | X > s)                      │
│ P(X ≤ t) = 1-e^(-λt)    Var(X) = 1/λ²      = P(X > t)                              │
│ F(x) = 1-e^(-λx)                           "Fresh start" property                  │
│                                                                                     │
│ SOLUTION B2:            SOLUTION B3:                                               │
│ X₁+...+Xₙ ~ Gamma(n,λ)  min{X₁,...,Xₙ} ~ Exp(λ₁+...+λₙ)                          │
│ if Xᵢ ~ Exp(λ) i.i.d.   if Xᵢ ~ Exp(λᵢ) independent                              │
└───────────────────────────────────────────────────────────────────────────────────┘

⚠️ COMMON MISTAKE: Parameter confusion!
• If "mean θ = 3" → λ = 1/3 (NOT λ = 3!)
• If "rate λ = 2" → mean = 1/2
• Check which parameterization is being used!
```

---

# PAGE 4: BRANCHES C-H - OTHER DISTRIBUTIONS

```
╔══════════════════════════════════════════════════════════════════════════════╗
║           BRANCH C: POISSON DISTRIBUTION                                      ║
║                      (Section 2.3)                                            ║
╚══════════════════════════════════════════════════════════════════════════════╝

SYNONYMS: "Poisson", "Pois(λ)", "counting process", "arrivals", "rate λ"

• P(X=k) = e^(-λ)λᵏ/k!
• E[X] = λ, Var(X) = λ
• Poisson Process: N(t) ~ Pois(λt), independent increments
• Sum of Poisson: Pois(λ₁) + Pois(λ₂) = Pois(λ₁+λ₂)

╔══════════════════════════════════════════════════════════════════════════════╗
║           BRANCH D: BINOMIAL DISTRIBUTION                                     ║
║                      (Section 2.2)                                            ║
╚══════════════════════════════════════════════════════════════════════════════╝

SYNONYMS: "Binomial", "Bin(n,p)", "n trials", "success probability p", 
          "number of successes"

• P(X=k) = C(n,k)pᵏ(1-p)^(n-k)
• E[X] = np, Var(X) = np(1-p)
• Sum of Bernoulli: X = X₁+...+Xₙ where Xᵢ ~ Bernoulli(p)
• Normal approx: for large n, X ≈ N(np, np(1-p))

╔══════════════════════════════════════════════════════════════════════════════╗
║           BRANCH E: GEOMETRIC DISTRIBUTION                                    ║
║                      (Section 2.4)                                            ║
╚══════════════════════════════════════════════════════════════════════════════╝

SYNONYMS: "Geometric", "Geom(p)", "first success", "waiting time (discrete)",
          "memoryless (discrete)", "trials until success"

• P(X=k) = p(1-p)ᵏ (failures before success) or P(X=k) = p(1-p)^(k-1) (trials to success)
• E[X] = (1-p)/p or 1/p (check parameterization!)
• Memoryless: P(X > m+n | X > m) = P(X > n)

╔══════════════════════════════════════════════════════════════════════════════╗
║           BRANCH F: UNIFORM DISTRIBUTION                                      ║
║                      (Section 3.2)                                            ║
╚══════════════════════════════════════════════════════════════════════════════╝

SYNONYMS: "Uniform", "U[a,b]", "equally likely", "uniformly at random"

• f(x) = 1/(b-a) for a ≤ x ≤ b
• E[X] = (a+b)/2, Var(X) = (b-a)²/12
• F(x) = (x-a)/(b-a)

╔══════════════════════════════════════════════════════════════════════════════╗
║           BRANCH G: GAMMA DISTRIBUTION                                        ║
║                      (Section 3.5)                                            ║
╚══════════════════════════════════════════════════════════════════════════════╝

SYNONYMS: "Gamma", "Gamma(α,β)", "Erlang (when α integer)", 
          "sum of exponentials", "time until r-th arrival"

• f(x) = (βᵅ/Γ(α))x^(α-1)e^(-βx), x > 0
• E[X] = α/β, Var(X) = α/β²
• Special case: Gamma(1,β) = Exp(β)
• Sum property: Exp(λ)+...+Exp(λ) (n times) = Gamma(n,λ)

╔══════════════════════════════════════════════════════════════════════════════╗
║           BRANCH H: LOGNORMAL DISTRIBUTION 🔥                                 ║
║                      (Section 7.3)                                            ║
╚══════════════════════════════════════════════════════════════════════════════╝

SYNONYMS: "Lognormal", "log-normal", "stock price", "S = S₀e^X"

• If log(Y) ~ N(μ,σ²), then Y is lognormal
• Y = e^X where X ~ N(μ,σ²)
• E[Y] = e^(μ + σ²/2) ⟸ CRITICAL FORMULA
• Var(Y) = e^(2μ+σ²)(e^(σ²)-1)
• P(Y ≤ y) = Φ((ln(y)-μ)/σ)

For stock prices: S_t = S₀e^Z where Z ~ N(μt, σ²t)
```

---

# PAGE 5: BRANCHES I-J - PROCESS/SCENARIO PROBLEMS

```
╔══════════════════════════════════════════════════════════════════════════════╗
║           BRANCH I: ARRIVAL/WAITING TIME SCENARIOS                            ║
╚══════════════════════════════════════════════════════════════════════════════╝

Problem describes process WITHOUT naming distribution explicitly:

┌─────────────────────────────────────────────────────────────────────────────┐
│ What type of scenario?                                                       │
└────────────────────────────────────────────┬────────────────────────────────┘
                                             │
        ┌────────────────┬───────────────────┼───────────────────┐
        │                │                   │                   │
        ▼                ▼                   ▼                   ▼
┌───────────────┐┌───────────────┐┌───────────────┐┌───────────────┐
│"Arrivals at  ││"Waiting time ││"n trials     ││"First success"│
│ rate λ"      ││ until event" ││ success p"   ││               │
│"Events per   ││"Time between"││"How many in n"││"Until success"│
│ unit time"   ││              ││              ││               │
└───────┬───────┘└───────┬───────┘└───────┬───────┘└───────┬───────┘
        │                │                │                │
        ▼                ▼                ▼                ▼
    POISSON          EXPONENTIAL        BINOMIAL         GEOMETRIC
  (Branch C)        (Branch B)         (Branch D)        (Branch E)


╔══════════════════════════════════════════════════════════════════════════════╗
║           BRANCH J: OTHER SCENARIOS                                           ║
╚══════════════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────────────────────────┐
│ What type of scenario?                                                       │
└────────────────────────────────────────────┬────────────────────────────────┘
                                             │
        ┌────────────────┬───────────────────┼───────────────────┐
        │                │                   │                   │
        ▼                ▼                   ▼                   ▼
┌───────────────┐┌───────────────┐┌───────────────┐┌───────────────┐
│"Without      ││"Random point ││"Game with    ││"Stock price" │
│ replacement" ││ on interval" ││ winnings"    ││"Financial"   │
└───────┬───────┘└───────┬───────┘└───────┬───────┘└───────┬───────┘
        │                │                │                │
        ▼                ▼                ▼                ▼
  HYPERGEOMETRIC      UNIFORM         May need CLT      LOGNORMAL
   (Section 2.6)    (Branch F)         (Branch S)       (Branch H)
```

---

# PAGE 6: BRANCHES K-O - MULTIPLE VARIABLES

```
╔══════════════════════════════════════════════════════════════════════════════╗
║           BRANCH K: JOINT DISTRIBUTION PROBLEMS                               ║
║                      (Section 4.1, 4.2)                                       ║
╚══════════════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────────────────────────┐
│ Given joint PDF/PMF f(x,y), what are you asked?                              │
└────────────────────────────────────────────┬────────────────────────────────┘
                                             │
        ┌────────────────┬───────────────────┼───────────────────┬────────────────┐
        │                │                   │                   │                │
        ▼                ▼                   ▼                   ▼                ▼
┌───────────────┐┌───────────────┐┌───────────────┐┌───────────────┐┌───────────────┐
│"Find c to   ││"Find marginal││"Find         ││"Find E[XY]"  ││"Check        │
│ make valid" ││ f_X(x)"      ││ conditional" ││or E[g(X,Y)]  ││ independence"│
└───────┬───────┘└───────┬───────┘└───────┬───────┘└───────┬───────┘└───────┬───────┘
        │                │                │                │                │
        ▼                ▼                ▼                ▼                ▼
┌───────────────────────────────────────────────────────────────────────────────────┐
│ c: ∬f(x,y)dxdy=1       f_X(x)=∫f(x,y)dy  f(y|x)=f(x,y)/f_X(x)                    │
│ Sum/integrate over     Integrate out     Conditional =                            │
│ support region         other variable    Joint / Marginal                         │
│                                                                                    │
│ E[g(X,Y)]=∬g(x,y)f(x,y)dxdy              Independence: f(x,y)=f_X(x)·f_Y(y)       │
│ Use for E[XY], E[X²Y], etc.               for ALL x,y in support                  │
└───────────────────────────────────────────────────────────────────────────────────┘


╔══════════════════════════════════════════════════════════════════════════════╗
║           BRANCH L: SUM OF RANDOM VARIABLES                                   ║
║                      (Section 5.2, 6.1)                                       ║
╚══════════════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────────────────────────┐
│ Problem asks about Y = X₁ + X₂ + ... + Xₙ                                    │
└────────────────────────────────────────────┬────────────────────────────────┘
                                             │
        ┌────────────────┬───────────────────┼───────────────────┐
        │                │                   │                   │
        ▼                ▼                   ▼                   ▼
┌───────────────┐┌───────────────┐┌───────────────┐┌───────────────┐
│ Variables    ││ Variables    ││ Want exact   ││ Large n, want│
│ are i.i.d.   ││ are indep    ││ distribution ││ approximation│
│ Normal       ││ but different││              ││              │
└───────┬───────┘└───────┬───────┘└───────┬───────┘└───────┬───────┘
        │                │                │                │
        ▼                ▼                ▼                ▼
   Sum is Normal      Use MGF          Use MGF or        USE CLT
   N(nμ, nσ²)         ψ_Y = ∏ψᵢ       convolution       (Branch S)
   Branch A           Identify result


╔══════════════════════════════════════════════════════════════════════════════╗
║           BRANCH M: MAX/MIN (ORDER STATISTICS)                                ║
║                      (Section 4.7)                                            ║
╚══════════════════════════════════════════════════════════════════════════════╝

For i.i.d. X₁,...,Xₙ with CDF F(x):

• F_max(x) = P(max ≤ x) = P(all Xᵢ ≤ x) = [F(x)]ⁿ
• F_min(x) = P(min ≤ x) = 1 - P(min > x) = 1 - [1-F(x)]ⁿ
• P(max > a) = 1 - [F(a)]ⁿ
• P(min > a) = [1 - F(a)]ⁿ


╔══════════════════════════════════════════════════════════════════════════════╗
║           BRANCH N: PRODUCT OR RATIO                                          ║
║                      (Section 4.6)                                            ║
╚══════════════════════════════════════════════════════════════════════════════╝

• For Y = XZ where X,Z independent: use transformation theorem
• For lognormal: if X,Y are lognormal independent, XY is lognormal
• Jacobian method: find f_Y(y) using |dx/dy|


╔══════════════════════════════════════════════════════════════════════════════╗
║           BRANCH O: CONDITIONAL GIVEN VALUE                                   ║
║                      (Section 4.2, 4.5, 7.1)                                  ║
╚══════════════════════════════════════════════════════════════════════════════╝

"Given X = x, find..." or "X|Y=y"

• Conditional PDF: f(y|x) = f(x,y)/f_X(x)
• Conditional expectation: E[Y|X=x] = ∫y·f(y|x)dy
• For bivariate normal: Y|X=x ~ N(μ_Y + ρ(σ_Y/σ_X)(x-μ_X), (1-ρ²)σ²_Y)
```

---

# PAGE 7-8: BRANCHES P-R - MOMENTS AND MGF

```
╔══════════════════════════════════════════════════════════════════════════════╗
║           BRANCH P: MGF (MOMENT GENERATING FUNCTION)                          ║
║                      (Section 5.2)                                            ║
╚══════════════════════════════════════════════════════════════════════════════╝

SYNONYMS: "MGF", "M(t)", "ψ(t)", "moment generating function"

Definition: M_X(t) = E[e^(tX)]

KEY PROPERTIES:
• E[Xⁿ] = M^(n)(0) (n-th derivative at 0)
• E[X] = M'(0), E[X²] = M''(0)
• For independent X,Y: M_{X+Y}(t) = M_X(t)·M_Y(t)
• Uniqueness: Same MGF ⟹ Same distribution

COMMON MGFs:
• Bernoulli(p): (1-p) + pe^t
• Binomial(n,p): [(1-p) + pe^t]ⁿ
• Poisson(λ): e^(λ(e^t - 1))
• Normal(μ,σ²): e^(μt + σ²t²/2)
• Exponential(λ): λ/(λ-t) for t < λ
• Gamma(α,β): [β/(β-t)]^α for t < β


╔══════════════════════════════════════════════════════════════════════════════╗
║           BRANCH Q: EXPECTATION AND VARIANCE                                  ║
║                      (Section 5.1)                                            ║
╚══════════════════════════════════════════════════════════════════════════════╝

EXPECTATION:
• Discrete: E[X] = Σx·P(X=x)
• Continuous: E[X] = ∫x·f(x)dx
• E[g(X)] = ∫g(x)·f(x)dx (LOTUS)
• Linearity: E[aX+bY] = aE[X] + bE[Y] (always!)

VARIANCE:
• Var(X) = E[X²] - (E[X])²
• Var(aX+b) = a²Var(X)
• If independent: Var(X+Y) = Var(X) + Var(Y)
• If NOT independent: Var(X+Y) = Var(X) + Var(Y) + 2Cov(X,Y)


╔══════════════════════════════════════════════════════════════════════════════╗
║           BRANCH R: COVARIANCE AND CORRELATION                                ║
║                      (Section 4.4)                                            ║
╚══════════════════════════════════════════════════════════════════════════════╝

COVARIANCE:
• Cov(X,Y) = E[XY] - E[X]E[Y]
• Cov(X,X) = Var(X)
• Cov(aX+b, cY+d) = ac·Cov(X,Y)
• If independent: Cov(X,Y) = 0 (but NOT vice versa!)

CORRELATION:
• ρ = Cov(X,Y)/(σ_X·σ_Y)
• -1 ≤ ρ ≤ 1
• ρ = 0: uncorrelated (NOT necessarily independent!)
• ρ = ±1: perfect linear relationship

⚠️ CRITICAL: Uncorrelated ≠ Independent (except for normal!)
```

---

# PAGE 9-10: BRANCH S - LIMIT THEOREMS AND CLT

```
╔══════════════════════════════════════════════════════════════════════════════╗
║           BRANCH S: CLT AND APPROXIMATIONS 🔥🔥🔥                              ║
║                      (Section 6.1, 6.2)                                       ║
╚══════════════════════════════════════════════════════════════════════════════╝

KEYWORDS: "large n", "approximate", "for large samples", "use normal", 
          "CLT", "central limit theorem", "as n → ∞"

┌─────────────────────────────────────────────────────────────────────────────┐
│ CENTRAL LIMIT THEOREM (CLT):                                                 │
│ If X₁, X₂, ..., Xₙ are i.i.d. with E[Xᵢ] = μ and Var(Xᵢ) = σ², then:       │
│                                                                              │
│                X̄ₙ - μ     S_n - nμ                                          │
│         Z = ───────── = ─────────── → N(0,1) as n → ∞                       │
│               σ/√n       σ√n                                                 │
│                                                                              │
│ Where X̄ₙ = (1/n)ΣXᵢ and Sₙ = ΣXᵢ                                           │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ CLT APPLICATION STEPS:                                                       │
│                                                                              │
│ 1. Identify what Xᵢ represents (single trial/observation)                   │
│ 2. Find E[Xᵢ] = μ and Var(Xᵢ) = σ²                                         │
│ 3. Define what you want: X̄ (average) or Sₙ (sum)                           │
│ 4. Standardize:                                                              │
│    • For X̄: Z = (X̄ - μ)/(σ/√n)                                            │
│    • For Sₙ: Z = (Sₙ - nμ)/(σ√n)                                            │
│ 5. Convert probability question to standard normal                           │
│ 6. Use Φ table                                                               │
└─────────────────────────────────────────────────────────────────────────────┘

EXAMPLE: "n = 100 games, win $2 with p = 0.5 each game, find P(total > $120)"
1. Xᵢ = winnings in game i
2. E[Xᵢ] = 2(0.5) + 0(0.5) = 1, Var(Xᵢ) = computed from distribution
3. Sₙ = total winnings
4. Z = (Sₙ - 100(1))/(σ√100) = (Sₙ - 100)/(10σ)
5. P(Sₙ > 120) = P(Z > (120-100)/(10σ)) = 1 - Φ(...)


╔══════════════════════════════════════════════════════════════════════════════╗
║           CONTINUITY CORRECTION (for discrete → normal)                       ║
╚══════════════════════════════════════════════════════════════════════════════╝

When approximating a discrete distribution with normal:
• P(X ≤ k) ≈ Φ((k + 0.5 - μ)/σ)
• P(X ≥ k) ≈ 1 - Φ((k - 0.5 - μ)/σ)
• P(X = k) ≈ Φ((k + 0.5 - μ)/σ) - Φ((k - 0.5 - μ)/σ)


╔══════════════════════════════════════════════════════════════════════════════╗
║           LAW OF LARGE NUMBERS (LLN)                                          ║
║                      (Section 6.3)                                            ║
╚══════════════════════════════════════════════════════════════════════════════╝

• Weak LLN: X̄ₙ →ᵖ μ as n → ∞
  (Sample mean converges in probability to population mean)

• Used for: "converges to", "in the limit", "as n → ∞"

Related inequalities:
• Markov: P(X ≥ a) ≤ E[X]/a for X ≥ 0, a > 0
• Chebyshev: P(|X - μ| ≥ kσ) ≤ 1/k²
```

---

# PAGE 11: BRANCH T - BAYESIAN STATISTICS

```
╔══════════════════════════════════════════════════════════════════════════════╗
║           BRANCH T: BAYESIAN STATISTICS 🔥🔥                                  ║
║                      (Section 7.1, 7.2)                                       ║
╚══════════════════════════════════════════════════════════════════════════════╝

KEYWORDS: "prior", "posterior", "update", "belief", "given the data",
          "conjugate", "Bayes", "evidence"

┌─────────────────────────────────────────────────────────────────────────────┐
│ BAYES' THEOREM:                                                              │
│                                                                              │
│              P(θ|data) ∝ P(data|θ) × P(θ)                                   │
│                                                                              │
│              Posterior ∝ Likelihood × Prior                                  │
│                                                                              │
│ Full formula:                                                                │
│              P(θ|x) = P(x|θ)P(θ) / ∫P(x|θ')P(θ')dθ'                        │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ [T1] What type of prior?                                                     │
└────────────────────────────────────────────┬────────────────────────────────┘
                                             │
        ┌────────────────────────────────────┼────────────────────────────────┐
        │                                    │                                │
        ▼                                    ▼                                ▼
┌───────────────────────┐    ┌───────────────────────┐    ┌───────────────────────┐
│ DISCRETE PRIOR        │    │ CONTINUOUS PRIOR      │    │ CONJUGATE PRIOR       │
│ P(θ = θ₁) = p₁        │    │ π(θ) continuous       │    │ Posterior same family │
│ P(θ = θ₂) = p₂        │    │                       │    │ as prior              │
│ ...                   │    │                       │    │                       │
└───────────┬───────────┘    └───────────┬───────────┘    └───────────┬───────────┘
            │                            │                            │
            ▼                            ▼                            ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│ DISCRETE:                                                                        │
│ P(θᵢ|data) = P(data|θᵢ)P(θᵢ) / Σⱼ P(data|θⱼ)P(θⱼ)                              │
│ Make a Bayes table!                                                              │
│                                                                                  │
│ CONTINUOUS:                                                                      │
│ π(θ|x) = L(x|θ)π(θ) / ∫L(x|θ')π(θ')dθ'                                         │
│                                                                                  │
│ CONJUGATE PAIRS:                                                                 │
│ • Binomial likelihood + Beta(α,β) prior → Beta(α+k, β+n-k) posterior            │
│ • Poisson likelihood + Gamma(α,β) prior → Gamma(α+Σxᵢ, β+n) posterior           │
│ • Normal likelihood + Normal prior → Normal posterior                            │
│ • Exponential likelihood + Gamma prior → Gamma posterior                         │
└─────────────────────────────────────────────────────────────────────────────────┘

BETA-BINOMIAL CONJUGATE (Most Common):
• Prior: θ ~ Beta(α, β)
• Data: k successes in n trials
• Posterior: θ|data ~ Beta(α + k, β + n - k)
• Posterior mean: (α + k)/(α + β + n)

PREDICTIVE DISTRIBUTION:
P(next observation | data) = ∫P(next | θ)π(θ|data)dθ
```

---

# PAGES 12-15: BRANCH U - MULTI-CONCEPT PROBLEMS

```
╔══════════════════════════════════════════════════════════════════════════════╗
║           BRANCH U: MULTI-CONCEPT PROBLEM PATTERNS                            ║
║                      50+ Common Combinations                                   ║
╚══════════════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PATTERN U1: i.i.d. GAUSSIANS + LINEAR COMBINATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Keywords: "i.i.d. N(μ,σ²)", "Gaussian", "Y = aX₁ + bX₂"
Required: Section 3.3 (Normal), Section 4.5 (Bivariate)

Steps:
1. Identify distribution as Normal (even if called "Gaussian")
2. Compute: E[Y] = aE[X₁] + bE[X₂]
3. Compute: Var(Y) = a²Var(X₁) + b²Var(X₂) (if independent)
4. Y ~ N(E[Y], Var(Y))

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PATTERN U2: GAUSSIAN VECTOR + INDEPENDENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Keywords: "Gaussian vector", "independent components", "MVN"
Required: Section 4.5

Steps:
1. "Independent components" → diagonal covariance → Cov(Xᵢ,Xⱼ) = 0 for i≠j
2. For MVN: uncorrelated ⟺ independent
3. Joint PDF factors into product

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PATTERN U3: EXPONENTIAL + CLT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Keywords: "i.i.d. Exponential", "large n", "approximate", "sample average"
Required: Section 3.4 (Exp), Section 6.1 (CLT)

Steps:
1. Identify: Xᵢ ~ Exp(λ), so E[Xᵢ] = 1/λ, Var(Xᵢ) = 1/λ²
2. For X̄ₙ: E[X̄] = 1/λ, Var(X̄) = 1/(nλ²), SD(X̄) = 1/(λ√n)
3. Standardize: Z = (X̄ - 1/λ)/(1/(λ√n))
4. Use Φ table

⚠️ Watch for "mean θ = 3" which means λ = 1/3!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PATTERN U4: LOGNORMAL STOCK PRICE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Keywords: "stock price", "S = S₀e^Z", "lognormal"
Required: Section 7.3

Steps:
1. S = S₀e^Z where Z ~ N(μ,σ²)
2. E[S] = S₀ · e^(μ + σ²/2)
3. For P(S > k): P(e^Z > k/S₀) = P(Z > ln(k/S₀)) = 1 - Φ((ln(k/S₀) - μ)/σ)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PATTERN U5: BAYESIAN UPDATE (DISCRETE PRIOR)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Keywords: "prior", "posterior", discrete hypotheses
Required: Section 7.1

Steps:
1. List hypotheses: H₁, H₂, ...
2. Assign prior probabilities: P(Hᵢ)
3. Compute likelihoods: P(data|Hᵢ)
4. Apply Bayes: P(Hᵢ|data) = P(data|Hᵢ)P(Hᵢ) / Σⱼ P(data|Hⱼ)P(Hⱼ)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PATTERN U6: BETA-BINOMIAL UPDATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Keywords: "Beta prior", "Binomial", "conjugate", "proportion"
Required: Section 7.2

Steps:
1. Prior: θ ~ Beta(α, β)
2. Observe k successes in n trials
3. Posterior: θ|data ~ Beta(α + k, β + n - k)
4. Posterior mean: (α + k)/(α + β + n)
5. Posterior variance: (α+k)(β+n-k)/[(α+β+n)²(α+β+n+1)]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PATTERN U7: JOINT PDF → COVARIANCE → CORRELATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Keywords: "covariance", "correlation", "joint pdf"
Required: Section 4.1, 4.4

Steps:
1. Find E[X] = ∫∫x·f(x,y)dxdy
2. Find E[Y] = ∫∫y·f(x,y)dxdy
3. Find E[XY] = ∫∫xy·f(x,y)dxdy
4. Find E[X²], E[Y²]
5. Cov(X,Y) = E[XY] - E[X]E[Y]
6. Var(X) = E[X²] - (E[X])², Var(Y) = E[Y²] - (E[Y])²
7. ρ = Cov(X,Y)/(σ_X·σ_Y)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PATTERN U8: CONDITIONAL EXPECTATION → TOTAL EXPECTATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Keywords: "E[X|Y]", "Law of Total Expectation", "conditional"
Required: Section 7.1

Steps:
1. Find E[X|Y=y] as a function of y
2. E[X] = E[E[X|Y]] = ∫E[X|Y=y]·f_Y(y)dy (or sum for discrete)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PATTERN U9: LAW OF TOTAL VARIANCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Keywords: "Var(X|Y)", "total variance", "Eve's Law"
Required: Section 7.1

Formula: Var(X) = E[Var(X|Y)] + Var(E[X|Y])
         "Total variance = average conditional variance + variance of conditional means"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PATTERN U10: BIVARIATE NORMAL → CONDITIONAL DISTRIBUTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Keywords: "bivariate normal", "conditional distribution", "Y|X=x"
Required: Section 4.5

For (X,Y) bivariate normal:
Y|X=x ~ N(μ_Y + ρ(σ_Y/σ_X)(x-μ_X), (1-ρ²)σ²_Y)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PATTERN U11: GAME/COIN + SUM + CLT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Keywords: "n games", "total winnings", "approximate"
Required: Section 2.4, 6.1

Steps:
1. Define Xᵢ = outcome of game i
2. Find E[Xᵢ], Var(Xᵢ) from game rules
3. Sₙ = X₁ + ... + Xₙ (total)
4. Apply CLT: (Sₙ - nE[Xᵢ])/(√n·SD(Xᵢ)) ≈ N(0,1)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PATTERN U12: ORDER STATISTICS + CDF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Keywords: "max", "min", "largest", "smallest"
Required: Section 4.7

For i.i.d. X₁,...,Xₙ with CDF F(x):
• P(max ≤ x) = [F(x)]ⁿ
• P(min ≤ x) = 1 - [1-F(x)]ⁿ
• P(max > x) = 1 - [F(x)]ⁿ

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PATTERN U13: MGF FOR DISTRIBUTION IDENTIFICATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Keywords: "show that Y has distribution", "MGF"
Required: Section 5.2

Steps:
1. Find M_Y(t) = E[e^(tY)]
2. Compare to known MGFs
3. If M_Y(t) = M_X(t), then Y has same distribution as X

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PATTERN U14: PRODUCT OF LOGNORMALS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Keywords: "XY", "product", "lognormal"
Required: Section 7.3

If X = e^Z₁, Y = e^Z₂ where Z₁, Z₂ are independent normals:
XY = e^(Z₁+Z₂) is lognormal with parameters μ₁+μ₂, σ₁²+σ₂²

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PATTERN U15: MONTY HALL VARIANTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Keywords: "Monty Hall", "doors", "reveal"
Required: Section 7.1, 8.1

Steps:
1. Define clearly what each door represents
2. Identify what Monty knows/does
3. Compute likelihood for each scenario
4. Apply Bayes' theorem

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PATTERN U16: PREDICTIVE DISTRIBUTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Keywords: "predict next", "predictive"
Required: Section 7.2

P(X_{n+1} = k | data) = ∫P(X_{n+1} = k | θ) · π(θ|data)dθ

For Beta-Binomial:
P(next success | data) = (α + k)/(α + β + n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PATTERN U17: MEETING PROBLEM (TWO UNIFORMS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Keywords: "arrive uniformly", "waiting", "meet"
Required: Section 3.2, 4.1

Steps:
1. Both A, B ~ Uniform independently
2. Draw the unit square
3. Identify region for condition (e.g., |A-B| < 15)
4. Compute area of region
5. Probability = Area of region / Total area

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PATTERN U18: TRANSFORMATION USING JACOBIAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Keywords: "find distribution of Y = g(X)", "transform"
Required: Section 4.6

For Y = g(X) where g is 1-1:
f_Y(y) = f_X(g^(-1)(y)) · |d/dy g^(-1)(y)|

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PATTERN U19: CONFIDENCE INTERVAL FROM CLT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Keywords: "confidence interval", "95%", "margin of error"
Required: Section 6.4

CI for μ: X̄ ± z_{α/2} · σ/√n

Common z values:
• 90%: z = 1.645
• 95%: z = 1.96
• 99%: z = 2.576

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PATTERN U20: POISSON PROCESS + EXPONENTIAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Keywords: "arrivals at rate λ", "time between arrivals"
Required: Section 2.3, 3.4

• N(t) ~ Poisson(λt) for arrivals in time t
• Time between arrivals ~ Exponential(λ)
• Time until k-th arrival ~ Gamma(k, λ)
```

---

# PAGE 16: QUICK-LOOKUP INDEX (100+ phrases)

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                       QUICK-LOOKUP INDEX                                      ║
║          "If you see THIS phrase → Go to THIS branch"                         ║
╚══════════════════════════════════════════════════════════════════════════════╝

A-D:
"approximate" → Branch S (CLT)
"arrival rate" → Branch C (Poisson) or B (Exponential)
"average of n" → Branch S (CLT)
"Bayesian" → Branch T
"bell curve" → Branch A (Normal)
"Beta prior" → Branch T (Pattern U6)
"binomial" → Branch D
"bivariate normal" → Branch A (Section A3)
"CLT" → Branch S
"conditional" → Branch O or T
"conjugate" → Branch T
"continuous" → Branch B, F, G, or A
"converges" → Branch S (LLN)
"correlation" → Branch R
"covariance" → Branch R
"defective" → Often Branch T (Bayesian)

E-I:
"equally likely" → Branch F (Uniform)
"expected value" → Branch Q
"Exp(λ)" → Branch B (Exponential)
"exponential" → Branch B
"first success" → Branch E (Geometric)
"Gamma" → Branch G
"Gaussian" → Branch A (Normal) ⟸ CRITICAL
"Gaussian vector" → Branch A, Section A3 ⟸ CRITICAL
"Geometric" → Branch E
"given that" → Branch O (Conditional)
"i.i.d." → Likely Branch S (CLT) or L (sums)
"independent" → Branch K (check independence)
"independent components" → Branch A, Section A3 ⟸ CRITICAL

J-O:
"joint" → Branch K
"jointly normal" → Branch A, Section A3
"large n" → Branch S (CLT)
"likelihood" → Branch T (Bayesian)
"lognormal" → Branch H
"marginal" → Branch K
"max" → Branch M (Order statistics)
"mean" → Branch Q
"memoryless" → Branch B (Exp) or E (Geom)
"MGF" → Branch P
"min" → Branch M (Order statistics)
"moment" → Branch P or Q
"Monty Hall" → Pattern U15
"multivariate normal" → Branch A, Section A3
"MVN" → Branch A, Section A3
"N(μ,σ²)" → Branch A (Normal)
"negative binomial" → Branch E
"normal" → Branch A
"order statistics" → Branch M

P-T:
"Poisson" → Branch C
"posterior" → Branch T
"predict" → Pattern U16
"prior" → Branch T
"product" → Branch N
"proportion" → Often Branch T (Beta-Binomial)
"quantile" → Branch A
"rate" → Branch C (Poisson) or B (Exponential)
"ratio" → Branch N
"sample mean" → Branch S (CLT)
"standard normal" → Branch A
"stock price" → Branch H (Lognormal)
"sum" → Branch L
"total expectation" → Pattern U8
"total variance" → Pattern U9
"transform" → Branch N or Section 4.6
"trials" → Branch D (Binomial) or E (Geometric)

U-Z:
"uncorrelated" → Branch R (≠ independent unless Normal!)
"Uniform" → Branch F
"update" → Branch T (Bayesian)
"variance" → Branch Q
"waiting time" → Branch B (Exp) or E (Geom)
"without replacement" → Hypergeometric (Section 2.6)
"Z" → Branch A (Standard Normal)
"ψ(t)" → Branch P (MGF)
"Φ(z)" → Branch A (Standard Normal CDF)
```

---

# FINAL PAGE: EXAM CHEAT CODE

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                         EXAM PANIC CHEAT CODE                                 ║
╚══════════════════════════════════════════════════════════════════════════════╝

🚨 IF YOU SEE:              DO THIS IMMEDIATELY:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"Gaussian"              →  It's NORMAL. Use Section 3.3 or 4.5
"Gaussian vector"       →  It's MVN. Check for "independent components"
"Independent components"→  Diagonal covariance. For MVN: independent!
"i.i.d." + large n      →  CLT! Section 6.1
"Mean θ = 3" (Exp)      →  λ = 1/3 (NOT λ = 3!)
"Stock price"           →  Lognormal. E[S] = S₀e^(μ+σ²/2)
"Update belief"         →  Bayes. Section 7.1
"Conjugate"             →  Beta-Binomial or Gamma-Poisson. Section 7.2
"max" or "min"          →  Order statistics. [F(x)]ⁿ or 1-[1-F(x)]ⁿ
"Approximate"           →  CLT. Section 6.1

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🏆 TOP 5 FORMULAS TO MEMORIZE:

1. CLT: Z = (X̄ - μ)/(σ/√n) ~ N(0,1)
2. Lognormal: E[e^X] = e^(μ + σ²/2) when X ~ N(μ,σ²)
3. Bivariate Normal Conditional: Y|X ~ N(μ_Y + ρ(σ_Y/σ_X)(X-μ_X), (1-ρ²)σ²_Y)
4. Beta-Binomial: Prior Beta(α,β) + k successes in n → Posterior Beta(α+k, β+n-k)
5. Order Statistics: P(max ≤ x) = [F(x)]ⁿ

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ COMPLETED: Massively expanded decision tree with exhaustive coverage
```

---

---

# ADDITIONAL PATTERNS: 50+ EXAM PROBLEM TYPES

## PATTERN CATEGORY A: GAUSSIAN/NORMAL PROBLEMS (12 Patterns)

### A1: Single Normal - Find Probability
**Trigger:** "X ~ N(μ,σ²)", "find P(X > a)"
**Method:** Standardize Z = (X-μ)/σ, use Φ table
**Formula:** P(X > a) = 1 - Φ((a-μ)/σ)

### A2: Sum of Independent Normals
**Trigger:** "X₁, X₂ independent normals", "find distribution of X₁ + X₂"
**Method:** Sum is normal with μ = μ₁+μ₂, σ² = σ₁²+σ₂²
**Key:** N(μ₁,σ₁²) + N(μ₂,σ₂²) = N(μ₁+μ₂, σ₁²+σ₂²)

### A3: Sample Mean of Normals
**Trigger:** "i.i.d. N(μ,σ²)", "sample mean X̄"
**Method:** X̄ ~ N(μ, σ²/n)
**Formula:** Z = (X̄ - μ)/(σ/√n)

### A4: Linear Combination of Jointly Normal
**Trigger:** "bivariate normal", "aX + bY"
**Method:** aX + bY ~ N(aμₓ + bμᵧ, a²σₓ² + b²σᵧ² + 2abρσₓσᵧ)
**Key:** Include correlation term!

### A5: Conditional Distribution (Bivariate Normal)
**Trigger:** "Y|X = x", "bivariate normal", "conditional"
**Formula:** Y|X=x ~ N(μᵧ + ρ(σᵧ/σₓ)(x-μₓ), (1-ρ²)σᵧ²)

### A6: Independence Check (MVN)
**Trigger:** "are X, Y independent?", "Gaussian vector"
**Method:** For MVN ONLY: independent ⟺ ρ = 0
**Warning:** This is UNIQUE to normal distributions!

### A7: Max/Min of Normals
**Trigger:** "max of n normal", "min of n normal"
**Method:** Use order statistics CDF formulas
**Formula:** P(max ≤ x) = [Φ((x-μ)/σ)]ⁿ

### A8: Gaussian Vector with Independent Components
**Trigger:** "Gaussian vector", "independent components"
**Meaning:** Diagonal covariance matrix, ρᵢⱼ = 0 for i≠j
**Method:** Joint = Product of marginals

### A9: Find a,b for Independence (MVN)
**Trigger:** "find a, b such that Y₁, Y₂ independent"
**Method:** Set Cov(Y₁,Y₂) = 0, solve for parameters
**Key:** For MVN, Cov = 0 means independence

### A10: P(X + Y > 0) for Bivariate Normal
**Trigger:** "P(X + Y > c)", "jointly normal"
**Method:** Find distribution of X+Y, then standardize
**Steps:** 1) E[X+Y], 2) Var(X+Y) with ρ, 3) Standardize

### A11: Conditional Expectation (Bivariate Normal)
**Trigger:** "E[Y|X=x]", "bivariate normal"
**Formula:** E[Y|X=x] = μᵧ + ρ(σᵧ/σₓ)(x-μₓ)

### A12: Conditional Variance (Bivariate Normal)
**Trigger:** "Var(Y|X=x)", "bivariate normal"
**Formula:** Var(Y|X=x) = (1-ρ²)σᵧ² (doesn't depend on x!)

---

## PATTERN CATEGORY B: CLT PROBLEMS (10 Patterns)

### B1: Basic CLT Application
**Trigger:** "large n", "approximate", "i.i.d."
**Method:** (X̄ - μ)/(σ/√n) → N(0,1)
**Steps:** 1) Find μ, σ², 2) Standardize, 3) Use Φ table

### B2: CLT for Sum
**Trigger:** "total", "sum Sₙ", "large n"
**Method:** (Sₙ - nμ)/(σ√n) ≈ N(0,1)
**Formula:** Sₙ ≈ N(nμ, nσ²)

### B3: CLT with Continuity Correction
**Trigger:** "discrete", "approximate", "binomial" + normal
**Method:** P(X ≤ k) ≈ Φ((k+0.5 - np)/√(np(1-p)))
**Key:** Add ±0.5 for discrete → continuous

### B4: Binomial Normal Approximation
**Trigger:** "Binomial", "large n", "approximate"
**Condition:** np(1-p) > 10
**Method:** X ~ Bin(n,p) ≈ N(np, np(1-p))

### B5: Poisson Normal Approximation
**Trigger:** "Poisson", "λ large", "approximate"
**Condition:** λ > 30
**Method:** X ~ Pois(λ) ≈ N(λ, λ)

### B6: Game/Coin + CLT
**Trigger:** "400 games", "total winnings", "approximate"
**Steps:** 
1) Define Xᵢ = single trial outcome
2) Find E[Xᵢ], Var(Xᵢ)
3) Apply CLT to Sₙ = ΣXᵢ

### B7: Exponential + CLT (⚠️ Common!)
**Trigger:** "i.i.d. Exp", "mean θ", "average X̄"
**Warning:** If "mean θ = 3", then λ = 1/3!
**Method:** E[Xᵢ] = 1/λ, Var(Xᵢ) = 1/λ², apply CLT

### B8: CLT for Proportion
**Trigger:** "sample proportion p̂", "large n"
**Method:** p̂ ≈ N(p, p(1-p)/n)
**Formula:** (p̂ - p)/√(p(1-p)/n) ≈ N(0,1)

### B9: Confidence Interval via CLT
**Trigger:** "confidence interval", "95%", "margin of error"
**Formula:** X̄ ± z_{α/2} · σ/√n
**Values:** 90%: z=1.645, 95%: z=1.96, 99%: z=2.576

### B10: Find Sample Size
**Trigger:** "how many samples", "precision ε"
**Method:** n ≥ (z_{α/2} · σ / ε)²

---

## PATTERN CATEGORY C: BAYESIAN PROBLEMS (10 Patterns)

### C1: Discrete Prior Update
**Trigger:** "prior P(θ=θᵢ)", "posterior", "Bayes"
**Method:** P(θᵢ|data) = P(data|θᵢ)P(θᵢ) / Σⱼ P(data|θⱼ)P(θⱼ)

### C2: Beta-Binomial Conjugate
**Trigger:** "Beta prior", "Binomial", "proportion"
**Method:** Beta(α,β) → Beta(α+k, β+n-k) after k successes in n trials

### C3: Gamma-Poisson Conjugate
**Trigger:** "Gamma prior", "Poisson", "rate"
**Method:** Gamma(α,β) → Gamma(α+Σxᵢ, β+n)

### C4: Monty Hall (Sober)
**Trigger:** "Monty Hall", "knows where car is"
**Method:** P(open B|car at A) = 1/2, P(open B|car at C) = 1
**Result:** Switch wins 2/3

### C5: Monty Hall (Dizzy)
**Trigger:** "Monty Hall", "doesn't know", "random"
**Method:** P(open B|car at A) = P(open B|car at C) = 1/2
**Result:** Doesn't matter, stay/switch both 1/2

### C6: Posterior Mean and Variance
**Trigger:** "E[θ|data]", "Var(θ|data)"
**Method:** Calculate from posterior distribution

### C7: Predictive Distribution
**Trigger:** "predict next", "P(X_{n+1}|data)"
**Method:** ∫P(X_{n+1}|θ)π(θ|data)dθ
**Beta-Binomial:** P(success) = (α+k)/(α+β+n)

### C8: Sequential Updating
**Trigger:** "observe more data", "update again"
**Method:** Posterior becomes prior for next update

### C9: Defective Rate Problem
**Trigger:** "proportion defective", "none defective"
**Method:** Binomial likelihood, update prior

### C10: Bayes Estimator
**Trigger:** "Bayes estimator", "minimize loss"
**Method:** E[θ|x] minimizes squared error

---

## PATTERN CATEGORY D: JOINT/MULTIVARIATE (8 Patterns)

### D1: Find Normalizing Constant
**Trigger:** "f(x,y) = c·g(x,y)", "find c"
**Method:** ∫∫f(x,y)dxdy = 1, solve for c

### D2: Marginal from Joint
**Trigger:** "find fₓ(x)", "marginal"
**Method:** fₓ(x) = ∫f(x,y)dy

### D3: Conditional from Joint
**Trigger:** "f(y|x)", "conditional density"
**Method:** f(y|x) = f(x,y)/fₓ(x)

### D4: Check Independence
**Trigger:** "are X, Y independent?"
**Method:** Check if f(x,y) = fₓ(x)·fᵧ(y) for ALL x,y
**Shortcut:** If f(x,y) has xy cross-term, NOT independent

### D5: E[XY] from Joint
**Trigger:** "find E[XY]", "covariance"
**Method:** E[XY] = ∫∫xy·f(x,y)dxdy

### D6: Correlation from Joint
**Trigger:** "find ρ", "correlation coefficient"
**Method:** 
1) Find E[X], E[Y], E[XY], E[X²], E[Y²]
2) Cov = E[XY] - E[X]E[Y]
3) ρ = Cov/(σₓσᵧ)

### D7: Meeting Problem
**Trigger:** "arrive uniformly", "wait at most t minutes"
**Method:** Draw unit square, find area where |X-Y| < t

### D8: Breaking Sticks
**Trigger:** "break at X uniform", "break smaller piece at Y"
**Method:** Use conditional distributions, law of total expectation

---

## PATTERN CATEGORY E: LOGNORMAL/FINANCE (6 Patterns)

### E1: Lognormal Expectation
**Trigger:** "E[S]", "S = S₀e^Z", "Z ~ N(μ,σ²)"
**Formula:** E[e^Z] = e^{μ + σ²/2}
**Key:** E[S] = S₀e^{μ + σ²/2}

### E2: Lognormal Probability
**Trigger:** "P(S > K)", "lognormal"
**Method:** P(S > K) = P(Z > ln(K/S₀)) = 1 - Φ((ln(K/S₀)-μ)/σ)

### E3: Stock Price Model
**Trigger:** "S = S₀e^Z", "Z ~ N((r-σ²/2)t, σ²t)"
**This is:** Black-Scholes setup

### E4: E[e^{-r}S] Problem (Practice Final)
**Trigger:** "E[e^{-r}S]", "discounted price"
**Method:** Use MGF of normal, simplifies to S₀

### E5: Option Pricing
**Trigger:** "call price", "E[(S-K)⁺]"
**Method:** Black-Scholes formula

### E6: Product of Lognormals
**Trigger:** "XY", "X, Y lognormal independent"
**Method:** XY = e^{Z₁+Z₂} is lognormal with μ₁+μ₂, σ₁²+σ₂²

---

## PATTERN CATEGORY F: TRANSFORMATIONS (4 Patterns)

### F1: Single Variable Transformation (1-1)
**Trigger:** "Y = g(X)", "find fᵧ(y)"
**Method:** fᵧ(y) = fₓ(g⁻¹(y))|dg⁻¹/dy|

### F2: CDF Method
**Trigger:** "find distribution of Y = g(X)"
**Method:** Fᵧ(y) = P(g(X) ≤ y), then differentiate

### F3: Jacobian (2D)
**Trigger:** "(U,V) = g(X,Y)", "find f_{UV}"
**Method:** f_{UV}(u,v) = f_{XY}(x(u,v),y(u,v))|J|
**Key:** Don't forget absolute value!

### F4: Order Statistics
**Trigger:** "max", "min", "X_{(k)}"
**Formulas:** 
- F_{max}(x) = [F(x)]ⁿ
- F_{min}(x) = 1 - [1-F(x)]ⁿ

---

## 🚨 EXAM PANIC PROTOCOL

### Step 1: READ the entire problem
- Underline key terms
- Circle distribution names/synonyms

### Step 2: IDENTIFY the pattern
- Look for keywords in list above
- Match to pattern category

### Step 3: RECALL the method
- Write down relevant formula
- Check parameters

### Step 4: EXECUTE
- Show all work
- Box final answer

### Step 5: VERIFY
- Does answer make sense?
- Is probability between 0 and 1?
- Check units/dimensions

---

_End of Comprehensive Decision Tree (Version 3.0 - 50+ Patterns)_
