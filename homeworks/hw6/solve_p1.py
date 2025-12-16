"""
Problem 1: Monty Hall - Sober and Dizzy
Solve parts (a), (b), (c) with Bayesian analysis
"""
import numpy as np
from fractions import Fraction

print("=" * 60)
print("PROBLEM 1: MONTY HALL - SOBER AND DIZZY")
print("=" * 60)

# Setup: Contestant picks door A. Monty opens door B, revealing a goat.
# Hypotheses: H_A (car behind A), H_B (car behind B), H_C (car behind C)

# Prior probabilities (uniform)
prior = {'H_A': Fraction(1, 3), 'H_B': Fraction(1, 3), 'H_C': Fraction(1, 3)}

print("\n" + "-" * 60)
print("PART (a): SOBER MONTY")
print("-" * 60)
print("\nSober Monty knows where the car is:")
print("- If car is behind A (contestant's choice), Monty randomly opens B or C")
print("- If car is behind B, Monty must open C (can't reveal car)")
print("- If car is behind C, Monty must open B (can't reveal car)")
print("\nData: Monty opens door B, showing a goat")

# Likelihood P(Monty opens B | H)
# P(B | H_A) = 1/2 (random choice between B and C)
# P(B | H_B) = 0 (can't open door with car)
# P(B | H_C) = 1 (must open B, since C has car)
likelihood_sober = {'H_A': Fraction(1, 2), 'H_B': Fraction(0, 1), 'H_C': Fraction(1, 1)}

print("\nBayes Table (Sober Monty):")
print("-" * 50)
print(f"{'Hypothesis':<12} {'Prior':<10} {'Likelihood':<12} {'Prior×Lik':<12}")
print("-" * 50)

unnorm_posterior_sober = {}
for h in ['H_A', 'H_B', 'H_C']:
    unnorm_posterior_sober[h] = prior[h] * likelihood_sober[h]
    print(f"{h:<12} {str(prior[h]):<10} {str(likelihood_sober[h]):<12} {str(unnorm_posterior_sober[h]):<12}")

total_sober = sum(unnorm_posterior_sober.values())
print("-" * 50)
print(f"{'Total':<12} {'':<10} {'':<12} {str(total_sober):<12}")

posterior_sober = {h: unnorm_posterior_sober[h] / total_sober for h in ['H_A', 'H_B', 'H_C']}

print("\nPosterior Probabilities:")
for h in ['H_A', 'H_B', 'H_C']:
    print(f"P({h} | data) = {unnorm_posterior_sober[h]} / {total_sober} = {posterior_sober[h]} = {float(posterior_sober[h]):.4f}")

print(f"\nConclusion: P(car behind C) = {posterior_sober['H_C']} = {float(posterior_sober['H_C']):.4f}")
print(f"           P(car behind A) = {posterior_sober['H_A']} = {float(posterior_sober['H_A']):.4f}")
print("Best strategy: SWITCH (to door C)")

print("\n" + "-" * 60)
print("PART (b): DIZZY MONTY")
print("-" * 60)
print("\nDizzy Monty doesn't know where the car is:")
print("- He randomly opens one of the two doors not chosen by contestant")
print("- He might accidentally reveal the car")
print("\nData: Monty opens door B, showing a goat")

# Likelihood P(Monty opens B AND shows goat | H)
# P(B with goat | H_A) = 1/2 (random choice, B definitely has goat)
# P(B with goat | H_B) = 0 (B has car, can't show goat from B)
# P(B with goat | H_C) = 1/2 (random choice, B has goat)
likelihood_dizzy = {'H_A': Fraction(1, 2), 'H_B': Fraction(0, 1), 'H_C': Fraction(1, 2)}

print("\nBayes Table (Dizzy Monty):")
print("-" * 50)
print(f"{'Hypothesis':<12} {'Prior':<10} {'Likelihood':<12} {'Prior×Lik':<12}")
print("-" * 50)

