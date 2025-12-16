# Question Taxonomy - Probability Theory

**Generated:** December 16, 2025
**Purpose:** Hierarchical taxonomy of all question types with recognition criteria and solution approaches

---

## 📊 HIERARCHICAL STRUCTURE OVERVIEW

```
LEVEL 1: Major Topic Areas (7 categories)
    └── LEVEL 2: Sub-topics (30+ subcategories)
        └── LEVEL 3: Question Types (60+ specific patterns)
            └── LEVEL 4: Solution Methods (100+ techniques)
```

---

# LEVEL 1: FUNDAMENTAL CONCEPTS (Pre-M1)

## L2.1: Basic Probability & Counting

### L3.1.1: Counting Arrangements
**Recognition Keywords:** "How many ways", "arrangements", "permutations"
**Required Concepts:** Factorials, permutations, combinations
**Solution Pattern L4:**
1. Identify if order matters (permutation) or not (combination)
2. Check for repetition
3. Apply appropriate formula: P(n,k) or C(n,k)
**Common Variations:** With/without replacement, circular arrangements
**Pitfalls:** Confusing P and C, double-counting

### L3.1.2: Sample Space Problems
**Recognition Keywords:** "All possible outcomes", "equally likely"
**Required Concepts:** Sample space definition, counting principles
**Solution Pattern L4:**
1. List or count all outcomes in S
2. Count favorable outcomes in event A
3. P(A) = |A|/|S|
**Common Variations:** Dice, cards, coins
**Pitfalls:** Missing outcomes, wrong granularity

### L3.1.3: Complement & Union Problems
**Recognition Keywords:** "At least one", "none", "either...or"
**Required Concepts:** Set operations, DeMorgan's laws
**Solution Pattern L4:**
1. Check if complement is easier
2. P(A^c) = 1 - P(A)
3. P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
**Common Variations:** Multiple events, nested complements
**Pitfalls:** Forgetting intersection term

## L2.2: Conditional Probability & Independence

### L3.2.1: Direct Conditional Calculation
**Recognition Keywords:** "Given that", "if we know", "conditional on"
**Required Concepts:** Conditional probability definition
**Solution Pattern L4:**
1. Identify condition B and target A
2. Find P(A ∩ B) and P(B)
3. P(A|B) = P(A ∩ B)/P(B)
**Common Variations:** Multiple conditions, sequential events
**Pitfalls:** Confusing P(A|B) with P(B|A)

### L3.2.2: Multiplication Rule Applications
**Recognition Keywords:** "Sequence of events", "then", "followed by"
**Required Concepts:** Chain rule, tree diagrams
**Solution Pattern L4:**
1. Break into sequence
2. P(A₁ ∩ ... ∩ Aₙ) = P(A₁)P(A₂|A₁)...P(Aₙ|A₁∩...∩Aₙ₋₁)
3. Draw tree if helpful
**Common Variations:** With/without replacement
**Pitfalls:** Wrong conditioning order

### L3.2.3: Independence Testing
**Recognition Keywords:** "Are...independent?", "Does...affect?"
**Required Concepts:** Independence definition
**Solution Pattern L4:**
1. Check P(A ∩ B) = P(A)P(B)
2. Or verify conditional equals marginal
3. State conclusion explicitly
**Common Variations:** Multiple variables, pairwise vs mutual
**Pitfalls:** Assuming independence without checking

## L2.3: Bayes' Theorem & Total Probability

### L3.3.1: Basic Bayesian Updates
**Recognition Keywords:** "Update probability", "given evidence", "posterior"
**Required Concepts:** Bayes' theorem, prior/posterior
**Solution Pattern L4:**
1. Identify hypotheses Hᵢ and evidence E
2. List P(Hᵢ) and P(E|Hᵢ)
3. P(Hᵢ|E) = P(E|Hᵢ)P(Hᵢ)/P(E)
4. Normalize if needed
**Common Variations:** Multiple hypotheses, sequential updates
**Pitfalls:** Wrong likelihood, forgetting normalization

