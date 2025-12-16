# COMPREHENSIVE DECISION TREE - 10-15 Page Version

**Generated:** December 16, 2025  
**Purpose:** Exhaustive decision tree covering EVERY possible question wording  
**Status:** Phase 13 - Massively Expanded Decision Tree

---

## HOW TO USE THIS TREE

1. **Start at ROOT (Page 1)**
2. **Answer each question** (Yes/No or select option)
3. **Follow the path** to terminal node or next branch
4. **Each terminal node shows:**
   - Section reference in cheat sheet
   - Key formula reminder
   - 2-3 keyword indicators
   - Common professor phrasing
   - Solution approach summary

---

# PAGE 1: ROOT CLASSIFICATION

```
═══════════════════════════════════════════════════════════════
DECISION TREE LEVEL 0: INITIAL CLASSIFICATION
═══════════════════════════════════════════════════════════════

START: Read the problem completely. Look for key terms.

┌─ Does problem mention specific distribution NAME?
│  ├─ "Normal" / "Gaussian" / "N(μ,σ²)" → See TREE BRANCH A (Page 2)
│  ├─ "Exponential" / "Exp(λ)" / "memoryless" → See TREE BRANCH B (Page 2)
│  ├─ "Poisson" / "counting process" / "arrivals" → See TREE BRANCH C (Page 3)
│  ├─ "Binomial" / "n trials" / "success/failure" → See TREE BRANCH D (Page 3)
│  ├─ "Geometric" / "first success" → See TREE BRANCH E (Page 4)
│  ├─ "Uniform" / "equally likely" → See TREE BRANCH F (Page 4)
│  ├─ "Gamma" / "Erlang" / "sum of exponentials" → See TREE BRANCH G (Page 4)
│  ├─ "Lognormal" / "stock price" / "e^X where X normal" → See TREE BRANCH H (Page 5)
│  ├─ "Beta" / "conjugate prior" → See TREE BRANCH I (Page 5)
│  └─ Other named distribution → See TREE BRANCH J (Page 5)

├─ Does problem describe a PROCESS or SCENARIO without naming distribution?
│  ├─ "Arrival process" / "events over time" → Likely Poisson, see TREE BRANCH C
│  ├─ "Waiting time between events" → Likely Exponential, see TREE BRANCH B
│  ├─ "Repeated trials until success" → Geometric/Negative Binomial, see TREE BRANCH E
│  ├─ "Random selection" / "draw from population" → See TREE BRANCH K (Page 5)
│  ├─ "Stock price" / "financial" → Likely Lognormal, see TREE BRANCH H
│  └─ Other scenario → See TREE BRANCH J (Page 6)

├─ Does problem ask about MULTIPLE random variables?
│  ├─ "Joint distribution" / "f(x,y)" → See TREE BRANCH K (Page 6)
│  ├─ "Sum of" / "X₁ + X₂ + ... + Xₙ" → See TREE BRANCH L (Page 7)
│  ├─ "Maximum/Minimum of" / "max{X₁,...,Xₙ}" → See TREE BRANCH M (Page 7)
│  ├─ "Product" / "XY" → See TREE BRANCH N (Page 8)
│  ├─ "Ratio" / "X/Y" → See TREE BRANCH N (Page 8)
│  ├─ "Conditional" / "X given Y" / "X|Y" → See TREE BRANCH O (Page 8)
│  ├─ "Gaussian vector" / "multivariate normal" → See TREE BRANCH A (Page 2)
│  └─ "Independent components" → See TREE BRANCH A (Page 2) - MVN with diagonal covariance

├─ Does problem ask about MOMENTS or GENERATING FUNCTIONS?
│  ├─ "MGF" / "moment generating function" / "ψ(t)" → See TREE BRANCH P (Page 9)
│  ├─ "E[X]" / "expected value" / "mean" → See TREE BRANCH Q (Page 9)
│  ├─ "Var(X)" / "variance" → See TREE BRANCH Q (Page 9)
│  ├─ "Cov(X,Y)" / "covariance" → See TREE BRANCH R (Page 10)
│  ├─ "Correlation" / "ρ" → See TREE BRANCH R (Page 10)
│  └─ "E[X|Y]" / "conditional expectation" → See TREE BRANCH O (Page 8)

├─ Does problem involve LIMITS or APPROXIMATIONS?
│  ├─ "As n → ∞" / "large n" → See TREE BRANCH S (Page 10)
│  ├─ "Approximate" → See TREE BRANCH S (Page 10)
│  ├─ "Converges" → See TREE BRANCH S (Page 10)
│  ├─ "CLT" / "Central Limit Theorem" → See TREE BRANCH S (Page 10)
│  └─ "Law of Large Numbers" / "LLN" → See TREE BRANCH S (Page 10)

├─ Does problem ask for PROOF or DERIVATION?
│  └─ See TREE BRANCH T (Page 11)

└─ Does problem involve BAYESIAN STATISTICS?
   ├─ "Update" / "posterior" / "prior" → See TREE BRANCH U (Page 11)
   ├─ "Bayes" / "Bayesian" → See TREE BRANCH U (Page 11)
   ├─ "Conjugate prior" → See TREE BRANCH U (Page 11)
   └─ "Likelihood" → See TREE BRANCH U (Page 11)
```

---

# PAGE 2: TREE BRANCH A - NORMAL/GAUSSIAN PROBLEMS

