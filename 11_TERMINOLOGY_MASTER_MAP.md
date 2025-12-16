# Terminology Master Map - Probability Theory

**Generated:** December 16, 2025
**Purpose:** Complete terminology database with synonym mappings for exam problem recognition

---

## 1. RANDOM VARIABLE TYPES & DISTRIBUTIONS

### Normal Distribution
| Term | Equivalents | Section Reference |
|------|-------------|-------------------|
| **Normal** | Gaussian, N(μ,σ²), bell curve, "approximately normal" | 3.3, 4.5 |
| **Standard Normal** | N(0,1), Z, Φ(z), "standardized" | 3.3 |
| **Bivariate Normal** | Jointly normal, Multivariate normal (2D), Gaussian vector, MVN, "joint normal distribution" | 4.5 |
| **Gaussian vector** | Multivariate normal, MVN, "independent components" (diagonal covariance) | 4.5 |
| **Sample mean of normals** | X̄ ~ N(μ, σ²/n), "average of i.i.d. normals" | 3.3, 6.1 |

**Recognition Patterns:**
- "X ~ N(μ,σ²)" → Normal distribution
- "X₁, X₂ are iid N(0,1)" → Standard normals
- "Gaussian vector with independent components" → MVN with diagonal covariance (Σ diagonal, ρ=0)
- "jointly normal" or "bivariate normal" → Use special properties (independence ⟺ ρ=0)
- "approximately normal" → CLT application

### Exponential Distribution
| Term | Equivalents | Section Reference |
|------|-------------|-------------------|
| **Exponential** | Exp(λ), waiting time, time until event, inter-arrival time, service time | 3.4 |
| **Memoryless (continuous)** | "fresh start", exponential property, no wear-and-tear | 3.4 |
| **Rate parameter** | λ, mean = 1/λ, variance = 1/λ² | 3.4 |

**Recognition Patterns:**
- "time until first arrival" → Exponential
- "waiting time between events" → Exponential
- "memoryless property" (continuous) → Exponential
- "service time" → Often Exponential
- "component lifetime" → Often Exponential
- f(x) = λe^(-λx) → Exponential(λ)

### Poisson Distribution
| Term | Equivalents | Section Reference |
|------|-------------|-------------------|
| **Poisson** | Pois(λ), counting process, arrivals, rare events | 2.3 |
| **Poisson Process** | Arrival process, counting process, events over time | 2.3 |
| **Rate** | λ, mean = variance = λ, events per unit time | 2.3 |

**Recognition Patterns:**
- "arrivals per hour/day" → Poisson
- "number of events in interval" → Poisson
- "rare events" → Poisson
- "counting process" → Poisson Process
- "independent increments" → Poisson Process
- P(X=k) = e^(-λ)λ^k/k! → Poisson(λ)

### Binomial Distribution
| Term | Equivalents | Section Reference |
|------|-------------|-------------------|
| **Binomial** | B(n,p), Bin(n,p), n trials, success/failure, number of successes | 2.2 |
| **Bernoulli trials** | Independent trials, success probability p | 2.2 |
| **Sum of Bernoulli** | Binomial(n,p) | 2.2 |

**Recognition Patterns:**
- "n independent trials" → Binomial
- "success probability p" → Binomial
- "number of successes in n trials" → Binomial
- "repeated independent experiments" → Binomial
- P(X=k) = C(n,k)p^k(1-p)^(n-k) → Binomial(n,p)

### Geometric Distribution
| Term | Equivalents | Section Reference |
|------|-------------|-------------------|
| **Geometric** | First success, waiting for success, Geo(p), trials until success | 2.4 |
| **Memoryless (discrete)** | "fresh start" (discrete), "forgets past" | 2.4 |
| **Number of failures** | Before first success (one parameterization) | 2.4 |

**Recognition Patterns:**
- "first success" → Geometric
- "trials until success" → Geometric
- "number of failures before success" → Geometric
- "memoryless property" (discrete) → Geometric
- P(X=k) = p(1-p)^k → Geometric(p)

