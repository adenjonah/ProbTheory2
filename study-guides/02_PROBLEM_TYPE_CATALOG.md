# Problem Type Catalog - Probability Theory

**Generated:** December 16, 2025
**Purpose:** Comprehensive catalog of all problem types with solution methodologies

---

## 🎯 PROBLEM CATEGORIES

### Category A: Counting & Combinatorics
### Category B: Basic Probability
### Category C: Conditional Probability & Independence
### Category D: Discrete Distributions
### Category E: Continuous Distributions
### Category F: Joint & Multivariate Distributions
### Category G: Expectations & Moments
### Category H: Transformations
### Category I: Limit Theorems & CLT
### Category J: Bayesian Statistics
### Category K: Finance Applications

---

## CATEGORY A: COUNTING & COMBINATORICS

### A1: Arrangements with Repetition
**Recognition:** "How many ways to arrange..."
**Method:**
1. Count total positions
2. Apply multinomial coefficient: n!/(n₁!n₂!...nₖ!)
**Example:** HW1 - Spelling BANANA
**Difficulty:** ⭐⭐

### A2: Sampling With/Without Replacement
**Recognition:** "Draw k items from n..."
**Method:**
- With replacement: n^k
- Without replacement: P(n,k) or C(n,k)
**Example:** HW2 - Balls from urn
**Difficulty:** ⭐⭐

### A3: Card Problems (Poker Hands)
**Recognition:** "Probability of poker hand type..."
**Method:**
1. Count favorable outcomes (combinations)
2. Divide by total possible hands C(52,n)
**Example:** HW1 - 6-card poker hands
**Difficulty:** ⭐⭐⭐

### A4: Birthday Problem Variants
**Recognition:** "Probability that at least two share..."
**Method:**
1. Often easier to compute complement
2. P(at least one match) = 1 - P(all different)
**Example:** HW1 - Birthday problem
**Difficulty:** ⭐⭐⭐

---

## CATEGORY B: BASIC PROBABILITY

### B1: Equally Likely Outcomes
**Recognition:** "Fair dice/coin..."
**Method:** P(A) = |A|/|S|
**Example:** Practice Midterm 1 - Dice rolls
**Difficulty:** ⭐

### B2: Complement Rule
**Recognition:** "At least one..." or "None..."
**Method:** P(A) = 1 - P(Aᶜ)
**Example:** De Méré's problem
**Difficulty:** ⭐⭐

### B3: Union/Intersection Problems
**Recognition:** "Either A or B..." or "Both A and B..."
**Method:**
- P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
- Use Venn diagrams for visualization
**Example:** Lecture examples
**Difficulty:** ⭐⭐

### B4: Non-transitive Dice
**Recognition:** Custom dice with unusual properties
**Method:** Enumerate all pairwise comparisons
**Example:** HW1 - Colored dice
**Difficulty:** ⭐⭐⭐

---

## CATEGORY C: CONDITIONAL PROBABILITY & INDEPENDENCE

### C1: Direct Conditional Probability
**Recognition:** "Given that B occurred, find P(A)..."
**Method:** P(A|B) = P(A ∩ B)/P(B)
**Example:** Russian roulette problem
**Difficulty:** ⭐⭐

### C2: Bayes' Theorem Applications
**Recognition:** "Update probability given evidence..."
**Method:**
1. Identify prior P(H)
2. Find likelihood P(E|H)
3. Apply Bayes: P(H|E) = P(E|H)P(H)/P(E)
**Example:** HW6 - Monty Hall (sober/dizzy)
**Difficulty:** ⭐⭐⭐

### C3: Law of Total Probability
**Recognition:** "Multiple cases/scenarios..."
**Method:**
1. Identify partition {Bᵢ}
2. P(A) = ∑P(A|Bᵢ)P(Bᵢ)
**Example:** HW2 - Machine defects
**Difficulty:** ⭐⭐