### L3.3.2: Total Probability Applications
**Recognition Keywords:** "Multiple cases", "partition", "different scenarios"
**Required Concepts:** Partitions, law of total probability
**Solution Pattern L4:**
1. Identify partition {Bᵢ}
2. Find P(Bᵢ) and P(A|Bᵢ)
3. P(A) = ΣP(A|Bᵢ)P(Bᵢ)
**Common Variations:** Continuous partitions
**Pitfalls:** Non-exhaustive partition

---

# LEVEL 1: DISCRETE RANDOM VARIABLES

## L2.4: Basic Discrete Distributions

### L3.4.1: PMF/CDF Problems
**Recognition Keywords:** "Probability mass function", "cumulative", "P(X=k)"
**Required Concepts:** PMF properties, CDF definition
**Solution Pattern L4:**
1. Verify Σp(x) = 1
2. F(x) = P(X ≤ x) = Σp(k) for k ≤ x
3. P(a < X ≤ b) = F(b) - F(a)
**Common Variations:** Finding constants, piecewise functions
**Pitfalls:** Wrong summation limits

### L3.4.2: Expectation & Variance (Discrete)
**Recognition Keywords:** "Expected value", "mean", "variance", "E[X]"
**Required Concepts:** Expectation definition, variance formula
**Solution Pattern L4:**
1. E[X] = Σx·P(X=x)
2. E[X²] = Σx²·P(X=x)
3. Var(X) = E[X²] - (E[X])²
**Common Variations:** Functions of X, conditional expectations
**Pitfalls:** Computational errors, forgetting square

## L2.5: Named Discrete Distributions

### L3.5.1: Binomial Problems
**Recognition Keywords:** "n trials", "success probability p", "exactly k successes"
**Required Concepts:** Binomial formula, properties
**Solution Pattern L4:**
1. Verify: fixed n, constant p, independent
2. P(X=k) = C(n,k)p^k(1-p)^(n-k)
3. Use E[X]=np, Var(X)=np(1-p)
4. For large n, consider normal approximation
**Common Variations:** At least/at most, multiple binomials
**Pitfalls:** Not checking conditions

### L3.5.2: Poisson Problems
**Recognition Keywords:** "Rate λ", "rare events", "per unit time"
**Required Concepts:** Poisson PMF, additivity
**Solution Pattern L4:**
1. Identify rate parameter λ
2. P(X=k) = e^(-λ)λ^k/k!
3. For sums: λ_total = Σλᵢ
**Common Variations:** Different time periods, Poisson approximation
**Pitfalls:** Wrong rate conversion

### L3.5.3: Geometric/Negative Binomial
**Recognition Keywords:** "First success", "waiting time", "r-th success"
**Required Concepts:** Geometric/NB formulas, memoryless property
**Solution Pattern L4:**
1. Geometric: P(X=k) = p(1-p)^k
2. Negative Binomial: Use combination formula
3. Apply memoryless property if relevant
**Common Variations:** Starting from 0 vs 1
**Pitfalls:** Wrong parameterization

### L3.5.4: Hypergeometric Problems
**Recognition Keywords:** "Without replacement", "finite population", "sample of size n"
**Required Concepts:** Hypergeometric formula
**Solution Pattern L4:**
1. Identify: population size N, successes K, sample n
2. P(X=k) = [C(K,k)C(N-K,n-k)]/C(N,n)
3. Check feasibility: max(0,n-N+K) ≤ k ≤ min(n,K)
**Common Variations:** Multiple categories
**Pitfalls:** Using binomial instead

---

# LEVEL 1: CONTINUOUS RANDOM VARIABLES

## L2.6: Basic Continuous Concepts