```
═══════════════════════════════════════════════════════════════
TREE BRANCH A: NORMAL/GAUSSIAN PROBLEMS
═══════════════════════════════════════════════════════════════

You identified: Normal/Gaussian distribution mentioned

KEY SYNONYMS TO REMEMBER:
- Gaussian ≡ Normal ≡ N(μ,σ²)
- Gaussian vector ≡ Multivariate normal ≡ MVN
- Standard normal ≡ N(0,1) ≡ Z
- "Independent components" means diagonal covariance matrix

┌─ Is it a SINGLE Gaussian random variable?
│  ├─ Problem: "X ~ N(μ,σ²), find P(X > a)"
│  │  → **Solution**: Standardize: Z = (X-μ)/σ, use Φ table
│  │  → **Section**: 3.2.1 - Standard Normal Calculations
│  │  → **Formula**: P(X > a) = 1 - Φ((a-μ)/σ)
│  │  → **Keywords**: "normal", "probability", "P(X > a)"
│  │
│  ├─ Problem: "X ~ N(μ,σ²), find E[g(X)]" 
│  │  ├─ Is g(X) linear? → E[aX+b] = aμ+b (Section 3.2.2)
│  │  ├─ Is g(X) = X²? → E[X²] = μ² + σ² (Section 3.2.3)
│  │  └─ Other g(X)? → Integration or MGF (Section 3.2.4)
│  │
│  └─ Problem: "X ~ N(μ,σ²), find distribution of Y = aX + b"
│     → **Solution**: Y ~ N(aμ+b, a²σ²)
│     → **Section**: 3.2.5 - Linear Transformations of Normal
│     → **Keywords**: "transform", "linear", "distribution of"

├─ Is it MULTIPLE independent Gaussians?
│  ├─ Problem: "X₁,...,Xₙ i.i.d. N(μ,σ²), find distribution of X̄ = (1/n)Σᵢ Xᵢ"
│  │  → **Solution**: X̄ ~ N(μ, σ²/n)
│  │  → **Section**: 3.3.1 - Sample Mean of Normals
│  │  → **Keywords**: "sample mean", "average", "i.i.d."
│  │
│  ├─ Problem: "X ~ N(μ₁,σ₁²), Y ~ N(μ₂,σ₂²) independent, find distribution of X+Y"
│  │  → **Solution**: X+Y ~ N(μ₁+μ₂, σ₁²+σ₂²)
│  │  → **Section**: 3.3.2 - Sum of Independent Normals
│  │  → **Keywords**: "sum", "independent", "distribution of"
│  │
│  └─ Problem: "X₁,...,Xₙ i.i.d. N(μ,σ²), find P(max Xᵢ > a)"
│     → **Solution**: P(max > a) = 1 - [Φ((a-μ)/σ)]ⁿ
│     → **Section**: 3.3.3 - Order Statistics of Normals
│     → **Keywords**: "maximum", "max", "order statistics"
│     → **Method**: Use independence: P(all ≤ a) = [P(X₁ ≤ a)]ⁿ

├─ Is it a GAUSSIAN VECTOR (multivariate)?
│  ├─ Problem mentions "Gaussian vector" / "multivariate normal" / "jointly normal"
│  │  ├─ Are components independent?
│  │  │  → **Key insight**: Independent components means diagonal covariance
│  │  │  → Joint PDF factors: f(x₁,...,xₙ) = ∏ fᵢ(xᵢ)
│  │  │  → **Section**: 4.3.1 - MVN with Independent Components
│  │  │  → **Keywords**: "independent components", "diagonal covariance"
│  │  │
│  │  ├─ Are components correlated?
│  │  │  → Need full covariance matrix
│  │  │  → **Section**: 4.3.2 - General Multivariate Normal
│  │  │  → **Keywords**: "correlated", "covariance matrix", "ρ"
│  │  │
│  │  └─ Problem: "Find marginal distribution"
│  │     → Marginals of MVN are univariate normal
│  │     → **Section**: 4.3.3 - Marginals of MVN
│  │     → **Keywords**: "marginal", "marginal distribution"
│  │
│  └─ Problem: "Linear transformation of Gaussian vector"
│     → If X ~ N(μ, Σ), then AX + b ~ N(Aμ+b, AΣAᵀ)
│     → **Section**: 4.3.4 - Linear Transformations of MVN
│     → **Keywords**: "linear transformation", "matrix transformation"

└─ Is it about STANDARD normal specifically?
   ├─ Problem: "Z ~ N(0,1), find P(|Z| > a)"
   │  → P(|Z| > a) = 2[1 - Φ(a)]
   │  → **Section**: 3.2.6 - Standard Normal Special Cases
   │  → **Keywords**: "standard normal", "absolute value"
   │
   └─ Problem: "Z ~ N(0,1), find E[Z²ⁿ]"
      → Use moment formula: E[Z²ⁿ] = (2n)!/(2ⁿ n!)
      → **Section**: 3.2.7 - Moments of Standard Normal
      → **Keywords**: "moments", "even moments"
```

---

# PAGE 3: TREE BRANCH B - EXPONENTIAL PROBLEMS

```
═══════════════════════════════════════════════════════════════
TREE BRANCH B: EXPONENTIAL DISTRIBUTION PROBLEMS
═══════════════════════════════════════════════════════════════

You identified: Exponential distribution mentioned

KEY SYNONYMS:
- Exponential ≡ Exp(λ) ≡ Memoryless continuous
- "Exponentially distributed with mean θ" → Exp(1/θ) [Note: mean = 1/λ]
- "Waiting time" → Often Exponential
- "Time until event" → Often Exponential

┌─ Single Exponential?
│  ├─ Problem: "X ~ Exp(λ), find P(X > t)"
│  │  → **Solution**: P(X > t) = e^(-λt)
│  │  → **Section**: 3.3 - Exponential Distribution
│  │  → **Formula**: CDF F(x) = 1 - e^(-λx)
│  │
│  ├─ Problem: "X ~ Exp(λ), find E[X]"
│  │  → **Solution**: E[X] = 1/λ
│  │  → **Section**: 3.3 - Exponential Distribution
│  │  → **Note**: If problem says "mean θ", then λ = 1/θ
│  │
│  └─ Problem: "Memoryless property"
│     → **Key**: P(X > s+t | X > s) = P(X > t)
│     → **Section**: 3.3 - Memoryless Property
│     → **Keywords**: "memoryless", "no memory"

├─ Multiple Exponentials?
│  ├─ Problem: "X₁,...,Xₙ i.i.d. Exp(λ), find distribution of sum"
│  │  → **Solution**: Sum ~ Gamma(n, λ)
│  │  → **Section**: 3.5 - Gamma Distribution
│  │  → **Method**: Use MGF or convolution
│  │
│  ├─ Problem: "X₁,...,Xₙ i.i.d. Exp(λ), find P(min Xᵢ > t)"
│  │  → **Solution**: P(min > t) = [e^(-λt)]ⁿ = e^(-nλt)
│  │  → **Section**: 4.7 - Order Statistics
│  │  → **Method**: Use independence and complement
│  │
│  └─ Problem: "X₁,...,Xₙ i.i.d. Exp(λ), find E[X̄] using CLT"
│     → **Solution**: Apply CLT: X̄ ≈ N(1/λ, 1/(nλ²))
│     → **Section**: 6.1 - CLT
│     → **Keywords**: "large n", "approximate", "CLT"

└─ Exponential in Context?
   ├─ Problem: "Poisson process with rate λ, find time until first arrival"
   │  → **Solution**: Time ~ Exp(λ)
   │  → **Section**: 3.3 - Exponential, 2.3 - Poisson Process
   │  → **Connection**: Inter-arrival times of Poisson are Exponential
   │
   └─ Problem: "Waiting time" / "Service time" / "Lifetime"
      → Often Exponential if memoryless property applies
      → **Section**: 3.3 - Exponential Distribution
```

---

# PAGE 4: TREE BRANCH C - POISSON PROBLEMS

```
═══════════════════════════════════════════════════════════════
TREE BRANCH C: POISSON DISTRIBUTION & PROCESS PROBLEMS
═══════════════════════════════════════════════════════════════

You identified: Poisson mentioned

KEY SYNONYMS:
- Poisson ≡ Poisson Process ≡ Counting process ≡ Arrival process
- "Rate λ" → Poisson(λt) for interval of length t
- "Arrivals" → Poisson
- "Rare events" → Poisson approximation

┌─ Single Poisson?
│  ├─ Problem: "X ~ Poisson(λ), find P(X = k)"
│  │  → **Solution**: P(X = k) = e^(-λ)λ^k/k!
│  │  → **Section**: 2.3 - Poisson Distribution
│  │
│  ├─ Problem: "X ~ Poisson(λ), find E[X]"
│  │  → **Solution**: E[X] = λ, Var(X) = λ
│  │  → **Section**: 2.3 - Poisson Distribution
│  │
│  └─ Problem: "Approximate Poisson with Normal"
│     → If λ > 30: X ≈ N(λ, λ)
│     → **Section**: 6.2 - Normal Approximation
│     → **Keywords**: "approximate", "large λ"

├─ Poisson Process?
│  ├─ Problem: "Arrivals at rate λ, find number in time t"
│  │  → **Solution**: N(t) ~ Poisson(λt)
│  │  → **Section**: 2.3 - Poisson Process
│  │  → **Keywords**: "rate", "per unit time", "arrivals"
│  │
│  ├─ Problem: "Time between arrivals"
│  │  → **Solution**: Inter-arrival time ~ Exp(λ)
│  │  → **Section**: 3.3 - Exponential (connected to Poisson)
│  │  → **Key**: Inter-arrival times of Poisson are Exponential
│  │
│  └─ Problem: "Sum of independent Poissons"
│     → **Solution**: Sum ~ Poisson(sum of rates)
│     → **Section**: 2.3 - Poisson Properties
│     → **Method**: Use MGF or direct property

└─ Poisson Approximation?
   ├─ Problem: "Approximate Binomial with Poisson"
   │  → If n large, p small, np = λ: Binomial(n,p) ≈ Poisson(λ)
   │  → **Section**: 2.3 - Poisson Approximation
   │  → **Condition**: n large, p small
   │
   └─ Problem: "Rare events"
      → Often Poisson approximation applies
      → **Section**: 2.3 - Poisson Distribution
```

