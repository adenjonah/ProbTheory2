# How to Use the Problem Index

**Generated:** December 16, 2025

## Quick Start

### Method 1: I Have a Specific Problem

1. **Find your problem** in `PROBLEM_DATABASE.md`
   - Organized by HW1 → HW6 → Practice Exams
   - Each problem has exact wording

2. **Look up solution path** in `PROBLEM_SOLUTION_PATHS.md`
   - Find primary section reference (e.g., Section 4.5)
   - Find relevant template (e.g., Template F)

3. **Go to cheatsheet** `FINAL_EXAM_CHEATSHEET.tex`
   - Find the section
   - Use the formulas

### Method 2: I Don't Know What Type of Problem This Is

1. **Identify keywords** in your problem:
   - "Gaussian" → Normal distribution
   - "Given X = x" → Conditional distribution
   - "Large n" → CLT
   - "Prior/Posterior" → Bayesian

2. **Use terminology lookup** in `PROBLEM_SOLUTION_PATHS.md` (bottom section)

3. **Find matching problems** to see solution approach

### Method 3: I Want to Review a Topic

1. **Go to "Problems by Type"** in `PROBLEM_SOLUTION_PATHS.md`
2. **Find your topic** (e.g., "Bivariate Normal")
3. **Practice all listed problems** with their solution paths

## Document Overview

| Document | Purpose | When to Use |
|----------|---------|-------------|
| `problem-index/PROBLEM_DATABASE.md` | All problems with exact wording | Finding specific problems |
| `problem-index/PROBLEM_SOLUTION_PATHS.md` | Section/template mappings | Solution approach |
| `problem-index/PROBLEM_VARIATIONS.md` | How problems can change | Understanding patterns |
| `cheatsheets/COMPLETE_PROBLEM_INDEX.tex` | Master document (PDF-ready) | Printing/comprehensive review |
| `problem-index/VALIDATION_CHECKLIST.md` | Verification report | Checking completeness |
| `cheatsheets/FINAL_EXAM_CHEATSHEET.tex` | Formulas and concepts | During problem solving |

## Critical Terminology Reminders

### MUST REMEMBER:

1. **"Gaussian" = "Normal"**
   - Don't be confused by the term
   - Go to Section 3.3 (univariate) or 4.5 (multivariate)

2. **"Gaussian vector" = "Multivariate Normal" = "Jointly Normal"**
   - For MVN: **independent ⟺ ρ = 0**
   - This is ONLY true for MVN!

3. **Exponential parameterization**
   - If problem says "mean θ = 3", then λ = 1/3
   - **NOT λ = 3**!

4. **"Large n" or "Approximate"**
   - Use Central Limit Theorem
   - Go to Section 6.1

5. **"Prior" and "Posterior"**
   - This is Bayesian statistics
   - Go to Section 7.2

## Problem Recognition Flowchart

```
START
  │
  ├── Is it about counting/combinatorics?
  │   └── YES → Section 1.5
  │
  ├── Is "given" or "conditional" used?
  │   ├── YES → Is it about updating beliefs?
  │   │         ├── YES → Section 7.2 (Bayes)
  │   │         └── NO → Section 1.2 or 4.2
  │   │
  ├── Is it about joint distribution (X,Y)?
  │   ├── YES → Is it "jointly normal" / "Gaussian vector"?
  │   │         ├── YES → Section 4.5
  │   │         └── NO → Section 4.1
  │   │
  ├── Does it mention "n games" or "400 times"?
  │   └── YES → Section 6.1 (CLT)
  │
  ├── Does it mention "stock price" or "lognormal"?
  │   └── YES → Section 7.3
  │
  ├── Is it about exponential distribution?
  │   └── YES → Section 3.4 (check λ vs mean!)
  │
  └── Not sure? → Use keyword lookup in PROBLEM_SOLUTION_PATHS.md
```

## Templates Quick Reference