### L3.6.1: PDF/CDF Problems
**Recognition Keywords:** "Density function", "probability density", "continuous"
**Required Concepts:** PDF properties, integration
**Solution Pattern L4:**
1. Verify ∫f(x)dx = 1
2. P(a < X < b) = ∫[a,b]f(x)dx
3. F(x) = ∫[-∞,x]f(t)dt
4. f(x) = F'(x)
**Common Variations:** Finding constants, piecewise PDFs
**Pitfalls:** Wrong integration limits

### L3.6.2: Expectation & Variance (Continuous)
**Recognition Keywords:** "Expected value of continuous", "E[X]", "Var(X)"
**Required Concepts:** Integration, expectation formulas
**Solution Pattern L4:**
1. E[X] = ∫x·f(x)dx
2. E[g(X)] = ∫g(x)·f(x)dx
3. Var(X) = E[X²] - (E[X])²
**Common Variations:** Complex functions, bounds
**Pitfalls:** Improper integrals

## L2.7: Named Continuous Distributions

### L3.7.1: Uniform Distribution
**Recognition Keywords:** "Equally likely over interval", "uniform on [a,b]"
**Required Concepts:** Uniform PDF, linear probabilities
**Solution Pattern L4:**
1. f(x) = 1/(b-a) for x ∈ [a,b]
2. P(c < X < d) = (d-c)/(b-a)
3. E[X] = (a+b)/2, Var(X) = (b-a)²/12
**Common Variations:** Conditional uniform
**Pitfalls:** Wrong bounds

### L3.7.2: Normal Distribution 🔥
**Recognition Keywords:** "Normal", "Gaussian", "N(μ,σ²)", "bell curve"
**Required Concepts:** Normal PDF, standardization
**Solution Pattern L4:**
1. Identify μ, σ²
2. Standardize: Z = (X-μ)/σ
3. Use standard normal table
4. Linear combinations remain normal
**Common Variations:** Sums of normals, truncated normal
**Pitfalls:** Forgetting to standardize

### L3.7.3: Exponential Distribution
**Recognition Keywords:** "Waiting time", "rate λ", "memoryless"
**Required Concepts:** Exponential PDF, memoryless property
**Solution Pattern L4:**
1. f(x) = λe^(-λx), x > 0
2. P(X > t) = e^(-λt)
3. Memoryless: P(X > s+t|X > s) = P(X > t)
4. E[X] = 1/λ
**Common Variations:** Minimum of exponentials
**Pitfalls:** Rate vs scale parameterization

### L3.7.4: Gamma/Beta Distributions
**Recognition Keywords:** "Shape parameter", "Gamma(α,λ)", "Beta(α,β)"
**Required Concepts:** Gamma function, special cases
**Solution Pattern L4:**
1. Identify parameters
2. Use provided formulas
3. Special case: Gamma(1,λ) = Exponential(λ)
4. Beta often for probabilities/proportions
**Common Variations:** Chi-square (special gamma)
**Pitfalls:** Complex integration

---

# LEVEL 1: MULTIVARIATE DISTRIBUTIONS 🔥

## L2.8: Joint Distributions

### L3.8.1: Joint PMF/PDF Problems
**Recognition Keywords:** "Joint distribution", "f(x,y)", "bivariate"
**Required Concepts:** Joint density properties
**Solution Pattern L4:**
1. Verify ∫∫f(x,y)dxdy = 1 (or ΣΣ for discrete)
2. P((X,Y) ∈ A) = ∫∫_A f(x,y)dxdy
3. Find constant c if needed
**Common Variations:** Triangular regions, constraints
**Pitfalls:** Wrong integration order/limits

### L3.8.2: Marginal Distributions
**Recognition Keywords:** "Marginal of X", "distribution of X alone"
**Required Concepts:** Marginal integration/summation
**Solution Pattern L4:**
1. Continuous: f_X(x) = ∫f(x,y)dy
2. Discrete: p_X(x) = Σ_y p(x,y)
3. Check bounds carefully
**Common Variations:** Complex regions
**Pitfalls:** Forgetting to integrate out other variable