### C4: Independence Testing
**Recognition:** "Are X and Y independent?"
**Method:**
- Check if f(x,y) = fₓ(x)·fᵧ(y) for all x,y
- Or verify P(X=x,Y=y) = P(X=x)P(Y=y)
**Example:** HW4 Problem 2
**Difficulty:** ⭐⭐

### C5: Pólya Urn Model
**Recognition:** "Balls added after each draw..."
**Method:** Track probability evolution with multiplication rule
**Example:** HW2 Problem 1
**Difficulty:** ⭐⭐⭐⭐

---

## CATEGORY D: DISCRETE DISTRIBUTIONS

### D1: Binomial Problems
**Recognition:** "n trials, probability p of success..."
**Method:**
1. Identify n, p
2. P(X = k) = C(n,k)p^k(1-p)^(n-k)
3. For large n, consider normal approximation
**Example:** Multiple homework problems
**Difficulty:** ⭐⭐

### D2: Poisson Problems
**Recognition:** "Rate λ per unit time..." or "Rare events..."
**Method:**
1. P(X = k) = e^(-λ)λ^k/k!
2. For sums: λ_total = λ₁ + λ₂ + ...
**Example:** Particle emission problems
**Difficulty:** ⭐⭐

### D3: Geometric/Negative Binomial
**Recognition:** "First success..." or "r-th success..."
**Method:**
- Geometric: P(X = k) = p(1-p)^k
- Negative Binomial: Use formula with combinations
**Example:** Lottery number problem
**Difficulty:** ⭐⭐⭐

### D4: Hypergeometric
**Recognition:** "Sampling without replacement from finite population..."
**Method:** P(X = k) = [C(r,k)C(b,n-k)]/C(r+b,n)
**Example:** Drawing colored balls
**Difficulty:** ⭐⭐⭐

### D5: Multinomial
**Recognition:** "Multiple categories, n trials..."
**Method:** Use multinomial PMF formula
**Example:** Lecture examples
**Difficulty:** ⭐⭐⭐

---

## CATEGORY E: CONTINUOUS DISTRIBUTIONS

### E1: Uniform Distribution
**Recognition:** "Equally likely over interval..."
**Method:**
- PDF: f(x) = 1/(b-a)
- Probabilities are proportional to length
**Example:** Breaking sticks problem
**Difficulty:** ⭐⭐

### E2: Normal Distribution
**Recognition:** "Normal with μ, σ²..." or "Bell curve..."
**Method:**
1. Standardize: Z = (X-μ)/σ
2. Use standard normal table/calculator
**Example:** HW5, HW6 multiple problems
**Difficulty:** ⭐⭐

### E3: Exponential Distribution
**Recognition:** "Waiting time..." or "Memoryless..."
**Method:**
- PDF: f(x) = λe^(-λx)
- P(X > t) = e^(-λt)
**Example:** Practice final - exponential sums
**Difficulty:** ⭐⭐

### E4: Gamma/Beta Distributions
**Recognition:** Complex PDFs with shape parameters
**Method:** Use provided formulas, often need integration
**Example:** HW6 - Beta-Binomial
**Difficulty:** ⭐⭐⭐⭐

### E5: Lognormal Distribution 🔥
**Recognition:** "Stock prices..." or "Y = e^X where X ~ Normal"
**Method:**
- Transform using properties of exponentials
- E[Y] = exp(μ + σ²/2)
**Example:** HW5 Problem 2, Practice Final
**Difficulty:** ⭐⭐⭐

---

## CATEGORY F: JOINT & MULTIVARIATE DISTRIBUTIONS 🔥

### F1: Finding Joint PDF/CDF
**Recognition:** "Joint distribution of X and Y..."
**Method:**
1. Verify ∫∫f(x,y)dxdy = 1
2. For CDF: F(x,y) = ∫∫f(u,v)dudv
**Example:** HW4 Problem 1(a)
**Difficulty:** ⭐⭐⭐

