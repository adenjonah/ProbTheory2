"""
Problem 6: Bayesian posterior with non-uniform prior
Proportion θ of defective items is unknown.
Prior: ξ(θ) = 2(1-θ) for θ ∈ (0, 1)
Data: 8 items selected, 3 defective
Find: Posterior distribution of θ
"""
import numpy as np
from scipy import stats, integrate
import sympy as sp
from fractions import Fraction

print("=" * 60)
print("PROBLEM 6: BAYESIAN POSTERIOR WITH NON-UNIFORM PRIOR")
print("=" * 60)

# Prior: ξ(θ) = 2(1-θ) for θ ∈ (0, 1)
# This is Beta(1, 2) since Beta(α, β) has pdf ∝ θ^(α-1) (1-θ)^(β-1)
# With α = 1, β = 2: pdf ∝ θ^0 (1-θ)^1 = (1-θ)
# Normalized: B(1,2) = Γ(1)Γ(2)/Γ(3) = 1×1/2 = 1/2
# So pdf = (1/B(1,2)) (1-θ) = 2(1-θ) ✓

print("\nPrior: ξ(θ) = 2(1-θ) for θ ∈ (0, 1)")
print("       This is Beta(1, 2)")
print("       Check: Beta(1,2) has pdf = (1/B(1,2)) θ^0 (1-θ)^1 = 2(1-θ) ✓")

# Likelihood: P(X = 3 | θ) where X ~ Binomial(8, θ)
# L(θ) = C(8,3) θ³ (1-θ)⁵

print("\nLikelihood: P(3 defective out of 8 | θ) = C(8,3) θ³ (1-θ)⁵")
print("           L(θ) ∝ θ³ (1-θ)⁵")

# Posterior ∝ Prior × Likelihood
# f(θ | data) ∝ 2(1-θ) × θ³ (1-θ)⁵
#            ∝ θ³ (1-θ)⁶

print("\nPosterior ∝ Prior × Likelihood")
print("          ∝ 2(1-θ) × θ³ (1-θ)⁵")
print("          ∝ θ³ (1-θ)⁶")

# This is the kernel of Beta(α, β) with α = 3+1 = 4, β = 6+1 = 7
# (Since Beta has pdf ∝ θ^(α-1) (1-θ)^(β-1))

print("\nRecognizing the Beta kernel:")
print("θ³ (1-θ)⁶ = θ^(4-1) (1-θ)^(7-1)")
print("\nTherefore: θ | data ~ Beta(4, 7)")

alpha_post = 4
beta_post = 7

# Compute normalization constant
from math import factorial
B_4_7 = factorial(3) * factorial(6) / factorial(10)
print(f"\nNormalization: ∫₀¹ θ³ (1-θ)⁶ dθ = B(4,7) = 3!6!/10! = {factorial(3)*factorial(6)}/{factorial(10)}")
print(f"             = {Fraction(factorial(3)*factorial(6), factorial(10))}")

print("\n" + "-" * 60)
print("POSTERIOR DISTRIBUTION")
print("-" * 60)

print(f"\nθ | data ~ Beta({alpha_post}, {beta_post})")

# Posterior pdf
norm_const = round(1 / B_4_7)
print(f"\nPosterior pdf: f(θ | data) = (1/B({alpha_post},{beta_post})) × θ³ × (1-θ)⁶")
print(f"             = {norm_const} × θ³ × (1-θ)⁶  for θ ∈ (0, 1)")

# Also compute mean and variance for completeness
mean_post = alpha_post / (alpha_post + beta_post)
var_post = (alpha_post * beta_post) / ((alpha_post + beta_post)**2 * (alpha_post + beta_post + 1))

print("\n" + "-" * 60)
print("ADDITIONAL: MEAN AND VARIANCE (not asked but useful)")
print("-" * 60)
print(f"E[θ | data] = {alpha_post} / ({alpha_post} + {beta_post}) = {Fraction(alpha_post, alpha_post + beta_post)} ≈ {mean_post:.6f}")
print(f"Var(θ | data) = {alpha_post}×{beta_post} / [{(alpha_post+beta_post)}² × {alpha_post+beta_post+1}]")
print(f"             = {alpha_post*beta_post} / {(alpha_post+beta_post)**2 * (alpha_post+beta_post+1)}")
print(f"             = {Fraction(alpha_post*beta_post, (alpha_post+beta_post)**2 * (alpha_post+beta_post+1))} ≈ {var_post:.6f}")

print("\n" + "=" * 60)
print("VERIFICATION")
print("=" * 60)

# Use scipy to verify
beta_dist = stats.beta(alpha_post, beta_post)
print(f"\nUsing scipy.stats.beta({alpha_post}, {beta_post}):")
print(f"Mean = {beta_dist.mean():.8f}")
print(f"Var = {beta_dist.var():.8f}")

# Numerical integration check for prior
def prior_pdf(theta):
    return 2 * (1 - theta)

prior_integral, _ = integrate.quad(prior_pdf, 0, 1)
print(f"\nPrior check: ∫₀¹ 2(1-θ) dθ = {prior_integral:.6f} (should be 1)")

# Numerical integration for posterior (unnormalized)
def posterior_unnorm(theta):
    return theta**3 * (1 - theta)**6

post_integral, _ = integrate.quad(posterior_unnorm, 0, 1)
print(f"Posterior normalization: ∫₀¹ θ³(1-θ)⁶ dθ = {post_integral:.10f}")
print(f"Expected B(4,7) = {B_4_7:.10f}")
print(f"Ratio (should be 1): {post_integral/B_4_7:.10f}")

# Verify posterior integrates to 1
def posterior_pdf(theta):
    return norm_const * theta**3 * (1 - theta)**6

post_pdf_integral, _ = integrate.quad(posterior_pdf, 0, 1)
print(f"\nPosterior pdf check: ∫₀¹ {norm_const} θ³(1-θ)⁶ dθ = {post_pdf_integral:.10f} (should be 1)")

print("\n" + "-" * 60)
print("SUMMARY")
print("-" * 60)
print(f"\nPosterior: θ | data ~ Beta(4, 7)")
print(f"Posterior pdf: f(θ | data) = 840 θ³ (1-θ)⁶ for θ ∈ (0, 1)")

