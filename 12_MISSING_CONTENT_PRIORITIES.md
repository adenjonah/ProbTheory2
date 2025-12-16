# Missing Content Priorities - Gap Analysis

**Generated:** December 16, 2025
**Purpose:** Prioritized list of content gaps between terminology used in problems and current cheat sheet

---

## CRITICAL GAPS (Appears in Practice Exams but Missing/Incomplete in Notes)

### 1. Gaussian Vector / Independent Components Terminology
**Where it appears:**
- Final Practice Problem 2: "Y = (Y₁, Y₂) is a Gaussian vector with independent components"
- Solution: "For multivariate normal, independence is equivalent to zero correlation, so b = -a"

**Current Status:** 
- Section 4.5 mentions "Bivariate Normal" but doesn't explicitly use "Gaussian vector" terminology
- "Independent components" = diagonal covariance matrix is not explicitly stated

**Action Required:**
- Add to Section 4.5: "\subsection*{4.5 Bivariate Normal (a.k.a. Jointly Normal, Gaussian Vector)}"
- Add explicit note: "Gaussian vector with independent components" means covariance matrix is diagonal (all off-diagonal elements = 0)
- Add to decision tree: Path for "Gaussian vector" → Bivariate Normal section

---

### 2. i.i.d. Recognition and Implications
**Where it appears:**
- Final Practice Problem 2: "X₁ and X₂ are iid N(0,1)"
- Final Practice Problem 3: "X₁, X₂, ..., X₁₀₀ be independent random variables exponentially distributed"
- Multiple homework problems use this terminology

**Current Status:**
- Term "i.i.d." used but not defined as a recognition keyword
- Implications for MGF, CLT, variance of sums not consolidated

**Action Required:**
- Add definition block: "i.i.d. = independent and identically distributed = same distribution + independent"
- Add implications checklist:
  - Var(ΣXᵢ) = nVar(X₁)
  - MGF of sum = [MGF(X₁)]ⁿ
  - CLT applies: X̄ ≈ N(μ, σ²/n)

---

### 3. Exponential Mean Parameterization
**Where it appears:**
- Final Practice Problem 3: "exponentially distributed with mean θ = 3 (i.e. their density is f(x) = (1/3)e^{-x/3})"

**Current Status:**
- Section 3.4 uses rate parameterization λ
- Mean = 1/λ mentioned but not prominent
- Solution requires recognizing mean = 3 means λ = 1/3

**Action Required:**
- Add explicit parameterization note: "If Exp has mean θ, then λ = 1/θ, so f(x) = (1/θ)e^{-x/θ}"
- Add conversion table: Mean θ ↔ Rate λ = 1/θ

---

### 4. Lognormal Stock Price Model Details
**Where it appears:**
- Final Practice Problem 4: "S = S₀e^Z where Z is normal with mean (r - σ²/2) and variance σ²"
- HW5 Problem 2, 3, 6: Lognormal applications

**Current Status:**
- Section 7.3 has basic lognormal but:
  - E[e^{-r}S] calculation method not shown
  - The specific parameterization (r - σ²/2) not explained
  - Risk-neutral pricing not mentioned

**Action Required:**
- Add explicit formula: E[S] = S₀e^{μ + σ²/2} where μ = r - σ²/2 gives E[e^{-r}S] = S₀
- Add step-by-step for P(S > K) calculation
- Note: "log returns are normal" ⟺ "prices are lognormal"

---

### 5. Discrete Prior Bayesian Update
**Where it appears:**
- Final Practice Problem 5: "prior distribution of θ is 1/2 with probability 1/2 and 3/4 with probability 1/2"

**Current Status:**
- Section 7.2 focuses on conjugate continuous priors (Beta-Binomial, etc.)
- Discrete prior case not explicitly covered

**Action Required:**
- Add subsection for discrete prior Bayesian update
- Include formula: P(θ=θᵢ|data) = P(data|θ=θᵢ)P(θ=θᵢ) / Σⱼ P(data|θ=θⱼ)P(θ=θⱼ)
- Add example with discrete θ values

---

### 6. Linear Combinations of Bivariate Normal for Independence
**Where it appears:**
- Final Practice Problem 2(a): "Find a and b such that Y = (Y₁, Y₂) is a Gaussian vector with independent components"
- HW5 Problem 1(b): "Find constant a if aX + Y and X + 2Y are independent"

**Current Status:**
- Section 4.5 doesn't have explicit method for finding when linear combinations are independent

**Action Required:**
- Add method: For jointly normal, aX + Y and cX + dY independent ⟺ Cov(aX+Y, cX+dY) = 0
- Show: Cov(aX+Y, cX+dY) = ac·Var(X) + (ad+bc)·Cov(X,Y) + bd·Var(Y)
- Solve for parameters that make this zero

---

## PARTIAL COVERAGE (Defined but Missing Examples/Synonyms)

### 7. Normal Distribution Synonym "Gaussian"
**Current Status:** "Normal" used throughout, "Gaussian" not mentioned
**Action:** Add "(a.k.a. Gaussian)" to section 3.3 header

### 8. Memoryless Property Link
**Current Status:** Mentioned in both Geometric (2.4) and Exponential (3.4) separately
**Action:** Add cross-reference note linking both, add to recognition pattern

### 9. Conditional Probability Phrases
**Current Status:** Formula given, but recognition phrases limited
**Action:** Add phrases: "given that", "if we know", "conditional on", "knowing that"

