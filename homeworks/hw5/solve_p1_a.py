"""
Problem 1a: Find P(X + Y > 0)
X and Y are jointly normal with:
μ_X = 1, σ²_X = 2, μ_Y = -2, σ²_Y = 3, ρ = -2/3
"""
import numpy as np
from scipy import stats
import sympy as sp

# Parameters
mu_X = 1
sigma2_X = 2
sigma_X = np.sqrt(sigma2_X)

mu_Y = -2
sigma2_Y = 3
sigma_Y = np.sqrt(sigma2_Y)

rho = -2/3

print("="*60)
print("Problem 1a: Find P(X + Y > 0)")
print("="*60)

# For Z = X + Y, where (X,Y) is bivariate normal:
# Z is normal with:
# μ_Z = μ_X + μ_Y
# σ²_Z = σ²_X + σ²_Y + 2ρσ_Xσ_Y

mu_Z = mu_X + mu_Y
sigma2_Z = sigma2_X + sigma2_Y + 2*rho*sigma_X*sigma_Y
sigma_Z = np.sqrt(sigma2_Z)

print(f"\nParameters:")
print(f"μ_X = {mu_X}")
print(f"σ²_X = {sigma2_X}, σ_X = {sigma_X:.6f}")
print(f"μ_Y = {mu_Y}")
print(f"σ²_Y = {sigma2_Y}, σ_Y = {sigma_Y:.6f}")
print(f"ρ = {rho:.6f}")

print(f"\nZ = X + Y is normal with:")
print(f"μ_Z = μ_X + μ_Y = {mu_X} + ({mu_Y}) = {mu_Z}")
print(f"σ²_Z = σ²_X + σ²_Y + 2ρσ_Xσ_Y")
print(f"     = {sigma2_X} + {sigma2_Y} + 2({rho:.6f})({sigma_X:.6f})({sigma_Y:.6f})")
print(f"     = {sigma2_Z:.10f}")
print(f"σ_Z = {sigma_Z:.10f}")

# P(X + Y > 0) = P(Z > 0) = 1 - Φ((0 - μ_Z)/σ_Z)
z_score = (0 - mu_Z) / sigma_Z
prob = 1 - stats.norm.cdf(z_score)

print(f"\nP(X + Y > 0) = P(Z > 0)")
print(f"            = 1 - Φ((0 - μ_Z)/σ_Z)")
print(f"            = 1 - Φ((0 - ({mu_Z}))/{sigma_Z:.10f})")
print(f"            = 1 - Φ({z_score:.10f})")
print(f"            = {prob:.10f}")

# Exact symbolic computation
print("\n" + "="*60)
print("EXACT SYMBOLIC COMPUTATION:")
print("="*60)

mu_X_sym = sp.Rational(1)
sigma2_X_sym = sp.Rational(2)
mu_Y_sym = sp.Rational(-2)
sigma2_Y_sym = sp.Rational(3)
rho_sym = sp.Rational(-2, 3)

sigma_X_sym = sp.sqrt(sigma2_X_sym)
sigma_Y_sym = sp.sqrt(sigma2_Y_sym)

mu_Z_sym = mu_X_sym + mu_Y_sym
sigma2_Z_sym = sigma2_X_sym + sigma2_Y_sym + 2*rho_sym*sigma_X_sym*sigma_Y_sym
sigma_Z_sym = sp.sqrt(sigma2_Z_sym)

print(f"μ_Z = {mu_Z_sym}")
print(f"σ²_Z = {sigma2_Z_sym} = {sp.simplify(sigma2_Z_sym)}")
print(f"σ_Z = {sigma_Z_sym} = {sp.simplify(sigma_Z_sym)}")

z_score_sym = -mu_Z_sym / sigma_Z_sym
print(f"z-score = {z_score_sym} = {sp.simplify(z_score_sym)}")

# Verify numeric matches symbolic
z_score_numeric = float(z_score_sym)
sigma_Z_numeric = float(sigma_Z_sym)
print(f"\nNumerical verification:")
print(f"z-score (symbolic→numeric): {z_score_numeric:.10f}")
print(f"z-score (direct numeric):   {z_score:.10f}")
print(f"Difference: {abs(z_score_numeric - z_score):.2e}")

print(f"\nσ_Z (symbolic→numeric): {sigma_Z_numeric:.10f}")
print(f"σ_Z (direct numeric):   {sigma_Z:.10f}")
print(f"Difference: {abs(sigma_Z_numeric - sigma_Z):.2e}")

print("\n" + "="*60)
print("VERIFICATION:")
print("="*60)

# Monte Carlo verification
np.random.seed(123456)
n_samples = 10000000
mean = [mu_X, mu_Y]
cov = [[sigma2_X, rho*sigma_X*sigma_Y],
       [rho*sigma_X*sigma_Y, sigma2_Y]]
samples = np.random.multivariate_normal(mean, cov, n_samples)
X_samples = samples[:, 0]
Y_samples = samples[:, 1]
Z_samples = X_samples + Y_samples

prob_mc = np.mean(Z_samples > 0)
print(f"Monte Carlo (n={n_samples}): P(X + Y > 0) = {prob_mc:.10f}")
print(f"Theoretical:                  P(X + Y > 0) = {prob:.10f}")
print(f"Difference: {abs(prob_mc - prob):.2e}")
print(f"Check: |difference| < 1e-3: {abs(prob_mc - prob) < 1e-3}")

print("\n" + "="*60)
print("FINAL ANSWER:")
print("="*60)
print(f"P(X + Y > 0) = {prob:.10f}")
print(f"             ≈ {prob:.6f}")

