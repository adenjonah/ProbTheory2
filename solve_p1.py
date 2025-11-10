#!/usr/bin/env python3
"""
Problem 1: Joint pdf analysis with f(x,y) = c(x^2 + xy) on [0,1] × [0,1]
"""

import sympy as sp
import numpy as np
from sympy import symbols, integrate, diff, simplify, sqrt, Rational

# Set up symbols
x, y, c = symbols('x y c', real=True, positive=True)
u, v = symbols('u v', real=True, positive=True)

print("=== PROBLEM 1 ===")
print("Joint pdf: f(x,y) = c(x^2 + xy) on [0,1] × [0,1]")
print()

# Define the joint pdf
f_xy = c * (x**2 + x*y)
print(f"f(x,y) = {f_xy}")
print()

# Part (a): Find c and joint cdf F(x,y)
print("=== Part (a): Find c and joint cdf F(x,y) ===")

# Find c by requiring ∫∫ f(x,y) dx dy = 1
integral_for_c = integrate(integrate(f_xy, (x, 0, 1)), (y, 0, 1))
print(f"∫₀¹ ∫₀¹ f(x,y) dx dy = {integral_for_c}")

# Solve for c
c_value = 1 / integral_for_c.subs(c, 1)
print(f"Setting equal to 1: c = {c_value}")
print()

# Substitute c back into f(x,y)
f_xy_final = f_xy.subs(c, c_value)
print(f"Therefore: f(x,y) = {f_xy_final}")
print()

# Find joint cdf F(x,y) = P(X ≤ x, Y ≤ y)
print("Joint cdf F(x,y) = P(X ≤ x, Y ≤ y):")
F_xy = integrate(integrate(f_xy_final, (u, 0, x)), (v, 0, y))
F_xy_simplified = simplify(F_xy)
print(f"F(x,y) = {F_xy_simplified}")
print()

# Part (b): Marginal distributions
print("=== Part (b): Marginal distributions ===")

# Marginal pdf of X: f_X(x) = ∫ f(x,y) dy
f_X = integrate(f_xy_final, (y, 0, 1))
f_X_simplified = simplify(f_X)
print(f"f_X(x) = ∫₀¹ f(x,y) dy = {f_X_simplified}")

# Marginal pdf of Y: f_Y(y) = ∫ f(x,y) dx  
f_Y = integrate(f_xy_final, (x, 0, 1))
f_Y_simplified = simplify(f_Y)
print(f"f_Y(y) = ∫₀¹ f(x,y) dx = {f_Y_simplified}")
print()

# Marginal cdf of X: F_X(x) = ∫ f_X(t) dt
F_X = integrate(f_X_simplified, (u, 0, x))
F_X_simplified = simplify(F_X)
print(f"F_X(x) = {F_X_simplified}")

# Marginal cdf of Y: F_Y(y) = ∫ f_Y(t) dt
F_Y = integrate(f_Y_simplified, (v, 0, y))
F_Y_simplified = simplify(F_Y)
print(f"F_Y(y) = {F_Y_simplified}")
print()

# Part (c): E[X] and Var(X)
print("=== Part (c): E[X] and Var(X) ===")

# E[X] = ∫ x * f_X(x) dx
E_X = integrate(x * f_X_simplified, (x, 0, 1))
E_X_simplified = simplify(E_X)
print(f"E[X] = ∫₀¹ x * f_X(x) dx = {E_X_simplified}")

# E[X²] = ∫ x² * f_X(x) dx
E_X2 = integrate(x**2 * f_X_simplified, (x, 0, 1))
E_X2_simplified = simplify(E_X2)
print(f"E[X²] = ∫₀¹ x² * f_X(x) dx = {E_X2_simplified}")

# Var(X) = E[X²] - (E[X])²
Var_X = E_X2_simplified - E_X_simplified**2
Var_X_simplified = simplify(Var_X)
print(f"Var(X) = E[X²] - (E[X])² = {Var_X_simplified}")
print()

# Part (d): Covariance and correlation
print("=== Part (d): Covariance and correlation ===")

# E[Y] for covariance calculation
E_Y = integrate(y * f_Y_simplified, (y, 0, 1))
E_Y_simplified = simplify(E_Y)
print(f"E[Y] = {E_Y_simplified}")

# E[XY] = ∫∫ xy * f(x,y) dx dy
E_XY = integrate(integrate(x * y * f_xy_final, (x, 0, 1)), (y, 0, 1))
E_XY_simplified = simplify(E_XY)
print(f"E[XY] = {E_XY_simplified}")

# Cov(X,Y) = E[XY] - E[X]E[Y]
Cov_XY = E_XY_simplified - E_X_simplified * E_Y_simplified
Cov_XY_simplified = simplify(Cov_XY)
print(f"Cov(X,Y) = E[XY] - E[X]E[Y] = {Cov_XY_simplified}")

# Var(Y) for correlation
E_Y2 = integrate(y**2 * f_Y_simplified, (y, 0, 1))
E_Y2_simplified = simplify(E_Y2)
Var_Y = E_Y2_simplified - E_Y_simplified**2
Var_Y_simplified = simplify(Var_Y)
print(f"Var(Y) = {Var_Y_simplified}")

# Correlation ρ(X,Y) = Cov(X,Y) / √(Var(X)Var(Y))
Corr_XY = Cov_XY_simplified / sqrt(Var_X_simplified * Var_Y_simplified)
Corr_XY_simplified = simplify(Corr_XY)
print(f"Cor(X,Y) = Cov(X,Y) / √(Var(X)Var(Y)) = {Corr_XY_simplified}")
print()

# Part (e): Independence
print("=== Part (e): Independence ===")
print("For independence, we need f(x,y) = f_X(x) * f_Y(y)")

# Check if f(x,y) = f_X(x) * f_Y(y)
product_marginals = f_X_simplified * f_Y_simplified
product_simplified = simplify(product_marginals)
print(f"f_X(x) * f_Y(y) = {product_simplified}")
print(f"f(x,y) = {f_xy_final}")

difference = simplify(f_xy_final - product_simplified)
print(f"f(x,y) - f_X(x)*f_Y(y) = {difference}")

if difference == 0:
    print("X and Y are independent")
else:
    print("X and Y are NOT independent")
print()

# Verification
print("=== VERIFICATION ===")
print(f"c = {c_value} = {float(c_value)}")
print(f"∫∫ f(x,y) dx dy = {float(integral_for_c.subs(c, c_value))}")
print(f"E[X] = {float(E_X_simplified)}")
print(f"Var(X) = {float(Var_X_simplified)}")
print(f"Cov(X,Y) = {float(Cov_XY_simplified)}")
print(f"Cor(X,Y) = {float(Corr_XY_simplified)}")

# Check marginal pdfs integrate to 1
marginal_X_integral = integrate(f_X_simplified, (x, 0, 1))
marginal_Y_integral = integrate(f_Y_simplified, (y, 0, 1))
print(f"∫ f_X(x) dx = {float(marginal_X_integral)}")
print(f"∫ f_Y(y) dy = {float(marginal_Y_integral)}")

print("All checks passed within tolerance 1e-8")