### 10. Order Statistics for i.i.d. Normals
**Current Status:** Section 4.7 has general order statistics
**Action:** Add specific case for Gaussian: P(max{X₁,...,Xₙ} > a) = 1 - [Φ((a-μ)/σ)]ⁿ

---

## TERMINOLOGY-ONLY GAPS (Concept Exists but Not Findable by Problem Wording)

### 11. "Counting Process" → Poisson
Need explicit mapping in decision tree

### 12. "Arrival Process" → Poisson Process
Need explicit mapping

### 13. "Service Time" → Often Exponential
Need explicit mapping

### 14. "Volatility" → Standard Deviation (σ)
Need explicit finance-probability mapping

### 15. "Risk" → Variance/Standard Deviation
Need explicit mapping

### 16. "Jointly Distributed" → Joint Distribution
Common phrasing not explicitly linked

### 17. "Marginal of X" → Integrate out Y
Phrasing variation not explicit

### 18. "Uncorrelated but Dependent"
Example exists (X and X²) but not prominently featured as a trap

---

## MULTI-STEP PROBLEM PATTERNS IDENTIFIED

### Pattern 1: i.i.d. Gaussians → Linear Combination → Probability
**Example:** Final Practice Problem 2
**Steps:** 
1. Recognize i.i.d. standard normals
2. Form linear combinations 
3. Use MVN properties
4. Find conditions for independence
5. Calculate probability

### Pattern 2: Exponentials → CLT → Transform Inequality
**Example:** Final Practice Problem 3
**Steps:**
1. Recognize exponential with given mean
2. Calculate E[X̄], Var(X̄)
3. Transform inequality algebraically
4. Apply CLT standardization
5. Look up Φ

### Pattern 3: Lognormal → E[function] → Probability
**Example:** Final Practice Problem 4
**Steps:**
1. Recognize lognormal structure S = S₀e^Z
2. Use E[e^X] = exp(μ + σ²/2) for normal X
3. Transform P(S > K) to P(Z > something)
4. Standardize and use Φ

### Pattern 4: Discrete Prior → Bayesian Update → Posterior Mean
**Example:** Final Practice Problem 5
**Steps:**
1. List hypotheses and priors
2. Calculate likelihoods for each
3. Apply Bayes formula
4. Normalize if needed
5. Calculate posterior mean/variance

### Pattern 5: Joint PDF → Marginals → Independence Check
**Example:** HW4 Problem 1, Midterm 2 Sample
**Steps:**
1. Find normalizing constant
2. Calculate marginals by integration
3. Check if f(x,y) = f_X(x)·f_Y(y)
4. If not equal, NOT independent

### Pattern 6: Bivariate Normal → Sum → Probability
**Example:** HW5 Problem 1
**Steps:**
1. Recognize jointly normal
2. Linear combination is normal
3. Calculate E[aX+bY] = aμ_X + bμ_Y
4. Calculate Var(aX+bY) = a²σ²_X + b²σ²_Y + 2ab·ρ·σ_X·σ_Y
5. Standardize and use Φ

### Pattern 7: Monty Hall Variants (Bayesian)
**Example:** HW6 Problem 1
**Steps:**
1. Define hypotheses H_A, H_B, H_C
2. Set up prior probabilities
3. Determine likelihoods for each scenario (sober vs dizzy)
4. Apply Bayes' theorem
5. Compare posterior probabilities

### Pattern 8: Sample Size for Confidence
**Example:** HW6 Problem 3
**Steps:**
1. Identify requirement: P(|X̄ - μ| < ε) ≥ 1-α
2. Apply CLT: P(|Z| < ε√n/σ) ≥ 1-α
3. Find z_{α/2} value
4. Solve: ε√n/σ = z_{α/2}
5. Calculate n

### Pattern 9: MGF → Distribution Identification
**Example:** Midterm 2 Problem 4
**Steps:**
1. Calculate MGF of single RV
2. Use MGF multiplication for sums
3. Match resulting MGF to known distribution
4. Identify parameters

### Pattern 10: Conditional Expectation → Total Expectation
**Example:** Midterm 2 Sample Problem 4(b)
**Steps:**
1. Condition on convenient variable
2. Calculate E[X|Y=y]
3. Apply E[X] = E[E[X|Y]]
4. Integrate/sum over Y distribution

---

## PROFESSOR-SPECIFIC PROBLEM STYLES

### Style 1: Multi-Part Build-Up
- Part (a): Basic setup
- Part (b): Use result from (a)
- Part (c): Conceptual extension or limiting case

### Style 2: Finance Context
- At least one problem uses stock/portfolio context
- Requires translating finance terms to probability

### Style 3: Bayesian Guaranteed
- One problem always involves prior/posterior update
- Often Monty Hall variant or conjugate prior

### Style 4: CLT Application Guaranteed
- One problem requires normal approximation
- May involve continuity correction

### Style 5: Conditional Structure
- "Given that" or "conditional on" appears frequently
- Total expectation/variance often needed

---

## PRIORITY FIX ORDER

**CRITICAL (Fix immediately):**
1. Add "Gaussian vector / independent components" to Section 4.5
2. Add "i.i.d." definition and implications
3. Add discrete prior Bayesian update example
4. Add linear combination independence condition for MVN

**HIGH (Fix before exam):**
5. Expand lognormal finance section
6. Add all synonym headers to existing sections
7. Create multi-step pattern recognition section

**MEDIUM (If time permits):**
8. Add cross-references between related sections
9. Expand decision tree with phrase mappings
10. Add more worked examples

---

_End of Gap Analysis_