---

# PAGE 5: TREE BRANCH D - BINOMIAL PROBLEMS

```
═══════════════════════════════════════════════════════════════
TREE BRANCH D: BINOMIAL DISTRIBUTION PROBLEMS
═══════════════════════════════════════════════════════════════

You identified: Binomial mentioned

KEY SYNONYMS:
- Binomial ≡ Binomial(n,p) ≡ Number of successes in n trials
- "n independent trials" → Binomial
- "Success probability p" → Binomial parameter

┌─ Basic Binomial?
│  ├─ Problem: "X ~ Binomial(n,p), find P(X = k)"
│  │  → **Solution**: P(X = k) = C(n,k)p^k(1-p)^(n-k)
│  │  → **Section**: 2.2 - Binomial Distribution
│  │
│  ├─ Problem: "X ~ Binomial(n,p), find E[X]"
│  │  → **Solution**: E[X] = np, Var(X) = np(1-p)
│  │  → **Section**: 2.2 - Binomial Distribution
│  │
│  └─ Problem: "n trials, success probability p"
│     → **Solution**: X ~ Binomial(n,p)
│     → **Section**: 2.2 - Binomial Distribution

├─ Binomial Approximation?
│  ├─ Problem: "Approximate Binomial with Normal"
│  │  → If np(1-p) > 10: X ≈ N(np, np(1-p))
│  │  → **Section**: 6.2 - Normal Approximation
│  │  → **Keywords**: "approximate", "large n"
│  │  → **Note**: Use continuity correction ±0.5
│  │
│  └─ Problem: "Approximate Binomial with Poisson"
│     → If n large, p small, np = λ: X ≈ Poisson(λ)
│     → **Section**: 2.3 - Poisson Approximation
│     → **Condition**: n large, p small

└─ Binomial as Sum?
   ├─ Problem: "X = X₁ + ... + Xₙ where Xᵢ ~ Bernoulli(p)"
   │  → **Solution**: X ~ Binomial(n,p)
   │  → **Section**: 2.2 - Binomial Distribution
   │  → **Key**: Sum of independent Bernoullis is Binomial
   │
   └─ Problem: "Indicator variables"
      → Sum of indicators ~ Binomial
      → **Section**: 2.2 - Binomial Distribution
```

---

# PAGE 6: TREE BRANCH E - GEOMETRIC PROBLEMS

```
═══════════════════════════════════════════════════════════════
TREE BRANCH E: GEOMETRIC DISTRIBUTION PROBLEMS
═══════════════════════════════════════════════════════════════

You identified: Geometric mentioned

KEY SYNONYMS:
- Geometric ≡ First success ≡ Waiting time (discrete)
- "Until first success" → Geometric
- "Memoryless" (discrete) → Geometric

┌─ Basic Geometric?
│  ├─ Problem: "X ~ Geometric(p), find P(X = k)"
│  │  → **Solution**: P(X = k) = p(1-p)^k (for failures before success)
│  │  → **Section**: 2.4 - Geometric Distribution
│  │  → **Note**: Alternative parameterization counts trials until success
│  │
│  ├─ Problem: "Expected number of trials until success"
│  │  → **Solution**: E[X] = 1/p
│  │  → **Section**: 2.4 - Geometric Distribution
│  │
│  └─ Problem: "Memoryless property"
│     → **Key**: P(X = m+n | X ≥ m) = P(X = n)
│     → **Section**: 2.4 - Memoryless Property
│     → **Keywords**: "memoryless", "no memory"

└─ Geometric in Context?
   ├─ Problem: "Expected number of games to win once"
   │  → If win probability = p, then E[games] = 1/p
   │  → **Section**: 2.4 - Geometric Distribution
   │
   └─ Problem: "First success" / "Until success"
      → Geometric distribution
      → **Section**: 2.4 - Geometric Distribution
```

---

# PAGE 7: TREE BRANCH F - UNIFORM PROBLEMS

```
═══════════════════════════════════════════════════════════════
TREE BRANCH F: UNIFORM DISTRIBUTION PROBLEMS
═══════════════════════════════════════════════════════════════

You identified: Uniform mentioned

KEY SYNONYMS:
- Uniform ≡ Uniformly distributed ≡ Equally likely ≡ U(a,b)
- "Random point" → Often Uniform
- "Equally likely" → Uniform

┌─ Continuous Uniform?
│  ├─ Problem: "X ~ Uniform(a,b), find PDF"
│  │  → **Solution**: f(x) = 1/(b-a) for a ≤ x ≤ b
│  │  → **Section**: 3.1 - Uniform Distribution
│  │
│  ├─ Problem: "X ~ Uniform(a,b), find P(c < X < d)"
│  │  → **Solution**: P = (d-c)/(b-a) [proportional to length]
│  │  → **Section**: 3.1 - Uniform Distribution
│  │
│  └─ Problem: "X ~ Uniform(a,b), find E[X]"
│     → **Solution**: E[X] = (a+b)/2, Var(X) = (b-a)²/12
│     → **Section**: 3.1 - Uniform Distribution

└─ Uniform in Context?
   ├─ Problem: "Random point on interval"
   │  → Often Uniform
   │  → **Section**: 3.1 - Uniform Distribution
   │
   └─ Problem: "Equally likely" / "Random selection"
      → Could be Uniform
      → **Section**: 3.1 - Uniform Distribution
```

---

# PAGE 8: TREE BRANCH G - GAMMA PROBLEMS

```
═══════════════════════════════════════════════════════════════
TREE BRANCH G: GAMMA DISTRIBUTION PROBLEMS
═══════════════════════════════════════════════════════════════

You identified: Gamma mentioned

KEY SYNONYMS:
- Gamma ≡ Erlang (when shape is integer) ≡ Sum of exponentials
- "Time until r-th event" → Gamma(r,λ) if inter-arrivals are Exp(λ)

┌─ Basic Gamma?
│  ├─ Problem: "X ~ Gamma(α,β), find PDF"
│  │  → **Solution**: f(x) = β^α/Γ(α) x^(α-1)e^(-βx), x > 0
│  │  → **Section**: 3.5 - Gamma Distribution
│  │
│  ├─ Problem: "X ~ Gamma(α,β), find E[X]"
│  │  → **Solution**: E[X] = α/β, Var(X) = α/β²
│  │  → **Section**: 3.5 - Gamma Distribution
│  │
│  └─ Problem: "Sum of exponentials"
│     → If Xᵢ ~ Exp(λ) independent, then ΣXᵢ ~ Gamma(n, λ)
│     → **Section**: 3.5 - Gamma Distribution
│     → **Method**: Use MGF

└─ Gamma Special Cases?
   ├─ Problem: "Erlang distribution"
   │  → Gamma with integer shape parameter
   │  → **Section**: 3.5 - Gamma Distribution
   │
   └─ Problem: "Time until r-th arrival"
      → If arrivals are Poisson(λ), time until r-th ~ Gamma(r, λ)
      → **Section**: 3.5 - Gamma Distribution
```

