# Problem Variations Guide

**Generated:** December 16, 2025
**Purpose:** Show 5+ variations for each problem type with solution path changes

---

# VARIATION PATTERN LIBRARY

## Pattern 1: Different Question Target

When original asks for $P(X = k)$, variations might ask for:
- $P(X \leq k)$ → Use CDF
- $P(X > k)$ → Use complement
- $P(a < X \leq b)$ → Use CDF difference
- $E[X]$ → Use expectation formula
- $\text{Var}(X)$ → Use variance formula
- Quantile/percentile → Inverse CDF

## Pattern 2: Different Distribution Parameters

When original uses specific parameters:
- Large n, small p (Binomial) → Poisson approximation
- Large n (any distribution) → CLT/Normal approximation
- Different parameterization → Check if λ vs 1/λ

## Pattern 3: Different Mathematical Operation

When original asks for probability:
- Conditional probability → $P(A|B) = P(A \cap B)/P(B)$
- Joint probability → $P(A \cap B)$
- Finding quantiles → Solve $F(x) = p$
- Transformation → Find distribution of $g(X)$

## Pattern 4: Different Solution Method

For same problem type:
- Direct calculation vs MGF approach
- CDF method vs PDF method
- Indicator variables vs direct counting
- Simulation vs exact formula

## Pattern 5: Terminology Variations

Same concept, different words:
- "Gaussian" = "Normal" = $N(\mu, \sigma^2)$
- "Gaussian vector" = "MVN" = "Jointly normal"
- "Independent components" = $\rho = 0$ (for MVN: independent!)
- "Mean $\theta$" for Exp means $\lambda = 1/\theta$

---

# BIVARIATE NORMAL PROBLEMS

## Representative Problem: HW5-Q1

**Original:**
Let X and Y be jointly normal with $\mu_X = 1$, $\sigma_X^2 = 2$, $\mu_Y = -2$, $\sigma_Y^2 = 3$, $\rho = -2/3$.
Find $P(X + Y > 0)$.

**Primary Solution:**
- Section: 4.5 (Bivariate Normal)
- Method: X + Y is normal, find parameters, standardize

---

### Variation 1: Find E[X + Y] instead

**If problem asked:** "Find E[X + Y]"

**Solution Change:**
- Much simpler: E[X + Y] = E[X] + E[Y] = 1 + (-2) = -1
- Section: 4.4 (only need expectation linearity)

**When to use:** Keywords "expected value", "mean"

---

### Variation 2: Find Var(X + Y) instead

**If problem asked:** "Find Var(X + Y)"

**Solution Change:**
- Must include correlation term
- Var(X+Y) = Var(X) + Var(Y) + 2Cov(X,Y)
- Cov(X,Y) = ρσ_X σ_Y
- Section: 4.4

**When to use:** Keywords "variance", "standard deviation"

---

### Variation 3: Find P(X > Y) instead

**If problem asked:** "Find P(X > Y)"

**Solution Change:**
- Define Z = X - Y
- Z is normal (linear combo of jointly normal)
- E[Z] = E[X] - E[Y] = 1 - (-2) = 3
- Var(Z) = Var(X) + Var(Y) - 2Cov(X,Y)
- Section: 4.5 (same method, different linear combination)

---

### Variation 4: Conditional distribution Y|X = x

**If problem asked:** "Find the distribution of Y given X = 80"

**Solution Change:**
- Use BVN conditional formula
- Y|X=x ~ N(μ_{Y|X}, σ²_{Y|X})
- μ_{Y|X} = μ_Y + ρ(σ_Y/σ_X)(x - μ_X)
- σ²_{Y|X} = (1-ρ²)σ²_Y
- Section: 4.5, Template F

**When to use:** "Given X = x", "conditional distribution"

---

### Variation 5: Find a, b for independence

**If problem asked:** "If Y₁ = aX + Y, Y₂ = X + bY, find a, b for Y₁, Y₂ independent"

**Solution Change:**
- For MVN: independence ⟺ Cov = 0
- Set Cov(Y₁, Y₂) = 0
- Solve for relationship between a and b
- Section: 4.5, Template G

**When to use:** "Independent components", "find parameters for independence"

---

### Variation 6: Different parameters (ρ = 0)

**If ρ = 0:**
- X and Y are independent (unique to normal!)
- Var(X+Y) = Var(X) + Var(Y) (no covariance term)
- P(X+Y > 0) simplifies
- Section: 4.5 with simplification

