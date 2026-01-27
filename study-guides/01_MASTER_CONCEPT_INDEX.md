# Master Concept Index - Probability Theory

**Generated:** December 16, 2025
**Purpose:** Alphabetical concept index with formulas, properties, and file references

---

## A

### Additivity (Finite)
- **Definition:** If A ∩ B = ∅, then P(A ∪ B) = P(A) + P(B)
- **References:** `lectures/chapter1.txt`
- **Introduced:** Pre-Midterm 1

### Axioms of Probability
- **Three Axioms:**
  1. Normalization: P(S) = 1
  2. Non-negativity: P(A) ≥ 0
  3. Additivity: P(A ∪ B) = P(A) + P(B) for disjoint A, B
- **References:** `lectures/chapter1.txt`
- **Introduced:** Pre-Midterm 1

---

## B

### Bayes' Theorem
- **Formula:** P(A|B) = P(B|A)P(A) / P(B)
- **Extended Form:** P(Bi|A) = P(A|Bi)P(Bi) / ∑P(A|Bj)P(Bj)
- **References:** `lectures/chapter2.txt`, `homeworks/hw2/hw2.txt`
- **Introduced:** Pre-Midterm 1
- **Applications:** Machine defects, medical diagnosis, Monty Hall

### Bernoulli Distribution
- **PMF:** P(X = x) = p^x(1-p)^(1-x), x ∈ {0,1}
- **Mean:** E[X] = p
- **Variance:** Var(X) = p(1-p)
- **MGF:** ψ(t) = (1-p) + pe^t
- **References:** `lectures/chapter5.txt`
- **Introduced:** Between Midterms

### Beta Distribution
- **PDF:** f(x) = [Γ(α+β)/(Γ(α)Γ(β))] x^(α-1)(1-x)^(β-1), 0 < x < 1
- **Mean:** E[X] = α/(α+β)
- **Variance:** Var(X) = αβ/[(α+β)²(α+β+1)]
- **References:** `lectures/chapter5.txt`, `homeworks/hw6/`
- **Introduced:** Post-Midterm 2
- **Note:** Conjugate prior for Binomial

### Binomial Distribution
- **PMF:** P(X = k) = C(n,k)p^k(1-p)^(n-k)
- **Mean:** E[X] = np
- **Variance:** Var(X) = np(1-p)
- **MGF:** ψ(t) = (1-p+pe^t)^n
- **References:** `lectures/chapter5.txt`
- **Introduced:** Between Midterms

### Bivariate Normal Distribution 🔥
- **Joint PDF:** Complex formula with correlation ρ
- **Properties:** Linear combinations are normal
- **Independence:** X,Y independent iff ρ = 0
- **References:** `lectures/chapter5.txt`, `homeworks/hw5/`
- **Introduced:** Post-Midterm 2

---

## C

### Central Limit Theorem (CLT) 🔥
- **Statement:** (X̄ - μ)/(σ/√n) → N(0,1) as n → ∞
- **Conditions:** iid variables, finite variance
- **Continuity Correction:** Add ±0.5 for discrete approximations
- **References:** `lectures/chapter4.txt`, `homeworks/hw5/`, `homeworks/hw6/`
- **Introduced:** Post-Midterm 2
- **Applications:** Normal approximations, confidence intervals

### Combinations
- **Formula:** C(n,k) = n!/(k!(n-k)!)
- **Properties:** C(n,k) = C(n,n-k)
- **References:** `lectures/chapter1.txt`
- **Introduced:** Pre-Midterm 1

### Conditional Expectation 🔥
- **Discrete:** E[X|Y=y] = ∑x · P(X=x|Y=y)
- **Continuous:** E[X|Y=y] = ∫x · f(x|y)dx
- **Law of Total Expectation:** E[X] = E[E[X|Y]]
- **Tower Property:** E[E[X|Y,Z]|Y] = E[X|Y]
- **References:** `practice-exams/professor-provided-review.txt`
- **Introduced:** Post-Midterm 2