### Negative Binomial Distribution
| Term | Equivalents | Section Reference |
|------|-------------|-------------------|
| **Negative Binomial** | NegBin(r,p), failures before r successes | 2.5 |
| **Sum of Geometrics** | r independent Geometric(p) | 2.5 |

**Recognition Patterns:**
- "failures before r-th success" → Negative Binomial
- "wait for r successes" → Negative Binomial
- "r = 1" → Geometric (special case)

### Uniform Distribution
| Term | Equivalents | Section Reference |
|------|-------------|-------------------|
| **Uniform** | U(a,b), Unif(a,b), equally likely, random point | 3.2 |
| **Standard Uniform** | U(0,1), Uniform(0,1) | 3.2 |

**Recognition Patterns:**
- "equally likely" → Uniform
- "random point in interval" → Uniform
- "uniformly distributed" → Uniform
- "random selection" → Often Uniform
- f(x) = 1/(b-a) for a ≤ x ≤ b → Uniform(a,b)

### Gamma Distribution
| Term | Equivalents | Section Reference |
|------|-------------|-------------------|
| **Gamma** | Γ(α,β), Gamma(r,λ), sum of exponentials | 3.5 |
| **Erlang** | Gamma with integer α, sum of n Exp(λ) | 3.5 |

**Recognition Patterns:**
- "sum of n exponentials" → Gamma(n,λ)
- "time until n-th arrival" → Gamma
- "α = 1" → Exponential (special case)
- "waiting time for r-th event" → Gamma

### Beta Distribution
| Term | Equivalents | Section Reference |
|------|-------------|-------------------|
| **Beta** | Beta(α,β), proportion, probability parameter | 3.6 |
| **Conjugate prior** | For Binomial likelihood | 7.2 |

**Recognition Patterns:**
- "proportion" → Often Beta
- "probability parameter" → Beta prior
- "prior for success probability" → Beta
- "support on (0,1)" → Beta

### Hypergeometric Distribution
| Term | Equivalents | Section Reference |
|------|-------------|-------------------|
| **Hypergeometric** | Sampling without replacement, finite population | 2.6 |
| **Finite population** | Not i.i.d., dependent draws | 2.6 |

**Recognition Patterns:**
- "without replacement" → Hypergeometric
- "finite population" → Hypergeometric
- "draw n from N, K successes" → Hypergeometric
- NOT binomial when sampling without replacement

### Lognormal Distribution
| Term | Equivalents | Section Reference |
|------|-------------|-------------------|
| **Lognormal** | LogN(μ,σ²), exp(Normal), stock prices | 7.3 |
| **Geometric Brownian Motion** | Stock price model, S = S₀e^Z | 7.3 |

**Recognition Patterns:**
- "log(X) is normal" → Lognormal
- "stock price model" → Lognormal
- "S = S₀e^Z where Z ~ N(μ,σ²)" → Lognormal
- "always positive, right-skewed" → Often Lognormal
- E[e^X] = exp(μ + σ²/2) for X ~ N(μ,σ²)

---

## 2. PROCESS & PROBLEM DESCRIPTIONS

### Independence Terminology
| Term | Equivalents | Meaning |
|------|-------------|---------|
| **i.i.d.** | Independent identically distributed, "iid", independent and identically distributed | Same distribution + independent |
| **Independent** | No influence, P(A∩B) = P(A)P(B) | Joint = product of marginals |
| **Independent components** | Diagonal covariance matrix, ρ = 0 for all pairs | For MVN: independent ⟺ uncorrelated |
| **Conditionally independent** | Independent given some variable | P(A,B\|C) = P(A\|C)P(B\|C) |

### Memoryless Property
| Distribution | Statement | Use |
|--------------|-----------|-----|
| **Exponential** | P(X > s+t \| X > s) = P(X > t) | Waiting times, "fresh start" |
| **Geometric** | P(X = k+t \| X ≥ k) = P(X = t) | Trial sequences |

### Waiting Time Problems
| Phrase | Usually Means | Distribution |
|--------|---------------|--------------|
| "Time until first event" | Inter-arrival time | Exponential |
| "Time until n-th event" | Sum of inter-arrivals | Gamma(n,λ) |
| "Waiting time between events" | Inter-arrival time | Exponential |
| "Service time" | Time to complete task | Often Exponential |
| "Trials until success" | Number of trials | Geometric |
| "Failures until r successes" | Count of failures | Negative Binomial |

