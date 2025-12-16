# Problem Solution Paths

**Generated:** December 16, 2025
**Purpose:** Map each problem to primary solution paths using FINAL_EXAM_CHEATSHEET.tex sections

---

# SECTION REFERENCE GUIDE

| Section | Topic | Key Concepts |
|---------|-------|--------------|
| 1.1 | Probability Axioms | P(A ∪ B), sample space |
| 1.2 | Conditional Probability | P(A\|B), multiplication rule |
| 1.3 | Bayes' Theorem | Posterior, likelihood, prior |
| 1.4 | Independence | P(A ∩ B) = P(A)P(B) |
| 1.5 | Counting Methods | Permutations, combinations |
| 2.1 | PMF and CDF | Discrete distributions |
| 2.2 | Binomial | n trials, success probability p |
| 2.3 | Poisson | Rate λ, counting process |
| 2.4 | Geometric | First success, memoryless |
| 2.5 | Negative Binomial | r-th success |
| 2.6 | Hypergeometric | Without replacement |
| 3.1 | PDF and CDF | Continuous distributions |
| 3.2 | Uniform | Equally likely |
| 3.3 | Normal/Gaussian | Bell curve, standardization |
| 3.4 | Exponential | Memoryless, waiting time |
| 3.5 | Gamma | Sum of exponentials |
| 3.6 | Beta | Conjugate prior |
| 4.1 | Joint Distributions | f(x,y), normalization |
| 4.2 | Marginal/Conditional | f_X(x), f(y\|x) |
| 4.3 | Independence (RVs) | f(x,y) = f_X(x)f_Y(y) |
| 4.4 | Covariance/Correlation | Cov, ρ |
| 4.5 | Bivariate Normal | MVN, Gaussian vector |
| 4.6 | Transformations | Jacobian, CDF method |
| 4.7 | Order Statistics | Max, min |
| 5.1 | MGF Definition | M(t) = E[e^tX] |
| 5.2 | MGF for Sums | Product property |
| 6.1 | CLT | Normal approximation |
| 6.2 | Normal Approximations | Continuity correction |
| 6.3 | Law of Large Numbers | Convergence |
| 6.4 | Confidence Intervals | z-intervals |
| 7.1 | Conditional Expectation | E[X\|Y], total expectation |
| 7.2 | Bayesian Statistics | Prior, posterior, conjugate |
| 7.3 | Lognormal | Stock prices, E[e^X] |
| 7.4 | Additional Concepts | Indicators, Jensen's |
| 8.x | Practice Problems | Worked examples |
| Template A-P | Multi-step | Problem patterns |

---

# HOMEWORK 1 SOLUTION PATHS

## HW1-Q1: Six-Card Poker Hands

**Problem Type:** Counting/Combinatorics

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 1.5 (Counting Methods)
- **Primary Formula:** $C(n,k) = \binom{n}{k} = \frac{n!}{k!(n-k)!}$
- **Supporting Section:** Section 1.1 (Probability Axioms)

**Decision Tree Path:**
START → Counting problem → Multiple categories → Use combinations → Section 1.5

**Solution Steps:**
1. Calculate total number of 6-card hands: C(52,6)
2. Count two-pair hands: Choose 2 ranks for pairs × choose 2 cards each × choose 2 different ranks × choose 1 card each
3. Count three-of-a-kind hands: Choose rank × choose 3 cards × choose 3 other ranks × choose 1 card each
4. Divide each by total

**Key Recognition Criteria:**
- "How many ways" or "probability of hand type"
- Multiple selection categories
- Card/poker context

---

## HW1-Q2: Irregular (Non-Transitive) Dice

**Problem Type:** Discrete Probability

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 2.1 (PMF and CDF)
- **Supporting Section:** Section 1.1 (Probability Axioms)

**Decision Tree Path:**
START → Discrete outcomes → Compare outcomes → Enumerate cases → Section 2.1

**Solution Steps:**
1. List all 36 pairs (die1, die2)
2. Count favorable outcomes for each comparison
3. For part (b): enumerate sum distributions and compare

**Key Recognition Criteria:**
- Non-standard dice faces
- Pairwise comparisons
- "Beats" relationship

---

## HW1-Q3: Birthday Problem

