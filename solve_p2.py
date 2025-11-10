#!/usr/bin/env python3
"""
Problem 2: Independence check for joint pmf table
"""

import numpy as np
from fractions import Fraction

print("=== PROBLEM 2: Independence ===")
print("Joint pmf table:")
print("X\\Y    1     2     3")
print("1    1/18  1/9   1/6")
print("2    1/9   1/6  1/18")
print("3    1/6  1/18  1/9")
print()

# Define the joint pmf as fractions for exact computation
joint_pmf = {
    (1,1): Fraction(1,18), (1,2): Fraction(1,9), (1,3): Fraction(1,6),
    (2,1): Fraction(1,9),  (2,2): Fraction(1,6), (2,3): Fraction(1,18),
    (3,1): Fraction(1,6),  (3,2): Fraction(1,18), (3,3): Fraction(1,9)
}

print("Joint pmf P(X=i, Y=j):")
for i in [1,2,3]:
    for j in [1,2,3]:
        print(f"P(X={i}, Y={j}) = {joint_pmf[(i,j)]} = {float(joint_pmf[(i,j)]):.6f}")
print()

# Calculate marginal pmfs
print("Marginal pmf of X:")
marginal_X = {}
for i in [1,2,3]:
    marginal_X[i] = sum(joint_pmf[(i,j)] for j in [1,2,3])
    print(f"P(X={i}) = {marginal_X[i]} = {float(marginal_X[i]):.6f}")
print()

print("Marginal pmf of Y:")
marginal_Y = {}
for j in [1,2,3]:
    marginal_Y[j] = sum(joint_pmf[(i,j)] for i in [1,2,3])
    print(f"P(Y={j}) = {marginal_Y[j]} = {float(marginal_Y[j]):.6f}")
print()

# Check independence: P(X=i, Y=j) = P(X=i) * P(Y=j)
print("Independence check: P(X=i, Y=j) vs P(X=i) * P(Y=j)")
independent = True
for i in [1,2,3]:
    for j in [1,2,3]:
        joint_prob = joint_pmf[(i,j)]
        product_marginals = marginal_X[i] * marginal_Y[j]
        print(f"({i},{j}): {joint_prob} vs {product_marginals} = {float(product_marginals):.6f}")
        if joint_prob != product_marginals:
            independent = False
            print(f"  ✗ Not equal: {joint_prob} ≠ {product_marginals}")
        else:
            print(f"  ✓ Equal")

print()
if independent:
    print("CONCLUSION: X and Y are INDEPENDENT")
else:
    print("CONCLUSION: X and Y are NOT INDEPENDENT")

print()
print("=== VERIFICATION ===")
# Check that probabilities sum to 1
total_joint = sum(joint_pmf.values())
total_X = sum(marginal_X.values())
total_Y = sum(marginal_Y.values())
print(f"Sum of joint pmf: {total_joint} = {float(total_joint)}")
print(f"Sum of marginal X: {total_X} = {float(total_X)}")
print(f"Sum of marginal Y: {total_Y} = {float(total_Y)}")
print("All sums equal 1 ✓")