---

### Variation 7: Asked for conditional probability

**If problem asked:** "Find P(X + Y > 0 | X > 0)"

**Solution Change:**
- Need joint event P(X + Y > 0, X > 0)
- Divide by P(X > 0)
- May require double integral or clever geometric argument
- Section: 4.5 with conditioning

---

### Variation 8: Using MGF approach

**Alternative method:**
- MGF of sum: M_{X+Y}(t) = E[e^{t(X+Y)}]
- For bivariate normal: known formula
- Section: 5.2 (MGF for sums)
- Usually overkill for this problem

---

### Quick Reference for BVN Variations

| Question Type | Key Formula | Section |
|--------------|-------------|---------|
| P(X+Y > c) | Sum is N(μ₁+μ₂, σ₁²+σ₂²+2ρσ₁σ₂) | 4.5 |
| P(X > Y) | Difference is normal | 4.5 |
| E[X+Y] | μ₁ + μ₂ | 4.4 |
| Var(X+Y) | σ₁² + σ₂² + 2ρσ₁σ₂ | 4.4 |
| Y\|X=x | N(μ_Y + ρ(σ_Y/σ_X)(x-μ_X), (1-ρ²)σ²_Y) | 4.5 |
| Independence | Set Cov = 0 | 4.5 |
| E[Y\|X=x] | μ_Y + ρ(σ_Y/σ_X)(x-μ_X) | 4.5 |
| Var(Y\|X) | (1-ρ²)σ²_Y (constant!) | 4.5 |

---

# CLT PROBLEMS

## Representative Problem: PF-Q1

**Original:**
Toss fair coin twice. Win $3 if HH, lose $1 if TT, $0 otherwise. Play 400 times. Find P(total ≥ $240).

**Primary Solution:**
- Section: 6.1 (CLT)
- Template: B (CLT Game Problems)
- Method: Find μ, σ² for single game, apply CLT

---

### Variation 1: Ask for expected total instead

**If problem asked:** "What is your expected total after 400 games?"

**Solution Change:**
- E[Total] = n × E[single game] = 400 × 0.5 = $200
- No CLT needed
- Section: 2.1 (just expectation)

---

### Variation 2: Ask for P(total < 180)

**If problem asked:** "P(total < $180)"

**Solution Change:**
- Same CLT approach
- Standardize: Z = (180 - 200)/30
- P(Z < -2/3) = Φ(-0.667)
- Section: 6.1

---

### Variation 3: Find quantile x such that P(total > x) = 0.9

**If problem asked:** "Find x such that winnings exceed x with probability 0.9"

**Solution Change:**
- 1 - Φ((x-200)/30) = 0.9
- Φ((x-200)/30) = 0.1
- (x-200)/30 = -1.28
- x = 200 - 38.4 = $161.60
- Section: 6.1 (inverse CLT)

---

### Variation 4: Different number of games (n = 100)

**If n = 100 instead of 400:**

**Solution Change:**
- Total ~ N(100×0.5, 100×2.25) = N(50, 225)
- SD = 15 instead of 30
- Standardize accordingly
- Section: 6.1 (same method, different parameters)

---

### Variation 5: Different game payoffs

**If win $5 for HH, lose $2 for TT:**

**Solution Change:**
- Recalculate E[X] = 5(1/4) - 2(1/4) = 0.75
- Recalculate Var(X) = E[X²] - E[X]²
- Apply CLT with new parameters
- Section: 6.1, Template B

---

### Variation 6: Biased coin (p ≠ 0.5)

**If P(H) = 0.6:**

**Solution Change:**
- P(HH) = 0.36, P(TT) = 0.16, P(other) = 0.48
- Recalculate E[X], Var(X)
- Apply CLT
- Section: 6.1

---

### Variation 7: Continuity correction

**If asking for discrete count:**
- P(Total ≥ 240) ≈ P(Y > 239.5) for continuous normal
- Section: 6.2 (continuity correction)

---

### Variation 8: Find minimum n for probability condition

**If problem asked:** "What's the smallest n such that P(total > 0) ≥ 0.99?"

**Solution Change:**
- Need P(S_n > 0) ≥ 0.99
- S_n ~ N(0.5n, 2.25n)
- Find n such that P(Z > -0.5n/1.5√n) ≥ 0.99
- Section: 6.1, Template K

---

### Quick Reference for CLT Variations

