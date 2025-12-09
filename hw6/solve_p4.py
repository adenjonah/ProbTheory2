"""
Problem 4: CLT Digit Average
16 digits chosen at random with replacement from {0, 1, ..., 9}.
What is probability their average lies between 4 and 6?
"""
import numpy as np
from scipy import stats

print("=" * 60)
print("PROBLEM 4: CLT DIGIT AVERAGE")
print("=" * 60)

# Single digit X uniform on {0, 1, ..., 9}
# E[X] = (0 + 1 + ... + 9) / 10 = 45 / 10 = 4.5
# E[X²] = (0² + 1² + ... + 9²) / 10 = 285 / 10 = 28.5
# Var(X) = E[X²] - (E[X])² = 28.5 - 20.25 = 8.25

mu = 4.5
var = 8.25
sigma = np.sqrt(var)

print(f"\nSingle digit X ~ Uniform{{0, 1, ..., 9}}")
print(f"E[X] = (0 + 1 + ... + 9) / 10 = 45/10 = {mu}")
print(f"E[X²] = (0² + 1² + ... + 9²) / 10 = 285/10 = 28.5")
print(f"Var(X) = E[X²] - (E[X])² = 28.5 - 20.25 = {var}")
print(f"σ = √{var} = √(33/4) = √33/2 ≈ {sigma:.6f}")

# n = 16 digits
n = 16

print(f"\nn = {n} digits")
print(f"X̄₁₆ = (X₁ + X₂ + ... + X₁₆) / 16")

# By CLT, X̄₁₆ ~ N(μ, σ²/n) approximately
sigma_xbar = sigma / np.sqrt(n)
print(f"\nBy CLT: X̄₁₆ ~ N({mu}, {var}/{n}) = N({mu}, {var/n})")
print(f"Standard deviation of X̄₁₆ = σ/√n = √33/2 ÷ 4 = √33/8 ≈ {sigma_xbar:.6f}")

# P(4 < X̄₁₆ < 6)
# Note: The interval [4, 6] is NOT symmetric around μ = 4.5
# Lower bound 4 is 0.5 below mean
# Upper bound 6 is 1.5 above mean

z_low = (4 - mu) / sigma_xbar
z_high = (6 - mu) / sigma_xbar

print(f"\nP(4 < X̄₁₆ < 6):")
print(f"Note: Interval [4, 6] is NOT symmetric around μ = 4.5")
print(f"  4 is {abs(4 - mu)} below the mean")
print(f"  6 is {abs(6 - mu)} above the mean")

print(f"\nStandardize:")
print(f"  z_low = (4 - {mu}) / {sigma_xbar:.6f} = {z_low:.6f}")
print(f"  z_high = (6 - {mu}) / {sigma_xbar:.6f} = {z_high:.6f}")

prob = stats.norm.cdf(z_high) - stats.norm.cdf(z_low)

print(f"\nP(4 < X̄₁₆ < 6) = Φ({z_high:.6f}) - Φ({z_low:.6f})")
print(f"                = {stats.norm.cdf(z_high):.6f} - {stats.norm.cdf(z_low):.6f}")
print(f"                = {prob:.6f}")

# Exact z values
# σ/√n = √33/8
# z_low = -0.5 / (√33/8) = -4/√33
# z_high = 1.5 / (√33/8) = 12/√33

from fractions import Fraction
import sympy as sp

print("\n" + "=" * 60)
print("EXACT CALCULATION")
print("=" * 60)

print("\nExact standard deviation:")
print("σ/√n = √33/8")

print("\nExact z-values:")
print("z_low = (4 - 4.5) / (√33/8) = -0.5 × 8/√33 = -4/√33")
print("z_high = (6 - 4.5) / (√33/8) = 1.5 × 8/√33 = 12/√33")

z_low_exact = -4 / np.sqrt(33)
z_high_exact = 12 / np.sqrt(33)

print(f"\nNumerical: z_low = -4/√33 = {z_low_exact:.8f}")
print(f"           z_high = 12/√33 = {z_high_exact:.8f}")

print(f"\nFinal Answer:")
print(f"P(4 < X̄₁₆ < 6) = Φ(12/√33) - Φ(-4/√33)")
print(f"               ≈ {prob:.6f}")

# Alternative expression using symmetry of normal distribution
# Φ(-a) = 1 - Φ(a)
# So P = Φ(12/√33) - (1 - Φ(4/√33)) = Φ(12/√33) + Φ(4/√33) - 1
print(f"\nAlternative form: Φ(12/√33) + Φ(4/√33) - 1")
alt_prob = stats.norm.cdf(z_high_exact) + stats.norm.cdf(-z_low_exact) - 1
print(f"                = {stats.norm.cdf(z_high_exact):.6f} + {stats.norm.cdf(-z_low_exact):.6f} - 1")
print(f"                = {alt_prob:.6f}")

print("\n" + "=" * 60)
print("VERIFICATION")
print("=" * 60)
print(f"z_low = {z_low:.8f}, z_high = {z_high:.8f}")
print(f"Φ(z_high) = {stats.norm.cdf(z_high):.8f}")
print(f"Φ(z_low) = {stats.norm.cdf(z_low):.8f}")
print(f"P(4 < X̄ < 6) = {prob:.8f}")
