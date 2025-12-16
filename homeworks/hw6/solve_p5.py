"""
Problem 5: Bayesian posterior with uniform prior
Proportion θ of defective items is unknown.
Prior: θ ~ Uniform[0, 1]
Data: 8 items selected, 3 defective
Find: Posterior distribution, expected mean and variance of θ
"""
import numpy as np
from scipy import stats, integrate
import sympy as sp
from fractions import Fraction

print("=" * 60)
print("PROBLEM 5: BAYESIAN POSTERIOR WITH UNIFORM PRIOR")
print("=" * 60)

# Prior: θ ~ Uniform[0, 1], so ξ(θ) = 1 for θ ∈ [0, 1]
# This is equivalent to Beta(1, 1)

# Likelihood: P(X = 3 | θ) where X ~ Binomial(8, θ)
# L(θ) = C(8,3) θ³ (1-θ)⁵

# Posterior ∝ Prior × Likelihood
# f(θ | data) ∝ 1 × θ³ (1-θ)⁵ = θ³ (1-θ)⁵

print("\nPrior: θ ~ Uniform[0, 1] ≡ Beta(1, 1)")
print("       ξ(θ) = 1 for θ ∈ [0, 1]")

print("\nLikelihood: P(3 defective out of 8 | θ) = C(8,3) θ³ (1-θ)⁵")
print("           L(θ) ∝ θ³ (1-θ)⁵")

print("\nPosterior ∝ Prior × Likelihood")
print("          ∝ 1 × θ³ (1-θ)⁵ = θ³ (1-θ)⁵")

# This is the kernel of Beta(α, β) with α = 3+1 = 4, β = 5+1 = 6
# (Since Beta has pdf ∝ θ^(α-1) (1-θ)^(β-1))

print("\nRecognizing the Beta kernel:")
print("θ³ (1-θ)⁵ = θ^(4-1) (1-θ)^(6-1)")
print("\nTherefore: θ | data ~ Beta(4, 6)")

alpha_post = 4
beta_post = 6

# Verify normalization
# ∫₀¹ θ³ (1-θ)⁵ dθ = B(4, 6) = Γ(4)Γ(6)/Γ(10) = 3!5!/9! = 6×120/362880 = 1/504
from math import factorial
B_4_6 = factorial(3) * factorial(5) / factorial(9)
print(f"\nNormalization: ∫₀¹ θ³ (1-θ)⁵ dθ = B(4,6) = 3!5!/9! = {factorial(3)*factorial(5)}/{factorial(9)} = {B_4_6}")
print(f"             = {Fraction(factorial(3)*factorial(5), factorial(9))}")

print("\n" + "-" * 60)
print("POSTERIOR DISTRIBUTION")
print("-" * 60)

print(f"\nθ | data ~ Beta({alpha_post}, {beta_post})")
print(f"\nPosterior pdf: f(θ | data) = (1/B({alpha_post},{beta_post})) × θ³ × (1-θ)⁵")
print(f"             = {int(1/B_4_6)} × θ³ × (1-θ)⁵  for θ ∈ [0, 1]")

print("\n" + "-" * 60)
print("EXPECTED VALUE (POSTERIOR MEAN)")
print("-" * 60)

# E[θ | data] = α / (α + β) for Beta(α, β)
mean_post = alpha_post / (alpha_post + beta_post)
print(f"\nFor Beta(α, β): E[θ] = α / (α + β)")
print(f"E[θ | data] = {alpha_post} / ({alpha_post} + {beta_post}) = {alpha_post}/{alpha_post + beta_post} = {mean_post}")
print(f"            = {Fraction(alpha_post, alpha_post + beta_post)}")

print("\n" + "-" * 60)
print("VARIANCE (POSTERIOR VARIANCE)")
print("-" * 60)

# Var(θ | data) = αβ / [(α + β)² (α + β + 1)] for Beta(α, β)
var_post = (alpha_post * beta_post) / ((alpha_post + beta_post)**2 * (alpha_post + beta_post + 1))
print(f"\nFor Beta(α, β): Var(θ) = αβ / [(α + β)² (α + β + 1)]")
print(f"Var(θ | data) = ({alpha_post} × {beta_post}) / [({alpha_post} + {beta_post})² × ({alpha_post} + {beta_post} + 1)]")
print(f"             = {alpha_post * beta_post} / [{(alpha_post + beta_post)**2} × {alpha_post + beta_post + 1}]")
print(f"             = {alpha_post * beta_post} / {(alpha_post + beta_post)**2 * (alpha_post + beta_post + 1)}")
print(f"             = {Fraction(alpha_post * beta_post, (alpha_post + beta_post)**2 * (alpha_post + beta_post + 1))}")
print(f"             ≈ {var_post:.6f}")

print("\n" + "=" * 60)
print("VERIFICATION")
print("=" * 60)

# Use scipy to verify
beta_dist = stats.beta(alpha_post, beta_post)
print(f"\nUsing scipy.stats.beta({alpha_post}, {beta_post}):")
print(f"Mean = {beta_dist.mean():.8f} (expected: {mean_post})")
print(f"Var = {beta_dist.var():.8f} (expected: {var_post:.8f})")

# Numerical integration check
def posterior_unnorm(theta):
    return theta**3 * (1 - theta)**5

norm_const, _ = integrate.quad(posterior_unnorm, 0, 1)
print(f"\nNumerical integration:")
print(f"∫₀¹ θ³(1-θ)⁵ dθ = {norm_const:.10f} (expected: {B_4_6:.10f})")

# Check mean via integration
def theta_times_posterior(theta):
    return theta * posterior_unnorm(theta) / norm_const

mean_numerical, _ = integrate.quad(theta_times_posterior, 0, 1)
print(f"E[θ] via integration = {mean_numerical:.8f} (expected: {mean_post})")

print("\n" + "-" * 60)
print("SUMMARY")
print("-" * 60)
print(f"\nPosterior: θ | data ~ Beta(4, 6)")
print(f"Posterior pdf: f(θ | data) = 504 θ³ (1-θ)⁵ for θ ∈ [0, 1]")
print(f"Expected mean: E[θ | data] = 2/5 = 0.4")
print(f"Variance: Var(θ | data) = 6/275 ≈ 0.0218")

