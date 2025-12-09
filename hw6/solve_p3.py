"""
Problem 3: CLT Sample Size
Mean is mu, standard deviation is 3.
Find smallest n for which P(|X_bar_n - mu| < 0.3) >= 0.95.
"""
import numpy as np
from scipy import stats

print("=" * 60)
print("PROBLEM 3: CLT SAMPLE SIZE")
print("=" * 60)

# Given
sigma = 3  # population standard deviation
epsilon = 0.3  # margin of error
confidence = 0.95

print(f"\nGiven:")
print(f"  σ = {sigma}")
print(f"  ε = {epsilon} (half-width of interval)")
print(f"  Required probability: P(|X̄_n - μ| < {epsilon}) ≥ {confidence}")

# By CLT, X̄_n is approximately N(μ, σ²/n)
# So (X̄_n - μ) / (σ/√n) ~ N(0, 1)
# P(|X̄_n - μ| < ε) = P(-ε < X̄_n - μ < ε)
#                   = P(-ε/(σ/√n) < Z < ε/(σ/√n))
#                   = P(-ε√n/σ < Z < ε√n/σ)
#                   = 2Φ(ε√n/σ) - 1

print("\nUsing CLT:")
print("  X̄_n ~ N(μ, σ²/n) approximately")
print("  P(|X̄_n - μ| < ε) = P(-ε√n/σ < Z < ε√n/σ) = 2Φ(ε√n/σ) - 1")

print(f"\nWe need: 2Φ(ε√n/σ) - 1 ≥ {confidence}")
print(f"         2Φ({epsilon}√n/{sigma}) - 1 ≥ {confidence}")
print(f"         Φ(0.1√n) ≥ {(1 + confidence)/2}")

# Find z-value for 97.5th percentile (two-tailed 95%)
z = stats.norm.ppf((1 + confidence) / 2)
print(f"\nNeed Φ(0.1√n) ≥ {(1 + confidence)/2}")
print(f"So 0.1√n ≥ Φ⁻¹({(1 + confidence)/2}) = {z:.6f}")

# Solve for n
# 0.1√n ≥ z
# √n ≥ 10z
# n ≥ 100z²

n_exact = (z * sigma / epsilon)**2
print(f"\nSolving: 0.1√n ≥ {z:.6f}")
print(f"         √n ≥ {z * sigma / epsilon:.6f}")
print(f"         n ≥ ({z:.6f} × {sigma} / {epsilon})² = {n_exact:.6f}")

n_min = int(np.ceil(n_exact))
print(f"\nSmallest integer n: n = {n_min}")

# Verification
print("\n" + "=" * 60)
print("VERIFICATION")
print("=" * 60)

for n_test in [n_min - 1, n_min, n_min + 1]:
    z_test = epsilon * np.sqrt(n_test) / sigma
    prob = 2 * stats.norm.cdf(z_test) - 1
    satisfies = "✓" if prob >= confidence else "✗"
    print(f"n = {n_test}: P(|X̄ - μ| < {epsilon}) = 2Φ({z_test:.6f}) - 1 = {prob:.8f} {satisfies}")

print(f"\nFinal Answer: n = {n_min}")
print(f"Check: {2 * stats.norm.cdf(epsilon * np.sqrt(n_min) / sigma) - 1:.8f} ≥ {confidence}")

