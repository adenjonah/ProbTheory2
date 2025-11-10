#!/usr/bin/env python3
"""
Problem 4: Uniform arrival times for lunch meeting
"""

import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, integrate, simplify, Rational

print("=== PROBLEM 4: Don't be late! ===")
print("A and B are independent uniform random variables on [0,60]")
print()

# Part (a): Joint pdf and cdf
print("=== Part (a): Joint pdf f(a,b) and joint cdf F(a,b) ===")

print("For uniform distribution on [0,60]:")
print("f_A(a) = 1/60 for a ∈ [0,60], 0 otherwise")
print("f_B(b) = 1/60 for b ∈ [0,60], 0 otherwise")
print()

print("Since A and B are independent:")
print("f(a,b) = f_A(a) * f_B(b) = (1/60) * (1/60) = 1/3600 for (a,b) ∈ [0,60] × [0,60]")
print()

print("Joint cdf F(a,b) = P(A ≤ a, B ≤ b):")
print("For 0 ≤ a ≤ 60 and 0 ≤ b ≤ 60:")
print("F(a,b) = ∫₀ᵃ ∫₀ᵇ (1/3600) du dv = (1/3600) * a * b = ab/3600")
print()

# Part (b): P(A < 30)
print("=== Part (b): P(Alicia arrives before 12:30) ===")
print("12:30 is 30 minutes after noon")
print("P(A < 30) = F_A(30) = 30/60 = 1/2")
prob_b = 30/60
print(f"P(A < 30) = {prob_b}")
print()

# Part (c): P(A < 15 and 30 < B < 45)
print("=== Part (c): P(A < 15 and 30 < B < 45) ===")
print("12:15 is 15 minutes after noon")
print("12:30 is 30 minutes after noon") 
print("12:45 is 45 minutes after noon")
print()

print("Method (i): Using independence")
print("P(A < 15) = 15/60 = 1/4")
print("P(30 < B < 45) = (45-30)/60 = 15/60 = 1/4")
print("P(A < 15 and 30 < B < 45) = P(A < 15) * P(30 < B < 45) = (1/4) * (1/4) = 1/16")
prob_c_method1 = (15/60) * (15/60)
print(f"Result: {prob_c_method1}")
print()

print("Method (ii): Area calculation")
print("Total area of [0,60] × [0,60] = 60 * 60 = 3600")
print("Area of [0,15] × [30,45] = 15 * 15 = 225")
print("Probability = 225/3600 = 1/16")
prob_c_method2 = 225/3600
print(f"Result: {prob_c_method2}")
print(f"Both methods agree: {prob_c_method1 == prob_c_method2}")
print()

# Part (d): P(A < B + 5) - Alicia arrives less than 5 minutes after Bernardo
print("=== Part (d): P(A < B + 5) ===")
print("We want P(A - B < 5), or equivalently P(A < B + 5)")
print("This is the region below the line a = b + 5")
print()

print("Using geometric approach:")
print("Total area = 60 × 60 = 3600")
print("We want the area below the line a = b + 5 within [0,60] × [0,60]")
print()
print("The line a = b + 5 intersects:")
print("- Left edge (b = 0): a = 5")
print("- Bottom edge (a = 0): b = -5 (outside domain)")
print("- Top edge (a = 60): b = 55") 
print("- Right edge (b = 60): a = 65 (outside domain)")
print()
print("The region above the line a = b + 5 is a triangle with vertices:")
print("(5, 0), (60, 0), (60, 55)")
print("Area above line = (1/2) * base * height = (1/2) * 55 * 55 = 1512.5")
print("Area below line = 3600 - 1512.5 = 2087.5")
print("P(A < B + 5) = 2087.5/3600 = 0.5798611...")

area_above = 0.5 * 55 * 55
area_below = 3600 - area_above
prob_d = area_below / 3600
print(f"P(A < B + 5) = {prob_d:.6f}")
print(f"As fraction: {area_below}/{3600} = {int(area_below*8)}/{int(3600*8)} = {int(area_below*8/25)}/{int(3600*8/25)}")
print()

# Part (e): Both wait at most 15 minutes
print("=== Part (e): Both wait at most 15 minutes ===")
print("They meet if |A - B| ≤ 15")
print("This is equivalent to -15 ≤ A - B ≤ 15, or B - 15 ≤ A ≤ B + 15")
print()
print("Geometric approach:")
print("We want the region between lines a = b - 15 and a = b + 15")
print("Total area = 60 × 60 = 3600")
print()
print("Area outside the strip (where they don't meet):")
print("Upper triangle: above a = b + 15")
print("- Vertices: (15, 0), (60, 0), (60, 45)")
print("- Area = (1/2) * 45 * 45 = 1012.5")
print()
print("Lower triangle: below a = b - 15") 
print("- Vertices: (0, 15), (0, 60), (45, 60)")
print("- Area = (1/2) * 45 * 45 = 1012.5")
print()
print("Total area where they don't meet = 1012.5 + 1012.5 = 2025")
print("Area where they do meet = 3600 - 2025 = 1575")
print("P(they meet) = 1575/3600 = 7/16")

area_upper_triangle = 0.5 * 45 * 45
area_lower_triangle = 0.5 * 45 * 45
area_no_meet = area_upper_triangle + area_lower_triangle
area_meet = 3600 - area_no_meet
prob_e = area_meet / 3600
print(f"P(they meet) = {prob_e:.6f} = {int(area_meet)}/{3600} = 7/16")
print()

print("=== VERIFICATION ===")
print(f"Part (b): P(A < 30) = {prob_b}")
print(f"Part (c): P(A < 15, 30 < B < 45) = {prob_c_method1} = {prob_c_method2}")
print(f"Part (d): P(A < B + 5) = {prob_d:.6f}")
print(f"Part (e): P(|A - B| ≤ 15) = {prob_e:.6f} = 7/16")

# Create visualization for part (e)
fig, ax = plt.subplots(1, 1, figsize=(8, 8))

# Draw the square
square_x = [0, 60, 60, 0, 0]
square_y = [0, 0, 60, 60, 0]
ax.plot(square_x, square_y, 'k-', linewidth=2)

# Draw the strip where they meet
a_vals = np.linspace(0, 60, 1000)
b_upper = a_vals + 15
b_lower = a_vals - 15

# Clip to domain
b_upper = np.clip(b_upper, 0, 60)
b_lower = np.clip(b_lower, 0, 60)

ax.fill_between(a_vals, b_lower, b_upper, alpha=0.3, color='green', label='They meet (|A-B| ≤ 15)')

# Draw boundary lines
ax.plot([0, 45], [15, 60], 'r--', linewidth=2, label='A = B - 15')
ax.plot([15, 60], [0, 45], 'b--', linewidth=2, label='A = B + 15')

ax.set_xlim(0, 60)
ax.set_ylim(0, 60)
ax.set_xlabel('A (Alicia arrival time)')
ax.set_ylabel('B (Bernardo arrival time)')
ax.set_title('Problem 4(e): Meeting Region')
ax.legend()
ax.grid(True, alpha=0.3)
ax.set_aspect('equal')

plt.tight_layout()
plt.savefig('figures/P4_e_meeting_region.png', dpi=150, bbox_inches='tight')
plt.close()

print("Saved visualization to figures/P4_e_meeting_region.png")
