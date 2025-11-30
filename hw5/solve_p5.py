"""
Problem 5: Bivariate Normal Parameters
Given conditional expectations:
- E[X₁|X₂] = 3.7 - 0.15X₂
- E[X₂|X₁] = 0.4 - 0.6X₁
- Var(X₂|X₁) = 3.64

Find: μ₁, σ₁², μ₂, σ₂², ρ
"""
import numpy as np
from scipy import stats
import sympy as sp

print("="*60)
print("Problem 5: Bivariate Normal Parameters")
print("="*60)

print("\nGiven:")
print("E[X₁|X₂] = 3.7 - 0.15X₂")
print("E[X₂|X₁] = 0.4 - 0.6X₁")
print("Var(X₂|X₁) = 3.64")

print("\n" + "="*60)
print("SOLUTION:")
print("="*60)

# For bivariate normal (X₁, X₂):
# E[X₁|X₂] = μ₁ + ρ(σ₁/σ₂)(X₂ - μ₂)
#          = (μ₁ - ρ(σ₁/σ₂)μ₂) + ρ(σ₁/σ₂)X₂
#
# Comparing with 3.7 - 0.15X₂:
# coefficient of X₂: ρ(σ₁/σ₂) = -0.15
# constant term: μ₁ - ρ(σ₁/σ₂)μ₂ = 3.7

# Similarly, E[X₂|X₁] = μ₂ + ρ(σ₂/σ₁)(X₁ - μ₁)
# Comparing with 0.4 - 0.6X₁:
# coefficient of X₁: ρ(σ₂/σ₁) = -0.6
# constant term: μ₂ - ρ(σ₂/σ₁)μ₁ = 0.4

# Also: Var(X₂|X₁) = σ₂²(1 - ρ²) = 3.64

print("\nFor bivariate normal, the conditional expectations have the form:")
print("E[X₁|X₂] = μ₁ + ρ(σ₁/σ₂)(X₂ - μ₂)")
print("E[X₂|X₁] = μ₂ + ρ(σ₂/σ₁)(X₁ - μ₁)")
print("\nExpanding and comparing coefficients:")
print("From E[X₁|X₂] = 3.7 - 0.15X₂:")
print("  ρ(σ₁/σ₂) = -0.15  ... (1)")
print("  μ₁ - ρ(σ₁/σ₂)μ₂ = 3.7  ... (2)")
print("\nFrom E[X₂|X₁] = 0.4 - 0.6X₁:")
print("  ρ(σ₂/σ₁) = -0.6  ... (3)")
print("  μ₂ - ρ(σ₂/σ₁)μ₁ = 0.4  ... (4)")

# From (1) and (3):
# ρ(σ₁/σ₂) = -0.15
# ρ(σ₂/σ₁) = -0.6
# Multiply: ρ² = (-0.15)(-0.6) = 0.09
# So ρ = ±0.3

print("\nMultiplying equations (1) and (3):")
print("ρ(σ₁/σ₂) × ρ(σ₂/σ₁) = (-0.15) × (-0.6)")
print("ρ² = 0.09")
print("ρ = ±0.3")

print("\nSince both coefficients are negative, ρ must be negative:")
rho = -0.3
print(f"ρ = {rho}")

# From Var(X₂|X₁) = σ₂²(1 - ρ²) = 3.64
var_X2_given_X1 = 3.64
sigma2_2 = var_X2_given_X1 / (1 - rho**2)
sigma_2 = np.sqrt(sigma2_2)

print(f"\nFrom Var(X₂|X₁) = σ₂²(1 - ρ²) = {var_X2_given_X1}:")
print(f"σ₂² = {var_X2_given_X1} / (1 - {rho**2})")
print(f"σ₂² = {var_X2_given_X1} / {1 - rho**2}")
print(f"σ₂² = {sigma2_2}")
print(f"σ₂ = {sigma_2}")

# From ρ(σ₁/σ₂) = -0.15
coeff_X2 = -0.15
sigma_1 = coeff_X2 * sigma_2 / rho
sigma2_1 = sigma_1**2

