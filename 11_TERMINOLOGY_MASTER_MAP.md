# TERMINOLOGY MASTER MAP - Complete Synonym Database

**Generated:** December 16, 2025  
**Purpose:** Comprehensive mapping of ALL terminology used in practice problems to concepts in cheat sheet  
**Status:** Phase 11 Complete

---

## TABLE OF CONTENTS

1. [Random Variable Types](#random-variable-types)
2. [Process/Problem Descriptions](#processproblem-descriptions)
3. [Mathematical Operations Described in Words](#mathematical-operations-described-in-words)
4. [Question Keywords and What They Signal](#question-keywords-and-what-they-signal)
5. [Special Professor Terminology](#special-professor-terminology)
6. [Reverse Lookup: Problem Phrase → Concept → Section](#reverse-lookup-problem-phrase--concept--section)

---

## RANDOM VARIABLE TYPES

### Normal Distribution
**Synonyms:**
- Normal ≡ Gaussian ≡ Normal random variable ≡ Gaussian vector ≡ N(μ,σ²) ≡ N(μ,σ²) random variable
- Standard normal ≡ N(0,1) ≡ Z ~ N(0,1) ≡ Standard normal random variable
- Multivariate normal ≡ MVN ≡ Gaussian vector ≡ Jointly normal ≡ Bivariate normal (when 2D)
- "X₁ and X₂ are iid N(0,1)" ≡ "X₁, X₂ independent standard normals"

**Problem Phrases Seen:**
- "X ~ N(μ,σ²)" → Normal distribution
- "Gaussian vector with independent components" → MVN with diagonal covariance
- "Jointly normal" → Bivariate/Multivariate normal
- "Standard normal" → N(0,1)
- "Normal random variable" → Any N(μ,σ²)

**Section Reference:** Section 3.2 (Normal), Section 4.5 (Bivariate Normal)

---

### Exponential Distribution
**Synonyms:**
- Exponential ≡ Exponential random variable ≡ Exp(λ) ≡ Memoryless continuous
- "Exponentially distributed with mean θ" ≡ Exp(1/θ) (note: mean = 1/λ, so λ = 1/θ)
- "Waiting time" (in context) → Often Exponential
- "Time until event" → Often Exponential

**Problem Phrases Seen:**
- "X₁,...,Xₙ are independent random variables exponentially distributed with mean θ" → Each Xᵢ ~ Exp(1/θ)
- "Memoryless property" → Exponential or Geometric
- "f(x) = (1/θ)e^(-x/θ)" → Exp(1/θ) where mean = θ

**Section Reference:** Section 3.3 (Exponential)

---

### Poisson Process
**Synonyms:**
- Poisson Process ≡ Counting process ≡ Arrival process ≡ Poisson(λt)
- "Events occurring at rate λ" → Poisson process
- "Number of arrivals" → Poisson
- "Rare events" → Poisson approximation

**Problem Phrases Seen:**
- "Arrivals per hour" → Poisson
- "Rate λ per unit time" → Poisson process
- "Counting process" → Poisson

**Section Reference:** Section 2.3 (Poisson), Section 3.3 (Exponential - inter-arrival times)

---

### Bernoulli
**Synonyms:**
- Bernoulli ≡ Binary random variable ≡ 0-1 random variable ≡ Indicator ≡ Indicator variable
- "Success/Failure" → Bernoulli trials
- "Takes values 0 or 1" → Bernoulli

**Problem Phrases Seen:**
- "Iᵢ = 1 if event A occurs, 0 otherwise" → Indicator/Bernoulli
- "Binary outcome" → Bernoulli

**Section Reference:** Section 2.2 (Binomial - sum of Bernoullis)

---

### Binomial Distribution
**Synonyms:**
- Binomial ≡ Binomial(n,p) ≡ Number of successes in n trials
- "n independent trials" → Binomial
- "Success probability p" → Binomial parameter

**Problem Phrases Seen:**
- "Toss coin n times" → Binomial(n, 1/2)
- "n trials, each with probability p" → Binomial(n,p)
- "Number of successes" → Binomial

**Section Reference:** Section 2.2

---

### Geometric Distribution
**Synonyms:**
- Geometric ≡ First success ≡ Waiting time (discrete) ≡ Number of failures before first success
- "Until first success" → Geometric
- "Memoryless" (discrete) → Geometric

**Problem Phrases Seen:**
- "Expected number of games to win once" → Geometric
- "Number of trials until..." → Geometric

**Section Reference:** Section 2.4

---

### Negative Binomial
**Synonyms:**
- Negative Binomial ≡ r-th success ≡ Failures before r-th success
- "Until r successes" → Negative Binomial

**Problem Phrases Seen:**
- "r-th success" → Negative Binomial

**Section Reference:** Section 2.5

---

### Uniform Distribution
**Synonyms:**
- Uniform ≡ Uniformly distributed ≡ Equally likely ≡ Uniform on [a,b] ≡ U(a,b)
- "Random point" → Often Uniform
- "Equally likely" → Uniform

**Problem Phrases Seen:**
- "Uniform on [a,b]" → Continuous uniform
- "Random selection" → Could be Uniform
- "Equally likely over interval" → Uniform

**Section Reference:** Section 3.1

---

### Gamma Distribution
**Synonyms:**
- Gamma ≡ Erlang (when shape parameter is integer) ≡ Sum of exponentials
- "Time until r-th event" → Gamma(r,λ) if inter-arrivals are Exp(λ)

**Problem Phrases Seen:**
- "Sum of exponentials" → Gamma
- "Time until r-th arrival" → Gamma

**Section Reference:** Section 3.5

---

### Lognormal Distribution
**Synonyms:**
- Lognormal ≡ Stock price model ≡ e^X where X ~ Normal
- "Stock price" → Often lognormal
- "Y = e^X where X is normal" → Lognormal

**Problem Phrases Seen:**
- "S = S₀e^Z where Z ~ N(...)" → Lognormal
- "Stock follows lognormal" → Lognormal

**Section Reference:** Section 7.3

---

### Beta Distribution
**Synonyms:**
- Beta ≡ Conjugate prior for Binomial ≡ Distribution on [0,1]
- "Proportion" → Often Beta
- "Prior for probability" → Beta

**Problem Phrases Seen:**
- "Beta prior" → Beta distribution
- "Conjugate prior" → Beta (for Binomial)

**Section Reference:** Section 3.6, Section 7.2

---

## PROCESS/PROBLEM DESCRIPTIONS

### Independence Terminology
**Phrases:**
- "Independent" ≡ "i.i.d." ≡ "Independent identically distributed" ≡ "Independent copies"
- "Independent components" (for vectors) → Diagonal covariance matrix
- "X₁,...,Xₙ are independent" → Can use product formulas
- "X and Y are independent" → f(x,y) = f_X(x)f_Y(y)

**Problem Context:**
- "X₁ and X₂ are iid N(0,1)" → Independent standard normals
- "Independent random variables" → Check if can simplify formulas

**Section Reference:** Section 1.4 (Events), Section 4.3 (Random Variables)

---

### Identically Distributed
**Phrases:**
- "i.i.d." ≡ "Identically distributed" ≡ "Same distribution" ≡ "Drawn from same population"
- "X₁,...,Xₙ are i.i.d." → All have same distribution, independent

**Problem Context:**
- "i.i.d. copies" → Independent and identically distributed
- "Same distribution" → Identically distributed

**Section Reference:** Throughout, especially CLT (Section 6.1)

---

### Memoryless Property
**Phrases:**
- "Memoryless" → Exponential (continuous) or Geometric (discrete)
- "No memory" → Memoryless property
- "As good as new" → Memoryless

**Problem Context:**
- "Memoryless property" → Check if Exponential or Geometric
- "Waiting time with memoryless property" → Exponential

**Section Reference:** Section 2.4 (Geometric), Section 3.3 (Exponential)

---

### Arrival Times / Waiting Times
**Phrases:**
- "Arrival times" → Usually Poisson process or Exponential inter-arrivals
- "Waiting time" → Could be Exponential, Gamma, or sum of random variables
- "Time until event" → Often Exponential
- "Time between arrivals" → Exponential (if Poisson process)

**Problem Context:**
- "Time until first arrival" → Exponential
- "Time until r-th arrival" → Gamma
- "Inter-arrival times" → Exponential (if Poisson)

**Section Reference:** Section 3.3 (Exponential), Section 3.5 (Gamma)

---

### Success/Failure Terminology
**Phrases:**
- "Success/Failure" → Bernoulli trials, Binomial, Geometric, Negative Binomial
- "Win/Lose" → Often Bernoulli or Binomial
- "Defective/Non-defective" → Binomial or Hypergeometric

**Problem Context:**
- "n trials, success probability p" → Binomial
- "First success" → Geometric
- "r-th success" → Negative Binomial

**Section Reference:** Section 2.2-2.5

---

## MATHEMATICAL OPERATIONS DESCRIBED IN WORDS

### Sums of Random Variables
**Phrases:**
- "Sum of independent random variables" → Use convolution or MGF
- "X₁ + X₂ + ... + Xₙ" → Sum of random variables
- "Total" → Often sum
- "Combined" → Often sum

**Solution Approaches:**
- If independent: Use MGF (multiply MGFs) or convolution
- If normal: Sum is normal with sum of means, sum of variances
- If Poisson: Sum is Poisson with sum of rates

**Section Reference:** Section 5.2 (MGF for sums), Section 4.3 (Independence)

---

### Minimum/Maximum of Random Variables
**Phrases:**
- "Minimum of" → Order statistics (X₍₁₎)
- "Maximum of" → Order statistics (X₍ₙ₎)
- "Min{X₁,...,Xₙ}" → Minimum order statistic
- "Max{X₁,...,Xₙ}" → Maximum order statistic

**Solution Approaches:**
- CDF method: P(max ≤ x) = [F(x)]ⁿ, P(min > x) = [1-F(x)]ⁿ
- For independent: Use independence property

**Section Reference:** Section 4.7 (Order Statistics)

---

### Conditional on Event
**Phrases:**
- "Conditional on event A" → Use conditional probability/conditional expectation
- "Given that X > a" → Conditional distribution, truncated distribution
- "X given Y" → Conditional distribution
- "P(X|Y)" → Conditional probability

**Solution Approaches:**
- Conditional PDF: f_{Y|X}(y|x) = f(x,y)/f_X(x)
- Conditional expectation: E[Y|X=x] = ∫ y f_{Y|X}(y|x) dy

**Section Reference:** Section 1.2 (Conditional Probability), Section 4.2 (Conditional Distributions), Section 7.1 (Conditional Expectation)

---

### Transformations of Random Variables
**Phrases:**
- "Transform of random variable" → Jacobian method or CDF method
- "Y = g(X)" → Transformation
- "Find distribution of Y = ..." → Transformation problem
- "Change of variables" → Jacobian method

**Solution Approaches:**
- One-to-one: Use Jacobian (multivariate) or derivative method (univariate)
- CDF method: Find F_Y(y) = P(g(X) ≤ y), then differentiate

**Section Reference:** Section 4.6 (Transformations)

---

### Linear Combinations
**Phrases:**
- "aX + bY" → Linear combination
- "Linear transformation" → aX + b
- "Weighted sum" → Linear combination

**Solution Approaches:**
- If normal: Linear combination is normal
- Use properties: E[aX+bY] = aE[X] + bE[Y]
- Var[aX+bY] = a²Var(X) + b²Var(Y) + 2abCov(X,Y)

**Section Reference:** Section 4.5 (Bivariate Normal - linear combinations are normal)

---

## QUESTION KEYWORDS AND WHAT THEY SIGNAL

### Probability Questions
**Keywords:**
- "Compute the probability that..." → Need CDF, PMF, or PDF
- "Find P(...)" → Probability calculation
- "What is the probability..." → Probability calculation
- "Calculate the probability..." → Probability calculation

**Approach:**
- Identify distribution
- Use appropriate formula (PMF, PDF, CDF)
- May need standardization for normal

**Section Reference:** Depends on distribution type

---

### Distribution Questions
**Keywords:**
- "Find the distribution of..." → Transformation problem
- "What is the distribution..." → Need full PDF/PMF/CDF
- "Determine the distribution..." → Full analysis needed

**Approach:**
- Identify transformation
- Use CDF method or Jacobian method
- Check if known distribution family

**Section Reference:** Section 4.6 (Transformations)

---

### Proof/Derivation Questions
**Keywords:**
- "Show that X has distribution..." → Proof/derivation using MGF or CDF
- "Prove that..." → Derivation needed
- "Derive..." → Step-by-step derivation

**Approach:**
- Use MGF uniqueness property
- Or use CDF method
- Show step-by-step

**Section Reference:** Section 5.1 (MGF), Section 4.6 (Transformations)

---

### Approximation Questions
**Keywords:**
- "Approximate..." → CLT, Normal approximation, Law of Large Numbers
- "For large n..." → CLT territory
- "As n → ∞" → Limit theorem
- "Approximately" → Often CLT

**Approach:**
- Check if CLT applies (iid, finite variance, large n)
- Standardize: Z = (X̄ - μ)/(σ/√n)
- Use normal table

**Section Reference:** Section 6.1 (CLT), Section 6.2 (Normal Approximation)

---

### Expectation Questions
**Keywords:**
- "Find E[X|Y]" → Conditional expectation
- "Expected value" → E[X]
- "Mean" → E[X]
- "Compute E[...]" → Expectation calculation

**Approach:**
- Use definition: E[X] = ∫ x f(x) dx or ∑ x p(x)
- For conditional: E[X|Y=y] = ∫ x f_{X|Y}(x|y) dx
- Use law of total expectation: E[X] = E[E[X|Y]]

**Section Reference:** Section 4.1 (Expectation), Section 7.1 (Conditional Expectation)

---

### Independence Questions
**Keywords:**
- "Are X and Y independent?" → Check joint vs product of marginals
- "Independent?" → Test independence
- "Check independence" → Verify f(x,y) = f_X(x)f_Y(y)

**Approach:**
- Find joint distribution
- Find marginals
- Check if product equals joint for ALL (x,y)
- For normal: Check if ρ = 0

**Section Reference:** Section 4.3 (Independence)

---

### Convergence Questions
**Keywords:**
- "Converges in probability/distribution" → Limit theorem question
- "As n → ∞" → Limit behavior
- "Limit" → Limit theorem

**Approach:**
- Identify type of convergence
- Use appropriate limit theorem (CLT, LLN)

**Section Reference:** Section 6.1 (CLT), Section 6.3 (LLN)

---

### Bayesian Questions
**Keywords:**
- "Update" → Bayesian update
- "Posterior" → Bayesian posterior
- "Prior" → Bayesian prior
- "Given evidence" → Bayesian update

**Approach:**
- Identify prior π(θ)
- Write likelihood L(x|θ)
- Compute posterior: π(θ|x) ∝ L(x|θ)π(θ)
- Normalize if needed

**Section Reference:** Section 7.2 (Bayesian Statistics)

---

## SPECIAL PROFESSOR TERMINOLOGY

### Notation Preferences
**Professor Uses:**
- ψ(t) for MGF (not M(t))
- Var(X) not σ²_X
- f(x) for both PMF and PDF
- g₁(x|y) for conditional PDF of X|Y
- π(θ) for prior, π(θ|x) for posterior
- L(x|θ) for likelihood
- Hᵢ for hypotheses in Bayes problems
- X̄ or X̄ₙ for sample mean
- X₍ₖ₎ for k-th order statistic
- I_A for indicator of event A
- →ᵈ for convergence in distribution
- →ᴾ for convergence in probability
- Φ(z) for standard normal CDF
- z_α for quantile where P(Z > z_α) = α

**Section Reference:** Appendix C in cheat sheet

---

### Finance-Specific Terminology
**Phrases:**
- "Stock price" → Lognormal model
- "Returns" → Often normal
- "Volatility" → Standard deviation σ
- "Portfolio" → Linear combination of assets
- "Risk" → Variance or standard deviation
- "Diversification" → Reducing variance through independence/negative correlation

**Problem Context:**
- "S = S₀e^Z" → Lognormal stock price
- "Portfolio variance" → Uses covariance matrix
- "Black-Scholes" → Option pricing with lognormal

**Section Reference:** Section 7.3 (Lognormal), Section 4.4 (Covariance - portfolio applications)

---

### Problem Structure Patterns
**Professor Patterns:**
- Part (a): Basic setup/calculation
- Part (b): Extension requiring part (a)
- Part (c): Conceptual twist or limiting behavior
- Finance context in at least one problem
- One Bayesian problem guaranteed
- One CLT/approximation problem guaranteed

**Section Reference:** Appendix D (Last-Minute Review Checklist)

---

## REVERSE LOOKUP: PROBLEM PHRASE → CONCEPT → SECTION

### Distribution Recognition

| Problem Phrase | Concept | Section Reference |
|----------------|---------|-------------------|
| "Gaussian" | Normal Distribution | Section 3.2 |
| "Gaussian vector" | Multivariate Normal | Section 4.5 |
| "Gaussian vector with independent components" | MVN with diagonal covariance | Section 4.5 |
| "N(μ,σ²)" | Normal Distribution | Section 3.2 |
| "Standard normal" | N(0,1) | Section 3.2 |
| "Jointly normal" | Bivariate Normal | Section 4.5 |
| "Memoryless" | Exponential (continuous) or Geometric (discrete) | Section 3.3 or 2.4 |
| "Arrival process" | Poisson Process | Section 2.3 |
| "Waiting time" | Exponential or Gamma | Section 3.3 or 3.5 |
| "i.i.d." | Independent Identically Distributed | Throughout |
| "Independent components" | Diagonal covariance matrix | Section 4.5 |
| "Stock price" | Lognormal | Section 7.3 |
| "Lognormal" | e^X where X ~ Normal | Section 7.3 |
| "Success/Failure" | Bernoulli/Binomial | Section 2.2 |
| "First success" | Geometric | Section 2.4 |
| "r-th success" | Negative Binomial | Section 2.5 |
| "Without replacement" | Hypergeometric | Section 2.6 |
| "Equally likely" | Uniform | Section 3.1 |

---

### Operation Recognition

| Problem Phrase | Concept | Section Reference |
|----------------|---------|-------------------|
| "Sum of independent" | Use MGF or convolution | Section 5.2 |
| "Maximum of" | Order statistics | Section 4.7 |
| "Minimum of" | Order statistics | Section 4.7 |
| "Conditional on" | Conditional probability/distribution | Section 1.2, 4.2 |
| "Given that" | Conditional | Section 1.2 |
| "Transform" | Transformation problem | Section 4.6 |
| "Find distribution of Y = g(X)" | Transformation | Section 4.6 |
| "Linear combination" | aX + bY | Section 4.5 (if normal) |
| "Approximate" | CLT or Normal approximation | Section 6.1, 6.2 |
| "Large n" | CLT | Section 6.1 |
| "As n → ∞" | Limit theorem | Section 6.1, 6.3 |

---

### Question Type Recognition

| Problem Phrase | Concept | Section Reference |
|----------------|---------|-------------------|
| "Compute the probability" | Probability calculation | Depends on distribution |
| "Find the distribution" | Transformation or identification | Section 4.6 |
| "Show that" | Proof/derivation | Section 5.1 (MGF) |
| "Are X and Y independent?" | Independence test | Section 4.3 |
| "Find E[X\|Y]" | Conditional expectation | Section 7.1 |
| "Update" | Bayesian update | Section 7.2 |
| "Posterior" | Bayesian posterior | Section 7.2 |
| "Converges" | Limit theorem | Section 6.1, 6.3 |
| "Covariance" | Cov(X,Y) | Section 4.4 |
| "Correlation" | ρ = Cov/(σ_X σ_Y) | Section 4.4 |

---

### Multi-Step Pattern Recognition

| Problem Pattern | Required Concepts | Sections |
|----------------|-------------------|----------|
| "i.i.d. Gaussians → Max/Min → Probability" | Independence, Normal, Order Statistics | 4.3, 3.2, 4.7 |
| "Poisson process + Exponential waiting times" | Poisson, Exponential | 2.3, 3.3 |
| "Conditional probability + Bayes theorem" | Conditional, Bayes | 1.2, 1.3 |
| "Transformation + Jacobian method" | Transformations | 4.6 |
| "Joint distribution + Independence + Correlation" | Joint, Independence, Covariance | 4.1, 4.3, 4.4 |
| "Bayesian + Prediction" | Bayesian, Predictive | 7.2 |
| "CLT + Normal approximation" | CLT, Normal | 6.1, 6.2 |
| "Bivariate Normal + Linear combination" | Bivariate Normal | 4.5 |
| "Lognormal + Expectation" | Lognormal, Expectation | 7.3, 4.1 |

---

## CRITICAL TERMINOLOGY GAPS IDENTIFIED

### Missing from Current Cheat Sheet

1. **"Gaussian vector"** - Mentioned in practice problems but not explicitly in cheat sheet
   - **Fix:** Add to Section 4.5 with explicit synonym mapping

2. **"Independent components"** - Used in problems but not clearly explained
   - **Fix:** Add explanation that this means diagonal covariance matrix

3. **"Exponentially distributed with mean θ"** - Parameter confusion (mean = 1/λ)
   - **Fix:** Add note about parameterization: Exp(λ) has mean 1/λ

4. **"i.i.d."** - Used everywhere but not explicitly defined in cheat sheet
   - **Fix:** Add definition in Section 1.4 or early sections

5. **"Memoryless property"** - Mentioned but not clearly linked to both Geometric and Exponential
   - **Fix:** Add cross-reference between Section 2.4 and 3.3

---

## COMPLETENESS CHECKLIST

- [x] All distribution names extracted
- [x] All synonyms identified
- [x] All problem phrases catalogued
- [x] All operation types mapped
- [x] All question keywords identified
- [x] Professor-specific terminology noted
- [x] Finance terminology mapped
- [x] Multi-step patterns identified
- [x] Gaps identified

---

**NEXT STEPS:** Use this map in Phase 12 to identify content gaps, then Phase 13 to expand decision tree, then Phase 14 to fill gaps.