| Question Type | Key Formula | Section |
|--------------|-------------|---------|
| P(S_n > c) | Standardize, use Φ | 6.1 |
| P(X̄ in range) | X̄ ~ N(μ, σ²/n) | 6.1 |
| Find quantile | Solve Φ((x-μ)/σ) = p | 6.1 |
| Find n for precision | n ≥ (zσ/ε)² | 6.1, Template K |
| Continuity correction | Add ±0.5 | 6.2 |
| Proportion | p̂ ~ N(p, p(1-p)/n) | 6.1 |
| Confidence interval | X̄ ± z_{α/2}σ/√n | 6.4 |

---

# BAYESIAN PROBLEMS

## Representative Problem: HW6-Q1 (Monty Hall)

**Original:**
Monty Hall with sober vs dizzy host. Find posterior probabilities and optimal strategy.

**Primary Solution:**
- Section: 7.2 (Bayesian Statistics)
- Template: J (Monty Hall Variants)
- Method: Bayes table with prior, likelihood, posterior

---

### Variation 1: Different likelihoods (host behavior)

**If host has different behavior:**
- Sober: knows car location
- Dizzy: random door selection
- Sleepy: always opens same door
- Key: Likelihood function changes!
- Section: 7.2

---

### Variation 2: Continuous prior instead of discrete

**If θ ~ Uniform(0,1) instead of discrete:**
- Posterior is Beta distribution
- Use conjugate prior result
- Section: 7.2 (Beta-Binomial)

---

### Variation 3: Multiple observations

**If observe multiple data points:**
- Sequential updating: posterior becomes prior
- Or: batch update with total counts
- Section: 7.2

---

### Variation 4: Predictive distribution

**If asked:** "Predict next observation"

**Solution Change:**
- P(X_{n+1} | data) = ∫ P(X_{n+1}|θ) π(θ|data) dθ
- Weight likelihood over posterior
- Section: 7.2, Template H

---

### Variation 5: Posterior mean and variance

**If asked:** "Find E[θ|data] and Var(θ|data)"

**Solution Change:**
- For discrete: weighted average over posterior
- For Beta(α,β): E = α/(α+β), Var = αβ/[(α+β)²(α+β+1)]
- Section: 7.2

---

### Variation 6: Different prior

**If prior not uniform:**
- Use given prior in Bayes formula
- For Beta(α,β) prior → Beta(α+k, β+n-k) posterior
- Section: 7.2

---

### Variation 7: Hypothesis testing

**If asked:** "Which hypothesis is most likely?"

**Solution Change:**
- Compare posterior probabilities
- Most likely = highest posterior
- Section: 7.2

---

### Variation 8: MAP vs posterior mean

**If asked for point estimate:**
- MAP (Maximum a Posteriori): mode of posterior
- Posterior mean: expected value
- Different for skewed distributions
- Section: 7.2

---

### Quick Reference for Bayesian Variations

| Question Type | Key Formula | Section |
|--------------|-------------|---------|
| Posterior | π(θ\|x) ∝ L(x\|θ)π(θ) | 7.2 |
| Beta-Binomial | Beta(α,β) → Beta(α+k, β+n-k) | 7.2 |
| Predictive | P(x_{n+1}\|data) = ∫P(x\|θ)π(θ\|data)dθ | 7.2 |
| Posterior mean | E[θ\|data] | 7.2 |
| MAP estimate | argmax π(θ\|data) | 7.2 |
| Gamma-Poisson | Gamma(α,β) → Gamma(α+Σx, β+n) | 7.2 |

---

# JOINT DISTRIBUTION PROBLEMS

## Representative Problem: HW4-Q1

**Original:**
f(x,y) = c(x² + xy) on [0,1]². Find c, marginals, covariance, check independence.

**Primary Solution:**
- Section: 4.1 (Joint Distributions)
- Method: Integrate, find marginals, compute moments

---

### Variation 1: Different support region

**If support is triangular: 0 < y < x < 1:**
- Integration limits change
- Be careful with order of integration
- Section: 4.1

---

### Variation 2: Ask for conditional distribution

**If asked:** "Find f(y|x)"

**Solution Change:**
- f(y|x) = f(x,y)/f_X(x)
- Must find marginal first
- Section: 4.2

---

### Variation 3: Ask for conditional expectation

**If asked:** "Find E[Y|X=x]"

**Solution Change:**
- E[Y|X=x] = ∫ y f(y|x) dy
- This is a function of x
- Section: 7.1 (Conditional Expectation)

---