print(f"\nFrom ρ(σ₁/σ₂) = {coeff_X2}:")
print(f"σ₁ = {coeff_X2} × σ₂ / ρ")
print(f"σ₁ = {coeff_X2} × {sigma_2} / {rho}")
print(f"σ₁ = {sigma_1}")
print(f"σ₁² = {sigma2_1}")

# Verify with the other equation
coeff_X1 = -0.6
sigma_2_check = coeff_X1 * sigma_1 / rho
print(f"\nVerification from ρ(σ₂/σ₁) = {coeff_X1}:")
print(f"σ₂ = {coeff_X1} × σ₁ / ρ = {coeff_X1} × {sigma_1} / {rho} = {sigma_2_check}")
print(f"Check: σ₂ values match: {np.isclose(sigma_2, sigma_2_check)}")

# Now find μ₁ and μ₂
# μ₁ - ρ(σ₁/σ₂)μ₂ = 3.7
# μ₁ - (-0.15)μ₂ = 3.7
# μ₁ + 0.15μ₂ = 3.7  ... (A)

# μ₂ - ρ(σ₂/σ₁)μ₁ = 0.4
# μ₂ - (-0.6)μ₁ = 0.4
# μ₂ + 0.6μ₁ = 0.4  ... (B)

print("\nFor the means:")
print("μ₁ - ρ(σ₁/σ₂)μ₂ = 3.7")
print("μ₁ + 0.15μ₂ = 3.7  ... (A)")
print("\nμ₂ - ρ(σ₂/σ₁)μ₁ = 0.4")
print("μ₂ + 0.6μ₁ = 0.4  ... (B)")

# From (B): μ₂ = 0.4 - 0.6μ₁
# Substitute into (A): μ₁ + 0.15(0.4 - 0.6μ₁) = 3.7
# μ₁ + 0.06 - 0.09μ₁ = 3.7
# 0.91μ₁ = 3.64
# μ₁ = 4

print("\nFrom (B): μ₂ = 0.4 - 0.6μ₁")
print("Substitute into (A): μ₁ + 0.15(0.4 - 0.6μ₁) = 3.7")
print("μ₁ + 0.06 - 0.09μ₁ = 3.7")
print("0.91μ₁ = 3.64")

mu_1 = 3.64 / 0.91
print(f"μ₁ = {mu_1}")

mu_2 = 0.4 - 0.6 * mu_1
print(f"\nμ₂ = 0.4 - 0.6 × {mu_1} = {mu_2}")

# Exact symbolic computation
print("\n" + "="*60)
print("EXACT SYMBOLIC COMPUTATION:")
print("="*60)

rho_sym = sp.Rational(-3, 10)
var_X2_given_X1_sym = sp.Rational(364, 100)

sigma2_2_sym = var_X2_given_X1_sym / (1 - rho_sym**2)
sigma_2_sym = sp.sqrt(sigma2_2_sym)

coeff_X2_sym = sp.Rational(-15, 100)
sigma_1_sym = coeff_X2_sym * sigma_2_sym / rho_sym
sigma2_1_sym = sigma_1_sym**2

# Means
# 0.91μ₁ = 3.64
mu_1_sym = sp.Rational(364, 100) / sp.Rational(91, 100)
mu_2_sym = sp.Rational(4, 10) - sp.Rational(6, 10) * mu_1_sym

print(f"ρ = {rho_sym} = {sp.simplify(rho_sym)}")
print(f"σ₂² = {sp.simplify(sigma2_2_sym)}")
print(f"σ₂ = {sp.simplify(sigma_2_sym)}")
print(f"σ₁² = {sp.simplify(sigma2_1_sym)}")
print(f"σ₁ = {sp.simplify(sigma_1_sym)}")
print(f"μ₁ = {sp.simplify(mu_1_sym)}")
print(f"μ₂ = {sp.simplify(mu_2_sym)}")

# Numerical verification
print("\n" + "="*60)
print("VERIFICATION:")
print("="*60)

# Verify the conditional expectations
mu_1_num = float(mu_1_sym)
mu_2_num = float(mu_2_sym)
sigma_1_num = float(sigma_1_sym)
sigma_2_num = float(sigma_2_sym)
rho_num = float(rho_sym)