### Arrival/Counting Processes
| Phrase | Interpretation | Model |
|--------|----------------|-------|
| "Arrivals occur at rate λ" | Poisson process | N(t) ~ Poisson(λt) |
| "Events in disjoint intervals" | Independent | Poisson process |
| "Counting process" | Number of events | Poisson |
| "Rate λ per unit time" | Expected count = λ | Poisson |

---

## 3. MATHEMATICAL OPERATIONS

### Transformations of Random Variables
| Operation | Method | Section |
|-----------|--------|---------|
| Y = g(X), single variable | CDF method or direct PDF formula | 4.6 |
| (U,V) = g(X,Y), bivariate | Jacobian method | 4.6 |
| Linear: Y = aX + b | Direct: E[Y] = aE[X]+b, Var(Y) = a²Var(X) | 3.3, 4.6 |
| Sum of independent | MGF multiplication or convolution | 5.1-5.2 |

**Key Formulas:**
- CDF Method: F_Y(y) = P(g(X) ≤ y)
- Jacobian: f_{UV}(u,v) = f_{XY}(x(u,v), y(u,v)) |J|
- J = |∂(x,y)/∂(u,v)| (absolute value of determinant)

### Sum of Random Variables
| Condition | Result | Method |
|-----------|--------|--------|
| Sum of i.i.d. normals | Normal | Direct |
| Sum of i.i.d. Poissons | Poisson(sum of λ) | MGF |
| Sum of i.i.d. Exponential(λ) | Gamma(n,λ) | MGF |
| Sum of independent binomials (same p) | Binomial(n₁+n₂, p) | MGF |
| Sum of independent gammas (same λ) | Gamma(α₁+α₂, λ) | MGF |

### Order Statistics
| Term | Formula | Section |
|------|---------|---------|
| Maximum of n i.i.d. | F_max(x) = [F(x)]^n | 4.7 |
| Minimum of n i.i.d. | F_min(x) = 1 - [1-F(x)]^n | 4.7 |
| k-th order statistic | Complex formula with (k-1)!(n-k)! | 4.7 |

---

## 4. QUESTION KEYWORDS & SIGNALS

### "Find/Compute" Questions
| Keyword | What to Do | Section |
|---------|------------|---------|
| "Find the probability that..." | Calculate P(event), use CDF/PMF/PDF | Various |
| "Find the distribution of..." | Transformation, identify parameters | 4.6 |
| "Find E[X]" | Expectation calculation | 4.1 |
| "Find Var(X)" | Use E[X²] - (E[X])² | 4.3 |
| "Find Cov(X,Y)" | Use E[XY] - E[X]E[Y] | 4.4 |
| "Find correlation" | Cov(X,Y)/(σ_X σ_Y) | 4.4 |
| "Find E[X\|Y]" | Conditional expectation | 7.1 |
| "Find the MGF" | E[e^{tX}] | 5.1 |

### "Show/Prove" Questions
| Keyword | What to Do | Method |
|---------|------------|--------|
| "Show X has distribution..." | Match MGF or derive PDF | MGF or CDF method |
| "Show X and Y are independent" | Verify joint = product of marginals | Direct calculation |
| "Prove..." | Rigorous derivation | Various |

### "Approximate" Questions
| Keyword | What to Use | Conditions |
|---------|-------------|------------|
| "Approximate" | CLT or Normal approximation | Large n |
| "For large n" | CLT | n ≥ 30 typically |
| "Use normal approximation" | Standardize, use Φ | np(1-p) > 10 for binomial |
| "Continuity correction" | Add ±0.5 for discrete | Discrete → Normal |

### Conditional Questions
| Phrase | Interpretation | Method |
|--------|----------------|--------|
| "Given that" | Conditional probability/expectation | P(A\|B), E[X\|Y] |
| "If we know" | Given information | Condition on it |
| "Conditional on" | Given event occurred | P(·\|event) |
| "X given Y = y" | Conditional distribution | f(x\|y) = f(x,y)/f_Y(y) |