### Variation 4: Find P(Y > X)

**If asked:** "Find P(Y > X)"

**Solution Change:**
- Integrate f(x,y) over region {y > x}
- ∫∫_{y>x} f(x,y) dxdy
- Section: 4.1

---

### Variation 5: Independence check with different joint

**If f(x,y) = g(x)h(y) (separable):**
- May be independent
- Check: does support factor?
- Does f factor into product of marginals?
- Section: 4.3

---

### Variation 6: Find CDF F(x,y)

**If asked:** "Find joint CDF"

**Solution Change:**
- F(x,y) = ∫∫ f(u,v) dudv with appropriate limits
- Section: 4.1

---

### Variation 7: Correlation instead of covariance

**If asked for ρ instead of Cov:**
- ρ = Cov(X,Y)/(σ_X σ_Y)
- Need to also compute standard deviations
- Section: 4.4

---

### Variation 8: Transform to new variables

**If asked:** "Find distribution of U = X + Y"

**Solution Change:**
- Use convolution or Jacobian method
- Or CDF method: F_U(u) = P(X + Y ≤ u)
- Section: 4.6

---

### Quick Reference for Joint Distribution Variations

| Question Type | Key Formula | Section |
|--------------|-------------|---------|
| Find c | ∫∫f(x,y)dxdy = 1 | 4.1 |
| Marginal | f_X(x) = ∫f(x,y)dy | 4.2 |
| Conditional | f(y\|x) = f(x,y)/f_X(x) | 4.2 |
| E[XY] | ∫∫xy f(x,y)dxdy | 4.4 |
| Independence | f(x,y) = f_X(x)f_Y(y) ∀(x,y) | 4.3 |
| Cov(X,Y) | E[XY] - E[X]E[Y] | 4.4 |
| E[Y\|X=x] | ∫y f(y\|x)dy | 7.1 |
| P(Y > X) | ∫∫_{y>x} f(x,y)dxdy | 4.1 |

---

# LOGNORMAL PROBLEMS

## Representative Problem: PF-Q4

**Original:**
S = S₀e^Z where Z ~ N(r - σ²/2, σ²). Find E[e^{-r}S] and P(S > 100).

**Primary Solution:**
- Section: 7.3 (Lognormal)
- Template: D (Lognormal Stock Price)

---

### Variation 1: Find E[S] directly

**If asked:** "Find E[S]"

**Solution Change:**
- E[S] = S₀ E[e^Z] = S₀ e^{μ + σ²/2}
- Key formula: E[e^X] = e^{μ + σ²/2} for X ~ N(μ, σ²)
- Section: 7.3

---

### Variation 2: Find Var(S)

**If asked:** "Find Var(S)"

**Solution Change:**
- Var(Y) = e^{2μ+σ²}(e^{σ²} - 1) where Y = e^X, X ~ N(μ,σ²)
- Section: 7.3

---

### Variation 3: Find median of S

**If asked:** "Find median of S"

**Solution Change:**
- Median of lognormal = e^μ
- Note: median ≠ mean for lognormal!
- Section: 7.3

---

### Variation 4: P(S < K) instead of P(S > K)

**If asked:** "Find P(S < 50)"

**Solution Change:**
- P(S < K) = P(Z < ln(K/S₀))
- = Φ((ln(K/S₀) - μ)/σ)
- Section: 7.3

---

### Variation 5: Product of lognormals

**If asked:** "Find distribution of S₁S₂ for independent lognormals"

**Solution Change:**
- ln(S₁S₂) = ln(S₁) + ln(S₂) ~ N(μ₁+μ₂, σ₁²+σ₂²)
- S₁S₂ is lognormal
- Section: 7.3, Template I

---

### Variation 6: Different time horizon

**If asking about S_t for different t:**
- Z_t ~ N((r-σ²/2)t, σ²t)
- Mean and variance scale with t
- Section: 7.3

---

### Variation 7: Find quantile (VaR)

**If asked:** "Find 95th percentile of S"

**Solution Change:**
- Find z_{0.95} from standard normal
- S_{0.95} = S₀ exp(μ + σ × z_{0.95})
- Section: 7.3

---

### Variation 8: Ratio of lognormals

**If asked:** "Find distribution of S₁/S₂"

**Solution Change:**
- ln(S₁/S₂) = ln(S₁) - ln(S₂) ~ N(μ₁-μ₂, σ₁²+σ₂²)
- Ratio is lognormal
- Section: 7.3

---

