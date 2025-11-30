"""
Problem 3: Product of Lognormal Variables
Let X and Y be independent random variables such that log(X) has the normal 
distribution with mean 1.6 and variance 4.5 and log(Y) has the normal 
distribution with mean 3 and variance 6. Find the mean of the product XY 
and the probability that XY > 10. Use simulation to evaluate the probability.
"""
import numpy as np
from scipy import stats
import sympy as sp

print("="*60)
print("Problem 3: Product of Lognormal Variables")
print("="*60)

# Parameters
mu_X = 1.6
sigma2_X = 4.5
sigma_X = np.sqrt(sigma2_X)

mu_Y = 3.0
sigma2_Y = 6.0
sigma_Y = np.sqrt(sigma2_Y)

print(f"\nParameters:")
print(f"log(X) ~ N(μ_X={mu_X}, σ²_X={sigma2_X}), σ_X={sigma_X:.6f}")
print(f"log(Y) ~ N(μ_Y={mu_Y}, σ²_Y={sigma2_Y}), σ_Y={sigma_Y:.6f}")
print(f"X and Y are independent")

# Since X and Y are independent:
# log(XY) = log(X) + log(Y) ~ N(μ_X + μ_Y, σ²_X + σ²_Y)
mu_XY = mu_X + mu_Y
sigma2_XY = sigma2_X + sigma2_Y
sigma_XY = np.sqrt(sigma2_XY)

print(f"\nSince X and Y are independent:")
print(f"log(XY) = log(X) + log(Y) ~ N(μ_XY, σ²_XY)")
print(f"μ_XY = μ_X + μ_Y = {mu_X} + {mu_Y} = {mu_XY}")
print(f"σ²_XY = σ²_X + σ²_Y = {sigma2_X} + {sigma2_Y} = {sigma2_XY}")
print(f"σ_XY = {sigma_XY:.6f}")

# Mean of XY
# For lognormal Z with parameters (μ, σ²): E[Z] = exp(μ + σ²/2)
mean_XY = np.exp(mu_XY + sigma2_XY/2)

print(f"\nMean of XY:")
print(f"For lognormal variable with parameters (μ, σ²):")
print(f"E[XY] = exp(μ_XY + σ²_XY/2)")
print(f"      = exp({mu_XY} + {sigma2_XY}/2)")
print(f"      = exp({mu_XY + sigma2_XY/2})")
print(f"      = {mean_XY:.10f}")

# Theoretical probability P(XY > 10)
# P(XY > 10) = P(log(XY) > log(10))
# = P((log(XY) - μ_XY)/σ_XY > (log(10) - μ_XY)/σ_XY)
# = 1 - Φ((log(10) - μ_XY)/σ_XY)

log10 = np.log(10)
z_score = (log10 - mu_XY) / sigma_XY
prob_theoretical = 1 - stats.norm.cdf(z_score)

print(f"\nTheoretical P(XY > 10):")
print(f"P(XY > 10) = P(log(XY) > log(10))")
print(f"           = P(log(XY) > {log10:.10f})")
print(f"           = 1 - Φ((log(10) - μ_XY) / σ_XY)")
print(f"           = 1 - Φ(({log10:.10f} - {mu_XY}) / {sigma_XY:.6f})")
print(f"           = 1 - Φ({z_score:.10f})")
print(f"           = {prob_theoretical:.10f}")

# SIMULATION (as requested)
print("\n" + "="*60)
print("SIMULATION:")
print("="*60)

np.random.seed(123456)
n_samples = 10000000

# Generate log(X) and log(Y) samples
log_X_samples = np.random.normal(mu_X, sigma_X, n_samples)
log_Y_samples = np.random.normal(mu_Y, sigma_Y, n_samples)

# Compute X and Y
X_samples = np.exp(log_X_samples)
Y_samples = np.exp(log_Y_samples)

# Compute XY
XY_samples = X_samples * Y_samples

# Compute mean
mean_XY_sim = np.mean(XY_samples)

