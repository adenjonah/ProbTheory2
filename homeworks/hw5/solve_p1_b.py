"""
Problem 1b: Find the constant a if we know aX + Y and X + 2Y are independent
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
print("Problem 1b: Find constant a for independence")
print("="*60)

print(f"\nParameters:")
print(f"σ²_X = {sigma2_X}")
print(f"σ²_Y = {sigma2_Y}")
print(f"ρ = {rho:.6f}")
print(f"Cov(X,Y) = ρσ_Xσ_Y = {cov_XY:.10f}")

# For U = aX + Y and V = X + 2Y to be independent (jointly normal),
# we need Cov(U, V) = 0
#
# Cov(aX + Y, X + 2Y) = a·Var(X) + 2a·Cov(X,Y) + Cov(X,Y) + 2·Var(Y)
#                      = a·σ²_X + (2a+1)·Cov(X,Y) + 2·σ²_Y
#
# Setting equal to 0:
# a·σ²_X + (2a+1)·ρσ_Xσ_Y + 2·σ²_Y = 0
# a·σ²_X + 2a·ρσ_Xσ_Y + ρσ_Xσ_Y + 2·σ²_Y = 0
# a(σ²_X + 2ρσ_Xσ_Y) = -(ρσ_Xσ_Y + 2σ²_Y)
# a = -(ρσ_Xσ_Y + 2σ²_Y) / (σ²_X + 2ρσ_Xσ_Y)

print("\nFor aX + Y and X + 2Y to be independent, we need Cov(aX + Y, X + 2Y) = 0")
print("\nCov(aX + Y, X + 2Y) = a·Var(X) + 2a·Cov(X,Y) + Cov(X,Y) + 2·Var(Y)")
print("                    = a·σ²_X + (2a+1)·Cov(X,Y) + 2·σ²_Y")

numerator = -(cov_XY + 2*sigma2_Y)
denominator = sigma2_X + 2*cov_XY
a = numerator / denominator

print(f"\nSetting equal to 0:")
print(f"a·σ²_X + (2a+1)·Cov(X,Y) + 2·σ²_Y = 0")
print(f"a(σ²_X + 2·Cov(X,Y)) = -(Cov(X,Y) + 2·σ²_Y)")
print(f"a = -(Cov(X,Y) + 2·σ²_Y) / (σ²_X + 2·Cov(X,Y))")
print(f"  = -({cov_XY:.10f} + 2·{sigma2_Y}) / ({sigma2_X} + 2·{cov_XY:.10f})")
print(f"  = {numerator:.10f} / {denominator:.10f}")
print(f"  = {a:.10f}")

# Exact symbolic computation
print("\n" + "="*60)
print("EXACT SYMBOLIC COMPUTATION:")
print("="*60)

sigma2_X_sym = sp.Rational(2)
sigma2_Y_sym = sp.Rational(3)
rho_sym = sp.Rational(-2, 3)
sigma_X_sym = sp.sqrt(sigma2_X_sym)
sigma_Y_sym = sp.sqrt(sigma2_Y_sym)
cov_XY_sym = rho_sym * sigma_X_sym * sigma_Y_sym

a_sym = -(cov_XY_sym + 2*sigma2_Y_sym) / (sigma2_X_sym + 2*cov_XY_sym)
a_simplified = sp.simplify(a_sym)

print(f"Cov(X,Y) = {cov_XY_sym} = {sp.simplify(cov_XY_sym)}")
print(f"a = -(Cov(X,Y) + 2σ²_Y) / (σ²_X + 2Cov(X,Y))")
print(f"  = {a_sym}")
print(f"  = {a_simplified}")

a_numeric = float(a_simplified)
print(f"\nNumerical value: {a_numeric:.10f}")
print(f"Direct calculation: {a:.10f}")
print(f"Difference: {abs(a_numeric - a):.2e}")

# Verification: check that Cov(aX + Y, X + 2Y) = 0
cov_check = a*sigma2_X + (2*a + 1)*cov_XY + 2*sigma2_Y
print("\n" + "="*60)
print("VERIFICATION:")
print("="*60)
print(f"Cov(aX + Y, X + 2Y) = a·σ²_X + (2a+1)·Cov(X,Y) + 2·σ²_Y")
print(f"                    = {a:.10f}·{sigma2_X} + ({2*a + 1:.10f})·{cov_XY:.10f} + 2·{sigma2_Y}")
print(f"                    = {cov_check:.15e}")
print(f"Check: |Cov| < 1e-8: {abs(cov_check) < 1e-8}")

# Monte Carlo verification
np.random.seed(123456)
n_samples = 1000000
mean = [mu_X, mu_Y]
cov_matrix = [[sigma2_X, cov_XY],
              [cov_XY, sigma2_Y]]
samples = np.random.multivariate_normal(mean, cov_matrix, n_samples)
X_samples = samples[:, 0]
Y_samples = samples[:, 1]

U_samples = a * X_samples + Y_samples
V_samples = X_samples + 2 * Y_samples

cov_UV = np.cov(U_samples, V_samples)[0, 1]
corr_UV = np.corrcoef(U_samples, V_samples)[0, 1]

print(f"\nMonte Carlo verification (n={n_samples}):")
print(f"Sample Cov(aX + Y, X + 2Y) = {cov_UV:.10e}")
print(f"Sample Corr(aX + Y, X + 2Y) = {corr_UV:.10e}")
print(f"Check: |Cov| < 1e-2: {abs(cov_UV) < 1e-2}")

print("\n" + "="*60)
print("FINAL ANSWER:")
print("="*60)
print(f"a = {a_simplified}")
print(f"  ≈ {a:.10f}")