### Quick Reference for Lognormal Variations

| Question Type | Key Formula | Section |
|--------------|-------------|---------|
| E[e^X], X~N(μ,σ²) | e^{μ + σ²/2} | 7.3 |
| P(S > K) | 1 - Φ((ln(K/S₀)-μ)/σ) | 7.3 |
| Median | e^μ | 7.3 |
| Variance | e^{2μ+σ²}(e^{σ²}-1) | 7.3 |
| Product | Lognormal with added μ, σ² | 7.3 |
| Ratio | Lognormal with subtracted μ | 7.3 |
| E[S] | S₀ e^{μ+σ²/2} | 7.3 |

---

# EXPONENTIAL DISTRIBUTION PROBLEMS

## Representative Problem: HW3-Q6

**Original:**
X ~ Exp(λ). Find survival function, mean, and distribution of min(X₁, X₂).

**Primary Solution:**
- Section: 3.4 (Exponential)

---

### Variation 1: Parameterization trap

**If "mean θ = 3":**
- CAREFUL: λ = 1/θ = 1/3
- NOT λ = 3!
- Section: 3.4

---

### Variation 2: Maximum instead of minimum

**If asked for max(X₁, X₂):**
- F_max(x) = [F(x)]² = (1 - e^{-λx})²
- Not exponential!
- Section: 4.7 (Order Statistics)

---

### Variation 3: Sum of exponentials

**If asked for X₁ + X₂:**
- Sum of n Exp(λ) is Gamma(n, λ)
- Section: 3.5 (Gamma)

---

### Variation 4: Memoryless property

**If asked:** "P(X > s+t | X > s)"

**Solution Change:**
- = P(X > t) by memoryless property
- Only works for exponential!
- Section: 3.4

---

### Variation 5: Conditional on event

**If asked:** "Find E[X | X > a]"

**Solution Change:**
- By memoryless: E[X | X > a] = a + E[X] = a + 1/λ
- Section: 3.4

---

### Variation 6: CLT for exponential average

**If large n, asking about X̄:**
- X̄ ~ N(1/λ, 1/(nλ²)) approximately
- Section: 6.1, Template C

---

### Variation 7: Competing exponentials

**If X ~ Exp(λ), Y ~ Exp(μ) independent:**
- P(X < Y) = λ/(λ+μ)
- Section: 3.4

---

### Quick Reference for Exponential Variations

| Question Type | Key Formula | Section |
|--------------|-------------|---------|
| P(X > x) | e^{-λx} | 3.4 |
| E[X] | 1/λ | 3.4 |
| Var(X) | 1/λ² | 3.4 |
| min of n | Exp(nλ) | 3.4 |
| Sum of n | Gamma(n, λ) | 3.5 |
| Memoryless | P(X>s+t\|X>s) = P(X>t) | 3.4 |
| P(X < Y) | λ/(λ+μ) | 3.4 |
| Mean θ → λ | λ = 1/θ | 3.4 |

---

# ORDER STATISTICS PROBLEMS

## Representative Problem: PM2-Q3b

**Original:**
X₁,...,X_n i.i.d. Uniform(-1,1). Find CDF of Z = max(X₁,...,X_n).

**Primary Solution:**
- Section: 4.7 (Order Statistics)
- Formula: F_max(z) = [F(z)]^n

---

### Variation 1: Find minimum instead

**If asked for min:**
- F_min(x) = 1 - [1-F(x)]^n
- Or: P(min > a) = [1-F(a)]^n
- Section: 4.7, Template L

---

### Variation 2: Find PDF of max

**If asked for density:**
- f_max(x) = n[F(x)]^{n-1}f(x)
- Section: 4.7

---

### Variation 3: Find E[max]

**If asked for expected maximum:**
- For Uniform(0,1): E[X_{(n)}] = n/(n+1)
- Section: 4.7

---

### Variation 4: Different distribution (Exponential)

**If X_i ~ Exp(λ):**
- Max: F_max(x) = (1-e^{-λx})^n
- Min: Exp(nλ) - nice closed form!
- Section: 4.7

---

### Variation 5: Range (max - min)

**If asked for range:**
- R = X_{(n)} - X_{(1)}
- Need joint distribution of max and min
- Section: 4.7

---

### Variation 6: k-th order statistic

**If asked for median (middle value):**
- Use general order statistic formula
- f_{X_{(k)}}(x) = n!/(k-1)!(n-k)! [F(x)]^{k-1}[1-F(x)]^{n-k}f(x)
- Section: 4.7