### L3.8.3: Conditional Distributions
**Recognition Keywords:** "Distribution of Y given X=x", "conditional PDF"
**Required Concepts:** Conditional density formula
**Solution Pattern L4:**
1. Find marginal f_X(x)
2. f(y|x) = f(x,y)/f_X(x)
3. Verify it integrates to 1
**Common Variations:** Discrete/continuous mix
**Pitfalls:** Zero marginal density

### L3.8.4: Independence in Joint Distributions
**Recognition Keywords:** "Are X and Y independent?"
**Required Concepts:** Independence criterion
**Solution Pattern L4:**
1. Find f(x,y), f_X(x), f_Y(y)
2. Check if f(x,y) = f_X(x)·f_Y(y) for all x,y
3. Alternative: Check if conditional = marginal
**Common Variations:** Pairwise vs mutual independence
**Pitfalls:** Assuming without verifying

## L2.9: Correlation & Dependence

### L3.9.1: Covariance Calculations
**Recognition Keywords:** "Cov(X,Y)", "covariance"
**Required Concepts:** Covariance formula
**Solution Pattern L4:**
1. Find E[X], E[Y], E[XY]
2. Cov(X,Y) = E[XY] - E[X]E[Y]
3. Properties: Cov(aX+b, cY+d) = ac·Cov(X,Y)
**Common Variations:** Multiple variables
**Pitfalls:** Computational errors

### L3.9.2: Correlation Coefficient
**Recognition Keywords:** "Correlation", "ρ", "linear relationship"
**Required Concepts:** Correlation definition
**Solution Pattern L4:**
1. Find Cov(X,Y), σ_X, σ_Y
2. ρ = Cov(X,Y)/(σ_X·σ_Y)
3. Check: -1 ≤ ρ ≤ 1
**Common Variations:** Perfect correlation
**Pitfalls:** Correlation ≠ causation

### L3.9.3: Bivariate Normal 🔥
**Recognition Keywords:** "Jointly normal", "bivariate normal", "correlation ρ"
**Required Concepts:** Bivariate normal properties
**Solution Pattern L4:**
1. Linear combinations are normal
2. Independence ⟺ ρ = 0
3. Conditional is normal: X|Y=y ~ N(...)
4. Use formulas for conditional mean/variance
**Common Variations:** Finding linear combination for independence
**Pitfalls:** Complex formulas

## L2.10: Transformations

### L3.10.1: Order Statistics
**Recognition Keywords:** "Min", "max", "k-th order statistic"
**Required Concepts:** Order statistic formulas
**Solution Pattern L4:**
1. For max: F_max(x) = [F(x)]^n
2. For min: F_min(x) = 1 - [1-F(x)]^n
3. General: Use complex formula with binomial
**Common Variations:** Range, median
**Pitfalls:** Wrong formula application

### L3.10.2: Jacobian Transformations 🔥
**Recognition Keywords:** "Transform (X,Y) to (U,V)", "change of variables"
**Required Concepts:** Jacobian determinant
**Solution Pattern L4:**
1. Define transformation: u=g(x,y), v=h(x,y)
2. Find inverse: x=x(u,v), y=y(u,v)
3. Compute Jacobian: |∂(x,y)/∂(u,v)|
4. f_UV(u,v) = f_XY(x(u,v),y(u,v))·|J|
**Common Variations:** Polar coordinates, sums/products
**Pitfalls:** Forgetting absolute value, wrong bounds

---

# LEVEL 1: MOMENT GENERATING FUNCTIONS 🔥

## L2.11: MGF Properties

### L3.11.1: Finding MGFs
**Recognition Keywords:** "MGF", "moment generating function", "M(t)"
**Required Concepts:** MGF definition
**Solution Pattern L4:**
1. M(t) = E[e^(tX)]
2. Discrete: Σe^(tx)P(X=x)
3. Continuous: ∫e^(tx)f(x)dx
4. Check convergence
**Common Variations:** Known distribution MGFs
**Pitfalls:** Integration difficulties