### Bayesian Questions
| Phrase | What to Do | Section |
|--------|------------|---------|
| "Update your belief" | Bayes' theorem | 7.1-7.2 |
| "Prior/Posterior" | Bayesian update | 7.1-7.2 |
| "Given the data" | Posterior distribution | 7.2 |
| "Predictive distribution" | Integrate over posterior | 7.3 |

---

## 5. PROFESSOR-SPECIFIC TERMINOLOGY

### Notation Preferences
| Professor Uses | Standard Notation | Meaning |
|----------------|-------------------|---------|
| ψ(t) | M(t), M_X(t) | Moment generating function |
| g₁(x\|y) | f_{X\|Y}(x\|y) | Conditional PDF of X given Y |
| π(θ) | Prior distribution | Prior |
| π(θ\|x) | f(θ\|x) | Posterior distribution |
| L(x\|θ) | f(x\|θ), p(x\|θ) | Likelihood function |
| Φ(z) | Standard normal CDF | P(Z ≤ z) for Z ~ N(0,1) |
| z_α | Critical value | P(Z > z_α) = α |

### Finance Applications
| Term | Probability Equivalent | Section |
|------|------------------------|---------|
| Stock price | Lognormal random variable | 7.3 |
| Volatility (σ) | Standard deviation | 7.3 |
| Log returns | Normal distribution | 7.3 |
| Portfolio return | Linear combination | 4.4 |
| Risk (σ) | Standard deviation | 4.3 |
| Diversification | Reducing variance via correlation | 4.4 |
| Black-Scholes | Lognormal stock model | 7.3 |
| Option pricing | E[e^{-r}(S-K)^+] | 7.3 |

### Problem Structure Patterns
| Professor Pattern | What It Usually Means |
|-------------------|----------------------|
| "Consider a game..." | Find E[X], use total expectation |
| "Suppose X,Y are jointly normal..." | Use bivariate normal properties |
| "Let X₁,...,Xₙ be i.i.d..." | CLT or LLN applies |
| "Update your belief..." | Bayesian problem |
| "What is the probability that..." | Direct calculation |
| "Find the distribution of..." | Transformation |

---

## 6. REVERSE LOOKUP: PHRASE → CONCEPT → SECTION

### A-C
| Phrase Seen | Concept | Section |
|-------------|---------|---------|
| "Approximately normal" | Central Limit Theorem | 6.1 |
| "Arrivals occur at rate λ" | Poisson Process | 2.3 |
| "Average of n observations" | Sample mean, CLT | 6.1 |
| "Bayesian update" | Bayes' theorem | 7.1-7.2 |
| "Bell curve" | Normal distribution | 3.3 |
| "Bernoulli trials" | Binomial distribution | 2.2 |
| "Bivariate normal" | Joint normal distribution | 4.5 |
| "CLT" | Central Limit Theorem | 6.1 |
| "Conditionally independent" | Independence given variable | 4.3 |
| "Confidence interval" | CI using CLT | 6.4 |
| "Conjugate prior" | Beta-Binomial, Gamma-Poisson | 7.2 |
| "Converges in distribution" | Limit theorem | 6.1-6.3 |
| "Converges in probability" | Law of Large Numbers | 6.3 |
| "Correlation" | ρ = Cov(X,Y)/(σ_X σ_Y) | 4.4 |
| "Counting process" | Poisson process | 2.3 |
| "Covariance" | Cov(X,Y) = E[XY] - E[X]E[Y] | 4.4 |

### D-G
| Phrase Seen | Concept | Section |
|-------------|---------|---------|
| "Defect rate" | Often Binomial or Poisson | 2.2, 2.3 |
| "Distribution of max/min" | Order statistics | 4.7 |
| "Draw without replacement" | Hypergeometric | 2.6 |
| "Equally likely" | Uniform distribution | 3.2 |
| "Expected value" | Expectation E[X] | 4.1 |
| "Exponential waiting time" | Exp(λ), memoryless | 3.4 |
| "Find the joint density" | Joint PDF | 4.1 |
| "First success" | Geometric distribution | 2.4 |
| "Gaussian" | Normal distribution | 3.3 |
| "Gaussian vector" | Multivariate normal | 4.5 |
| "Geometric" | Trials until first success | 2.4 |
| "Given that" | Conditional probability | 1.2 |