---

# PAGE 9: TREE BRANCH H - LOGNORMAL PROBLEMS

```
═══════════════════════════════════════════════════════════════
TREE BRANCH H: LOGNORMAL DISTRIBUTION PROBLEMS
═══════════════════════════════════════════════════════════════

You identified: Lognormal mentioned

KEY SYNONYMS:
- Lognormal ≡ Stock price model ≡ e^X where X ~ Normal
- "Stock price" → Often lognormal
- "Y = e^X where X is normal" → Lognormal

┌─ Basic Lognormal?
│  ├─ Problem: "Y = e^X where X ~ N(μ,σ²), find E[Y]"
│  │  → **Solution**: E[Y] = e^(μ + σ²/2)
│  │  → **Section**: 7.3 - Lognormal Distribution
│  │  → **Method**: Use MGF of normal or direct integration
│  │
│  ├─ Problem: "S = S₀e^Z where Z ~ N(...), find P(S > K)"
│  │  → **Solution**: Transform to normal: P(S > K) = P(Z > log(K/S₀))
│  │  → **Section**: 7.3 - Lognormal Distribution
│  │  → **Keywords**: "stock price", "S = S₀e^Z"
│  │
│  └─ Problem: "Stock price model"
│     → Often lognormal: S_t = S₀e^(μt + σW_t)
│     → **Section**: 7.3 - Lognormal Distribution
│     → **Finance**: Black-Scholes model foundation

└─ Lognormal Properties?
   ├─ Problem: "E[e^(-r)S]" where S is lognormal
   │  → Use properties of lognormal and exponential
   │  → **Section**: 7.3 - Lognormal Distribution
   │  → **Finance**: Discounted stock price
   │
   └─ Problem: "Product of lognormals"
      → Product is lognormal (sum of normals in exponent)
      → **Section**: 7.3 - Lognormal Distribution
```

---

# PAGE 10: TREE BRANCH I - BETA PROBLEMS

```
═══════════════════════════════════════════════════════════════
TREE BRANCH I: BETA DISTRIBUTION PROBLEMS
═══════════════════════════════════════════════════════════════

You identified: Beta mentioned

KEY SYNONYMS:
- Beta ≡ Conjugate prior for Binomial ≡ Distribution on [0,1]
- "Proportion" → Often Beta
- "Prior for probability" → Beta

┌─ Basic Beta?
│  ├─ Problem: "X ~ Beta(α,β), find PDF"
│  │  → **Solution**: f(x) = [Γ(α+β)/(Γ(α)Γ(β))] x^(α-1)(1-x)^(β-1), 0 < x < 1
│  │  → **Section**: 3.6 - Beta Distribution
│  │
│  ├─ Problem: "X ~ Beta(α,β), find E[X]"
│  │  → **Solution**: E[X] = α/(α+β), Var(X) = αβ/[(α+β)²(α+β+1)]
│  │  → **Section**: 3.6 - Beta Distribution
│  │
│  └─ Problem: "Conjugate prior for Binomial"
│     → Beta(α,β) prior + Binomial data → Beta(α+x, β+n-x) posterior
│     → **Section**: 7.2 - Conjugate Priors
│     → **Keywords**: "conjugate", "Beta-Binomial"

└─ Beta in Bayesian Context?
   ├─ Problem: "Prior Beta, update with Binomial data"
   │  → Use conjugate prior property
   │  → **Section**: 7.2 - Bayesian Statistics
   │
   └─ Problem: "Proportion θ" / "Probability p"
      → Often Beta prior
      → **Section**: 7.2 - Bayesian Statistics
```

---

# PAGE 11: TREE BRANCH J - OTHER DISTRIBUTIONS

```
═══════════════════════════════════════════════════════════════
TREE BRANCH J: OTHER DISTRIBUTIONS
═══════════════════════════════════════════════════════════════

You identified: Other named distribution

┌─ Negative Binomial?
│  ├─ Problem: "r-th success" / "Failures before r successes"
│  │  → **Solution**: X ~ Negative Binomial(r, p)
│  │  → **Section**: 2.5 - Negative Binomial
│  │  → **PMF**: P(X = k) = C(k+r-1, k)p^r(1-p)^k
│  │
│  └─ Problem: "E[X]" where X ~ NegBin(r,p)
│     → **Solution**: E[X] = r(1-p)/p
│     → **Section**: 2.5 - Negative Binomial

├─ Hypergeometric?
│  ├─ Problem: "Sampling without replacement"
│  │  → **Solution**: X ~ Hypergeometric(N, K, n)
│  │  → **Section**: 2.6 - Hypergeometric Distribution
│  │  → **Keywords**: "without replacement", "finite population"
│  │
│  └─ Problem: "Draw n balls from urn with K red, N-K blue"
│     → Hypergeometric distribution
│     → **Section**: 2.6 - Hypergeometric Distribution

└─ Multinomial?
   ├─ Problem: "Multiple categories, n trials"
   │  → **Solution**: Multinomial distribution
   │  → **Section**: (See lecture notes)
   │  → **Keywords**: "multiple categories", "n trials"
   │
   └─ Problem: "Joint distribution of counts"
      → Often Multinomial
      → **Section**: (See lecture notes)
```

---

# PAGE 12: TREE BRANCH K - JOINT DISTRIBUTIONS

```
═══════════════════════════════════════════════════════════════
TREE BRANCH K: JOINT DISTRIBUTION PROBLEMS
═══════════════════════════════════════════════════════════════

You identified: Joint distribution mentioned

KEY SYNONYMS:
- Joint distribution ≡ f(x,y) ≡ Joint PDF/PMF
- "Bivariate" → Two variables
- "Multivariate" → Multiple variables

┌─ Finding Joint Distribution?
│  ├─ Problem: "Given f(x,y), verify it's a valid PDF"
│  │  → **Solution**: Check f(x,y) ≥ 0 and ∫∫f(x,y)dxdy = 1
│  │  → **Section**: 4.1 - Joint Distributions
│  │
│  ├─ Problem: "Find constant c such that f(x,y) = c·g(x,y) is valid PDF"
│  │  → **Solution**: Set ∫∫f(x,y)dxdy = 1, solve for c
│  │  → **Section**: 4.1 - Joint Distributions
│  │
│  └─ Problem: "Find joint PDF of (X,Y)"
│     → Use given information or transformation
│     → **Section**: 4.1 - Joint Distributions

├─ Marginal Distributions?
│  ├─ Problem: "Find marginal PDF of X"
│  │  → **Solution**: f_X(x) = ∫f(x,y)dy
│  │  → **Section**: 4.2 - Marginal Distributions
│  │  → **Keywords**: "marginal", "marginal distribution"
│  │
│  └─ Problem: "Find marginal PMF"
│     → **Solution**: p_X(x) = Σ_y p(x,y)
│     → **Section**: 4.2 - Marginal Distributions

└─ Conditional Distributions?
   ├─ Problem: "Find conditional PDF f_{Y|X}(y|x)"
   │  → **Solution**: f_{Y|X}(y|x) = f(x,y)/f_X(x)
   │  → **Section**: 4.2 - Conditional Distributions
   │  → **Keywords**: "conditional", "given X=x"
   │
   └─ Problem: "Find conditional distribution"
      → Divide joint by marginal
      → **Section**: 4.2 - Conditional Distributions
```

---

# PAGE 13: TREE BRANCH L - SUMS OF RANDOM VARIABLES