**Problem Type:** Counting with Complement

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 1.5 (Counting Methods)
- **Primary Formula:** P(B) = 1 - P(no shared birthdays) = 1 - $\frac{365!/(365-n)!}{365^n}$
- **Supporting Section:** Section 1.1 (Complement Rule)

**Decision Tree Path:**
START → "At least one" → Use complement → Counting → Section 1.5

**Solution Steps:**
1. Define sample space: all n-tuples of birthdays
2. Use complement: P(shared) = 1 - P(all different)
3. P(all different) = 365/365 × 364/365 × ... × (365-n+1)/365

**Key Recognition Criteria:**
- "At least one" → complement
- Birthday/collision problem
- Simulation mentioned

---

## HW1-Q4: Dice Difference

**Problem Type:** Discrete Probability

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 2.1 (PMF and CDF)
- **Primary Formula:** Enumerate and count

**Decision Tree Path:**
START → Two dice → Difference condition → Enumerate → Section 2.1

**Solution Steps:**
1. List all 36 outcomes
2. Identify pairs where |X - Y| < 3
3. Count favorable outcomes: 26/36

**Key Recognition Criteria:**
- Difference of dice
- Simple enumeration

---

## HW1-Q5: School Grades

**Problem Type:** Weighted Probability

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 1.1 (Probability Axioms)
- **Primary Formula:** P(odd) = P(grade 1) + P(grade 3) + P(grade 5)

**Solution Steps:**
1. Let each of grades 2-6 have k students, grade 1 has 2k
2. Total = 7k students
3. P(odd) = (2k + k + k)/7k = 4/7

---

## HW1-Q6: Three Coins

**Problem Type:** Simple Counting

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 1.5 (Counting Methods)
- **Primary Formula:** P = favorable/total = 2/8 = 1/4

**Solution Steps:**
1. Total outcomes: 2³ = 8
2. Favorable: HHH or TTT = 2
3. P = 2/8 = 1/4

---

## HW1-Q7: Elevator Problem

**Problem Type:** Counting without Replacement

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 1.5 (Counting Methods)
- **Primary Formula:** P(n,k)/n^k for ordered vs unordered

**Solution Steps:**
1. Total ways: 7⁵ (each of 5 people chooses from 7 floors)
2. Favorable: P(7,5) = 7!/2! (no repeats)
3. P = 7!/(2! × 7⁵)

**Key Recognition Criteria:**
- "No two same" → without replacement
- Independence between choices

---

## HW1-Q8: Ball Drawing

**Problem Type:** Symmetry/Exchangeability

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 1.1 (Probability Axioms)
- **Key Insight:** Symmetry - every ball equally likely in any position

**Solution Steps:**
1. All parts: P = r/100
2. By symmetry, position doesn't matter
3. Each ball equally likely to be first, 50th, or last

**Key Recognition Criteria:**
- Without replacement but asking about specific positions
- Symmetry argument

---

# HOMEWORK 2 SOLUTION PATHS

## HW2-Q1: Polya Urn Model

**Problem Type:** Sequential Conditional Probability

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 1.2 (Conditional Probability)
- **Primary Formula:** Chain rule: P(A₁∩A₂∩A₃∩A₄) = P(A₁)P(A₂|A₁)P(A₃|A₁∩A₂)P(A₄|A₁∩A₂∩A₃)

**Solution Steps:**
1. P(R₁) = r/(r+b)
2. P(R₂|R₁) = (r+k)/(r+b+k)
3. P(R₃|R₁R₂) = (r+2k)/(r+b+2k)
4. P(B₄|R₁R₂R₃) = b/(r+b+3k)
5. Multiply all

**Key Recognition Criteria:**
- Reinforcement/urn model
- Sequential draws with changing composition

---

## HW2-Q2: Craps Game

**Problem Type:** Conditional Probability with Geometric

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 1.2 (Conditional Probability)
- **Supporting Section:** Section 2.4 (Geometric Distribution)
- **Primary Formula:** Total probability over first roll outcomes

**Solution Steps:**
1. P(win|first roll = k) for each k
2. For k ∈ {4,5,6,8,9,10}: P(win|point=k) = P(k before 7 or 11)
3. Use geometric series for repeated rolls
4. Sum over all cases with weights

**Key Recognition Criteria:**
- Multi-stage game
- "Until" condition → geometric