### F2: Marginal Distributions
**Recognition:** "Find marginal of X..." or "Distribution of X alone..."
**Method:**
- Discrete: pₓ(x) = ∑ᵧp(x,y)
- Continuous: fₓ(x) = ∫f(x,y)dy
**Example:** HW4 Problem 1(b)
**Difficulty:** ⭐⭐

### F3: Conditional Distributions
**Recognition:** "Distribution of Y given X = x..."
**Method:** f(y|x) = f(x,y)/fₓ(x)
**Example:** Breaking sticks (professor's review)
**Difficulty:** ⭐⭐⭐

### F4: Covariance & Correlation
**Recognition:** "Find Cov(X,Y) or ρ(X,Y)..."
**Method:**
1. Cov(X,Y) = E[XY] - E[X]E[Y]
2. ρ = Cov(X,Y)/(σₓσᵧ)
**Example:** HW4 Problem 1(d)
**Difficulty:** ⭐⭐⭐

### F5: Bivariate Normal 🔥
**Recognition:** "X and Y jointly normal..." or involves ρ
**Method:**
- Linear combinations are normal
- Independence iff ρ = 0
**Example:** HW5 Problem 1
**Difficulty:** ⭐⭐⭐⭐

### F6: Order Statistics
**Recognition:** "Min/max of random variables..."
**Method:**
- F_min(x) = 1 - [1-F(x)]^n
- F_max(x) = [F(x)]^n
**Example:** HW4 Problem 3
**Difficulty:** ⭐⭐⭐⭐

---

## CATEGORY G: EXPECTATIONS & MOMENTS

### G1: Basic Expectation
**Recognition:** "Find E[X]..."
**Method:**
- Discrete: E[X] = ∑x·P(X=x)
- Continuous: E[X] = ∫x·f(x)dx
**Example:** HW3 multiple problems
**Difficulty:** ⭐⭐

### G2: Expectation of Functions
**Recognition:** "Find E[g(X)]..."
**Method:**
- Don't find distribution of g(X)
- Use E[g(X)] = ∫g(x)f(x)dx directly
**Example:** HW3 Problem 1(g)
**Difficulty:** ⭐⭐⭐

### G3: Conditional Expectation 🔥
**Recognition:** "E[X|Y]..." or "Law of total expectation..."
**Method:**
1. Find E[X|Y=y] for each y
2. E[X] = E[E[X|Y]]
**Example:** Stick breaking (professor's review)
**Difficulty:** ⭐⭐⭐⭐

### G4: Moment Generating Functions 🔥
**Recognition:** "Find MGF..." or "Use MGF to find..."
**Method:**
1. M(t) = E[e^(tX)]
2. E[X^k] = M^(k)(0)
3. For sums: M_sum = ∏M_i (if independent)
**Example:** HW3, various problems
**Difficulty:** ⭐⭐⭐⭐

### G5: Variance Calculations
**Recognition:** "Find Var(X)..."
**Method:**
- Var(X) = E[X²] - (E[X])²
- For sums: Var(∑Xᵢ) = ∑Var(Xᵢ) + 2∑Cov(Xᵢ,Xⱼ)
**Example:** HW3 Problem 1(h)
**Difficulty:** ⭐⭐⭐

---

## CATEGORY H: TRANSFORMATIONS

### H1: Single Variable Transformations
**Recognition:** "Y = g(X), find distribution of Y..."
**Method:**
- CDF method: Find F_Y, differentiate
- PDF method: f_Y(y) = f_X(g⁻¹(y))|dg⁻¹/dy|
**Example:** Y = 1/X transformations
**Difficulty:** ⭐⭐⭐

### H2: Jacobian Transformations 🔥
**Recognition:** "Transform (X,Y) to (U,V)..."
**Method:**
1. Find Jacobian |∂(x,y)/∂(u,v)|
2. f_UV(u,v) = f_XY(x(u,v), y(u,v))|J|
**Example:** HW4 Problem 4
**Difficulty:** ⭐⭐⭐⭐⭐

### H3: Sums of Random Variables
**Recognition:** "Distribution of X + Y..."
**Method:**
- Convolution for independent variables
- Or use MGFs: M_sum = M_X · M_Y
**Example:** Sum of exponentials
**Difficulty:** ⭐⭐⭐⭐

### H4: Probability Integral Transform
**Recognition:** "Generate random variables..." or "U = F(X)..."
**Method:** F(X) ~ Uniform(0,1)
**Example:** Lecture Chapter 3
**Difficulty:** ⭐⭐⭐

---

## CATEGORY I: LIMIT THEOREMS & CLT 🔥

### I1: Central Limit Theorem Applications
**Recognition:** "Large n..." or "Approximate using normal..."
**Method:**
1. Check conditions (n large, finite variance)
2. Standardize: Z = (X̄ - μ)/(σ/√n)
3. Apply continuity correction if discrete
**Example:** HW5, HW6 - 400 games problem
**Difficulty:** ⭐⭐⭐⭐

### I2: Normal Approximation to Binomial
**Recognition:** "Large n, binomial..."
**Method:**
1. Check np(1-p) > 10
2. X ~ N(np, np(1-p))
3. Continuity correction: P(X = k) ≈ P(k-0.5 < Y < k+0.5)
**Example:** HW6 CLT problems
**Difficulty:** ⭐⭐⭐

### I3: Law of Large Numbers
**Recognition:** "As n → ∞..." or "Convergence of average..."
**Method:**
- Show E[X̄] = μ
- Show Var(X̄) = σ²/n → 0
**Example:** Conceptual problems
**Difficulty:** ⭐⭐⭐

### I4: Confidence Intervals
**Recognition:** "95% confidence..." or "Margin of error..."
**Method:**
1. Use CLT for X̄
2. CI: X̄ ± z_(α/2) · σ/√n
**Example:** HW6 applications
**Difficulty:** ⭐⭐⭐

### I5: Quantile Problems
**Recognition:** "Find x such that P(X < x) = p..."
**Method:**
1. Standardize if normal
2. Use inverse normal function
**Example:** Practice Final Problem 1(c)
**Difficulty:** ⭐⭐⭐

---

## CATEGORY J: BAYESIAN STATISTICS 🔥

### J1: Basic Bayesian Updating
**Recognition:** "Update belief..." or "Posterior distribution..."
**Method:**
1. Prior: π(θ)
2. Likelihood: L(x|θ)
3. Posterior: π(θ|x) ∝ L(x|θ)π(θ)
**Example:** HW6 - Monty Hall
**Difficulty:** ⭐⭐⭐⭐

### J2: Conjugate Priors
**Recognition:** "Beta-Binomial..." or "Gamma-Poisson..."
**Method:**
- Beta prior + Binomial → Beta posterior
- Update parameters directly
**Example:** HW6 Problem 2
**Difficulty:** ⭐⭐⭐⭐

### J3: Posterior Expectations
**Recognition:** "Expected value given data..."
**Method:** E[θ|data] = ∫θ · π(θ|data)dθ
**Example:** HW6 Bayesian problems
**Difficulty:** ⭐⭐⭐⭐⭐

### J4: Predictive Distributions
**Recognition:** "Probability of next observation..."
**Method:** P(X_(n+1)|X₁,...,Xₙ) = ∫P(X_(n+1)|θ)π(θ|data)dθ
**Example:** Advanced Bayesian problems
**Difficulty:** ⭐⭐⭐⭐⭐

---

## CATEGORY K: FINANCE APPLICATIONS 🔥

### K1: Stock Price Models
**Recognition:** "Stock price S..." or "Lognormal..."
**Method:**
- S = S₀e^X where X ~ N(μ,σ²)
- E[S] = S₀exp(μ + σ²/2)
**Example:** Practice Final Problem 4
**Difficulty:** ⭐⭐⭐⭐

### K2: Portfolio Problems
**Recognition:** "Multiple stocks..." or "Diversification..."
**Method:**
- Use covariance matrix
- Portfolio variance formula
**Example:** HW5 Problem 6
**Difficulty:** ⭐⭐⭐⭐

### K3: Option Pricing Basics
**Recognition:** "Call option..." or "Put option..."
**Method:** Apply Black-Scholes concepts
**Example:** Professor's finance examples
**Difficulty:** ⭐⭐⭐⭐⭐

### K4: Risk Measures
**Recognition:** "VaR..." or "Expected shortfall..."
**Method:** Use quantiles and conditional expectations
**Example:** Advanced finance problems
**Difficulty:** ⭐⭐⭐⭐⭐

---

## 📊 SOLUTION METHODOLOGY PATTERNS

### Pattern 1: "Find Probability" Problems
1. Identify distribution type
2. Set up appropriate formula
3. Calculate using tables/software
4. Check answer makes sense (0 ≤ P ≤ 1)

### Pattern 2: "Find Distribution" Problems
1. Start with definition/transformation
2. Use CDF method or PDF method
3. Verify it's valid distribution (integrates to 1)
4. Find parameters if needed

### Pattern 3: "Independence Test" Problems
1. Find joint distribution
2. Find marginals
3. Check if product equals joint
4. State conclusion clearly

### Pattern 4: "Expectation/Variance" Problems
1. Identify what needs computing
2. Use linearity when possible
3. For complex functions, integrate directly
4. Use shortcuts (MGF, known formulas)

### Pattern 5: "Approximation" Problems
1. Check conditions for approximation
2. Identify parameters
3. Apply continuity correction if needed
4. Calculate using normal distribution

### Pattern 6: "Bayesian Update" Problems
1. Identify prior, likelihood, data
2. Apply Bayes' theorem or conjugacy
3. Normalize to get posterior
4. Answer specific question asked

---

## 🎯 COMMON PITFALLS BY CATEGORY

### Counting & Combinatorics
- ❌ Confusing permutations and combinations
- ❌ Double-counting outcomes
- ❌ Wrong formula for with/without replacement

### Probability Basics
- ❌ Forgetting to normalize
- ❌ Misapplying independence
- ❌ Wrong complement calculation

### Continuous Distributions
- ❌ Forgetting Jacobian in transformations
- ❌ Not checking bounds of integration
- ❌ Confusing PDF and CDF

### Joint Distributions
- ❌ Wrong limits for marginals
- ❌ Assuming independence without checking
- ❌ Incorrect covariance formula

### CLT & Approximations
- ❌ Forgetting continuity correction
- ❌ Not checking CLT conditions
- ❌ Using wrong variance formula

### Bayesian Statistics
- ❌ Not normalizing posterior
- ❌ Wrong conjugate prior match
- ❌ Confusing prior and posterior

---

## 📈 DIFFICULTY PROGRESSION

### Beginner (⭐)
- Basic probability calculations
- Simple counting
- Standard distributions

### Intermediate (⭐⭐-⭐⭐⭐)
- Conditional probability
- Joint distributions
- Expectation calculations
- Basic transformations

### Advanced (⭐⭐⭐⭐-⭐⭐⭐⭐⭐)
- CLT applications
- Bayesian inference
- Complex transformations
- Multi-step problems
- Finance applications

---

## 📚 CROSS-REFERENCE TO HOMEWORK

### HW1 (Pre-M1)
- Card problems (A3)
- Non-transitive dice (B4)
- Birthday problem (A4)

### HW2 (Pre-M1)
- Pólya urn (C5)
- Craps game (C3)
- Machine defects (C3)

### HW3 (Between)
- Joint PMF (F1)
- Expectations (G1-G2)
- MGF (G4)

### HW4 (Between)
- Joint continuous (F1-F4)
- Order statistics (F6)
- Transformations (H1-H2)

### HW5 (Post-M2) 🔥
- Bivariate normal (F5)
- Lognormal (E5)
- CLT (I1-I2)

### HW6 (Post-M2) 🔥
- Bayesian (J1-J3)
- CLT applications (I1)
- Confidence intervals (I4)

---

_End of Problem Type Catalog_