```
═══════════════════════════════════════════════════════════════
TREE BRANCH L: SUMS OF RANDOM VARIABLES
═══════════════════════════════════════════════════════════════

You identified: Sum of random variables

KEY SYNONYMS:
- "Sum of" ≡ "X₁ + X₂ + ... + Xₙ" ≡ "Total" ≡ "Combined"

┌─ Independent Sums?
│  ├─ Problem: "X₁,...,Xₙ independent, find distribution of sum"
│  │  ├─ Are they Normal? → Sum is Normal (sum means, sum variances)
│  │  │  → **Section**: 3.3.2 - Sum of Independent Normals
│  │  │
│  │  ├─ Are they Poisson? → Sum is Poisson (sum rates)
│  │  │  → **Section**: 2.3 - Poisson Properties
│  │  │
│  │  ├─ Are they Exponential? → Sum is Gamma
│  │  │  → **Section**: 3.5 - Gamma Distribution
│  │  │
│  │  └─ Other? → Use MGF: M_{sum}(t) = ∏M_{Xᵢ}(t)
│  │     → **Section**: 5.2 - MGF for Sums
│  │
│  └─ Problem: "Find E[sum]" or "Find Var(sum)"
│     ├─ E[sum] = ΣE[Xᵢ] (always)
│     ├─ Var(sum) = ΣVar(Xᵢ) if independent
│     └─ Var(sum) = ΣVar(Xᵢ) + 2ΣCov(Xᵢ,Xⱼ) if dependent
│     → **Section**: 4.4 - Covariance

├─ Dependent Sums?
│  ├─ Problem: "X₁,...,Xₙ dependent, find Var(sum)"
│  │  → **Solution**: Var(sum) = ΣVar(Xᵢ) + 2Σ_{i<j}Cov(Xᵢ,Xⱼ)
│  │  → **Section**: 4.4 - Covariance
│  │
│  └─ Problem: "Find distribution of sum" (dependent)
│     → Use convolution or MGF (if MGF exists)
│     → **Section**: 4.6 - Transformations (convolution)

└─ Sample Mean?
   ├─ Problem: "X̄ = (1/n)ΣXᵢ, find distribution"
   │  ├─ If Xᵢ ~ N(μ,σ²) i.i.d. → X̄ ~ N(μ, σ²/n)
   │  │  → **Section**: 3.3.1 - Sample Mean of Normals
   │  │
   │  └─ If large n → Use CLT: X̄ ≈ N(μ, σ²/n)
   │     → **Section**: 6.1 - CLT
   │
   └─ Problem: "Find E[X̄]" or "Find Var(X̄)"
      → E[X̄] = μ, Var(X̄) = σ²/n
      → **Section**: 6.1 - CLT
```

---

# PAGE 14: TREE BRANCH M - ORDER STATISTICS (MAX/MIN)

```
═══════════════════════════════════════════════════════════════
TREE BRANCH M: ORDER STATISTICS (MAXIMUM/MINIMUM)
═══════════════════════════════════════════════════════════════

You identified: Maximum/Minimum mentioned

KEY SYNONYMS:
- Maximum ≡ Max{X₁,...,Xₙ} ≡ X₍ₙ₎
- Minimum ≡ Min{X₁,...,Xₙ} ≡ X₍₁₎

┌─ Maximum?
│  ├─ Problem: "Find P(max Xᵢ > a)" where Xᵢ independent
│  │  → **Solution**: P(max > a) = 1 - P(all ≤ a) = 1 - [P(X₁ ≤ a)]ⁿ
│  │  → **Section**: 4.7 - Order Statistics
│  │  → **Method**: Use independence and complement
│  │
│  ├─ Problem: "Find distribution of max Xᵢ"
│  │  → **Solution**: F_{max}(x) = [F(x)]ⁿ, f_{max}(x) = n[F(x)]^(n-1)f(x)
│  │  → **Section**: 4.7 - Order Statistics
│  │
│  └─ Problem: "Find E[max Xᵢ]"
│     → Use distribution found above, then E[max] = ∫xf_{max}(x)dx
│     → **Section**: 4.7 - Order Statistics

├─ Minimum?
│  ├─ Problem: "Find P(min Xᵢ > a)" where Xᵢ independent
│  │  → **Solution**: P(min > a) = [P(X₁ > a)]ⁿ = [1-F(a)]ⁿ
│  │  → **Section**: 4.7 - Order Statistics
│  │  → **Method**: Use independence
│  │
│  ├─ Problem: "Find distribution of min Xᵢ"
│  │  → **Solution**: F_{min}(x) = 1 - [1-F(x)]ⁿ, f_{min}(x) = n[1-F(x)]^(n-1)f(x)
│  │  → **Section**: 4.7 - Order Statistics
│  │
│  └─ Problem: "Find E[min Xᵢ]"
│     → Use distribution found above
│     → **Section**: 4.7 - Order Statistics

└─ Special Cases?
   ├─ Problem: "Max/Min of Uniform(0,1)"
   │  → Use formulas above with F(x) = x
   │  → **Section**: 4.7 - Order Statistics
   │
   └─ Problem: "Max/Min of Normal"
      → Use formulas above with Φ((x-μ)/σ)
      → **Section**: 4.7 - Order Statistics
```

---

# PAGE 15: TREE BRANCH N - PRODUCTS/RATIOS

```
═══════════════════════════════════════════════════════════════
TREE BRANCH N: PRODUCTS AND RATIOS
═══════════════════════════════════════════════════════════════

You identified: Product or Ratio mentioned

┌─ Products?
│  ├─ Problem: "Find distribution of XY" where X,Y independent
│  │  → **Solution**: Use transformation method or MGF
│  │  → **Section**: 4.6 - Transformations
│  │  → **Method**: Let U = XY, find f_U(u) using Jacobian or CDF method
│  │
│  ├─ Problem: "Find E[XY]"
│  │  ├─ If independent → E[XY] = E[X]E[Y]
│  │  │  → **Section**: 4.3 - Independence
│  │  │
│  │  └─ If dependent → E[XY] = ∫∫xy f(x,y)dxdy
│  │     → **Section**: 4.1 - Joint Distributions
│  │
│  └─ Problem: "Product of lognormals"
│     → Product is lognormal (sum of normals in exponent)
│     → **Section**: 7.3 - Lognormal Distribution

└─ Ratios?
   ├─ Problem: "Find distribution of X/Y"
   │  → **Solution**: Use transformation method (Jacobian)
   │  → **Section**: 4.6 - Transformations
   │  → **Method**: Let U = X, V = X/Y, find Jacobian
   │
   └─ Problem: "Find E[X/Y]"
      → Use definition: E[X/Y] = ∫∫(x/y)f(x,y)dxdy
      → **Section**: 4.1 - Joint Distributions
```

---

# PAGE 16: TREE BRANCH O - CONDITIONAL DISTRIBUTIONS & EXPECTATIONS