### Conditional Probability
- **Definition:** P(A|B) = P(A ∩ B)/P(B)
- **Multiplication Rule:** P(A ∩ B) = P(B)P(A|B)
- **Chain Rule:** P(A₁∩...∩Aₙ) = P(A₁)P(A₂|A₁)...P(Aₙ|A₁∩...∩Aₙ₋₁)
- **References:** `lectures/chapter2.txt`
- **Introduced:** Pre-Midterm 1

### Conditional Variance
- **Formula:** Var(X|Y=y) = E[(X - E[X|Y=y])²|Y=y]
- **Law of Total Variance:** Var(X) = E[Var(X|Y)] + Var(E[X|Y])
- **References:** `practice-exams/professor-provided-review.txt`
- **Introduced:** Post-Midterm 2

### Conjugate Priors 🔥
- **Beta-Binomial:** Beta prior → Beta posterior
- **Gamma-Poisson:** Gamma prior → Gamma posterior
- **Normal-Normal:** Normal prior → Normal posterior
- **References:** `homeworks/hw6/`
- **Introduced:** Post-Midterm 2

### Correlation
- **Formula:** ρ(X,Y) = Cov(X,Y)/(σₓσᵧ)
- **Range:** -1 ≤ ρ ≤ 1
- **Independence:** Independent → ρ = 0 (not vice versa)
- **References:** `lectures/chapter4.txt`, `homeworks/hw4/`
- **Introduced:** Between Midterms

### Covariance
- **Formula:** Cov(X,Y) = E[(X-μₓ)(Y-μᵧ)] = E[XY] - E[X]E[Y]
- **Properties:** Cov(X,X) = Var(X), Cov(aX+b, cY+d) = ac·Cov(X,Y)
- **References:** `lectures/chapter4.txt`, `homeworks/hw4/`
- **Introduced:** Between Midterms

### Cumulative Distribution Function (CDF)
- **Definition:** F(x) = P(X ≤ x)
- **Properties:** Non-decreasing, right-continuous, F(-∞)=0, F(∞)=1
- **References:** `lectures/chapter3.txt`
- **Introduced:** Between Midterms

---

## D

### DeMorgan's Laws
- **(A ∪ B)ᶜ = Aᶜ ∩ Bᶜ**
- **(A ∩ B)ᶜ = Aᶜ ∪ Bᶜ**
- **References:** `lectures/chapter1.txt`
- **Introduced:** Pre-Midterm 1

---

## E

### Expectation (Expected Value)
- **Discrete:** E[X] = ∑x·P(X=x)
- **Continuous:** E[X] = ∫x·f(x)dx
- **Linearity:** E[aX+b] = aE[X]+b
- **Functions:** E[g(X)] = ∑g(x)P(X=x) or ∫g(x)f(x)dx
- **References:** `lectures/chapter4.txt`
- **Introduced:** Between Midterms

### Exponential Distribution
- **PDF:** f(x) = λe^(-λx), x > 0
- **Mean:** E[X] = 1/λ
- **Variance:** Var(X) = 1/λ²
- **MGF:** ψ(t) = λ/(λ-t), t < λ
- **Memoryless Property:** P(X > s+t|X > s) = P(X > t)
- **References:** `lectures/chapter5.txt`
- **Introduced:** Post-Midterm 2

---

## G

### Gamma Distribution
- **PDF:** f(x) = [λʳ/Γ(r)]x^(r-1)e^(-λx), x > 0
- **Mean:** E[X] = r/λ
- **Variance:** Var(X) = r/λ²
- **Special Cases:** r=1 gives Exponential(λ)
- **References:** `lectures/chapter5.txt`
- **Introduced:** Post-Midterm 2