---

## HW2-Q3: Machine Defects (Bayes)

**Problem Type:** Law of Total Probability

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 1.3 (Bayes' Theorem) - but just uses total probability
- **Primary Formula:** P(D) = Σ P(D|State_i)P(State_i)

**Decision Tree Path:**
START → Multiple sources → Total probability → Section 1.3

**Solution Steps:**
1. P(defective) = 0.02(0.8) + 0.1(0.1) + 0.3(0.1) = 0.056

---

## HW2-Q4: Particle Penetration (Binomial)

**Problem Type:** Binomial Distribution

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 2.2 (Binomial Distribution)
- **Primary Formula:** P(X=k) = C(n,k)p^k(1-p)^(n-k)

**Decision Tree Path:**
START → Named distribution → "n trials, success p" → Binomial → Section 2.2

**Solution Steps:**
1. X ~ Binomial(10, 0.01)
2. P(X=1) = C(10,1)(0.01)¹(0.99)⁹

**Key Recognition Criteria:**
- Fixed n trials
- Independent
- Constant p
- Count successes

---

## HW2-Q5: World Series

**Problem Type:** Negative Binomial

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 2.5 (Negative Binomial)
- **Primary Formula:** Sum over scenarios where A wins 4th required game

**Solution Steps:**
1. A must win exactly 4 games
2. Can happen in 4, 5, 6, or 7 games
3. P(A wins in exactly k games) = C(k-1,3)(1/3)⁴(2/3)^(k-4)
4. Sum for k = 4,5,6,7

**Key Recognition Criteria:**
- "First to r wins"
- Negative binomial setup

---

## HW2-Q6: Two Boys Throwing

**Problem Type:** Geometric with Alternation

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 2.4 (Geometric Distribution)
- **Primary Formula:** Product of miss probabilities

**Solution Steps:**
1. A's 3rd throw is the 5th throw overall
2. Need: A miss, B miss, A miss, B miss, A hit
3. P = (2/3)(3/4)(2/3)(3/4)(1/3)

**Key Recognition Criteria:**
- Alternating trials
- "First success on specific trial"

---

## HW2-Q7: Five Coins (Bayes)

**Problem Type:** Bayesian Inference

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 7.2 (Bayesian Statistics)
- **Primary Formula:** P(coin_i|H) = P(H|coin_i)P(coin_i)/Σ_j P(H|coin_j)P(coin_j)
- **Supporting Section:** Section 1.3 (Bayes' Theorem)

**Decision Tree Path:**
START → "Posterior" or "given evidence" → Bayes → Section 7.2

**Solution Steps:**
1. Prior: P(coin_i) = 1/5 for all i
2. Likelihood: P(H|coin_i) = p_i
3. Apply Bayes formula
4. For (b): use posterior as new weights

**Key Recognition Criteria:**
- "Posterior probability"
- Multiple hypotheses
- Update after observation

---

## HW2-Q8: Binary Paradox

**Problem Type:** Conditional Probability (Sample Space)

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 1.2 (Conditional Probability)
- **Key Insight:** Different conditioning events have different sample spaces

**Solution Steps:**
(a) Given older is female: {(F,M), (F,F)} → P(FF) = 1/2
(b) Given at least one male: {(M,M), (M,F), (F,M)} → P(MM) = 1/3

**Key Recognition Criteria:**
- "Given" with different phrasings
- Sample space matters

---

## HW2-Q9: Blue Taxi (Bayes)

**Problem Type:** Bayesian Reasoning (Base Rate Fallacy)

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 7.2 (Bayesian Statistics)
- **Primary Formula:** P(blue|says blue) = P(says blue|blue)P(blue)/P(says blue)

**Decision Tree Path:**
START → "Given witness says" → Bayes with false positive → Section 7.2

**Solution Steps:**
1. Prior: P(blue) = 1/100
2. Likelihood: P(says blue|blue) = 0.99, P(says blue|green) = 0.02
3. P(says blue) = 0.99(1/100) + 0.02(99/100) = 0.0297
4. P(blue|says blue) = 0.99/100 / 0.0297 ≈ 0.33

**Key Recognition Criteria:**
- Base rate vs. test accuracy
- False positive rate
- Legal/medical context

---

## HW2-Q10: Four Dice (Bayes)

**Problem Type:** Bayesian Inference

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 7.2 (Bayesian Statistics)
- **Supporting Section:** Section 1.3 (Bayes' Theorem)

**Decision Tree Path:**
START → "Prior" and "posterior" → Dice selection → Bayes → Section 7.2

**Solution Steps:**
1. Prior: P(D4)=1/4, P(D6)=1/4, P(D8)=2/4
2. Likelihood: P(R=3|die) = 1/(sides) if 3 ≤ sides, else 0
3. Apply Bayes formula

---

## HW2-Q11: Coin Flip Runs (Simulation)

**Problem Type:** Simulation/Monte Carlo

**PRIMARY SOLUTION PATH:**
- **Main Section:** Not in cheatsheet (simulation problem)
- **Key Concept:** Law of Large Numbers for estimation

**Solution Steps:**
1. Simulate many trials
2. Record longest run each trial
3. Average for estimation
4. Proportion exceeding 8 for probability

---

# HOMEWORK 3 SOLUTION PATHS

## HW3-Q1: Joint PMF

**Problem Type:** Joint Distribution Analysis

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 4.1 (Joint Distributions)
- **Supporting Sections:** Section 4.2 (Marginals), Section 4.4 (Covariance)
- **Primary Formulas:** 
  - Normalization: Σ p(x,y) = 1
  - Marginal: p_X(x) = Σ_y p(x,y)
  - Cov(X,Y) = E[XY] - E[X]E[Y]

**Decision Tree Path:**
START → Joint PMF given → Find c, marginals, moments → Section 4.1

**Solution Steps:**
1. Sum all p(x,y) values, set = 1, solve for c
2. Marginals by summing rows/columns
3. Expectations by weighted sums
4. Variance formula

**Key Recognition Criteria:**
- Joint PMF with constant c
- Multiple sub-parts asking for various quantities

---

## HW3-Q2: Three-Sided Die

**Problem Type:** Multinomial/Conditional

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 2.2 (Binomial) generalized
- **Supporting Section:** Section 1.2 (Conditional Probability)

**Solution Steps:**
(a) Binomial for count of 3's: C(6,3)(1/4)³(3/4)³
(b) Conditional: given total count, find position probability
(c) Given exact composition, count arrangements
(d) Conditional PMF with restricted support

---

## HW3-Q3: Geometric Distribution Property

**Problem Type:** Proof (Uniform Conditional)

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 2.4 (Geometric Distribution)
- **Key Insight:** Sum of geometrics, conditional on sum

**Solution Steps:**
1. P(X=i, X+Y=n) = P(X=i)P(Y=n-i)
2. P(X+Y=n) = Σ P(X=i)P(Y=n-i)
3. Ratio gives uniform 1/(n-1)

---

## HW3-Q4: Biased Coin Tosses

**Problem Type:** Independence/Binomial

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 2.2 (Binomial Distribution)
- **Supporting Section:** Section 1.4 (Independence)

**Solution Steps:**
(a) Show P(A∩B) = P(A)P(B) by calculation
(b) Product of binomial probabilities for non-overlapping parts
(c) Negative binomial concept
(d) Overlapping events - careful counting

---

## HW3-Q5: Reward for Patterns

**Problem Type:** Indicator Variables

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 7.4 (Indicator Variables)
- **Primary Formula:** R = Σ I_i where I_i = 1 if pattern HT at position i

**Solution Steps:**
1. Define I_i = I(position i is H, position i+1 is T)
2. E[I_i] = p(1-p)
3. E[R] = (n-1)p(1-p)
4. Var(R) = Σ Var(I_i) + 2Σ Cov(I_i, I_j)

**Key Recognition Criteria:**
- Counting patterns
- Use indicator random variables
- Adjacent positions have covariance

---

## HW3-Q6: Exponential Time to Failure

**Problem Type:** Exponential Distribution

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 3.4 (Exponential Distribution)
- **Primary Formulas:**
  - P(X > x) = e^(-λx)
  - E[X] = 1/λ, Var(X) = 1/λ²
  - min of exponentials is exponential

**Decision Tree Path:**
START → "Exponential" or "waiting time" → Section 3.4

**Solution Steps:**
(a) P(X ≥ x) = e^(-λx)
(b) E[X] = 1/λ, SD = 1/λ
(c) P(T > t) = P(X₁ > t)P(X₂ > t) = e^(-2λt) → T ~ Exp(2λ)
(d) Sum rates: λ_total = 2 + 3 + 5 = 10, E[T] = 1/10

**Key Recognition Criteria:**
- Exponential distribution
- Minimum of exponentials
- Sum of rates property

---

## HW3-Q7: Change of Scale (Transformations)

**Problem Type:** Transformation of Random Variables

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 4.6 (Transformations)
- **Primary Formula:** f_Y(y) = f_X(g^(-1)(y))|dg^(-1)/dy|

**Decision Tree Path:**
START → "Find distribution of Y=g(X)" → Transformation → Section 4.6

**Solution Steps:**
(a) Y = 3X: f_Y(y) = (1/3)e^(-y/3) for y > 0
(b) W = aX + b: f_W(w) = (1/a)e^(-(w-b)/a) for w > b
(c) V = X³: use CDF method or Jacobian

---

## HW3-Q8: Transformations and Moments

**Problem Type:** Expectations of Transformed Variables

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 4.6 (Transformations)
- **Supporting Section:** Section 3.4 (Exponential moments)

**Solution Steps:**
(a) E[aX+b] = aE[X]+b, Var(aX+b) = a²Var(X)
(b) E[X³] = ∫ x³ e^(-x) dx = 6 (gamma integral)
(c) Median: F(m) = 0.5 → m = ln(2) for Exp(1)

---

# HOMEWORK 4 SOLUTION PATHS

## HW4-Q1: Joint PDF Analysis

**Problem Type:** Joint Continuous Distribution

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 4.1 (Joint Distributions)
- **Supporting Sections:** Section 4.2, Section 4.4
- **Template:** Section 8.4 in cheatsheet

**Decision Tree Path:**
START → Joint PDF f(x,y) → Find c, marginals, covariance → Section 4.1

**Solution Steps:**
1. ∬f(x,y)dxdy = 1 → c = 12/7
2. Marginals by integration
3. E[X], E[Y], E[XY], E[X²], E[Y²]
4. Cov = E[XY] - E[X]E[Y]
5. Independence: check if f(x,y) = f_X(x)f_Y(y)

**Key Recognition Criteria:**
- Joint PDF with unknown constant
- Rectangular support
- Cross-term xy → likely not independent

---

## HW4-Q2: Independence from Joint PMF

**Problem Type:** Independence Check (Discrete)

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 4.3 (Independence of RVs)
- **Primary Formula:** Independent iff p(x,y) = p_X(x)·p_Y(y) for ALL (x,y)

**Solution Steps:**
1. Compute marginals p_X(x) and p_Y(y)
2. Check if p(x,y) = p_X(x)p_Y(y) for all entries
3. If any fails → NOT independent

---

## HW4-Q3: Correlation Analysis

**Problem Type:** Covariance/Correlation

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 4.4 (Covariance and Correlation)
- **Primary Formulas:**
  - Cov(X,Y) = E[XY] - E[X]E[Y]
  - ρ = Cov(X,Y)/(σ_X σ_Y)

**Solution Steps:**
1. Joint distribution as function of c
2. E[X] = 0, E[Y] = 0 (symmetric about 0)
3. E[XY] = depends on c
4. Independence: c = 1/4
5. Perfect correlation: c = 0 or c = 1/2

---

## HW4-Q4: Meeting Problem (Don't Be Late!)

**Problem Type:** Geometric Probability (Two Uniforms)

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 4.1 (Joint Distributions)
- **Supporting Section:** Section 3.2 (Uniform)
- **Template:** Template U17 (Meeting Problem)

**Decision Tree Path:**
START → Two uniforms, geometric condition → Draw square → Section 4.1

**Solution Steps:**
(a) f(a,b) = 1/3600 on [0,60]²
(b) P(A < 30) = 1/2
(c) Rectangle area / total area
(d) P(A < B + 5): shade region, compute area
(e) P(|A-B| < 15): band around diagonal, area = 1 - (45)²/3600

**Key Recognition Criteria:**
- Two uniform arrival times
- |A - B| < constant → geometric probability
- Draw the square!

---

## HW4-Q5: Overlapping Sums

**Problem Type:** Covariance of Sums

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 4.4 (Covariance)
- **Primary Formula:** Cov(ΣX_i, ΣX_j) = Σ Cov(X_i, X_j) for overlapping indices

**Solution Steps:**
1. X = X_1 + ... + X_n
2. Y = X_{n-7} + ... + X_{2n-8}
3. Overlap: X_{n-7}, ..., X_n (8 variables)
4. Cov(X,Y) = Σ Var(X_i) for overlapping indices = 8·(1/4)
5. Var(X) = n/4, Var(Y) = n/4
6. ρ = Cov/(SD_X·SD_Y)

---

# HOMEWORK 5 SOLUTION PATHS

## HW5-Q1: Bivariate Normal

**Problem Type:** Bivariate Normal Distribution

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 4.5 (Bivariate Normal)
- **Supporting Section:** Section 3.3 (Normal)
- **Template:** Template A, Template F, Template G

**Decision Tree Path:**
START → "Jointly normal" or "bivariate normal" → Section 4.5

**Solution Steps:**
(a) X+Y is normal. Find E[X+Y], Var(X+Y) with correlation term
(b) Set Cov(aX+Y, X+2Y) = 0, solve for a
(c) Conditional on linear constraint → use BVN conditional formula

**Key Recognition Criteria:**
- "Jointly normal" = bivariate normal
- Linear combinations are normal
- Independence ↔ ρ = 0 (for MVN only!)

---

## HW5-Q2: Lognormal Distribution

**Problem Type:** Lognormal

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 7.3 (Lognormal Distribution)
- **Primary Formula:** P(X ≤ x) = Φ((ln(x) - μ)/σ)

**Decision Tree Path:**
START → "Lognormal" → Section 7.3

**Solution Steps:**
1. X lognormal(3, 1.44) means ln(X) ~ N(3, 1.44)
2. P(X ≤ 6.05) = P(ln(X) ≤ ln(6.05)) = Φ((ln(6.05)-3)/1.2)

---

## HW5-Q3: Product of Lognormal Variables

**Problem Type:** Product of Lognormals

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 7.3 (Lognormal)
- **Template:** Template I (Product of Lognormals)
- **Primary Formula:** XY is lognormal if X, Y are independent lognormals

**Solution Steps:**
1. ln(X) ~ N(1.6, 4.5), ln(Y) ~ N(3, 6)
2. ln(XY) = ln(X) + ln(Y) ~ N(4.6, 10.5)
3. E[XY] = e^(4.6 + 10.5/2) = e^9.85
4. P(XY > 10): standardize ln(XY)

---

## HW5-Q4: Conditional Probability in Bivariate Normal

**Problem Type:** BVN Conditional Distribution

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 4.5 (Bivariate Normal)
- **Template:** Template F (Bivariate Normal Conditional)
- **Primary Formula:** Y|X=x ~ N(μ_Y + ρ(σ_Y/σ_X)(x-μ_X), (1-ρ²)σ_Y²)

**Solution Steps:**
1. B|A=80 ~ N(μ_B|A, σ²_B|A)
2. μ_B|A = 90 + 0.8(16/10)(80-85) = 90 - 6.4 = 83.6
3. σ²_B|A = (1-0.64)×256 = 92.16
4. P(B > 90 | A=80) = 1 - Φ((90-83.6)/9.6)

---

## HW5-Q5: Bivariate Normal Parameters

**Problem Type:** BVN Parameter Recovery

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 4.5 (Bivariate Normal)
- **Template:** Template N

**Key Formulas:**
- E[X₁|X₂] = μ₁ + ρ(σ₁/σ₂)(X₂-μ₂)
- Var(X₂|X₁) = (1-ρ²)σ₂²

**Solution Steps:**
1. Match E[X₁|X₂] = 3.7 - 0.15X₂ to formula
2. Match E[X₂|X₁] = 0.4 - 0.6X₁ to formula
3. Use Var(X₂|X₁) = 3.64
4. Solve system for all parameters

---

## HW5-Q6: Stock Returns

**Problem Type:** Data Analysis (Normal Fit)

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 3.3 (Normal Distribution)
- **Supporting:** Section 7.3 (Lognormal - for returns)

**Solution Steps:**
1. Download data
2. Calculate returns
3. Fit normal distribution
4. Compare empirical vs theoretical probabilities

---

# HOMEWORK 6 SOLUTION PATHS

## HW6-Q1: Monty Hall (Sober and Dizzy)

**Problem Type:** Bayesian Inference

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 7.2 (Bayesian Statistics)
- **Template:** Template J (Monty Hall Variants)
- **Section:** 8.1 (Bayesian Problems)

**Decision Tree Path:**
START → "Monty Hall" → Different likelihoods → Bayes table → Section 7.2

**Solution Steps:**
(a) Sober Monty:
- P(opens B|H_A) = 1/2, P(opens B|H_B) = 0, P(opens B|H_C) = 1
- Posterior: P(H_A|data) = 1/3, P(H_C|data) = 2/3
- Strategy: SWITCH

(b) Dizzy Monty:
- P(opens B|any) = 1/2
- Posterior unchanged from prior
- Strategy: doesn't matter

(c) Weighted combination

**Key Recognition Criteria:**
- "Monty Hall"
- Different host behaviors → different likelihoods
- Same data, different posteriors

---

## HW6-Q2: Dice Prediction (Bayesian)

**Problem Type:** Bayesian with Predictive Distribution

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 7.2 (Bayesian Statistics)
- **Template:** Template H (Predictive Distributions)

**Solution Steps:**
1. Prior: uniform over 5 dice
2. Likelihood: P(7|die) = 1/(sides) if sides ≥ 7, else 0
3. Posterior after n 7's: proportional to (1/sides)^n × prior
4. As n→∞: posterior concentrates on D8 (smallest die where 7 possible)
5. Predictive: weight over posterior

---

## HW6-Q3: CLT Sample Size

**Problem Type:** CLT Application

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 6.1 (CLT)
- **Template:** Template K (Finding n for CLT Probability)

**Decision Tree Path:**
START → "Sample size for precision" → CLT → Section 6.1

**Solution Steps:**
1. P(|X̄-μ| < 0.3) ≥ 0.95
2. Standardize: P(|Z| < 0.3√n/3) ≥ 0.95
3. Need 0.3√n/3 ≥ 1.96
4. n ≥ (1.96×3/0.3)² = 384.16 → n = 385

---

## HW6-Q4: CLT for Digit Average

**Problem Type:** CLT Application

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 6.1 (CLT)
- **Template:** Template B (CLT Game Problems)

**Solution Steps:**
1. X_i ~ Uniform{0,1,...,9}
2. E[X_i] = 4.5, Var(X_i) = 8.25
3. X̄ ≈ N(4.5, 8.25/16)
4. P(4 < X̄ < 6) = Φ((6-4.5)/0.718) - Φ((4-4.5)/0.718)

---

## HW6-Q5: Beta-Binomial (Uniform Prior)

**Problem Type:** Conjugate Prior

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 7.2 (Bayesian Statistics)
- **Primary Formula:** Beta(α,β) + k successes in n → Beta(α+k, β+n-k)

**Decision Tree Path:**
START → "Prior" + "Binomial data" → Beta-Binomial → Section 7.2

**Solution Steps:**
1. Prior: θ ~ Uniform(0,1) = Beta(1,1)
2. Data: 3 defective in 8
3. Posterior: θ|data ~ Beta(1+3, 1+5) = Beta(4,6)
4. E[θ|data] = 4/10 = 0.4
5. Var(θ|data) = 4×6/(10²×11) = 24/1100

---

## HW6-Q6: Beta-Binomial (Non-uniform Prior)

**Problem Type:** Conjugate Prior (General Beta)

**PRIMARY SOLUTION PATH:**
- **Main Section:** Section 7.2 (Bayesian Statistics)
- **Primary Formula:** Beta(α,β) prior → Beta(α+k, β+n-k) posterior

**Solution Steps:**
1. Prior: ξ(θ) = 2(1-θ) = Beta(1,2)
2. Data: 3 defective in 8
3. Posterior: θ|data ~ Beta(1+3, 2+5) = Beta(4,7)

---

# PRACTICE EXAM SOLUTION PATHS

## PM1-Q1: Dice Rolls (Multinomial)
- **Section:** 1.5 (Counting), 2.2 (Binomial generalized)
- Part (a): Complement rule
- Part (b): Multinomial coefficient
- Part (c): Inclusion-exclusion

## PM1-Q2: Set Theory
- **Section:** 1.2, 1.4
- Logic and counterexamples

## PM1-Q3: Married Couples
- **Section:** 1.5 (Counting)
- Circular permutations

## PM1-Q4: Dice and Cards
- **Section:** 2.6 (Hypergeometric), 1.3 (Bayes)
- Part (a): Total probability
- Part (b): Bayes' theorem

## PM2-Q1: Joint PDF Triangular
- **Section:** 4.1, 4.2, 4.4
- Same as HW4-Q1 pattern

## PM2-Q2: Joint PDF with Exponential
- **Section:** 4.1, 4.2, 7.1 (Conditional expectation)

## PM2-Q3: Uniform [-1,1]
- **Section:** 3.2, 4.7, 4.4
- Variance of X², max CDF, correlation

## PM2-Q4: Coin Game with MGF
- **Section:** 5.1, 5.2, 7.1
- **Template:** Template B

## PF-Q1: Coin Game CLT
- **Section:** 6.1 (CLT)
- **Template:** Template B
- **Section:** 8.2 (CLT Applications)

## PF-Q2: Gaussian Vector
- **Section:** 4.5 (Bivariate Normal)
- **Template:** Template A, Template G
- **Section:** 8.3 (Bivariate Normal)

## PF-Q3: Exponential CLT
- **Section:** 6.1 (CLT), 3.4 (Exponential)
- **Template:** Template C
- **Section:** 8.6 (Exponential & Memoryless)

## PF-Q4: Lognormal Stock
- **Section:** 7.3 (Lognormal)
- **Template:** Template D
- **Section:** 8.5 (Lognormal Distribution)

## PF-Q5: Discrete Bayesian
- **Section:** 7.2 (Bayesian Statistics)
- **Template:** Template E
- **Section:** 8.8 (Conjugate Priors)

---

# QUICK REFERENCE: PROBLEM → SECTION LOOKUP

| Problem Type | Primary Section | Template |
|--------------|-----------------|----------|
| Counting/Combinatorics | 1.5 | - |
| Conditional Probability | 1.2 | - |
| Bayes' Theorem | 1.3, 7.2 | E, J |
| Independence Check | 1.4, 4.3 | - |
| Binomial | 2.2 | - |
| Poisson | 2.3 | P |
| Geometric | 2.4 | - |
| Hypergeometric | 2.6 | - |
| Uniform | 3.2 | - |
| Normal/Gaussian | 3.3 | - |
| Exponential | 3.4 | C |
| Joint Distribution | 4.1 | - |
| Marginal/Conditional | 4.2 | - |
| Covariance/Correlation | 4.4 | - |
| Bivariate Normal | 4.5 | A, F, G, N |
| Transformations | 4.6 | - |
| Order Statistics | 4.7 | L |
| MGF | 5.1, 5.2 | - |
| CLT | 6.1 | B, C, K, O |
| Confidence Intervals | 6.4 | - |
| Conditional Expectation | 7.1 | M |
| Bayesian | 7.2 | E, H, J |
| Lognormal | 7.3 | D, I |
| Meeting Problem | 4.1 | U17 |

---

# KEYWORD → SECTION QUICK LOOKUP

| If You See... | Go To Section |
|---------------|---------------|
| "Gaussian" | 3.3 or 4.5 (Normal!) |
| "Gaussian vector" | 4.5 (MVN) |
| "Independent components" | 4.5 (ρ=0 for MVN) |
| "i.i.d." + large n | 6.1 (CLT) |
| "Approximate" | 6.1 (CLT) |
| "Prior/Posterior" | 7.2 (Bayesian) |
| "Conjugate" | 7.2 (Beta-Binomial) |
| "Stock price" | 7.3 (Lognormal) |
| "Mean θ = 3" (Exp) | 3.4 (λ = 1/3!) |
| "Memoryless" | 3.4 (Exponential) |
| "Max/Min" | 4.7 (Order Statistics) |
| "n games" | 6.1 (CLT), Template B |
| "Monty Hall" | 7.2, Template J |
| "Without replacement" | 2.6 (Hypergeometric) |