```
═══════════════════════════════════════════════════════════════
TREE BRANCH O: CONDITIONAL DISTRIBUTIONS & EXPECTATIONS
═══════════════════════════════════════════════════════════════

You identified: Conditional mentioned

KEY SYNONYMS:
- Conditional ≡ "Given that" ≡ "X|Y" ≡ "X given Y"

┌─ Conditional Probability?
│  ├─ Problem: "Find P(A|B)"
│  │  → **Solution**: P(A|B) = P(A∩B)/P(B)
│  │  → **Section**: 1.2 - Conditional Probability
│  │
│  └─ Problem: "Given that X > a, find P(Y > b)"
│     → **Solution**: P(Y > b | X > a) = P(Y > b, X > a)/P(X > a)
│     → **Section**: 1.2 - Conditional Probability

├─ Conditional Distribution?
│  ├─ Problem: "Find f_{Y|X}(y|x)"
│  │  → **Solution**: f_{Y|X}(y|x) = f(x,y)/f_X(x)
│  │  → **Section**: 4.2 - Conditional Distributions
│  │
│  └─ Problem: "Find conditional distribution of Y given X = x"
│     → Divide joint by marginal
│     → **Section**: 4.2 - Conditional Distributions

├─ Conditional Expectation?
│  ├─ Problem: "Find E[X|Y = y]"
│  │  → **Solution**: E[X|Y=y] = ∫x f_{X|Y}(x|y)dx
│  │  → **Section**: 7.1 - Conditional Expectation
│  │
│  ├─ Problem: "Find E[X|Y]" (as function of Y)
│  │  → E[X|Y] is a function of Y
│  │  → **Section**: 7.1 - Conditional Expectation
│  │
│  └─ Problem: "Use law of total expectation"
│     → E[X] = E[E[X|Y]]
│     → **Section**: 7.1 - Conditional Expectation

└─ Conditional Variance?
   ├─ Problem: "Find Var(X|Y = y)"
   │  → **Solution**: Var(X|Y=y) = E[(X-E[X|Y=y])²|Y=y]
   │  → **Section**: 7.1 - Conditional Variance
   │
   └─ Problem: "Use law of total variance"
      → Var(X) = E[Var(X|Y)] + Var(E[X|Y])
      → **Section**: 7.1 - Conditional Variance
```

---

# PAGE 17: TREE BRANCH P - MOMENT GENERATING FUNCTIONS

```
═══════════════════════════════════════════════════════════════
TREE BRANCH P: MOMENT GENERATING FUNCTIONS
═══════════════════════════════════════════════════════════════

You identified: MGF mentioned

KEY SYNONYMS:
- MGF ≡ Moment generating function ≡ ψ(t) (professor's notation)

┌─ Finding MGF?
│  ├─ Problem: "Find MGF of X"
│  │  → **Solution**: M_X(t) = E[e^(tX)] = ∫e^(tx)f(x)dx or Σe^(tx)p(x)
│  │  → **Section**: 5.1 - MGF Definition
│  │
│  └─ Problem: "Find MGF of g(X)"
│     → M_{g(X)}(t) = E[e^(tg(X))]
│     → **Section**: 5.1 - MGF Definition

├─ Using MGF for Moments?
│  ├─ Problem: "Use MGF to find E[X]"
│  │  → **Solution**: E[X] = M'(0)
│  │  → **Section**: 5.1 - MGF Properties
│  │
│  ├─ Problem: "Use MGF to find E[X²]"
│  │  → **Solution**: E[X²] = M''(0)
│  │  → **Section**: 5.1 - MGF Properties
│  │
│  └─ Problem: "Find k-th moment"
│     → **Solution**: E[X^k] = M^(k)(0)
│     → **Section**: 5.1 - MGF Properties

├─ Using MGF for Sums?
│  ├─ Problem: "Find MGF of sum X₁ + ... + Xₙ" (independent)
│  │  → **Solution**: M_{sum}(t) = ∏M_{Xᵢ}(t)
│  │  → **Section**: 5.2 - MGF for Sums
│  │
│  └─ Problem: "Use MGF to find distribution of sum"
│     → Multiply MGFs, match to known MGF
│     → **Section**: 5.2 - MGF for Sums

└─ Using MGF for Identification?
   ├─ Problem: "Show that X has distribution Y using MGF"
   │  → Compute MGF of X, match to MGF of Y
   │  → **Section**: 5.1 - MGF Uniqueness
   │
   └─ Problem: "Prove distribution using MGF"
      → Use uniqueness property of MGF
      → **Section**: 5.1 - MGF Uniqueness
```

---

# PAGE 18: TREE BRANCH Q - EXPECTATIONS & VARIANCES

```
═══════════════════════════════════════════════════════════════
TREE BRANCH Q: EXPECTATIONS & VARIANCES
═══════════════════════════════════════════════════════════════

You identified: Expectation or Variance mentioned

┌─ Basic Expectation?
│  ├─ Problem: "Find E[X]"
│  │  ├─ Discrete → E[X] = Σx·P(X=x)
│  │  │  → **Section**: 2.1 - Discrete Expectation
│  │  │
│  │  └─ Continuous → E[X] = ∫xf(x)dx
│  │     → **Section**: 3.1 - Continuous Expectation
│  │
│  ├─ Problem: "Find E[g(X)]"
│  │  ├─ Discrete → E[g(X)] = Σg(x)·P(X=x)
│  │  └─ Continuous → E[g(X)] = ∫g(x)f(x)dx
│  │     → **Section**: 4.1 - Expectation of Functions
│  │
│  └─ Problem: "Find E[X + Y]"
│     → **Solution**: E[X+Y] = E[X] + E[Y] (always)
│     → **Section**: 4.1 - Linearity of Expectation

├─ Basic Variance?
│  ├─ Problem: "Find Var(X)"
│  │  → **Solution**: Var(X) = E[X²] - (E[X])²
│  │  → **Section**: 4.3 - Variance
│  │
│  ├─ Problem: "Find Var(aX + b)"
│  │  → **Solution**: Var(aX+b) = a²Var(X)
│  │  → **Section**: 4.3 - Variance Properties
│  │
│  └─ Problem: "Find Var(X + Y)"
│     ├─ If independent → Var(X+Y) = Var(X) + Var(Y)
│     │  → **Section**: 4.3 - Variance Properties
│     │
│     └─ If dependent → Var(X+Y) = Var(X) + Var(Y) + 2Cov(X,Y)
│        → **Section**: 4.4 - Covariance

└─ Using Properties?
   ├─ Problem: "Use linearity of expectation"
   │  → E[aX + bY + c] = aE[X] + bE[Y] + c
   │  → **Section**: 4.1 - Linearity
   │
   └─ Problem: "Use law of total expectation"
      → E[X] = E[E[X|Y]]
      → **Section**: 7.1 - Conditional Expectation
```

---

# PAGE 19: TREE BRANCH R - COVARIANCE & CORRELATION

```
═══════════════════════════════════════════════════════════════
TREE BRANCH R: COVARIANCE & CORRELATION
═══════════════════════════════════════════════════════════════

You identified: Covariance or Correlation mentioned

┌─ Covariance?
│  ├─ Problem: "Find Cov(X,Y)"
│  │  → **Solution**: Cov(X,Y) = E[XY] - E[X]E[Y]
│  │  → **Section**: 4.4 - Covariance
│  │  → **Method**: Find E[X], E[Y], E[XY], then apply formula
│  │
│  ├─ Problem: "Find Cov(aX+b, cY+d)"
│  │  → **Solution**: Cov(aX+b, cY+d) = ac·Cov(X,Y)
│  │  → **Section**: 4.4 - Covariance Properties
│  │
│  └─ Problem: "Are X and Y independent? Check covariance"
│     → If independent → Cov(X,Y) = 0
│     → But Cov = 0 does NOT imply independence (except for normal)
│     → **Section**: 4.3 - Independence, 4.4 - Covariance

├─ Correlation?
│  ├─ Problem: "Find correlation ρ(X,Y)"
│  │  → **Solution**: ρ = Cov(X,Y)/(σ_X·σ_Y)
│  │  → **Section**: 4.4 - Correlation
│  │  → **Properties**: -1 ≤ ρ ≤ 1
│  │
│  └─ Problem: "Interpret correlation"
│     → ρ > 0: positive linear relationship
│     → ρ < 0: negative linear relationship
│     → ρ = 0: no linear relationship (but may be dependent)
│     → **Section**: 4.4 - Correlation

└─ Special Cases?
   ├─ Problem: "For bivariate normal, ρ = 0 iff independent"
   │  → Unique property of normal distribution
   │  → **Section**: 4.5 - Bivariate Normal
   │
   └─ Problem: "Portfolio variance"
      → Uses covariance matrix
      → **Section**: 4.4 - Covariance (Finance applications)
```