# Check E[X₁|X₂] = 3.7 - 0.15X₂
# For X₂ = 0:
X2_test = 0
E_X1_given_X2 = mu_1_num + rho_num * (sigma_1_num / sigma_2_num) * (X2_test - mu_2_num)
expected = 3.7 - 0.15 * X2_test
print(f"E[X₁|X₂={X2_test}] = {E_X1_given_X2:.10f}")
print(f"Expected: {expected:.10f}")
print(f"Match: {np.isclose(E_X1_given_X2, expected)}")

# For X₂ = 10:
X2_test = 10
E_X1_given_X2 = mu_1_num + rho_num * (sigma_1_num / sigma_2_num) * (X2_test - mu_2_num)
expected = 3.7 - 0.15 * X2_test
print(f"\nE[X₁|X₂={X2_test}] = {E_X1_given_X2:.10f}")
print(f"Expected: {expected:.10f}")
print(f"Match: {np.isclose(E_X1_given_X2, expected)}")

# Check E[X₂|X₁] = 0.4 - 0.6X₁
# For X₁ = 0:
X1_test = 0
E_X2_given_X1 = mu_2_num + rho_num * (sigma_2_num / sigma_1_num) * (X1_test - mu_1_num)
expected = 0.4 - 0.6 * X1_test
print(f"\nE[X₂|X₁={X1_test}] = {E_X2_given_X1:.10f}")
print(f"Expected: {expected:.10f}")
print(f"Match: {np.isclose(E_X2_given_X1, expected)}")

# For X₁ = 5:
X1_test = 5
E_X2_given_X1 = mu_2_num + rho_num * (sigma_2_num / sigma_1_num) * (X1_test - mu_1_num)
expected = 0.4 - 0.6 * X1_test
print(f"\nE[X₂|X₁={X1_test}] = {E_X2_given_X1:.10f}")
print(f"Expected: {expected:.10f}")
print(f"Match: {np.isclose(E_X2_given_X1, expected)}")

# Check Var(X₂|X₁)
var_X2_given_X1_calc = sigma_2_num**2 * (1 - rho_num**2)
print(f"\nVar(X₂|X₁) = σ₂²(1 - ρ²) = {var_X2_given_X1_calc:.10f}")
print(f"Expected: {var_X2_given_X1:.10f}")
print(f"Match: {np.isclose(var_X2_given_X1_calc, var_X2_given_X1)}")

# Monte Carlo verification
print("\n" + "="*60)
print("MONTE CARLO VERIFICATION:")
print("="*60)

np.random.seed(123456)
n_samples = 1000000

cov_12 = rho_num * sigma_1_num * sigma_2_num
mean = [mu_1_num, mu_2_num]
cov_matrix = [[sigma2_1, cov_12],
              [cov_12, sigma2_2]]

samples = np.random.multivariate_normal(mean, cov_matrix, n_samples)
X1_samples = samples[:, 0]
X2_samples = samples[:, 1]

print(f"Sample size: n = {n_samples}")
print(f"\nSample statistics:")
print(f"E[X₁] = {np.mean(X1_samples):.6f}, True: {mu_1_num:.6f}")
print(f"E[X₂] = {np.mean(X2_samples):.6f}, True: {mu_2_num:.6f}")
print(f"Var(X₁) = {np.var(X1_samples, ddof=1):.6f}, True: {sigma2_1:.6f}")
print(f"Var(X₂) = {np.var(X2_samples, ddof=1):.6f}, True: {sigma2_2:.6f}")
print(f"Corr(X₁,X₂) = {np.corrcoef(X1_samples, X2_samples)[0,1]:.6f}, True: {rho_num:.6f}")

print("\n" + "="*60)
print("FINAL ANSWERS:")
print("="*60)
print(f"μ₁ = {mu_1_sym} = {mu_1_num}")
print(f"σ₁² = {sp.simplify(sigma2_1_sym)} = {sigma2_1}")
print(f"μ₂ = {mu_2_sym} = {mu_2_num}")
print(f"σ₂² = {sp.simplify(sigma2_2_sym)} = {sigma2_2}")
print(f"ρ = {rho_sym} = {rho_num}")