### H-L
| Phrase Seen | Concept | Section |
|-------------|---------|---------|
| "Hypothesis" | Prior in Bayesian context | 1.3, 7.1 |
| "i.i.d." | Independent identically distributed | Various |
| "Independent components" | Diagonal covariance, ρ=0 | 4.5 |
| "Inter-arrival time" | Exponential distribution | 3.4 |
| "Jacobian" | Transformation method | 4.6 |
| "Joint density" | f(x,y) | 4.1 |
| "Jointly normal" | Bivariate normal | 4.5 |
| "Large n" | CLT applies | 6.1 |
| "Large sample" | CLT, normal approximation | 6.1-6.2 |
| "Law of large numbers" | X̄ → μ as n → ∞ | 6.3 |
| "Likelihood" | P(data\|parameter) | 7.1 |
| "Linear combination" | aX + bY | 3.3, 4.5 |
| "Log returns" | Normal distribution | 7.3 |
| "Lognormal" | Y = e^X where X ~ Normal | 7.3 |

### M-P
| Phrase Seen | Concept | Section |
|-------------|---------|---------|
| "Marginal distribution" | Integrate out other variable | 4.2 |
| "Maximum/Minimum" | Order statistics | 4.7 |
| "Mean" | E[X], expectation | 4.1 |
| "Memoryless" | Exponential or Geometric | 3.4, 2.4 |
| "MGF" | Moment generating function | 5.1 |
| "Moment generating function" | E[e^{tX}] | 5.1 |
| "Multivariate normal" | Joint normal, MVN | 4.5 |
| "n trials" | Binomial | 2.2 |
| "Negative binomial" | Failures before r successes | 2.5 |
| "Normal approximation" | Use CLT for discrete | 6.2 |
| "Number of arrivals" | Poisson | 2.3 |
| "Number of successes" | Binomial | 2.2 |
| "Poisson process" | Arrivals at rate λ | 2.3 |
| "Posterior" | P(θ\|data) | 7.1 |
| "Prior" | P(θ) before data | 7.1 |
| "Probability integral transform" | F(X) ~ Uniform(0,1) | 3.8 |

### Q-S
| Phrase Seen | Concept | Section |
|-------------|---------|---------|
| "Quantile" | F^{-1}(p) | 3.1 |
| "Random point" | Uniform distribution | 3.2 |
| "Rate λ" | Poisson or Exponential parameter | 2.3, 3.4 |
| "Sample mean" | X̄ = (1/n)ΣXᵢ | 6.1 |
| "Service time" | Often Exponential | 3.4 |
| "Standard deviation" | σ = √Var(X) | 4.3 |
| "Standard normal" | N(0,1), Z | 3.3 |
| "Standardize" | Z = (X-μ)/σ | 3.3 |
| "Stock price" | Lognormal model | 7.3 |
| "Success/failure" | Bernoulli/Binomial | 2.2 |
| "Sum of exponentials" | Gamma distribution | 3.5 |
| "Sum of independent" | Use MGF or convolution | 5.2 |

### T-Z
| Phrase Seen | Concept | Section |
|-------------|---------|---------|
| "Total expectation" | E[X] = E[E[X\|Y]] | 7.1 |
| "Total probability" | P(A) = ΣP(A\|Bᵢ)P(Bᵢ) | 1.3 |
| "Total variance" | Var(X) = E[Var(X\|Y)] + Var(E[X\|Y]) | 7.1 |
| "Transformation" | Y = g(X), find distribution | 4.6 |
| "Trials until success" | Geometric | 2.4 |
| "Uncorrelated" | Cov(X,Y) = 0, ρ = 0 | 4.4 |
| "Update belief" | Bayesian, posterior | 7.1 |
| "Variance" | Var(X) = E[X²] - (E[X])² | 4.3 |
| "Volatility" | σ in finance, standard deviation | 7.3 |
| "Waiting time" | Exponential, Gamma | 3.4, 3.5 |
| "Without replacement" | Hypergeometric | 2.6 |