### Geometric Distribution
- **PMF:** P(X = k) = p(1-p)^k, k = 0,1,2,...
- **Mean:** E[X] = (1-p)/p
- **Variance:** Var(X) = (1-p)/p²
- **Memoryless Property:** P(X = k+t|X ≥ k) = P(X = t)
- **References:** `lectures/chapter5.txt`
- **Introduced:** Between Midterms

---

## H

### Hypergeometric Distribution
- **PMF:** P(X = k) = [C(r,k)C(b,n-k)]/C(r+b,n)
- **Context:** Sampling without replacement
- **Mean:** E[X] = nr/(r+b)
- **Variance:** Complex formula involving finite population correction
- **References:** `lectures/chapter5.txt`
- **Introduced:** Between Midterms

---

## I

### Independence
- **Events:** P(A ∩ B) = P(A)P(B)
- **Random Variables:** F(x,y) = Fₓ(x)Fᵧ(y)
- **Test:** f(x,y) = fₓ(x)fᵧ(y) for all x,y
- **Consequences:** E[XY] = E[X]E[Y], Cov(X,Y) = 0
- **References:** `lectures/chapter2.txt`, `homeworks/hw4/`
- **Introduced:** Pre-Midterm 1

### Indicator Random Variables
- **Definition:** I_A = 1 if A occurs, 0 otherwise
- **Mean:** E[I_A] = P(A)
- **Variance:** Var(I_A) = P(A)(1-P(A))
- **References:** `practice-exams/professor-provided-review.txt`
- **Introduced:** Between Midterms

---

## J

### Jacobian (Transformations) 🔥
- **Formula:** |J| = |∂(x,y)/∂(u,v)|
- **Use:** Transform joint densities
- **References:** `lectures/chapter3.txt`, `homeworks/hw4/`
- **Introduced:** Post-Midterm 2

### Jensen's Inequality
- **Statement:** For convex g: E[g(X)] ≥ g(E[X])
- **Example:** E[X²] ≥ (E[X])²
- **References:** `practice-exams/professor-provided-review.txt`
- **Introduced:** Between Midterms

### Joint Distributions
- **Discrete:** P(X=x, Y=y) = pₓᵧ(x,y)
- **Continuous:** Joint PDF f(x,y)
- **Marginals:** fₓ(x) = ∫f(x,y)dy
- **References:** `homeworks/hw4/`
- **Introduced:** Between Midterms

---

## L

### Law of Large Numbers (LLN) 🔥
- **Weak LLN:** X̄ →ᵖ μ as n → ∞
- **Strong LLN:** X̄ →ᵃ·ˢ· μ as n → ∞
- **Condition:** Finite mean (weak), finite variance (strong)
- **References:** `lectures/chapter4.txt`
- **Introduced:** Post-Midterm 2

### Law of Total Expectation
- **Formula:** E[X] = E[E[X|Y]]
- **Discrete:** E[X] = ∑E[X|Y=y]P(Y=y)
- **Continuous:** E[X] = ∫E[X|Y=y]fᵧ(y)dy
- **References:** `practice-exams/professor-provided-review.txt`
- **Introduced:** Post-Midterm 2

### Law of Total Probability
- **Formula:** P(A) = ∑P(A|Bᵢ)P(Bᵢ)
- **Condition:** {Bᵢ} forms a partition
- **References:** `lectures/chapter2.txt`
- **Introduced:** Pre-Midterm 1

### Law of Total Variance
- **Formula:** Var(X) = E[Var(X|Y)] + Var(E[X|Y])
- **References:** `practice-exams/professor-provided-review.txt`
- **Introduced:** Post-Midterm 2

### Lognormal Distribution 🔥
- **Definition:** Y = e^X where X ~ N(μ,σ²)
- **PDF:** Complex formula
- **Mean:** E[Y] = exp(μ + σ²/2)
- **Applications:** Stock prices, finance
- **References:** `homeworks/hw5/`, `practice-exams/final-practice.txt`
- **Introduced:** Post-Midterm 2