unnorm_posterior_dizzy = {}
for h in ['H_A', 'H_B', 'H_C']:
    unnorm_posterior_dizzy[h] = prior[h] * likelihood_dizzy[h]
    print(f"{h:<12} {str(prior[h]):<10} {str(likelihood_dizzy[h]):<12} {str(unnorm_posterior_dizzy[h]):<12}")

total_dizzy = sum(unnorm_posterior_dizzy.values())
print("-" * 50)
print(f"{'Total':<12} {'':<10} {'':<12} {str(total_dizzy):<12}")

posterior_dizzy = {h: unnorm_posterior_dizzy[h] / total_dizzy for h in ['H_A', 'H_B', 'H_C']}

print("\nPosterior Probabilities:")
for h in ['H_A', 'H_B', 'H_C']:
    print(f"P({h} | data) = {unnorm_posterior_dizzy[h]} / {total_dizzy} = {posterior_dizzy[h]} = {float(posterior_dizzy[h]):.4f}")

print(f"\nConclusion: P(car behind A) = P(car behind C) = {posterior_dizzy['H_A']} = {float(posterior_dizzy['H_A']):.4f}")
print("Best strategy: INDIFFERENT (switching doesn't help)")

print("\n" + "-" * 60)
print("PART (c): UNCERTAIN MONTY (P(sober)=0.7, P(dizzy)=0.3)")
print("-" * 60)

# Combined likelihood using law of total probability
# P(data | H) = P(sober) * P(data | H, sober) + P(dizzy) * P(data | H, dizzy)
p_sober = Fraction(7, 10)
p_dizzy = Fraction(3, 10)

likelihood_combined = {}
for h in ['H_A', 'H_B', 'H_C']:
    likelihood_combined[h] = p_sober * likelihood_sober[h] + p_dizzy * likelihood_dizzy[h]

print("\nCombined Likelihoods:")
for h in ['H_A', 'H_B', 'H_C']:
    print(f"P(data | {h}) = 0.7 × {likelihood_sober[h]} + 0.3 × {likelihood_dizzy[h]} = {likelihood_combined[h]} = {float(likelihood_combined[h]):.4f}")

print("\nBayes Table (Uncertain Monty):")
print("-" * 50)
print(f"{'Hypothesis':<12} {'Prior':<10} {'Likelihood':<12} {'Prior×Lik':<12}")
print("-" * 50)

unnorm_posterior_combined = {}
for h in ['H_A', 'H_B', 'H_C']:
    unnorm_posterior_combined[h] = prior[h] * likelihood_combined[h]
    print(f"{h:<12} {str(prior[h]):<10} {str(likelihood_combined[h]):<12} {str(unnorm_posterior_combined[h]):<12}")

total_combined = sum(unnorm_posterior_combined.values())
print("-" * 50)
print(f"{'Total':<12} {'':<10} {'':<12} {str(total_combined):<12}")

posterior_combined = {h: unnorm_posterior_combined[h] / total_combined for h in ['H_A', 'H_B', 'H_C']}

print("\nPosterior Probabilities:")
for h in ['H_A', 'H_B', 'H_C']:
    print(f"P({h} | data) = {unnorm_posterior_combined[h]} / {total_combined} = {posterior_combined[h]} = {float(posterior_combined[h]):.4f}")

print(f"\nConclusion: P(car behind C) = {posterior_combined['H_C']} = {float(posterior_combined['H_C']):.4f}")
print(f"           P(car behind A) = {posterior_combined['H_A']} = {float(posterior_combined['H_A']):.4f}")
print("Best strategy: SWITCH (to door C)")

print("\n" + "=" * 60)
print("VERIFICATION")
print("=" * 60)
# Verify posteriors sum to 1
for name, post in [("Sober", posterior_sober), ("Dizzy", posterior_dizzy), ("Combined", posterior_combined)]:
    total = sum(post.values())
    print(f"{name}: Sum of posteriors = {total} (check: {total == 1})")

print("\nAll computations verified with exact fractions.")