---

# PAGE 20: TREE BRANCH S - LIMIT THEOREMS & APPROXIMATIONS

```
═══════════════════════════════════════════════════════════════
TREE BRANCH S: LIMIT THEOREMS & APPROXIMATIONS
═══════════════════════════════════════════════════════════════

You identified: Limits or Approximations mentioned

KEY SYNONYMS:
- "Large n" → CLT
- "Approximate" → CLT or Normal approximation
- "As n → ∞" → Limit theorem

┌─ Central Limit Theorem?
│  ├─ Problem: "X₁,...,Xₙ i.i.d. with mean μ, variance σ², find approximate distribution of X̄"
│  │  → **Solution**: X̄ ≈ N(μ, σ²/n) for large n
│  │  → **Section**: 6.1 - CLT
│  │  → **Standardize**: Z = (X̄-μ)/(σ/√n) ≈ N(0,1)
│  │
│  ├─ Problem: "Find approximate probability using CLT"
│  │  → Apply CLT, standardize, use normal table
│  │  → **Section**: 6.1 - CLT
│  │  → **Example**: "400 games, approximate P(total > 240)"
│  │
│  └─ Problem: "How large must n be for CLT to apply?"
│     → Typically n ≥ 30, but depends on distribution
│     → **Section**: 6.1 - CLT

├─ Normal Approximation?
│  ├─ Problem: "Approximate Binomial with Normal"
│  │  → If np(1-p) > 10: X ≈ N(np, np(1-p))
│  │  → **Section**: 6.2 - Normal Approximation
│  │  → **Important**: Use continuity correction ±0.5
│  │
│  ├─ Problem: "Approximate Poisson with Normal"
│  │  → If λ > 30: X ≈ N(λ, λ)
│  │  → **Section**: 6.2 - Normal Approximation
│  │
│  └─ Problem: "Continuity correction"
│     → For discrete → continuous: P(X = k) ≈ P(k-0.5 < Y < k+0.5)
│     → **Section**: 6.2 - Normal Approximation

├─ Law of Large Numbers?
│  ├─ Problem: "As n → ∞, what happens to X̄?"
│  │  → **Solution**: X̄ → μ (converges in probability)
│  │  → **Section**: 6.3 - LLN
│  │
│  └─ Problem: "Sample mean converges to"
│     → True mean μ
│     → **Section**: 6.3 - LLN

└─ Confidence Intervals?
   ├─ Problem: "Find 95% confidence interval for μ"
   │  → **Solution**: X̄ ± z_{0.025}·(σ/√n)
   │  → **Section**: 6.4 - Confidence Intervals
   │  → **Common z values**: z_{0.05} = 1.645, z_{0.025} = 1.96, z_{0.005} = 2.576
   │
   └─ Problem: "Margin of error"
      → Half-width of confidence interval
      → **Section**: 6.4 - Confidence Intervals
```

---

# PAGE 21: TREE BRANCH T - PROOFS & DERIVATIONS

```
═══════════════════════════════════════════════════════════════
TREE BRANCH T: PROOFS & DERIVATIONS
═══════════════════════════════════════════════════════════════

You identified: Proof or Derivation requested

┌─ Using MGF?
│  ├─ Problem: "Show that X has distribution Y using MGF"
│  │  → Compute MGF of X, show it matches MGF of Y
│  │  → **Section**: 5.1 - MGF Uniqueness
│  │
│  └─ Problem: "Prove sum of normals is normal"
│     → Use MGF: M_{X+Y}(t) = M_X(t)M_Y(t) = e^{(μ₁+μ₂)t + (σ₁²+σ₂²)t²/2}
│     → **Section**: 5.2 - MGF for Sums

├─ Using CDF Method?
│  ├─ Problem: "Derive PDF of Y = g(X)"
│  │  → Find F_Y(y) = P(g(X) ≤ y), then differentiate
│  │  → **Section**: 4.6 - Transformations
│  │
│  └─ Problem: "Prove distribution using CDF"
│     → Use CDF method
│     → **Section**: 4.6 - Transformations

├─ Using Properties?
│  ├─ Problem: "Prove independence implies Cov = 0"
│  │  → E[XY] = E[X]E[Y] if independent, so Cov = 0
│  │  → **Section**: 4.3 - Independence, 4.4 - Covariance
│  │
│  └─ Problem: "Prove law of total expectation"
│     → Use definition and properties
│     → **Section**: 7.1 - Conditional Expectation

└─ Step-by-Step Derivation?
   ├─ Problem: "Derive formula step by step"
   │  → Show each step clearly
   │  → Use appropriate method (MGF, CDF, properties)
   │
   └─ Problem: "Prove theorem"
      → Follow proof structure
      → Use definitions and properties
```

---

# PAGE 22: TREE BRANCH U - BAYESIAN STATISTICS

```
═══════════════════════════════════════════════════════════════
TREE BRANCH U: BAYESIAN STATISTICS
═══════════════════════════════════════════════════════════════

You identified: Bayesian statistics mentioned

KEY SYNONYMS:
- "Update" → Bayesian update
- "Posterior" → π(θ|x)
- "Prior" → π(θ)
- "Likelihood" → L(x|θ)

┌─ Basic Bayesian Update?
│  ├─ Problem: "Update prior with data"
│  │  → **Solution**: Posterior ∝ Prior × Likelihood
│  │  → π(θ|x) = [L(x|θ)π(θ)] / ∫L(x|θ)π(θ)dθ
│  │  → **Section**: 7.2 - Bayesian Statistics
│  │
│  ├─ Problem: "Find posterior distribution"
│  │  → Use Bayes' theorem
│  │  → **Section**: 7.2 - Bayesian Statistics
│  │
│  └─ Problem: "Monty Hall" / "Update probability given evidence"
│     → Use Bayes' theorem with likelihoods
│     → **Section**: 7.2 - Bayesian Statistics, 8.1 - Monty Hall example

├─ Conjugate Priors?
│  ├─ Problem: "Beta-Binomial conjugate"
│  │  → Prior: Beta(α,β), Data: Binomial(n,x)
│  │  → Posterior: Beta(α+x, β+n-x)
│  │  → **Section**: 7.2 - Conjugate Priors
│  │
│  ├─ Problem: "Gamma-Poisson conjugate"
│  │  → Prior: Gamma(α,β), Data: Poisson observations
│  │  → Posterior: Gamma(α+Σxᵢ, β+n)
│  │  → **Section**: 7.2 - Conjugate Priors
│  │
│  └─ Problem: "Normal-Normal conjugate"
│     → With known variance
│     → **Section**: 7.2 - Conjugate Priors

├─ Predictive Distribution?
│  ├─ Problem: "Find predictive distribution"
│  │  → Integrate over posterior: p(x_{new}|data) = ∫p(x_{new}|θ)π(θ|data)dθ
│  │  → **Section**: 7.2 - Predictive Distribution
│  │
│  └─ Problem: "Predict next observation"
│     → Use predictive distribution
│     → **Section**: 7.2 - Predictive Distribution

└─ Bayesian Inference?
   ├─ Problem: "Find posterior mean"
   │  → E[θ|data] = ∫θ·π(θ|data)dθ
   │  → **Section**: 7.2 - Bayesian Statistics
   │
   └─ Problem: "Find posterior variance"
      → Var(θ|data) = E[θ²|data] - (E[θ|data])²
      → **Section**: 7.2 - Bayesian Statistics
```

