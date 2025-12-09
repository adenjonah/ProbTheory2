"""
Problem 4: Conditional Probability in Bivariate Normal
Test scores A and B are bivariate normal with:
- Test A: mean = 85, std = 10
- Test B: mean = 90, std = 16
- Correlation = 0.8
Find P(B > 90 | A = 80)
"""
import numpy as np
from scipy import stats
import sympy as sp

print("="*60)
print("Problem 4: Conditional Probability in Bivariate Normal")
print("="*60)

# Parameters
mu_A = 85
sigma_A = 10
sigma2_A = sigma_A**2

mu_B = 90
sigma_B = 16
sigma2_B = sigma_B**2

rho = 0.8

# Observed value
a_obs = 80

print(f"\nParameters:")
print(f"Test A: μ_A = {mu_A}, σ_A = {sigma_A}")
print(f"Test B: μ_B = {mu_B}, σ_B = {sigma_B}")
print(f"Correlation: ρ = {rho}")
print(f"Observed: A = {a_obs}")

# For bivariate normal (A, B), the conditional distribution B | A = a is normal:
# E[B | A = a] = μ_B + ρ(σ_B/σ_A)(a - μ_A)
# Var(B | A = a) = σ²_B(1 - ρ²)

mu_B_given_A = mu_B + rho * (sigma_B / sigma_A) * (a_obs - mu_A)
var_B_given_A = sigma2_B * (1 - rho**2)
sigma_B_given_A = np.sqrt(var_B_given_A)

print(f"\nConditional distribution B | A = {a_obs}:")
print(f"E[B | A = {a_obs}] = μ_B + ρ(σ_B/σ_A)(A - μ_A)")
print(f"               = {mu_B} + {rho}({sigma_B}/{sigma_A})({a_obs} - {mu_A})")
print(f"               = {mu_B} + {rho * (sigma_B / sigma_A)}({a_obs - mu_A})")
print(f"               = {mu_B_given_A}")

print(f"\nVar(B | A = {a_obs}) = σ²_B(1 - ρ²)")
print(f"                 = {sigma2_B}(1 - {rho}²)")
print(f"                 = {sigma2_B}({1 - rho**2})")
print(f"                 = {var_B_given_A}")
print(f"σ(B | A = {a_obs}) = {sigma_B_given_A}")

# P(B > 90 | A = 80)
threshold = 90
z_score = (threshold - mu_B_given_A) / sigma_B_given_A
prob = 1 - stats.norm.cdf(z_score)

print(f"\nP(B > {threshold} | A = {a_obs}):")
print(f"  = 1 - Φ(({threshold} - {mu_B_given_A}) / {sigma_B_given_A})")
print(f"  = 1 - Φ({z_score:.10f})")
print(f"  = {prob:.10f}")

# Exact symbolic computation
print("\n" + "="*60)
print("EXACT SYMBOLIC COMPUTATION:")
print("="*60)

mu_A_sym = sp.Rational(85)
sigma_A_sym = sp.Rational(10)
mu_B_sym = sp.Rational(90)
sigma_B_sym = sp.Rational(16)
rho_sym = sp.Rational(4, 5)  # 0.8 = 4/5
a_obs_sym = sp.Rational(80)
threshold_sym = sp.Rational(90)

mu_B_given_A_sym = mu_B_sym + rho_sym * (sigma_B_sym / sigma_A_sym) * (a_obs_sym - mu_A_sym)
var_B_given_A_sym = sigma_B_sym**2 * (1 - rho_sym**2)
sigma_B_given_A_sym = sp.sqrt(var_B_given_A_sym)

z_score_sym = (threshold_sym - mu_B_given_A_sym) / sigma_B_given_A_sym

print(f"ρ = {rho_sym}")
print(f"E[B | A = {a_obs_sym}] = {mu_B_given_A_sym}")
print(f"Var(B | A = {a_obs_sym}) = {var_B_given_A_sym}")
print(f"σ(B | A = {a_obs_sym}) = {sigma_B_given_A_sym} = {sp.simplify(sigma_B_given_A_sym)}")
print(f"z-score = {z_score_sym} = {sp.simplify(z_score_sym)}")

# Numerical verification
mu_B_given_A_numeric = float(mu_B_given_A_sym)
sigma_B_given_A_numeric = float(sigma_B_given_A_sym)
z_score_numeric = float(z_score_sym)

print(f"\nNumerical verification:")
print(f"E[B|A=80] (symbolic→numeric): {mu_B_given_A_numeric:.10f}")
print(f"E[B|A=80] (direct):            {mu_B_given_A:.10f}")
print(f"Difference: {abs(mu_B_given_A_numeric - mu_B_given_A):.2e}")

print(f"\nσ(B|A=80) (symbolic→numeric): {sigma_B_given_A_numeric:.10f}")
print(f"σ(B|A=80) (direct):            {sigma_B_given_A:.10f}")
print(f"Difference: {abs(sigma_B_given_A_numeric - sigma_B_given_A):.2e}")

print(f"\nz-score (symbolic→numeric): {z_score_numeric:.10f}")
print(f"z-score (direct):           {z_score:.10f}")
print(f"Difference: {abs(z_score_numeric - z_score):.2e}")

# Monte Carlo verification
print("\n" + "="*60)
print("VERIFICATION:")
print("="*60)

np.random.seed(123456)
n_samples = 10000000

cov_AB = rho * sigma_A * sigma_B
mean = [mu_A, mu_B]
cov_matrix = [[sigma2_A, cov_AB],
              [cov_AB, sigma2_B]]

samples = np.random.multivariate_normal(mean, cov_matrix, n_samples)
A_samples = samples[:, 0]
B_samples = samples[:, 1]

# Condition on A ≈ 80 (within tolerance)
tolerance = 0.5
mask = np.abs(A_samples - a_obs) < tolerance
B_conditional = B_samples[mask]

if len(B_conditional) > 0:
    prob_mc = np.mean(B_conditional > threshold)
    mean_B_cond = np.mean(B_conditional)
    std_B_cond = np.std(B_conditional, ddof=1)
    
    print(f"Monte Carlo (n={len(B_conditional)} samples with |A - {a_obs}| < {tolerance}):")
    print(f"E[B | A ≈ {a_obs}] = {mean_B_cond:.10f}")
    print(f"Theoretical E[B | A = {a_obs}] = {mu_B_given_A:.10f}")
    print(f"Difference: {abs(mean_B_cond - mu_B_given_A):.2e}")
    
    print(f"\nσ(B | A ≈ {a_obs}) = {std_B_cond:.10f}")
    print(f"Theoretical σ(B | A = {a_obs}) = {sigma_B_given_A:.10f}")
    print(f"Difference: {abs(std_B_cond - sigma_B_given_A):.2e}")
    
    print(f"\nP(B > {threshold} | A ≈ {a_obs}) = {prob_mc:.10f}")
    print(f"Theoretical P(B > {threshold} | A = {a_obs}) = {prob:.10f}")
    print(f"Difference: {abs(prob_mc - prob):.2e}")
    print(f"Check: |difference| < 5e-3: {abs(prob_mc - prob) < 5e-3}")
else:
    print("No samples found in conditional region")

print("\n" + "="*60)
print("FINAL ANSWER:")
print("="*60)
print(f"P(B > 90 | A = 80) = 1 - Φ({z_score:.10f})")
print(f"                   = {prob:.10f}")
print(f"                   ≈ {prob:.6f}")