---

## 7. CRITICAL SYNONYM CHAINS

### Chain 1: Normal Family
```
Normal ≡ Gaussian ≡ N(μ,σ²) ≡ "bell curve" ≡ "approximately normal"
    ↓
Standard Normal ≡ N(0,1) ≡ Z ≡ "standardized"
    ↓
Bivariate Normal ≡ Jointly Normal ≡ MVN (2D) ≡ "Gaussian vector"
    ↓ (special case)
Independent components ≡ Diagonal Σ ≡ ρ = 0 ≡ Uncorrelated (for normals, same as independent!)
```

### Chain 2: Counting/Waiting
```
Poisson(λ) ≡ "arrivals" ≡ "counting process" ≡ "events at rate λ"
    ↓ (inter-arrival times)
Exponential(λ) ≡ "waiting time" ≡ "memoryless" ≡ "time until event"
    ↓ (sum of n exponentials)
Gamma(n,λ) ≡ "time until n-th arrival" ≡ "Erlang" (if n integer)
```

### Chain 3: Trials/Successes
```
Bernoulli(p) ≡ "success/failure" ≡ "binary" ≡ "indicator"
    ↓ (sum of n)
Binomial(n,p) ≡ "n trials" ≡ "number of successes"
    ↓ (wait for first)
Geometric(p) ≡ "first success" ≡ "trials until" ≡ "memoryless (discrete)"
    ↓ (wait for r-th)
Negative Binomial(r,p) ≡ "r successes" ≡ "sum of r geometrics"
```

### Chain 4: Bayesian
```
Prior ≡ π(θ) ≡ "belief before data"
    ↓ (+ Likelihood)
Posterior ≡ π(θ|x) ≡ "updated belief" ≡ "belief after data"
    ↓
Posterior ∝ Likelihood × Prior
    ↓ (special cases)
Beta-Binomial ≡ Conjugate ≡ "closed-form update"
Gamma-Poisson ≡ Conjugate
Normal-Normal ≡ Conjugate (known variance)
```

---

## 8. DISTRIBUTION PARAMETER NOTATION VARIANTS

| Distribution | Notation Variants | Parameters |
|--------------|-------------------|------------|
| Normal | N(μ,σ²), N(μ,σ), Normal(μ,σ²) | Mean μ, Variance σ² |
| Exponential | Exp(λ), Exp(β), Exponential(λ) | Rate λ (mean = 1/λ) |
| Poisson | Pois(λ), Poisson(λ), Po(λ) | Mean = Variance = λ |
| Binomial | Bin(n,p), B(n,p), Binomial(n,p) | n trials, prob p |
| Gamma | Γ(α,β), Gamma(α,β), Gamma(r,λ) | Shape α, Rate β |
| Beta | Beta(α,β), Be(α,β) | Shape parameters α, β |

**Warning:** Some textbooks use scale parameter (1/rate) for Exponential and Gamma!

---

## 9. KEY FORMULA QUICK REFERENCE BY SYNONYM

### "Find the mean" = E[X]
- Discrete: Σ x·P(X=x)
- Continuous: ∫ x·f(x)dx
- Conditional: E[X|Y=y] = ∫ x·f(x|y)dx

### "Find the variance" = Var(X)
- Var(X) = E[X²] - (E[X])²
- Var(aX+b) = a²Var(X)
- Var(X+Y) = Var(X) + Var(Y) + 2Cov(X,Y)

### "Find the covariance" = Cov(X,Y)
- Cov(X,Y) = E[XY] - E[X]E[Y]
- Cov(X,X) = Var(X)
- Independent → Cov = 0 (but NOT vice versa!)

### "Find the correlation" = ρ
- ρ = Cov(X,Y)/(σ_X · σ_Y)
- -1 ≤ ρ ≤ 1
- For bivariate normal: ρ = 0 ⟺ independent

### "Apply CLT" = Central Limit Theorem
- Z = (X̄ - μ)/(σ/√n) → N(0,1)
- X̄ ≈ N(μ, σ²/n) for large n
- Continuity correction: ±0.5 for discrete

---

_End of Terminology Master Map_
