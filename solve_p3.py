#!/usr/bin/env python3
"""
Problem 3: Correlation analysis for binary random variables
"""

import sympy as sp
from sympy import symbols, sqrt, simplify, Rational, solve

print("=== PROBLEM 3: Correlation ===")
print("X and Y are random variables with:")
print("P(X = 1) = P(X = -1) = 1/2")
print("P(Y = 1) = P(Y = -1) = 1/2")
print("Let c = P(X = 1 and Y = 1)")
print()

# Define symbol
c = symbols('c', real=True)

print("=== Part (a): Joint distribution, Cov(X,Y), and Cor(X,Y) ===")

# Joint distribution
print("Joint distribution:")
print("P(X = 1, Y = 1) = c")
print("P(X = 1, Y = -1) = P(X = 1) - P(X = 1, Y = 1) = 1/2 - c")
print("P(X = -1, Y = 1) = P(Y = 1) - P(X = 1, Y = 1) = 1/2 - c")
print("P(X = -1, Y = -1) = 1 - c - (1/2 - c) - (1/2 - c) = 1 - 1/2 - 1/2 + c = c")
print()

# Verify probabilities sum to 1
total_prob = c + (Rational(1,2) - c) + (Rational(1,2) - c) + c
total_simplified = simplify(total_prob)
print(f"Total probability: {total_simplified}")
print()

# Calculate E[X], E[Y], E[XY]
print("Expected values:")
E_X = 1 * Rational(1,2) + (-1) * Rational(1,2)
E_Y = 1 * Rational(1,2) + (-1) * Rational(1,2)
print(f"E[X] = 1 * (1/2) + (-1) * (1/2) = {E_X}")
print(f"E[Y] = 1 * (1/2) + (-1) * (1/2) = {E_Y}")
print()

# E[XY]
E_XY = (1 * 1 * c + 
        1 * (-1) * (Rational(1,2) - c) + 
        (-1) * 1 * (Rational(1,2) - c) + 
        (-1) * (-1) * c)
E_XY_simplified = simplify(E_XY)
print(f"E[XY] = 1*1*c + 1*(-1)*(1/2-c) + (-1)*1*(1/2-c) + (-1)*(-1)*c")
print(f"      = c - (1/2-c) - (1/2-c) + c")
print(f"      = c - 1/2 + c - 1/2 + c + c")
print(f"      = 4c - 1")
print(f"E[XY] = {E_XY_simplified}")
print()

# Covariance
Cov_XY = E_XY_simplified - E_X * E_Y
Cov_XY_simplified = simplify(Cov_XY)
print(f"Cov(X,Y) = E[XY] - E[X]E[Y] = {E_XY_simplified} - {E_X} * {E_Y} = {Cov_XY_simplified}")
print()

# Variance calculations
print("Variance calculations:")
E_X2 = 1**2 * Rational(1,2) + (-1)**2 * Rational(1,2)
E_Y2 = 1**2 * Rational(1,2) + (-1)**2 * Rational(1,2)
Var_X = E_X2 - E_X**2
Var_Y = E_Y2 - E_Y**2
print(f"E[X²] = 1² * (1/2) + (-1)² * (1/2) = {E_X2}")
print(f"E[Y²] = 1² * (1/2) + (-1)² * (1/2) = {E_Y2}")
print(f"Var(X) = E[X²] - (E[X])² = {E_X2} - ({E_X})² = {Var_X}")
print(f"Var(Y) = E[Y²] - (E[Y])² = {E_Y2} - ({E_Y})² = {Var_Y}")
print()

# Correlation
Cor_XY = Cov_XY_simplified / sqrt(Var_X * Var_Y)
Cor_XY_simplified = simplify(Cor_XY)
print(f"Cor(X,Y) = Cov(X,Y) / √(Var(X)Var(Y)) = {Cov_XY_simplified} / √({Var_X} * {Var_Y})")
print(f"         = {Cov_XY_simplified} / √{Var_X * Var_Y} = {Cov_XY_simplified} / 1")
print(f"Cor(X,Y) = {Cor_XY_simplified}")
print()

print("=== Part (b): Independence and perfect correlation ===")

# Independence: Cov(X,Y) = 0
print("For independence, we need Cov(X,Y) = 0:")
independence_eq = sp.Eq(Cov_XY_simplified, 0)
c_independent = solve(independence_eq, c)
print(f"{Cov_XY_simplified} = 0")
print(f"c = {c_independent[0]}")
print()

# Perfect correlation: |Cor(X,Y)| = 1
print("For 100% correlation, we need |Cor(X,Y)| = 1:")
print(f"|{Cor_XY_simplified}| = 1")
print(f"|4c - 1| = 1")
print("This gives us: 4c - 1 = 1 or 4c - 1 = -1")
perfect_corr_pos = solve(sp.Eq(4*c - 1, 1), c)
perfect_corr_neg = solve(sp.Eq(4*c - 1, -1), c)
print(f"4c - 1 = 1  ⟹  c = {perfect_corr_pos[0]}")
print(f"4c - 1 = -1 ⟹  c = {perfect_corr_neg[0]}")
print()

# Verify constraints on c
print("Constraint verification:")
print("Since c = P(X=1, Y=1), we need 0 ≤ c ≤ 1")
print("Also, P(X=1, Y=-1) = 1/2 - c ≥ 0, so c ≤ 1/2")
print("And P(X=-1, Y=1) = 1/2 - c ≥ 0, so c ≤ 1/2")
print("Therefore: 0 ≤ c ≤ 1/2")
print()
print(f"Independence: c = {c_independent[0]} = {float(c_independent[0])} ✓ (within [0, 1/2])")
print(f"Perfect positive correlation: c = {perfect_corr_pos[0]} = {float(perfect_corr_pos[0])} ✓ (within [0, 1/2])")
print(f"Perfect negative correlation: c = {perfect_corr_neg[0]} = {float(perfect_corr_neg[0])} ✓ (within [0, 1/2])")

print()
print("=== VERIFICATION ===")
# Test specific values
test_values = [Rational(1,4), Rational(1,2), 0]
for c_val in test_values:
    cov_val = Cov_XY_simplified.subs(c, c_val)
    cor_val = Cor_XY_simplified.subs(c, c_val)
    print(f"c = {c_val}: Cov(X,Y) = {cov_val} = {float(cov_val):.3f}, Cor(X,Y) = {cor_val} = {float(cor_val):.3f}")
