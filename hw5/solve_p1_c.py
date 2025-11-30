"""
Problem 1c: Find P(X + Y > 0 | 2X - Y = 0)
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
cov_XY = rho * sigma_X * sigma_Y

print("="*60)
print("Problem 1c: Find P(X + Y > 0 | 2X - Y = 0)")
print("="*60)

print(f"\nParameters:")
print(f"μ_X = {mu_X}, σ²_X = {sigma2_X}")
print(f"μ_Y = {mu_Y}, σ²_Y = {sigma2_Y}")
print(f"ρ = {rho:.6f}")
print(f"Cov(X,Y) = {cov_XY:.10f}")

# Let U = X + Y and V = 2X - Y
# We need P(U > 0 | V = 0)

# First, compute the joint distribution of (U, V)
mu_U = mu_X + mu_Y
mu_V = 2*mu_X - mu_Y

# Var(U) = Var(X + Y)
var_U = sigma2_X + sigma2_Y + 2*cov_XY

# Var(V) = Var(2X - Y)
var_V = 4*sigma2_X + sigma2_Y - 4*cov_XY

# Cov(U, V) = Cov(X + Y, 2X - Y)
cov_UV = 2*sigma2_X - sigma2_Y + (2 - 1)*cov_XY

print("\nLet U = X + Y and V = 2X - Y")
print(f"μ_U = μ_X + μ_Y = {mu_X} + ({mu_Y}) = {mu_U}")
print(f"μ_V = 2μ_X - μ_Y = 2({mu_X}) - ({mu_Y}) = {mu_V}")

print(f"\nVar(U) = σ²_X + σ²_Y + 2Cov(X,Y)")
print(f"       = {sigma2_X} + {sigma2_Y} + 2({cov_XY:.10f})")
print(f"       = {var_U:.10f}")

print(f"\nVar(V) = 4σ²_X + σ²_Y - 4Cov(X,Y)")
print(f"       = 4({sigma2_X}) + {sigma2_Y} - 4({cov_XY:.10f})")
print(f"       = {var_V:.10f}")

print(f"\nCov(U,V) = Cov(X+Y, 2X-Y)")
print(f"         = 2Var(X) - Var(Y) + (2-1)Cov(X,Y)")
print(f"         = 2({sigma2_X}) - {sigma2_Y} + {cov_XY:.10f}")
print(f"         = {cov_UV:.10f}")

# Conditional distribution: U | V = 0
# E[U | V = 0] = E[U] + Cov(U,V)/Var(V) * (0 - E[V])
mu_U_given_V0 = mu_U + (cov_UV / var_V) * (0 - mu_V)

# Var(U | V = 0) = Var(U) - Cov(U,V)²/Var(V)
var_U_given_V0 = var_U - (cov_UV**2) / var_V
sigma_U_given_V0 = np.sqrt(var_U_given_V0)

print("\n" + "="*60)
print("CONDITIONAL DISTRIBUTION: U | V = 0")
print("="*60)

print(f"\nE[U | V = 0] = E[U] + Cov(U,V)/Var(V) * (0 - E[V])")
print(f"             = {mu_U} + ({cov_UV:.10f}/{var_V:.10f}) * (0 - {mu_V})")
print(f"             = {mu_U} + {cov_UV/var_V:.10f} * ({-mu_V})")
print(f"             = {mu_U_given_V0:.10f}")

print(f"\nVar(U | V = 0) = Var(U) - Cov(U,V)²/Var(V)")
print(f"               = {var_U:.10f} - ({cov_UV:.10f})² / {var_V:.10f}")
print(f"               = {var_U_given_V0:.10f}")
print(f"σ(U | V = 0) = {sigma_U_given_V0:.10f}")

# P(U > 0 | V = 0)
z_score = (0 - mu_U_given_V0) / sigma_U_given_V0
prob = 1 - stats.norm.cdf(z_score)

print(f"\nP(U > 0 | V = 0) = P(X + Y > 0 | 2X - Y = 0)")
print(f"                 = 1 - Φ((0 - {mu_U_given_V0:.10f})/{sigma_U_given_V0:.10f})")
print(f"                 = 1 - Φ({z_score:.10f})")
print(f"                 = {prob:.10f}")

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
cov_XY_sym = rho_sym * sigma_X_sym * sigma_Y_sym

mu_U_sym = mu_X_sym + mu_Y_sym
mu_V_sym = 2*mu_X_sym - mu_Y_sym

var_U_sym = sigma2_X_sym + sigma2_Y_sym + 2*cov_XY_sym
var_V_sym = 4*sigma2_X_sym + sigma2_Y_sym - 4*cov_XY_sym
cov_UV_sym = 2*sigma2_X_sym - sigma2_Y_sym + cov_XY_sym

mu_U_given_V0_sym = mu_U_sym + (cov_UV_sym / var_V_sym) * (0 - mu_V_sym)
var_U_given_V0_sym = var_U_sym - (cov_UV_sym**2) / var_V_sym

print(f"Cov(X,Y) = {sp.simplify(cov_XY_sym)}")
print(f"μ_U = {mu_U_sym}")
print(f"μ_V = {mu_V_sym}")
print(f"Var(U) = {sp.simplify(var_U_sym)}")
print(f"Var(V) = {sp.simplify(var_V_sym)}")
print(f"Cov(U,V) = {sp.simplify(cov_UV_sym)}")
print(f"\nE[U | V = 0] = {sp.simplify(mu_U_given_V0_sym)}")
print(f"Var(U | V = 0) = {sp.simplify(var_U_given_V0_sym)}")

sigma_U_given_V0_sym = sp.sqrt(var_U_given_V0_sym)
z_score_sym = -mu_U_given_V0_sym / sigma_U_given_V0_sym

print(f"σ(U | V = 0) = {sp.simplify(sigma_U_given_V0_sym)}")
print(f"z-score = {sp.simplify(z_score_sym)}")

# Numerical verification
mu_U_given_V0_numeric = float(mu_U_given_V0_sym)
z_score_numeric = float(z_score_sym)

print(f"\nNumerical verification:")
print(f"E[U|V=0] (symbolic→numeric): {mu_U_given_V0_numeric:.10f}")
print(f"E[U|V=0] (direct):            {mu_U_given_V0:.10f}")
print(f"Difference: {abs(mu_U_given_V0_numeric - mu_U_given_V0):.2e}")

print(f"\nz-score (symbolic→numeric): {z_score_numeric:.10f}")
print(f"z-score (direct):           {z_score:.10f}")
print(f"Difference: {abs(z_score_numeric - z_score):.2e}")

# Monte Carlo verification
print("\n" + "="*60)
print("VERIFICATION:")
print("="*60)

np.random.seed(123456)
n_samples = 10000000
mean = [mu_X, mu_Y]
cov_matrix = [[sigma2_X, cov_XY],
              [cov_XY, sigma2_Y]]
samples = np.random.multivariate_normal(mean, cov_matrix, n_samples)
X_samples = samples[:, 0]
Y_samples = samples[:, 1]

U_samples = X_samples + Y_samples
V_samples = 2*X_samples - Y_samples

# Condition on V ≈ 0 (within tolerance)
tolerance = 0.1
mask = np.abs(V_samples) < tolerance
U_conditional = U_samples[mask]

if len(U_conditional) > 0:
    prob_mc = np.mean(U_conditional > 0)
    print(f"Monte Carlo (n={len(U_conditional)} samples with |V| < {tolerance}):")
    print(f"P(U > 0 | |V| < {tolerance}) = {prob_mc:.10f}")
    print(f"Theoretical P(U > 0 | V = 0) = {prob:.10f}")
    print(f"Difference: {abs(prob_mc - prob):.2e}")
    print(f"Check: |difference| < 5e-3: {abs(prob_mc - prob) < 5e-3}")
else:
    print("No samples found in conditional region")

print("\n" + "="*60)
print("FINAL ANSWER:")
print("="*60)
print(f"P(X + Y > 0 | 2X - Y = 0) = {prob:.10f}")
print(f"                          ≈ {prob:.6f}")