---

## M

### Marginal Distributions
- **Discrete:** pₓ(x) = ∑ᵧp(x,y)
- **Continuous:** fₓ(x) = ∫f(x,y)dy
- **References:** `homeworks/hw4/`
- **Introduced:** Between Midterms

### Median
- **Definition:** Value m where P(X ≤ m) ≥ 0.5 and P(X ≥ m) ≥ 0.5
- **Property:** Minimizes E[|X - d|]
- **References:** `lectures/chapter4.txt`
- **Introduced:** Between Midterms

### Memoryless Property
- **Exponential:** P(X > s+t|X > s) = P(X > t)
- **Geometric:** P(X = k+t|X ≥ k) = P(X = t)
- **References:** `lectures/chapter5.txt`
- **Introduced:** Post-Midterm 2

### Moment Generating Function (MGF) 🔥
- **Definition:** M(t) = E[e^(tX)]
- **Properties:** 
  - M'(0) = E[X]
  - M''(0) = E[X²]
  - Uniqueness: Same MGF → Same distribution
- **Sum of Independent:** Mₓ₊ᵧ(t) = Mₓ(t)Mᵧ(t)
- **References:** `lectures/chapter4.txt`, `homeworks/hw3/`
- **Introduced:** Post-Midterm 2

### Moments
- **k-th Moment:** E[X^k]
- **Central Moment:** E[(X-μ)^k]
- **Standardized:** E[((X-μ)/σ)^k]
- **References:** `lectures/chapter4.txt`
- **Introduced:** Between Midterms

### Multinomial Coefficients
- **Formula:** n!/(n₁!n₂!...nₖ!)
- **Use:** Counting arrangements with repetitions
- **References:** `lectures/chapter1.txt`
- **Introduced:** Pre-Midterm 1

### Multinomial Distribution
- **PMF:** P(X₁=n₁,...,Xₖ=nₖ) = [n!/(∏nᵢ!)]∏pᵢ^(nᵢ)
- **Mean:** E[Xᵢ] = npᵢ
- **Covariance:** Cov(Xᵢ,Xⱼ) = -npᵢpⱼ
- **References:** `lectures/chapter5.txt`
- **Introduced:** Post-Midterm 2

### Multiplication Rule
- **Two Events:** P(A ∩ B) = P(B)P(A|B)
- **Chain:** P(A₁∩...∩Aₙ) = P(A₁)P(A₂|A₁)...
- **References:** `lectures/chapter2.txt`
- **Introduced:** Pre-Midterm 1

---

## N

### Negative Binomial Distribution
- **PMF:** P(X = k) = C(k+r-1,k)p^r(1-p)^k
- **Context:** Failures before r-th success
- **Mean:** E[X] = r(1-p)/p
- **Variance:** Var(X) = r(1-p)/p²
- **References:** `lectures/chapter5.txt`
- **Introduced:** Between Midterms

### Normal Distribution 🔥
- **PDF:** f(x) = (1/√(2πσ²))exp(-(x-μ)²/(2σ²))
- **Mean:** E[X] = μ
- **Variance:** Var(X) = σ²
- **MGF:** ψ(t) = exp(μt + σ²t²/2)
- **Standard Normal:** Z = (X-μ)/σ ~ N(0,1)
- **References:** `lectures/chapter5.txt`
- **Introduced:** Post-Midterm 2

### Normal Approximation 🔥
- **Binomial:** np(1-p) > 10 recommended
- **Poisson:** λ > 30 recommended
- **Continuity Correction:** Add ±0.5
- **References:** `homeworks/hw5/`, `homeworks/hw6/`
- **Introduced:** Post-Midterm 2

---

## O

### Order Statistics
- **Definition:** X₍₁₎ ≤ X₍₂₎ ≤ ... ≤ X₍ₙ₎
- **Min:** X₍₁₎ = min(X₁,...,Xₙ)
- **Max:** X₍ₙ₎ = max(X₁,...,Xₙ)
- **PDF formulas:** Complex, involve (n-1)! terms
- **References:** `homeworks/hw4/`
- **Introduced:** Between Midterms

