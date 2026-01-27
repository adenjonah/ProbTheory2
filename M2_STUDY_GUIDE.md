# Midterm 2 Study Guide

**Scope:** Chapter 3 (Random Variables) + Chapter 4 (Expectations through Covariance)
**Format:** 4 problems, 100 points, ~1.5 hours
**Materials:** Open book

---

## Table of Contents
1. [Topic Overview](#topic-overview)
2. [Core Formulas](#core-formulas)
3. [Problem Types & Approaches](#problem-types--approaches)
4. [Decision Tree](#decision-tree)
5. [Practice Problems](#practice-problems)
6. [Common Mistakes](#common-mistakes)

---

## Topic Overview

### What's ON M2
| Topic | Chapter | Key Skills |
|-------|---------|------------|
| Random Variables | 3.1-3.3 | Define PMF, PDF, CDF |
| Functions of RVs | 3.8-3.9 | Transform distributions |
| Expectation | 4.1-4.2 | Compute E[X], E[g(X)] |
| Variance | 4.3 | Compute Var(X), use properties |
| Covariance & Correlation | 4.6 | Cov(X,Y), Cor(X,Y), independence |
| Joint Distributions | 4.1 | Joint PDF/PMF, marginals |
| Conditional Distributions | 4.2 | f(x|y), E[X|Y=y] |
| Order Statistics | 3.9 | CDF of max/min |

### What's NOT on M2 (Final only)
- Central Limit Theorem
- Bivariate Normal
- Law of Large Numbers
- Bayesian Statistics / Conjugate Priors
- Lognormal distribution
- MGF uniqueness theorems

---

## Core Formulas

### Expectation
```
Discrete:   E[X] = sum over x of x * P(X=x)
Continuous: E[X] = integral of x * f(x) dx

E[g(X)] = sum/integral of g(x) * f(x)

Linearity: E[aX + bY + c] = a*E[X] + b*E[Y] + c
```

### Variance
```
Var(X) = E[(X - mu)^2] = E[X^2] - (E[X])^2

Properties:
- Var(aX + b) = a^2 * Var(X)
- If X,Y independent: Var(X + Y) = Var(X) + Var(Y)
- General: Var(X + Y) = Var(X) + Var(Y) + 2*Cov(X,Y)
```

### Covariance & Correlation
```
Cov(X,Y) = E[(X - mu_X)(Y - mu_Y)] = E[XY] - E[X]*E[Y]

Properties:
- Cov(X,X) = Var(X)
- Cov(aX + b, cY + d) = ac * Cov(X,Y)
- Cov(X + Y, Z) = Cov(X,Z) + Cov(Y,Z)

Correlation:
Cor(X,Y) = Cov(X,Y) / (sigma_X * sigma_Y)

Range: -1 <= Cor(X,Y) <= 1
```

### Joint Distributions
```
Joint PDF/PMF: f(x,y) or P(X=x, Y=y)

Marginal (continuous):
f_X(x) = integral of f(x,y) dy
f_Y(y) = integral of f(x,y) dx

Marginal (discrete):
P(X=x) = sum over y of P(X=x, Y=y)

Joint CDF:
F(x,y) = P(X <= x, Y <= y) = integral from -inf to x, -inf to y of f(u,v) dv du

Normalization:
integral over all x,y of f(x,y) dx dy = 1
```

### Conditional Distributions
```
Conditional PDF:
f(x|y) = f(x,y) / f_Y(y)

Conditional Expectation:
E[X | Y=y] = integral of x * f(x|y) dx

E[g(X) | Y=y] = integral of g(x) * f(x|y) dx
```

### Independence Test
```
X and Y are independent IFF:
- f(x,y) = f_X(x) * f_Y(y)  for ALL x,y
- F(x,y) = F_X(x) * F_Y(y)  for ALL x,y

If independent: Cov(X,Y) = 0
WARNING: Cov(X,Y) = 0 does NOT imply independence!
```

### Order Statistics
```
For iid X_1, ..., X_n with CDF F(x):

Maximum Z = max(X_1, ..., X_n):
F_Z(z) = P(Z <= z) = P(all X_i <= z) = [F(z)]^n

Minimum W = min(X_1, ..., X_n):
F_W(w) = P(W <= w) = 1 - P(W > w) = 1 - [1 - F(w)]^n
```

### Transformations
```
If Y = g(X) where g is monotonic:

PDF method:
f_Y(y) = f_X(g^{-1}(y)) * |d/dy [g^{-1}(y)]|

CDF method:
F_Y(y) = P(Y <= y) = P(g(X) <= y)
Then differentiate to get f_Y(y)
```

---

## Problem Types & Approaches

### Type 1: Joint PDF Problems
**Given:** Joint PDF f(x,y) on some region

**Common asks:**
1. **Find c** (normalization constant)
   - Set up: integral of f(x,y) dx dy = 1
   - Watch integration bounds!

2. **Find marginals**
   - f_X(x) = integral of f(x,y) dy
   - f_Y(y) = integral of f(x,y) dx

3. **Find E[X], E[Y], E[XY]**
   - E[X] = integral of x * f_X(x) dx
   - E[XY] = double integral of xy * f(x,y) dx dy

4. **Find Cov and Cor**
   - Cov = E[XY] - E[X]*E[Y]
   - Cor = Cov / (sigma_X * sigma_Y)

5. **Test independence**
   - Check if f(x,y) = f_X(x) * f_Y(y)
   - Or find counterexample

**Example regions:**
- Rectangle: 0 < x < 1, 0 < y < 1
- Triangle: 0 < x < y, 0 < y < 1
- Triangle: 0 < y < x, 0 < x < 1

### Type 2: Independence Testing
**Methods:**
1. **Factorization:** Check if f(x,y) factors into g(x)*h(y)
2. **Counterexample:** Find ONE (x,y) where f(x,y) != f_X(x)*f_Y(y)
3. **Covariance:** If Cov != 0, NOT independent
   - But Cov = 0 doesn't prove independence!

**Classic trap:** X and X^2
- Cor(X, X^2) = 0 for symmetric distributions
- But X and X^2 are NOT independent (functional relationship)

### Type 3: Conditional Distribution/Expectation
**Formula:**
```
f(x|y) = f(x,y) / f_Y(y)

E[X | Y=y] = integral of x * f(x|y) dx
E[X^2 | Y=y] = integral of x^2 * f(x|y) dx
```

**Steps:**
1. Find marginal f_Y(y)
2. Compute f(x|y) = f(x,y) / f_Y(y)
3. Verify f(x|y) integrates to 1 over x
4. Compute conditional expectation

### Type 4: Order Statistics (Max/Min)
**For CDF of max/min of iid variables:**

```
Z = max(X_1, ..., X_n)
P(Z <= z) = [P(X <= z)]^n = [F_X(z)]^n

W = min(X_1, ..., X_n)
P(W <= w) = 1 - [1 - F_X(w)]^n
```

**Example:** X_i ~ Uniform[-1,1]
- F_X(x) = (x+1)/2 for -1 <= x <= 1
- F_Z(z) = [(z+1)/2]^n

### Type 5: Variance of Functions (X^2, etc.)
**For Y = g(X):**
```
Var(Y) = E[Y^2] - (E[Y])^2
       = E[g(X)^2] - (E[g(X)])^2
```

**Example:** Var(X^2) where X ~ Uniform[-1,1]
- E[X^2] = integral of x^2 * (1/2) dx = 1/3
- E[X^4] = integral of x^4 * (1/2) dx = 1/5
- Var(X^2) = 1/5 - (1/3)^2 = 1/5 - 1/9 = 4/45

### Type 6: Geometric Probability Problems
**Setup:** Two independent uniforms, find probability of region

**Method:**
1. Draw the square (or rectangle) of possible values
2. Shade the region satisfying the condition
3. Probability = (shaded area) / (total area)

**Common regions:**
- |A - B| <= c: diagonal band
- A < B + c: region above/below diagonal
- min(A,B) or max(A,B) conditions

### Type 7: MGF Problems
**Definition:**
```
M_X(t) = E[e^{tX}]
```

**Key properties:**
- M'(0) = E[X]
- M''(0) = E[X^2]
- Sum of independents: M_{X+Y}(t) = M_X(t) * M_Y(t)

**For coin toss game (win $a or $b):**
```
M_X(t) = p*e^{at} + (1-p)*e^{bt}

For n independent games:
M_{S_n}(t) = [M_X(t)]^n
```

### Type 8: Random Stopping (Tower Property)
**Setup:** Play N games where N is random

**Use Law of Total Expectation:**
```
E[Y] = E[E[Y|N]]

If Y = X_1 + ... + X_N:
E[Y|N=n] = n * E[X]
E[Y] = E[N * E[X]] = E[N] * E[X]
```

---

## Decision Tree

```
GIVEN A PROBLEM, ASK:

1. Is it about a JOINT distribution?
   |
   +-- YES --> Find c? Marginals? Cov/Cor? Independence?
   |           Go to Type 1-3
   |
   +-- NO --> Continue...

2. Is it about MAX or MIN of iid variables?
   |
   +-- YES --> Use order statistics formulas (Type 4)
   |
   +-- NO --> Continue...

3. Is it about variance of a FUNCTION like X^2?
   |
   +-- YES --> Compute E[g(X)^2] - (E[g(X)])^2 (Type 5)
   |
   +-- NO --> Continue...

4. Is it a GEOMETRIC probability (arrival times, meeting)?
   |
   +-- YES --> Draw region, compute area ratio (Type 6)
   |
   +-- NO --> Continue...

5. Does it mention MGF or E[e^{tX}]?
   |
   +-- YES --> Use MGF properties (Type 7)
   |
   +-- NO --> Continue...

6. Is there a RANDOM number of trials?
   |
   +-- YES --> Use Tower Law: E[Y] = E[E[Y|N]] (Type 8)
   |
   +-- NO --> Basic expectation/variance calculation
```

---

## Practice Problems

### From M2 Practice Exam
| Problem | Topics | Key Technique |
|---------|--------|---------------|
| 1 | Joint PDF, Cov, Var, Cor | Double integrals, E[XY] formula |
| 2 | Joint PDF, marginals, conditional, E[X^2\|Y] | f(x\|y) = f(x,y)/f_Y(y) |
| 3 | Uniform, Var(X^2), order stats, Cor(X,X^2) | Var formula, independence test |
| 4 | MGF, Tower Law | Product of MGFs, E[E[Y\|N]] |

### From HW3
| Problem | Topics |
|---------|--------|
| 1 | Joint PMF, marginals, E[X], Var(X+Y) |
| 2 | Three-sided die, conditional PMF |
| 3 | Geometric RVs, conditional probability |
| 4 | Binomial, conditional probability |
| 5 | Indicator variables, E[R], Var(R) |
| 6-8 | Exponential, transformations, min of exponentials |

### From HW4
| Problem | Topics |
|---------|--------|
| 1 | Joint PDF, CDF, marginals, Cov, Cor, independence |
| 2 | Independence test for joint PMF |
| 3 | Binary RVs, Cov = Cor, independence conditions |
| 4 | Geometric probability (lunch meeting) |
| 5 | Overlapping sums, Cov of correlated sums |

### Key Files to Review
- `practice-exams/midterm2-practice.txt` - Practice exam
- `practice-exams/mid-2-prac-sol.txt` - Full solutions
- `homeworks/hw3/hw3.txt` - Problem set 3
- `homeworks/hw4/hw4.tex` - Problem set 4
- `homeworks/hw4/solutions/` - Detailed HW4 solutions

---

## Common Mistakes

### 1. Integration Bounds
**Wrong:** Always integrating from 0 to 1
**Right:** Check the region! Triangular regions have variable bounds.

Example: f(x,y) = 1/y for 0 < x < y, 0 < y < 1
- To find f_Y(y): integrate x from 0 to y, NOT 0 to 1
- To find f_X(x): integrate y from x to 1, NOT 0 to 1

### 2. Independence vs Uncorrelated
**Wrong:** "Cov = 0, so they're independent"
**Right:** Cov = 0 means uncorrelated. Independence requires f(x,y) = f_X(x)*f_Y(y)

Classic example: X ~ Uniform[-1,1], Y = X^2
- Cov(X, X^2) = 0 (by symmetry)
- But X and X^2 are NOT independent

### 3. Var(X+Y) Formula
**Wrong:** Always using Var(X) + Var(Y)
**Right:** Var(X+Y) = Var(X) + Var(Y) + 2*Cov(X,Y)

Only simplifies when X,Y are independent!

### 4. Conditional vs Marginal
**Wrong:** Using marginal when asked for conditional
**Right:**
- Marginal: f_X(x) = integral of f(x,y) dy
- Conditional: f(x|y) = f(x,y) / f_Y(y)

### 5. Order Statistic CDFs
**Wrong:** P(max > z) = [P(X > z)]^n
**Right:** P(max <= z) = [P(X <= z)]^n

For max, ALL must be <= z
For min, at least ONE must be <= z

### 6. Forgetting to Verify
After computing a PDF, verify:
- It's non-negative everywhere
- It integrates to 1
- The support is correct

---

## Quick Reference Card

### Must-Know Formulas
```
E[X] = integral x*f(x) dx
Var(X) = E[X^2] - (E[X])^2
Cov(X,Y) = E[XY] - E[X]E[Y]
Cor(X,Y) = Cov(X,Y) / (sigma_X * sigma_Y)

f(x|y) = f(x,y) / f_Y(y)
E[X|Y=y] = integral x*f(x|y) dx

F_max(z) = [F(z)]^n
F_min(w) = 1 - [1-F(w)]^n

E[Y] = E[E[Y|N]]  (Tower Law)
```

### Distribution Quick Facts
| Distribution | E[X] | Var(X) |
|--------------|------|--------|
| Uniform[a,b] | (a+b)/2 | (b-a)^2/12 |
| Bernoulli(p) | p | p(1-p) |
| Binomial(n,p) | np | np(1-p) |
| Geometric(p) | (1-p)/p | (1-p)/p^2 |
| Exponential(lambda) | 1/lambda | 1/lambda^2 |
| Poisson(lambda) | lambda | lambda |

---

*Good luck on M2!*
