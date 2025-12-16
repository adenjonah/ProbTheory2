"""
Problem 2: Lognormal Distribution
Let X have the lognormal distribution with parameters 3 and 1.44.
Find the probability that X ≤ 6.05.
"""
import numpy as np
from scipy import stats
import sympy as sp

print("="*60)
print("Problem 2: Lognormal Distribution")
print("="*60)

# Parameters of the lognormal distribution
# If X ~ Lognormal(μ, σ²), then log(X) ~ N(μ, σ²)
mu = 3
sigma2 = 1.44
sigma = np.sqrt(sigma2)

x_threshold = 6.05

print(f"\nParameters:")
print(f"X ~ Lognormal(μ={mu}, σ²={sigma2})")
print(f"This means: log(X) ~ N(μ={mu}, σ²={sigma2})")
print(f"σ = √{sigma2} = {sigma}")

# P(X ≤ 6.05) = P(log(X) ≤ log(6.05))
# Since log(X) ~ N(μ, σ²), we have:
# P(log(X) ≤ log(6.05)) = Φ((log(6.05) - μ) / σ)

log_threshold = np.log(x_threshold)
z_score = (log_threshold - mu) / sigma
prob = stats.norm.cdf(z_score)

print(f"\nP(X ≤ {x_threshold}) = P(log(X) ≤ log({x_threshold}))")
print(f"                     = P(log(X) ≤ {log_threshold:.10f})")
print(f"                     = Φ((log({x_threshold}) - {mu}) / {sigma})")
print(f"                     = Φ(({log_threshold:.10f} - {mu}) / {sigma})")
print(f"                     = Φ({z_score:.10f})")
print(f"                     = {prob:.10f}")

# Alternative: use scipy's lognorm directly
# Note: scipy's lognorm uses shape parameter s = σ, scale parameter = exp(μ)
prob_scipy = stats.lognorm.cdf(x_threshold, s=sigma, scale=np.exp(mu))
print(f"\nVerification using scipy.stats.lognorm:")
print(f"P(X ≤ {x_threshold}) = {prob_scipy:.10f}")
print(f"Difference: {abs(prob - prob_scipy):.2e}")

# Exact symbolic computation
print("\n" + "="*60)
print("EXACT SYMBOLIC COMPUTATION:")
print("="*60)

mu_sym = sp.Rational(3)
sigma2_sym = sp.Rational(144, 100)  # 1.44 = 144/100
sigma_sym = sp.sqrt(sigma2_sym)

x_threshold_sym = sp.Rational(605, 100)  # 6.05 = 605/100
log_threshold_sym = sp.log(x_threshold_sym)

z_score_sym = (log_threshold_sym - mu_sym) / sigma_sym

print(f"μ = {mu_sym}")
print(f"σ² = {sigma2_sym} = {sp.nsimplify(sigma2_sym)}")
print(f"σ = {sigma_sym} = {sp.simplify(sigma_sym)}")
print(f"x = {x_threshold_sym}")
print(f"log(x) = {log_threshold_sym}")
print(f"z-score = (log(x) - μ) / σ = {z_score_sym}")

z_score_simplified = sp.simplify(z_score_sym)
print(f"        = {z_score_simplified}")

# Numerical verification
z_score_numeric = float(z_score_sym)
log_threshold_numeric = float(log_threshold_sym)

print(f"\nNumerical verification:")
print(f"log({x_threshold}) (symbolic→numeric): {log_threshold_numeric:.10f}")
print(f"log({x_threshold}) (direct):           {log_threshold:.10f}")
print(f"Difference: {abs(log_threshold_numeric - log_threshold):.2e}")

print(f"\nz-score (symbolic→numeric): {z_score_numeric:.10f}")
print(f"z-score (direct):           {z_score:.10f}")
print(f"Difference: {abs(z_score_numeric - z_score):.2e}")

# Monte Carlo verification
print("\n" + "="*60)
print("VERIFICATION:")
print("="*60)

np.random.seed(123456)
n_samples = 10000000

# Generate lognormal samples
# Method 1: Generate normal samples and exponentiate
log_X_samples = np.random.normal(mu, sigma, n_samples)
X_samples = np.exp(log_X_samples)

prob_mc = np.mean(X_samples <= x_threshold)

print(f"Monte Carlo (n={n_samples}):")
print(f"P(X ≤ {x_threshold}) = {prob_mc:.10f}")
print(f"Theoretical:          {prob:.10f}")
print(f"Difference: {abs(prob_mc - prob):.2e}")
print(f"Check: |difference| < 1e-3: {abs(prob_mc - prob) < 1e-3}")

# Additional statistics
print(f"\nSample statistics:")
print(f"Mean of X: {np.mean(X_samples):.6f}")
print(f"Theoretical mean: {np.exp(mu + sigma2/2):.6f}")
print(f"Median of X: {np.median(X_samples):.6f}")
print(f"Theoretical median: {np.exp(mu):.6f}")

print("\n" + "="*60)
print("FINAL ANSWER:")
print("="*60)
print(f"P(X ≤ 6.05) = Φ({z_score:.10f})")
print(f"            = {prob:.10f}")
print(f"            ≈ {prob:.6f}")


