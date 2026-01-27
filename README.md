# Probability Theory 2 - Study Materials

Study materials for Probability Theory final exam prep.

## Quick Navigation

### Exam Prep (Start Here)
- [`output/FINAL_EXAM_CHEATSHEET.pdf`](output/FINAL_EXAM_CHEATSHEET.pdf) - Printable formula reference
- [`study-guides/10_FINAL_CHECKLIST.md`](study-guides/10_FINAL_CHECKLIST.md) - Pre-exam checklist
- [`study-guides/04_DECISION_TREE.md`](study-guides/04_DECISION_TREE.md) - Problem-solving decision tree

### Problem Practice
- [`problem-index/HOW_TO_USE_PROBLEM_INDEX.md`](problem-index/HOW_TO_USE_PROBLEM_INDEX.md) - How to find and solve problems
- [`problem-index/PROBLEM_DATABASE.md`](problem-index/PROBLEM_DATABASE.md) - All problems with exact wording
- [`problem-index/PROBLEM_SOLUTION_PATHS.md`](problem-index/PROBLEM_SOLUTION_PATHS.md) - Solution approaches by type

### Reference Materials
- [`study-guides/01_MASTER_CONCEPT_INDEX.md`](study-guides/01_MASTER_CONCEPT_INDEX.md) - Alphabetical concept lookup
- [`study-guides/11_TERMINOLOGY_MASTER_MAP.md`](study-guides/11_TERMINOLOGY_MASTER_MAP.md) - Terminology definitions
- [`study-guides/02_PROBLEM_TYPE_CATALOG.md`](study-guides/02_PROBLEM_TYPE_CATALOG.md) - Problem types categorized

## Directory Structure

```
ProbTheory2/
├── study-guides/       # Numbered study guides and indexes
├── problem-index/      # Problem database and solution paths
├── cheatsheets/        # LaTeX source for printable references
├── lectures/           # Lecture slide transcripts (ch1-5)
├── homeworks/          # HW1-6 with solutions
├── practice-exams/     # Practice exams with solutions
└── output/             # Compiled PDFs
```

## By Topic (Post-Midterm 2 Focus)

### Central Limit Theorem
- `homeworks/hw5/` and `homeworks/hw6/`
- `practice-exams/final-practice.txt`

### Bivariate Normal
- `lectures/chapter5.txt`
- `homeworks/hw5/`

### Bayesian Statistics
- `homeworks/hw6/`
- `practice-exams/final-prac-sol.txt`

### Lognormal / Finance
- `homeworks/hw5/`
- `practice-exams/final-practice.txt`

## Compiled PDFs

All compiled PDFs are in the [`output/`](output/) folder:
- `FINAL_EXAM_CHEATSHEET.pdf` - Formula reference
- `COMPLETE_PROBLEM_INDEX.pdf` - Full problem index
- `DECISION_TREE_POCKET_GUIDE.pdf` - Quick decision guide
- `TERMINOLOGY_CHEATSHEET.pdf` - Term definitions
- `TOP_20_PROBLEM_PATTERNS.pdf` - Common patterns

## Building PDFs

To rebuild PDFs from LaTeX source:
```bash
cd cheatsheets
pdflatex FINAL_EXAM_CHEATSHEET.tex
pdflatex FINAL_EXAM_CHEATSHEET.tex  # Run twice for TOC
mv *.pdf ../output/
```