# Compute P(XY > 10)
prob_sim = np.mean(XY_samples > 10)

print(f"Sample size: n = {n_samples}")
print(f"\nMean of XY:")
print(f"  Simulation:  {mean_XY_sim:.10f}")
print(f"  Theoretical: {mean_XY:.10f}")
print(f"  Difference:  {abs(mean_XY_sim - mean_XY):.6e}")
print(f"  Relative error: {abs(mean_XY_sim - mean_XY)/mean_XY:.6e}")

print(f"\nP(XY > 10):")
print(f"  Simulation:  {prob_sim:.10f}")
print(f"  Theoretical: {prob_theoretical:.10f}")
print(f"  Difference:  {abs(prob_sim - prob_theoretical):.6e}")

# Exact symbolic computation
print("\n" + "="*60)
print("EXACT SYMBOLIC COMPUTATION:")
print("="*60)

mu_X_sym = sp.Rational(16, 10)  # 1.6
sigma2_X_sym = sp.Rational(45, 10)  # 4.5
mu_Y_sym = sp.Rational(3)
sigma2_Y_sym = sp.Rational(6)

mu_XY_sym = mu_X_sym + mu_Y_sym
sigma2_XY_sym = sigma2_X_sym + sigma2_Y_sym

mean_XY_sym = sp.exp(mu_XY_sym + sigma2_XY_sym/2)

print(f"μ_XY = {mu_XY_sym}")
print(f"σ²_XY = {sigma2_XY_sym}")
print(f"E[XY] = exp(μ_XY + σ²_XY/2)")
print(f"      = exp({mu_XY_sym} + {sigma2_XY_sym}/2)")
print(f"      = exp({sp.simplify(mu_XY_sym + sigma2_XY_sym/2)})")
print(f"      = {mean_XY_sym}")

mean_XY_numeric = float(mean_XY_sym)
print(f"\nNumerical from symbolic: {mean_XY_numeric:.10f}")
print(f"Direct numerical:        {mean_XY:.10f}")
print(f"Difference: {abs(mean_XY_numeric - mean_XY):.2e}")

# Additional sample statistics
print("\n" + "="*60)
print("ADDITIONAL SAMPLE STATISTICS:")
print("="*60)

print(f"Median of XY (simulation): {np.median(XY_samples):.6f}")
print(f"Median of XY (theoretical): {np.exp(mu_XY):.6f}")

print(f"Std of XY (simulation): {np.std(XY_samples):.6f}")
# For lognormal: Var = (exp(σ²) - 1) * exp(2μ + σ²)
var_XY_theoretical = (np.exp(sigma2_XY) - 1) * np.exp(2*mu_XY + sigma2_XY)
std_XY_theoretical = np.sqrt(var_XY_theoretical)
print(f"Std of XY (theoretical): {std_XY_theoretical:.6f}")

print(f"\nPercentiles of XY:")
for p in [25, 50, 75, 90, 95, 99]:
    sim_percentile = np.percentile(XY_samples, p)
    print(f"  {p}th percentile: {sim_percentile:.6f}")

print("\n" + "="*60)
print("VERIFICATION:")
print("="*60)
print(f"Mean check: |simulation - theoretical| / theoretical")
print(f"          = {abs(mean_XY_sim - mean_XY)/mean_XY:.6e}")
print(f"          < 0.01: {abs(mean_XY_sim - mean_XY)/mean_XY < 0.01}")

print(f"\nProbability check: |simulation - theoretical|")
print(f"                 = {abs(prob_sim - prob_theoretical):.6e}")
print(f"                 < 1e-3: {abs(prob_sim - prob_theoretical) < 1e-3}")

print("\n" + "="*60)
print("FINAL ANSWERS:")
print("="*60)
print(f"Mean of XY: {mean_XY:.10f}")
print(f"          ≈ {mean_XY:.2f}")
print(f"\nP(XY > 10) (simulation): {prob_sim:.10f}")
print(f"                       ≈ {prob_sim:.6f}")
print(f"\nRandom seed: 123456")