---

## P

### Partition
- **Definition:** Disjoint sets {Bᵢ} with ∪Bᵢ = S
- **Use:** Law of Total Probability
- **References:** `lectures/chapter2.txt`
- **Introduced:** Pre-Midterm 1

### Permutations
- **Formula:** P(n,k) = n!/(n-k)!
- **With Repetition:** n^k
- **References:** `lectures/chapter1.txt`
- **Introduced:** Pre-Midterm 1

### Poisson Distribution
- **PMF:** P(X = k) = e^(-λ)λ^k/k!
- **Mean:** E[X] = λ
- **Variance:** Var(X) = λ
- **MGF:** ψ(t) = exp(λ(e^t - 1))
- **Poisson Process:** Rate λ per unit time
- **References:** `lectures/chapter5.txt`
- **Introduced:** Between Midterms

### Poisson Process
- **Properties:** 
  1. Arrivals in interval t ~ Poisson(λt)
  2. Disjoint intervals independent
- **References:** `lectures/chapter5.txt`
- **Introduced:** Post-Midterm 2

### Posterior Distribution 🔥
- **Formula:** π(θ|x) ∝ L(x|θ)π(θ)
- **Bayesian Update:** Prior × Likelihood → Posterior
- **References:** `homeworks/hw6/`
- **Introduced:** Post-Midterm 2

### Prior Distribution 🔥
- **Definition:** Distribution of parameter before data
- **Types:** Informative, non-informative, conjugate
- **References:** `homeworks/hw6/`
- **Introduced:** Post-Midterm 2

### Probability Density Function (PDF)
- **Properties:** f(x) ≥ 0, ∫f(x)dx = 1
- **CDF Relation:** F'(x) = f(x)
- **References:** `lectures/chapter3.txt`
- **Introduced:** Between Midterms

### Probability Integral Transform
- **Theorem:** If X has CDF F, then F(X) ~ Uniform(0,1)
- **Inverse:** If U ~ Uniform(0,1), then F⁻¹(U) has CDF F
- **References:** `lectures/chapter3.txt`
- **Introduced:** Between Midterms

### Probability Mass Function (PMF)
- **Definition:** P(X = x) for discrete X
- **Properties:** p(x) ≥ 0, ∑p(x) = 1
- **References:** `lectures/chapter3.txt`
- **Introduced:** Between Midterms

---

## Q

### Quantile Function
- **Definition:** F⁻¹(p) = inf{x: F(x) ≥ p}
- **Use:** Random variable generation
- **References:** `lectures/chapter3.txt`
- **Introduced:** Between Midterms

---

## R

### Random Variable
- **Definition:** Function from sample space to real numbers
- **Types:** Discrete (countable), Continuous (uncountable)
- **References:** `lectures/chapter3.txt`
- **Introduced:** Between Midterms

---

## S

### Sample Space
- **Definition:** Set of all possible outcomes
- **Properties:** Mutually exclusive, collectively exhaustive
- **Notation:** S or Ω
- **References:** `lectures/chapter1.txt`
- **Introduced:** Pre-Midterm 1

### Standard Deviation
- **Formula:** σ = √Var(X)
- **Interpretation:** Typical deviation from mean
- **References:** `lectures/chapter4.txt`
- **Introduced:** Between Midterms

### Standard Normal
- **Definition:** Z ~ N(0,1)
- **PDF:** φ(z) = (1/√(2π))exp(-z²/2)
- **CDF:** Φ(z) = ∫_{-∞}^z φ(t)dt
- **References:** `lectures/chapter5.txt`
- **Introduced:** Post-Midterm 2

---

## T

