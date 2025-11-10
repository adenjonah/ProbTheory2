#!/usr/bin/env python3
"""
Problem 5: Overlapping sums of exponential random variables
"""

import sympy as sp
from sympy import symbols, simplify, sqrt

print("=== PROBLEM 5: Overlapping sums ===")
print("X₁, X₂, ... are independent exponential(2) random variables")
print("X = sum of first n variables: X = X₁ + X₂ + ... + Xₙ")
print("Y = sum from Xₙ₋₇ to X₂ₙ₋₈: Y = Xₙ₋₇ + Xₙ₋₆ + ... + X₂ₙ₋₈")
print("Assume n ≥ 8")
print()

# Define symbol
n = symbols('n', integer=True, positive=True)

print("=== Analysis of the sums ===")
print("X includes: X₁, X₂, ..., Xₙ")
print("Y includes: Xₙ₋₇, Xₙ₋₆, ..., X₂ₙ₋₈")
print()

# Find the overlap
print("Finding the overlap:")
print("X includes indices: 1, 2, ..., n")
print("Y includes indices: n-7, n-6, ..., 2n-8")
print()
print("For overlap, we need indices that appear in both ranges:")
print("Overlap occurs when: max(1, n-7) ≤ i ≤ min(n, 2n-8)")
print()
print("Since n ≥ 8:")
print("- n-7 ≥ 1, so max(1, n-7) = n-7")
print("- 2n-8 ≥ n when 2n-8 ≥ n, i.e., n ≥ 8 ✓")
print("- So min(n, 2n-8) = n")
print()
print("Therefore, overlap indices: n-7, n-6, n-5, n-4, n-3, n-2, n-1, n")
print("Number of overlapping terms: 8")
print()

# Variance of exponential(λ) is 1/λ²
print("=== Variance calculations ===")
print("For exponential(2): Var(Xᵢ) = 1/2² = 1/4")
print()

# Size of each sum
print("Size of X: n terms")
print("Size of Y: (2n-8) - (n-7) + 1 = 2n - 8 - n + 7 + 1 = n terms")
print("Size of overlap: 8 terms")
print()

# Covariance calculation using linearity
print("=== Covariance calculation ===")
print("Cov(X, Y) = Cov(∑ᵢ₌₁ⁿ Xᵢ, ∑ⱼ₌ₙ₋₇²ⁿ⁻⁸ Xⱼ)")
print()
print("Using linearity of covariance:")
print("Cov(X, Y) = ∑ᵢ₌₁ⁿ ∑ⱼ₌ₙ₋₇²ⁿ⁻⁸ Cov(Xᵢ, Xⱼ)")
print()
print("Since the Xᵢ are independent:")
print("Cov(Xᵢ, Xⱼ) = 0 if i ≠ j")
print("Cov(Xᵢ, Xⱼ) = Var(Xᵢ) = 1/4 if i = j")
print()
print("Therefore, Cov(X, Y) equals the sum of variances of overlapping terms:")
print("Cov(X, Y) = ∑ᵢ₌ₙ₋₇ⁿ Var(Xᵢ) = ∑ᵢ₌ₙ₋₇ⁿ (1/4) = 8 × (1/4) = 2")

cov_XY = 2
print(f"Cov(X, Y) = {cov_XY}")
print()

# Variance calculations
print("=== Variance of X and Y ===")
print("Var(X) = Var(∑ᵢ₌₁ⁿ Xᵢ) = ∑ᵢ₌₁ⁿ Var(Xᵢ) = n × (1/4) = n/4")
print("Var(Y) = Var(∑ⱼ₌ₙ₋₇²ⁿ⁻⁸ Xⱼ) = ∑ⱼ₌ₙ₋₇²ⁿ⁻⁸ Var(Xⱼ) = n × (1/4) = n/4")

var_X = n/4
var_Y = n/4
print(f"Var(X) = {var_X}")
print(f"Var(Y) = {var_Y}")
print()

# Correlation calculation
print("=== Correlation calculation ===")
print("Cor(X, Y) = Cov(X, Y) / √(Var(X) × Var(Y))")
print(f"         = {cov_XY} / √({var_X} × {var_Y})")
print(f"         = 2 / √((n/4) × (n/4))")
print(f"         = 2 / √(n²/16)")
print(f"         = 2 / (n/4)")
print(f"         = 8/n")

cor_XY = 8/n
print(f"Cor(X, Y) = {cor_XY}")
print()

print("=== VERIFICATION ===")
print("Let's verify with a specific value, say n = 8:")
n_val = 8
cov_val = 2
var_X_val = n_val/4
var_Y_val = n_val/4
cor_val = 8/n_val

print(f"n = {n_val}:")
print(f"Cov(X, Y) = {cov_val}")
print(f"Var(X) = {var_X_val}")
print(f"Var(Y) = {var_Y_val}")
print(f"Cor(X, Y) = {cor_val}")
print()

print("Checking correlation formula:")
cor_check = cov_val / (var_X_val * var_Y_val)**0.5
print(f"Cor(X, Y) = {cov_val} / √({var_X_val} × {var_Y_val}) = {cov_val} / {(var_X_val * var_Y_val)**0.5} = {cor_check}")
print(f"Matches 8/n = 8/{n_val} = {8/n_val} ✓")
print()

print("Let's also verify with n = 16:")
n_val2 = 16
cor_val2 = 8/n_val2
print(f"n = {n_val2}: Cor(X, Y) = 8/{n_val2} = {cor_val2}")
print()

print("=== SUMMARY ===")
print("Cov(X, Y) = 2")
print("Cor(X, Y) = 8/n")
print()
print("The overlap size is always 8 terms regardless of n (as long as n ≥ 8)")
print("This gives a constant covariance of 2")
print("The correlation decreases as n increases because the variances grow with n")