### Template A: Gaussian Vector
**Use when:** "Jointly normal", linear combinations of normals
**Key fact:** For MVN, independence ⟺ Cov = 0

### Template B: CLT Game Problems
**Use when:** Playing game n times, "approximately"
**Key formula:** S_n ≈ N(nμ, nσ²)

### Template C: Exponential + CLT
**Use when:** Average of exponential random variables
**Warning:** Check if given mean or rate!

### Template D: Lognormal Stock Price
**Use when:** S = S₀e^Z, stock prices
**Key formula:** E[e^X] = e^{μ + σ²/2}

### Template E: Bayesian Discrete Prior
**Use when:** Prior is discrete (e.g., P(θ=1/2) = P(θ=3/4) = 1/2)
**Method:** Bayes table

### Template F: BVN Conditional
**Use when:** "Given X = x, find Y"
**Key formula:** Y|X=x ~ N(μ_Y + ρ(σ_Y/σ_X)(x-μ_X), (1-ρ²)σ²_Y)

### Template J: Monty Hall
**Use when:** Monty Hall variants
**Key insight:** Different host behaviors = different likelihoods

### Template K: Find n for CLT
**Use when:** "Smallest n such that P(|X̄ - μ| < ε) ≥ 1-α"
**Key formula:** n ≥ (z_{α/2} σ / ε)²

## Common Mistakes to Avoid

1. **Exponential: λ vs 1/λ**
   - Mean = 1/λ
   - If told "mean = 3", then λ = 1/3

2. **Normal vs MVN**
   - Uncorrelated ≠ independent (in general)
   - But for MVN: uncorrelated = independent!

3. **Forgetting correlation in Var(X+Y)**
   - Var(X+Y) = Var(X) + Var(Y) + 2Cov(X,Y)
   - Only simplifies to Var(X) + Var(Y) if independent

4. **CLT: σ vs σ/√n**
   - Individual: X ~ dist(μ, σ²)
   - Average: X̄ ~ N(μ, σ²/n)

5. **Lognormal: parameters**
   - X lognormal(μ, σ²) means ln(X) ~ N(μ, σ²)
   - E[X] ≠ μ !
   - E[X] = e^{μ + σ²/2}

## Study Strategy

### For Final Exam Preparation:

1. **Week before exam:**
   - Review all problem types in `PROBLEM_SOLUTION_PATHS.md`
   - Practice one problem from each type
   - Focus on your weak areas

2. **Day before exam:**
   - Review `COMPLETE_PROBLEM_INDEX.tex` Section 6 (Terminology)
   - Review `FINAL_EXAM_CHEATSHEET.tex`
   - Focus on formulas

3. **During exam:**
   - Read problem carefully
   - Identify keywords
   - Map to section/template
   - Write formulas first, then solve

### For Specific Topics:

1. Identify topic in "Problems by Type"
2. Do ALL listed problems
3. Review variations in `PROBLEM_VARIATIONS.md`
4. Create your own variations

## Printing Recommendations

### For Comprehensive Review:
```bash
pdflatex COMPLETE_PROBLEM_INDEX.tex
pdflatex COMPLETE_PROBLEM_INDEX.tex  # Run twice for TOC
```
Print `COMPLETE_PROBLEM_INDEX.pdf`

### For Quick Reference (Exam Allowed Materials):
Print only `FINAL_EXAM_CHEATSHEET.pdf` (if allowed)

### For Problem Practice:
Keep `PROBLEM_DATABASE.md` and `PROBLEM_SOLUTION_PATHS.md` open side by side

## Need More Help?

1. **Can't find a problem type?**
   - Check terminology dictionary
   - Search for keywords in `PROBLEM_DATABASE.md`

2. **Don't understand a solution path?**
   - Look at similar problems in the same section
   - Review the corresponding section in `FINAL_EXAM_CHEATSHEET.tex`

3. **Want more practice?**
   - Use variations from `PROBLEM_VARIATIONS.md`
   - Change parameters in existing problems
   - Combine different problem types