---

### Variation 7: Probability of max in range

**If asked:** "P(max > a)"

**Solution Change:**
- P(max > a) = 1 - [F(a)]^n
- Section: 4.7

---

### Quick Reference for Order Statistics Variations

| Question Type | Key Formula | Section |
|--------------|-------------|---------|
| P(max ≤ x) | [F(x)]^n | 4.7 |
| P(min ≤ x) | 1 - [1-F(x)]^n | 4.7 |
| P(max > a) | 1 - [F(a)]^n | 4.7 |
| f_max(x) | n[F(x)]^{n-1}f(x) | 4.7 |
| E[max] (Unif) | n/(n+1) | 4.7 |
| E[min] (Unif) | 1/(n+1) | 4.7 |
| min of Exp(λ) | Exp(nλ) | 4.7 |

---

# MULTI-STEP PROBLEM VARIATIONS

## Pattern: Component Changes

For complex problems requiring multiple concepts, show how changes propagate:

### Example: i.i.d. Normals → Max → Probability

**Original:** X₁,...,X₁₀ i.i.d. N(0,1). Find P(max > 2).

| Change | Affected Steps | New Sections |
|--------|---------------|--------------|
| Different distribution (Exp) | Step 1 | 3.4 instead of 3.3 |
| Min instead of Max | Step 2 | 4.7 (different formula) |
| Sum instead of Max | Steps 2-3 | 3.3 (sum of normals) |
| Ask for E[max] | Step 3 | 4.7 |
| Not i.i.d. | All steps | Need joint distribution |
| Large n | May use CLT | 6.1 |

---

### Example: Joint PDF → Covariance → Correlation

**Original:** f(x,y) = c(x² + xy). Find ρ.

| Change | Affected Steps | New Sections |
|--------|---------------|--------------|
| Different region | Step 1 (integration) | 4.1 |
| Ask for Cov only | Stop earlier | 4.4 |
| Ask for independence | Check product | 4.3 |
| Add transformation | New variable | 4.6 |
| Conditional distribution | Division step | 4.2 |

---

### Example: Bayesian Update Chain

**Original:** Prior → Data → Posterior

| Change | Affected Steps | Notes |
|--------|---------------|-------|
| Different prior | Likelihood unchanged | Posterior changes |
| Different data | Prior unchanged | Likelihood changes |
| Continuous prior | Integration | Use conjugate |
| Predictive | One more step | Weight over posterior |
| Sequential update | Chain | Posterior → Prior |

---

# TERMINOLOGY VARIATION TABLE

| Original Term | Variations | Same Section |
|--------------|------------|--------------|
| Gaussian | Normal, N(μ,σ²), bell curve | 3.3 |
| Gaussian vector | MVN, jointly normal, bivariate normal | 4.5 |
| Independent components | ρ = 0, diagonal covariance | 4.5 |
| Exponential | Exp(λ), memoryless, waiting time | 3.4 |
| Mean θ (Exp) | λ = 1/θ (NOT θ!) | 3.4 |
| Rate λ | Mean = 1/λ | 3.4 |
| i.i.d. | Independent and identically distributed | 6.1 |
| CLT | Central Limit Theorem, normal approximation | 6.1 |
| Prior | Initial belief, before data | 7.2 |
| Posterior | Updated belief, after data | 7.2 |
| Conjugate | Posterior same family as prior | 7.2 |
| Lognormal | e^X where X normal, stock price | 7.3 |
| ψ(t) | MGF, M(t), moment generating function | 5.1 |

---

# QUICK DECISION TABLE: VARIATION TYPE → ACTION

| If Problem Changes From... To... | Change In Solution |
|----------------------------------|-------------------|
| P(X=k) → P(X≤k) | Use CDF instead of PMF |
| P(X>a) → P(X<a) | Complement or direct |
| E[X] → Var(X) | Additional computation |
| Probability → Quantile | Inverse CDF |
| Single RV → Sum | Use MGF or convolution |
| Sum → Average | Divide by n |
| Exact → Approximate | Use CLT (Section 6.1) |
| Binomial, large n → ? | Normal approximation |
| Single observation → n observations | Update formula |
| Discrete prior → Continuous prior | Integral instead of sum |
| Joint → Marginal | Integrate out |
| Joint → Conditional | Divide by marginal |
| Independent → Correlated | Add covariance terms |
| Normal → General | May need CLT |