---

# PAGE 23: QUICK REFERENCE INDEX

## If You See THIS Phrase → Go to THIS Branch

### Distribution Names
- "Gaussian" / "Normal" → Branch A (Page 2)
- "Exponential" / "Memoryless" → Branch B (Page 2)
- "Poisson" / "Arrivals" → Branch C (Page 3)
- "Binomial" / "n trials" → Branch D (Page 3)
- "Geometric" / "First success" → Branch E (Page 4)
- "Uniform" / "Equally likely" → Branch F (Page 4)
- "Gamma" / "Sum of exponentials" → Branch G (Page 4)
- "Lognormal" / "Stock price" → Branch H (Page 5)
- "Beta" / "Conjugate prior" → Branch I (Page 5)

### Operations
- "Sum of" / "X₁ + X₂" → Branch L (Page 7)
- "Maximum" / "Minimum" → Branch M (Page 7)
- "Product" / "XY" → Branch N (Page 8)
- "Ratio" / "X/Y" → Branch N (Page 8)
- "Conditional" / "Given that" → Branch O (Page 8)
- "Transform" / "Distribution of Y = g(X)" → Branch N or 4.6

### Moments & Functions
- "MGF" / "Moment generating function" → Branch P (Page 9)
- "E[X]" / "Expected value" → Branch Q (Page 9)
- "Var(X)" / "Variance" → Branch Q (Page 9)
- "Cov(X,Y)" / "Correlation" → Branch R (Page 10)

### Limits & Approximations
- "Large n" / "Approximate" → Branch S (Page 10)
- "CLT" / "Central Limit Theorem" → Branch S (Page 10)
- "Converges" → Branch S (Page 10)

### Bayesian
- "Update" / "Posterior" / "Prior" → Branch U (Page 11)
- "Bayesian" / "Bayes" → Branch U (Page 11)

### Joint & Multivariate
- "Joint distribution" / "f(x,y)" → Branch K (Page 6)
- "Gaussian vector" / "Multivariate normal" → Branch A (Page 2)
- "Independent components" → Branch A (Page 2) - MVN

---

# PAGE 24: MULTI-STEP PROBLEM PATTERNS

## Common Combination Patterns

### Pattern 1: i.i.d. Gaussians → Max/Min → Probability
**Recognition:** "X₁,...,Xₙ i.i.d. N(μ,σ²), find P(max Xᵢ > a)"
**Solution:**
1. Identify: Independent normals
2. Use independence: P(max ≤ a) = [P(X₁ ≤ a)]ⁿ = [Φ((a-μ)/σ)]ⁿ
3. Complement: P(max > a) = 1 - [Φ((a-μ)/σ)]ⁿ
**Sections:** 4.3 (Independence), 3.2 (Normal), 4.7 (Order Statistics)

### Pattern 2: Poisson Process + Exponential Waiting Times
**Recognition:** "Arrivals at rate λ, find time until first arrival"
**Solution:**
1. Identify: Poisson process
2. Key: Inter-arrival times are Exponential(λ)
3. Find: P(T > t) = e^(-λt)
**Sections:** 2.3 (Poisson), 3.3 (Exponential)

### Pattern 3: Conditional Probability + Bayes Theorem
**Recognition:** "Given evidence, update probability"
**Solution:**
1. Identify prior P(H)
2. Find likelihood P(E|H)
3. Apply Bayes: P(H|E) = P(E|H)P(H)/P(E)
**Sections:** 1.2 (Conditional), 1.3 (Bayes)

### Pattern 4: Transformation + Jacobian Method
**Recognition:** "Find distribution of Y = g(X,Y)"
**Solution:**
1. Define transformation
2. Find inverse
3. Compute Jacobian
4. Apply formula: f_{UV}(u,v) = f_{XY}(x,y)|J|
**Sections:** 4.6 (Transformations)

### Pattern 5: Joint + Independence + Correlation
**Recognition:** "Find joint, check independence, compute correlation"
**Solution:**
1. Find joint distribution
2. Find marginals
3. Check independence: f(x,y) =? f_X(x)f_Y(y)
4. Compute correlation: ρ = Cov/(σ_X σ_Y)
**Sections:** 4.1 (Joint), 4.3 (Independence), 4.4 (Correlation)

### Pattern 6: Bayesian + Prediction
**Recognition:** "Update posterior, then predict next observation"
**Solution:**
1. Update: Posterior ∝ Prior × Likelihood
2. Predict: Integrate over posterior
**Sections:** 7.2 (Bayesian), Predictive Distribution

### Pattern 7: CLT + Normal Approximation
**Recognition:** "Large n, approximate probability"
**Solution:**
1. Identify: i.i.d., large n
2. Apply CLT: X̄ ≈ N(μ, σ²/n)
3. Standardize and use normal table
**Sections:** 6.1 (CLT), 6.2 (Normal Approximation)

### Pattern 8: Bivariate Normal + Linear Combination
**Recognition:** "X,Y jointly normal, find distribution of aX + bY"
**Solution:**
1. Key: Linear combinations of bivariate normal are normal
2. Find mean: E[aX+bY] = aμ_X + bμ_Y
3. Find variance: Var(aX+bY) = a²σ_X² + b²σ_Y² + 2abρσ_Xσ_Y
**Sections:** 4.5 (Bivariate Normal)

### Pattern 9: Lognormal + Expectation
**Recognition:** "S = S₀e^Z, find E[S]"
**Solution:**
1. Identify: Lognormal (Z ~ Normal)
2. Use formula: E[S] = S₀e^(μ + σ²/2)
**Sections:** 7.3 (Lognormal)

### Pattern 10: Conditional Expectation + Total Expectation
**Recognition:** "Find E[X] using E[X|Y]"
**Solution:**
1. Find E[X|Y=y]
2. Use law: E[X] = E[E[X|Y]]
**Sections:** 7.1 (Conditional Expectation)

---

# PAGE 25: EXAM STRATEGY & TIME MANAGEMENT

## Quick Identification (< 10 seconds)
1. **Scan for keywords** first
2. **Check notation** (f(x,y)? P(A|B)? E[X]?)
3. **Count variables** (one or multiple?)
4. **Note distribution names** (Normal? Binomial?)
5. **Look for "large n"** → CLT territory

## When Stuck
1. **Check problem type** against this tree
2. **Identify all given information**
3. **Match to terminal node**
4. **Apply formula from that section**

## Time Management (90 minutes, 3 questions)
- **0-5 min:** Read all problems, identify types using decision tree
- **5-35 min:** Question 1 (aim for 30 min max)
- **35-65 min:** Question 2 (aim for 30 min max)
- **65-85 min:** Question 3 (aim for 20 min)
- **85-90 min:** Review, check arithmetic

## High-Yield Topics (Post-M2 Focus)
1. Central Limit Theorem applications
2. Bivariate Normal problems
3. Bayesian updates (especially Monty Hall variants)
4. Conditional Expectation and Total Expectation
5. Lognormal/Finance applications
6. Joint distributions (finding marginals, checking independence)
7. Covariance and correlation calculations
8. MGF for finding distributions of sums
9. Normal approximations with continuity correction
10. Confidence intervals using CLT

---

**END OF DECISION TREE**