### Transformations of Random Variables
- **One-to-One:** g(y) = f(h(y))|h'(y)|
- **Jacobian Method:** For multivariate
- **CDF Method:** Find F_Y, then differentiate
- **References:** `lectures/chapter3.txt`, `homeworks/hw4/`
- **Introduced:** Between Midterms/Post-Midterm 2

---

## U

### Uniform Distribution
- **Discrete:** P(X = k) = 1/n, k = 1,...,n
- **Continuous PDF:** f(x) = 1/(b-a), a < x < b
- **Mean:** E[X] = (a+b)/2
- **Variance:** Var(X) = (b-a)²/12
- **References:** `lectures/chapter5.txt`
- **Introduced:** Between Midterms

### Union Bound
- **Formula:** P(∪Aᵢ) ≤ ∑P(Aᵢ)
- **References:** `lectures/chapter1.txt`
- **Introduced:** Pre-Midterm 1

---

## V

### Variance
- **Formula:** Var(X) = E[(X-μ)²] = E[X²] - (E[X])²
- **Properties:** Var(aX+b) = a²Var(X)
- **Sum of Independent:** Var(X+Y) = Var(X) + Var(Y)
- **References:** `lectures/chapter4.txt`
- **Introduced:** Between Midterms

---

## FORMULA QUICK REFERENCE

### Key Probability Formulas
1. **Bayes:** P(A|B) = P(B|A)P(A)/P(B)
2. **Total Probability:** P(A) = ∑P(A|Bᵢ)P(Bᵢ)
3. **Independence:** P(A∩B) = P(A)P(B)

### Key Expectation Formulas
1. **Linearity:** E[aX+b] = aE[X]+b
2. **Law of Total:** E[X] = E[E[X|Y]]
3. **Variance:** Var(X) = E[X²] - (E[X])²
4. **Covariance:** Cov(X,Y) = E[XY] - E[X]E[Y]

### Key Distribution Formulas
1. **Binomial:** P(X=k) = C(n,k)p^k(1-p)^(n-k)
2. **Poisson:** P(X=k) = e^(-λ)λ^k/k!
3. **Normal:** f(x) = (1/√(2πσ²))exp(-(x-μ)²/(2σ²))
4. **Exponential:** f(x) = λe^(-λx)

### CLT & Approximations 🔥
1. **CLT:** √n(X̄-μ)/σ → N(0,1)
2. **Binomial Approx:** X ~ N(np, np(1-p))
3. **Continuity Correction:** P(X=k) ≈ P(k-0.5 < Y < k+0.5)

---

## CONCEPT DEPENDENCY GRAPH

```
Probability Axioms
    ├── Sample Space & Events
    ├── Conditional Probability
    │   ├── Independence
    │   ├── Bayes' Theorem
    │   └── Total Probability
    └── Random Variables
        ├── Discrete
        │   ├── PMF
        │   ├── Expectation
        │   └── Special Distributions
        ├── Continuous
        │   ├── PDF/CDF
        │   ├── Transformations
        │   └── Special Distributions
        └── Joint/Multivariate
            ├── Marginals
            ├── Conditional Distributions
            ├── Covariance/Correlation
            └── Bivariate Normal
                └── CLT & Limit Theorems
```

---

## CHRONOLOGICAL INTRODUCTION

### Pre-Midterm 1 (Before Oct 2)
- Probability axioms, sample spaces
- Counting methods, combinatorics
- Conditional probability, independence
- Bayes' theorem

### Between Midterms (Oct 2 - Nov 6)
- Random variables (discrete/continuous)
- PMF, PDF, CDF
- Expectation, variance
- Special distributions (basic)
- Joint distributions
- Covariance, correlation

### Post-Midterm 2 (After Nov 6) 🔥
- Moment generating functions
- Bivariate Normal
- Law of Large Numbers
- Central Limit Theorem
- Bayesian statistics
- Conditional expectation
- Advanced transformations
- Finance applications

---

_End of Master Concept Index_