### L3.11.2: Using MGFs for Moments
**Recognition Keywords:** "Use MGF to find E[X^k]", "moments from MGF"
**Required Concepts:** MGF derivatives
**Solution Pattern L4:**
1. E[X^k] = M^(k)(0)
2. E[X] = M'(0)
3. E[X²] = M''(0)
4. Var(X) = M''(0) - [M'(0)]²
**Common Variations:** Central moments
**Pitfalls:** Differentiation errors

### L3.11.3: MGF Uniqueness & Sums
**Recognition Keywords:** "Distribution of sum", "identify distribution"
**Required Concepts:** MGF uniqueness, independence
**Solution Pattern L4:**
1. For sum of independent: M_sum(t) = ∏M_i(t)
2. Match with known MGF
3. Identify distribution
**Common Variations:** Linear combinations
**Pitfalls:** Forgetting independence requirement

---

# LEVEL 1: LIMIT THEOREMS 🔥

## L2.12: Law of Large Numbers

### L3.12.1: LLN Applications
**Recognition Keywords:** "As n→∞", "converges to", "sample mean"
**Required Concepts:** Weak/Strong LLN
**Solution Pattern L4:**
1. Verify finite mean (weak) or variance (strong)
2. Show X̄_n → μ
3. For weak: P(|X̄_n - μ| > ε) → 0
4. For strong: X̄_n →^{a.s.} μ
**Common Variations:** Rate of convergence
**Pitfalls:** Confusing weak/strong

## L2.13: Central Limit Theorem

### L3.13.1: CLT Applications 🔥
**Recognition Keywords:** "Large n", "approximate", "sum of many"
**Required Concepts:** CLT statement
**Solution Pattern L4:**
1. Check: iid, finite variance, large n
2. Standardize: Z = (X̄ - μ)/(σ/√n)
3. Z ~ N(0,1) approximately
4. Apply continuity correction if discrete
**Common Variations:** Non-identical distributions
**Pitfalls:** Small n, infinite variance

### L3.13.2: Normal Approximations
**Recognition Keywords:** "Approximate using normal", "large sample"
**Required Concepts:** Approximation conditions
**Solution Pattern L4:**
1. Binomial: Check np(1-p) > 10
2. Poisson: Check λ > 30
3. Apply CLT with parameters
4. Continuity correction: ±0.5
**Common Variations:** Other distributions
**Pitfalls:** Poor approximation conditions

### L3.13.3: Confidence Intervals
**Recognition Keywords:** "95% confidence", "margin of error"
**Required Concepts:** CLT, quantiles
**Solution Pattern L4:**
1. Use CLT for X̄
2. Find critical value z_α/2
3. CI: X̄ ± z_α/2·(σ/√n)
4. Interpret correctly
**Common Variations:** Unknown variance (t-distribution)
**Pitfalls:** Wrong interpretation

---

# LEVEL 1: SPECIAL TOPICS & APPLICATIONS 🔥

## L2.14: Conditional Expectation

### L3.14.1: Law of Total Expectation
**Recognition Keywords:** "E[E[X|Y]]", "iterated expectation"
**Required Concepts:** Conditional expectation
**Solution Pattern L4:**
1. Find E[X|Y=y] for each y
2. E[X] = E[E[X|Y]]
3. Discrete: Σ E[X|Y=y]P(Y=y)
4. Continuous: ∫ E[X|Y=y]f_Y(y)dy
**Common Variations:** Multiple conditioning
**Pitfalls:** Wrong order of operations

### L3.14.2: Conditional Variance
**Recognition Keywords:** "Var(X|Y)", "conditional variance"
**Required Concepts:** Law of total variance
**Solution Pattern L4:**
1. Var(X|Y=y) = E[X²|Y=y] - (E[X|Y=y])²
2. Law: Var(X) = E[Var(X|Y)] + Var(E[X|Y])
3. Compute each term
**Common Variations:** Hierarchical models
**Pitfalls:** Complex calculations

## L2.15: Bayesian Statistics

### L3.15.1: Conjugate Priors 🔥
**Recognition Keywords:** "Beta-Binomial", "Gamma-Poisson", "conjugate"
**Required Concepts:** Conjugacy
**Solution Pattern L4:**
1. Identify likelihood and prior family
2. Beta(α,β) + Binomial → Beta(α+x, β+n-x)
3. Gamma(α,β) + Poisson → Gamma(α+Σx, β+n)
4. Update parameters directly
**Common Variations:** Normal-Normal
**Pitfalls:** Wrong parameterization

### L3.15.2: Posterior Computations
**Recognition Keywords:** "Posterior distribution", "Bayesian update"
**Required Concepts:** Bayes theorem for densities
**Solution Pattern L4:**
1. Prior: π(θ)
2. Likelihood: L(x|θ)
3. Posterior: π(θ|x) ∝ L(x|θ)π(θ)
4. Normalize to integrate to 1
**Common Variations:** Multiple observations
**Pitfalls:** Forgetting normalization

## L2.16: Finance Applications

### L3.16.1: Lognormal Models 🔥
**Recognition Keywords:** "Stock price", "S = S₀e^X", "lognormal"
**Required Concepts:** Lognormal distribution
**Solution Pattern L4:**
1. If X ~ N(μ,σ²), then e^X ~ Lognormal
2. E[e^X] = exp(μ + σ²/2)
3. Var[e^X] = exp(2μ+σ²)[exp(σ²)-1]
**Common Variations:** Options, returns
**Pitfalls:** Confusing log vs exponential

### L3.16.2: Portfolio Theory
**Recognition Keywords:** "Portfolio", "diversification", "risk"
**Required Concepts:** Covariance matrix
**Solution Pattern L4:**
1. Return: R_p = Σw_i R_i
2. Variance: σ²_p = w^T Σ w
3. Minimize variance subject to constraints
**Common Variations:** Efficient frontier
**Pitfalls:** Matrix calculations

---

## 🔄 MULTI-STEP PROBLEM FLOWCHARTS

### Flowchart 1: Joint Distribution Complete Analysis
```
START: Given f(x,y)
    ├─ Step 1: Verify valid (∫∫ = 1)
    ├─ Step 2: Find marginals
    ├─ Step 3: Check independence
    ├─ Step 4: Calculate E[X], E[Y]
    ├─ Step 5: Find E[XY]
    ├─ Step 6: Compute Cov(X,Y)
    └─ Step 7: Find correlation ρ
```

### Flowchart 2: CLT Problem Complete Solution
```
START: Large sample problem
    ├─ Step 1: Verify CLT conditions
    ├─ Step 2: Identify μ, σ
    ├─ Step 3: Standardize
    ├─ Step 4: Apply continuity correction
    ├─ Step 5: Use normal table
    └─ Step 6: Interpret result
```

### Flowchart 3: Bayesian Update Process
```
START: Prior + Data
    ├─ Step 1: Identify prior π(θ)
    ├─ Step 2: Write likelihood L(x|θ)
    ├─ Step 3: Check for conjugacy
    ├─ If conjugate:
    │   └─ Update parameters directly
    ├─ If not:
    │   ├─ Compute π(θ|x) ∝ L(x|θ)π(θ)
    │   └─ Normalize
    └─ Step 4: Answer specific question
```

### Flowchart 4: Transformation Problem
```
START: Y = g(X) or (U,V) = g(X,Y)
    ├─ Single variable:
    │   ├─ If monotonic: Use formula
    │   └─ Otherwise: Use CDF method
    └─ Multiple variables:
        ├─ Set up transformation
        ├─ Find inverse
        ├─ Compute Jacobian
        └─ Apply formula
```

---

## 📊 RECOGNITION DECISION TREE

```
START: Read Problem
│
├─ Contains "probability"?
│   ├─ Yes → Check for:
│   │   ├─ "Given that" → Conditional (L3.2.1)
│   │   ├─ "At least" → Complement (L3.1.3)
│   │   └─ Named distribution → Go to Distributions
│   └─ No → Continue
│
├─ Contains "E[" or "expected"?
│   ├─ Yes → Check for:
│   │   ├─ "Given" → Conditional expectation (L3.14.1)
│   │   ├─ Joint variables → Need E[XY] (L3.9.1)
│   │   └─ Single variable → Basic expectation
│   └─ No → Continue
│
├─ Contains "distribution"?
│   ├─ Yes → Check for:
│   │   ├─ Two variables → Joint distribution (L3.8.1)
│   │   ├─ "Transform" → Transformation (L3.10.2)
│   │   └─ Named type → Special distribution
│   └─ No → Continue
│
├─ Contains "large n" or "approximate"?
│   ├─ Yes → CLT/Approximation (L3.13.1)
│   └─ No → Continue
│
└─ Contains "update" or "posterior"?
    └─ Yes → Bayesian (L3.15.1-2)
```

---

## 🎯 SOLUTION TEMPLATES BY LEVEL

### Template for Level 3 Problems

```python
def solve_problem(problem_type, given_data):
    """
    Generic solution template
    """
    # Step 1: Identify problem type from keywords
    keywords = extract_keywords(problem_text)
    category = map_to_category(keywords)
    
    # Step 2: Extract given information
    parameters = parse_parameters(given_data)
    
    # Step 3: Apply appropriate formula/method
    if category == "conditional_probability":
        result = P_A_intersect_B / P_B
    elif category == "CLT":
        z = (x_bar - mu) / (sigma / sqrt(n))
        result = normal_cdf(z)
    # ... more cases
    
    # Step 4: Verify and interpret
    check_validity(result)
    return interpret_in_context(result)
```

---

## 📈 DIFFICULTY PROGRESSION MAP

### Beginner → Intermediate
- L3.1.1 → L3.4.1: Basic counting to PMFs
- L3.2.1 → L3.3.1: Conditional to Bayes
- L3.6.1 → L3.7.2: PDF basics to Normal

### Intermediate → Advanced
- L3.5.1 → L3.13.2: Binomial to approximations
- L3.8.1 → L3.10.2: Joint to transformations
- L3.11.1 → L3.11.3: MGF basics to applications

### Advanced → Expert
- L3.13.1 → L3.15.1: CLT to Bayesian
- L3.10.2 → L3.16.1: Transformations to finance
- All multi-step combinations

---

## 🚨 CRITICAL EXAM PATTERNS

### Most Common on Finals (Based on Practice)
1. **CLT Applications** (appears in every final)
2. **Bivariate Normal** (post-M2 emphasis)
3. **Bayesian Updates** (professor's favorite)
4. **Expectation/Variance** (fundamental)
5. **Transformations** (tests understanding)

### Time-Consuming Problems
1. Jacobian transformations (10-15 min)
2. Multi-part joint distributions (15-20 min)
3. Complete Bayesian analysis (10-15 min)

### Quick Points
1. Basic probability (2-3 min)
2. Standard distributions (3-5 min)
3. Direct formula applications (2-3 min)

---

## 📝 PROFESSOR-SPECIFIC PATTERNS

### Notation Preferences
- Uses ψ(t) for MGF (not M(t))
- Writes Var(X) not σ²_X
- Prefers f(x) for both PMF and PDF

### Favorite Problem Types
1. Finance applications (every homework)
2. Conditional expectation (conceptual)
3. CLT with real data
4. Bayesian with conjugate priors

### Common Tricks
- Independence that isn't obvious
- Continuity correction needed
- Hidden conditioning
- Multi-step reasoning required

---

_End of Question Taxonomy_
