# Complete Problem Database

**Generated:** December 16, 2025
**Purpose:** Complete extraction of all problems from homework and practice exams

---

# HOMEWORK 1

## HW1-Q1: Six-Card Poker Hands

**Full Problem Statement:**
For this problem, let's consider hands with 6 cards. Here are two types:
- **Two-pair:** Two cards have one rank, two cards have another rank, and the remaining two cards have two different ranks. e.g. 2♦, 2♣, 5♦, 5♠, Q♥, K♦
- **Three-of-a-kind:** Three cards have one rank and the remaining three cards have three other ranks. e.g. 2♦, 2♣, 2♥, 5♦, 9♦, K♦

Calculate the probability of each type of hand. Which is more probable?

**Given Information:**
- 6 cards drawn from standard 52-card deck
- Definitions of two-pair and three-of-a-kind for 6-card hands

**Question Asks For:**
- Probability of two-pair
- Probability of three-of-a-kind
- Comparison of which is more probable

**Key Terminology Used:**
- Poker hand, rank, combinations, probability

---

## HW1-Q2: Irregular (Non-Transitive) Dice

**Full Problem Statement:**
Consider 3 dice with different colors with 6 faces however the numbers of the dice are as follows:
- Blue: 333336
- Orange: 144444
- White: 222555

(a) Find the probability that white beats orange, the probability that orange beats blue and the probability that blue beats white. Can you line the dice up in order from best to worst?

(b) Suppose you roll two white dice against two blue dice. What is the probability that the sum of the white dice is greater than the sum of the blue dice?

**Given Information:**
- Three dice with specific face values
- Blue: four 3's, one 6
- Orange: one 1, four 4's, one 4
- White: three 2's, three 5's

**Question Asks For:**
- Part (a): P(White > Orange), P(Orange > Blue), P(Blue > White), ordering
- Part (b): P(sum of 2 white > sum of 2 blue)

**Key Terminology Used:**
- Non-transitive, pairwise comparison, sum of dice

---

## HW1-Q3: Birthday Problem

**Full Problem Statement:**
Ignoring leap days, the days of the year can be numbered 1 to 365. Assume that birthdays are equally likely to fall on any day of the year. Consider a group of n people, of which you are not a member.

(a) Define the probability function P for S. (This will depend on n.)

(b) Consider the following events:
- A: "someone in the group shares your birthday"
- B: "some two people in the group share a birthday"
- C: "some three people in the group share a birthday"
Carefully describe the subset of S that corresponds to each event.

(c) Find an exact formula for P(A). What is the smallest n such that P(A) > 0.5?

(d) Justify why n in part (c) is greater than 365/2 without doing any computation.

(e) Use simulation to estimate the smallest n for which P(B) > 0.9.

(f) Find an exact formula for P(B).

(g) Use simulation to estimate the smallest n for which P(C) > 0.5.

**Given Information:**
- 365 days in a year (ignoring leap days)
- Birthdays equally likely on any day
- Group of n people (you are not a member)

**Question Asks For:**
- Part (a): Probability function definition
- Part (b): Set descriptions for events A, B, C
- Part (c): Formula for P(A), smallest n for P(A) > 0.5
- Part (d): Heuristic justification
- Part (e): Simulation for P(B) > 0.9
- Part (f): Exact formula for P(B)
- Part (g): Simulation for P(C) > 0.5

**Key Terminology Used:**
- Sample space, probability function, birthday problem, simulation

---

## HW1-Q4: Dice Difference

**Full Problem Statement:**
If two balanced dice are rolled, what is the probability that the difference between the two numbers that appear will be less than 3?

**Given Information:**
- Two fair dice
- Looking at |X - Y| < 3

**Question Asks For:**
- P(|X - Y| < 3)

**Key Terminology Used:**
- Balanced dice, difference, probability

---

## HW1-Q5: School Grades

**Full Problem Statement:**
A school contains students in grades 1, 2, 3, 4, 5, and 6. Grades 2, 3, 4, 5, and 6 all contain the same number of students, but there are twice this number in grade 1. What is the probability that the selected student will be in an odd-numbered grade?

**Given Information:**
- Grades 1-6
- Grade 1 has twice as many students as other grades
- Grades 2-6 have equal numbers

**Question Asks For:**
- P(student in odd grade)

**Key Terminology Used:**
- Conditional probability, weighted probability

---

## HW1-Q6: Three Coins

**Full Problem Statement:**
If three fair coins are tossed, what is the probability that all three faces will be the same?

**Given Information:**
- Three fair coins

**Question Asks For:**
- P(all same face)

**Key Terminology Used:**
- Fair coin, probability

---

## HW1-Q7: Elevator Problem

**Full Problem Statement:**
An elevator in a building starts with five passengers and stops at seven floors. If every passenger is equally likely to get off at each floor and all the passengers leave independently of each other, what is the probability that no two passengers will get off at the same floor?

**Given Information:**
- 5 passengers
- 7 floors
- Each passenger equally likely to exit at any floor
- Independence between passengers

**Question Asks For:**
- P(no two passengers exit at same floor)

**Key Terminology Used:**
- Independence, equally likely, permutations

---

## HW1-Q8: Ball Drawing

**Full Problem Statement:**
A box contains 100 balls, of which r are red. Suppose that the balls are drawn from the box one at a time, at random, without replacement. Determine:
(a) the probability that the first ball drawn will be red
(b) the probability that the 50th ball drawn will be red
(c) the probability that the last ball drawn will be red

**Given Information:**
- 100 balls total
- r red balls
- Drawing without replacement

**Question Asks For:**
- Part (a): P(1st ball is red)
- Part (b): P(50th ball is red)
- Part (c): P(last ball is red)

**Key Terminology Used:**
- Without replacement, random selection

---

# HOMEWORK 2

## HW2-Q1: Polya Urn Model

**Full Problem Statement:**
A box contains r red balls and b blue balls. One ball is selected at random and its color is observed. The ball is then returned to the box and k additional balls of the same color are also put into the box. A second ball is then selected at random, its color is observed, and it is returned to the box together with k additional balls of the same color. Each time another ball is selected, the process is repeated. If four balls are selected, what is the probability that the first three balls will be red and the fourth ball will be blue?

**Given Information:**
- Initial: r red balls, b blue balls
- Reinforcement: add k balls of observed color after each draw
- Four balls selected total

**Question Asks For:**
- P(first 3 red, 4th blue)

**Key Terminology Used:**
- Polya urn, conditional probability, reinforcement

---

## HW2-Q2: Craps Game

**Full Problem Statement:**
Consider the following version of the game of craps: The player rolls two dice. If the sum on the first roll is 7 or 11, the player wins the game immediately. If the sum on the first roll is 2, 3, or 12, the player loses the game immediately. However, if the sum on the first roll is 4, 5, 6, 8, 9, or 10, then the two dice are rolled again and again until the sum is either 7 or 11 or the original value. If the original value is obtained a second time before either 7 or 11 is obtained, then the player wins. If either 7 or 11 is obtained before the original value is obtained a second time, then the player loses. Determine the probability that the player will win this game.

**Given Information:**
- Two dice rolled
- Win immediately: sum = 7 or 11
- Lose immediately: sum = 2, 3, or 12
- Otherwise: repeat until sum = 7, 11, or original value

**Question Asks For:**
- P(player wins)

**Key Terminology Used:**
- Craps, conditional probability, geometric series

---

## HW2-Q3: Machine Defects (Bayes)

**Full Problem Statement:**
A machine produces defective parts with three different probabilities depending on its state of repair. If the machine is in good working order, it produces defective parts with probability 0.02. If it is wearing down, it produces defective parts with probability 0.1. If it needs maintenance, it produces defective parts with probability 0.3. The probability that the machine is in good working order is 0.8, the probability that it is wearing down is 0.1, and the probability that it needs maintenance is 0.1. Compute the probability that a randomly selected part will be defective.

**Given Information:**
- P(defective | good) = 0.02
- P(defective | wearing down) = 0.1
- P(defective | needs maintenance) = 0.3
- P(good) = 0.8, P(wearing down) = 0.1, P(needs maintenance) = 0.1

**Question Asks For:**
- P(part is defective)

**Key Terminology Used:**
- Law of total probability, conditional probability

---

## HW2-Q4: Particle Penetration (Binomial)

**Full Problem Statement:**
Suppose that the probability that any particle emitted by a radioactive material will penetrate a certain shield is 0.01. If 10 particles are emitted, what is the probability that exactly one of the particles will penetrate the shield?

**Given Information:**
- P(penetrate) = 0.01
- n = 10 particles

**Question Asks For:**
- P(exactly 1 penetrates)

**Key Terminology Used:**
- Binomial distribution, independent trials

---

## HW2-Q5: World Series

**Full Problem Statement:**
In the World Series of baseball, two teams A and B play a sequence of games against each other, and the first team that wins a total of four games becomes the winner of the World Series. If the probability that team A will win any particular game against team B is 1/3, what is the probability that team A will win the World Series?

**Given Information:**
- First to 4 wins
- P(A wins single game) = 1/3

**Question Asks For:**
- P(A wins World Series)

**Key Terminology Used:**
- Negative binomial, series of games

---

## HW2-Q6: Two Boys Throwing

**Full Problem Statement:**
Two boys A and B throw a ball at a target. Suppose that the probability that boy A will hit the target on any throw is 1/3 and the probability that boy B will hit the target on any throw is 1/4. Suppose also that boy A throws first and the two boys take turns throwing. Determine the probability that the target will be hit for the first time on the third throw of boy A.

**Given Information:**
- P(A hits) = 1/3
- P(B hits) = 1/4
- A throws first, alternating turns

**Question Asks For:**
- P(first hit on A's 3rd throw)

**Key Terminology Used:**
- Geometric distribution, alternating trials

---

## HW2-Q7: Five Coins (Bayes)

**Full Problem Statement:**
Suppose that a box contains five coins and that for each coin there is a different probability that a head will be obtained when the coin is tossed. Let $p_i$ denote the probability of a head when the i-th coin is tossed (i = 1,...,5), and suppose that $p_1 = 0$, $p_2 = 1/4$, $p_3 = 1/2$, $p_4 = 3/4$, and $p_5 = 1$.

(a) Suppose that one coin is selected at random from the box and when it is tossed once, a head is obtained. What is the posterior probability that the i-th coin was selected (i = 1,...,5)?

(b) If the same coin were tossed again, what would be the probability of obtaining another head?

(c) If a tail had been obtained on the first toss of the selected coin and the same coin were tossed again, what would be the probability of obtaining a head on the second toss?

**Given Information:**
- Five coins with p₁=0, p₂=1/4, p₃=1/2, p₄=3/4, p₅=1
- Uniform prior on coin selection

**Question Asks For:**
- Part (a): Posterior P(coin i | head)
- Part (b): P(second head | first head)
- Part (c): P(second head | first tail)

**Key Terminology Used:**
- Bayes' theorem, posterior probability, prior probability

---

## HW2-Q8: Binary Paradox

**Full Problem Statement:**
For this problem assume that kids are equally probable to be male or female.

(a) Our king had two kids. The older kid is female. What is the probability that both kids are female?

(b) Our king had two kids. At least one of them is male. What is the probability that both kids are males?

**Given Information:**
- P(male) = P(female) = 1/2
- Two children

**Question Asks For:**
- Part (a): P(both female | older is female)
- Part (b): P(both male | at least one male)

**Key Terminology Used:**
- Conditional probability, sample space

---

## HW2-Q9: Blue Taxi (Bayes)

**Full Problem Statement:**
In a city with one hundred taxis, 1 is blue and 99 are green. A witness observes a hit-and-run by a taxi at night and recalls that the taxi was blue, so the police arrest the blue taxi driver who was on duty that night. The driver proclaims their innocence and hires you to defend them in court. You hire a scientist to test the witness' ability to distinguish blue and green taxis under conditions similar to the night of accident. The data suggests that the witness sees blue cars as blue 99% of the time and green cars as blue 2% of the time.

Write a speech for the jury to give them reasonable doubt about your client's guilt.

**Given Information:**
- 1 blue taxi, 99 green taxis
- P(witness says blue | actually blue) = 0.99
- P(witness says blue | actually green) = 0.02
- Witness says taxi was blue

**Question Asks For:**
- Bayes analysis for jury (reasonable doubt argument)

**Key Terminology Used:**
- Bayes' theorem, false positive, base rate fallacy

---

## HW2-Q10: Four Dice (Bayes)

**Full Problem Statement:**
There are four dice in a drawer: one D4 (4 sides), one D6 (6-sides), and two D8 (8 sides). Your friend secretly grabs one of the four dice at random. Let S be the number of sides on the chosen die.

(a) What is the probability that 4 side appears? What is the probability that 6 side appears? What is the probability that 8 side appears? (this is called prior)

(b) Now, without showing it to you, your friend rolls the chosen die and tells you the result. Let R be the result of the roll. Use Bayes' rule to find P(S = s | R = 3) for s = 4, 6, 8. Which die is most likely if R = 3?

(c) Which die is most likely if R = 6? Hint: You can either repeat the computation in (b), or you can reason based on your result in (b).

(d) Which die is most likely if R = 7? No computations are needed!

**Given Information:**
- 1 D4, 1 D6, 2 D8 dice
- Uniform selection from 4 dice

**Question Asks For:**
- Part (a): Prior probabilities
- Part (b): Posterior P(S=s | R=3)
- Part (c): Posterior for R=6
- Part (d): Posterior for R=7

**Key Terminology Used:**
- Bayes' theorem, prior, posterior, likelihood

---

## HW2-Q11: Coin Flip Runs (Simulation)

**Full Problem Statement:**
In this problem we will use R to simulate flipping a fair coin 50 times. We'll use the simulation to explore 'runs'.

(a) Make up a sequence of length 50 consisting of ones and zeros. Try to make the sequence look like it was randomly generated by flipping a coin.

(b) A run is a sequence of all 1s or all 0s. How long is the longest run in your answer to part (a)?

(c) Use R to simulate the average length of the longest run in 50 flips of a fair coin. Do this three times with 10000 trials each time and report the three results.

(d) A small modification of your code will let you estimate the probability of a run of 8 or more in 50 flips. Do this three times with 10000 trials each time. Report the three results.

**Given Information:**
- 50 coin flips
- Fair coin (p = 0.5)

**Question Asks For:**
- Part (a): Manual sequence
- Part (b): Longest run in manual sequence
- Part (c): Simulated average longest run
- Part (d): P(run ≥ 8)

**Key Terminology Used:**
- Simulation, runs, Monte Carlo

---

# HOMEWORK 3

## HW3-Q1: Joint PMF

**Full Problem Statement:**
Random variables X and Y have the joint PMF:
$$p_{X,Y}(x, y) = \begin{cases} c(x^2 + y^2), & \text{if } x \in \{1, 2, 4\} \text{ and } y \in \{1, 3\} \\ 0, & \text{otherwise} \end{cases}$$

(a) What is the value of the constant c?
(b) What is P(Y < X)?
(c) What is P(Y > X)?
(d) What is P(Y = X)?
(e) What is P(Y = 3)?
(f) Find the marginal PMFs $p_X(x)$ and $p_Y(y)$.
(g) Find the expectations E[X], E[Y] and E[XY].
(h) Find the variances var(X), var(Y) and var(X + Y).

**Given Information:**
- Joint PMF: $c(x^2 + y^2)$
- Support: x ∈ {1, 2, 4}, y ∈ {1, 3}

**Question Asks For:**
- Normalization constant c
- Various probabilities
- Marginal PMFs
- Expectations and variances

**Key Terminology Used:**
- Joint PMF, marginal PMF, expectation, variance, covariance

---

## HW3-Q2: Three-Sided Die

**Full Problem Statement:**
Assume that we have a three-sided die with faces numbered 1, 2, and 3. The PMF for the result of any one roll of this die is:
$$p_X(x) = \begin{cases} 1/2, & \text{if } x = 1 \\ 1/4, & \text{if } x = 2 \\ 1/4, & \text{if } x = 3 \\ 0, & \text{otherwise} \end{cases}$$

Consider a sequence of six independent rolls of this die, and let $X_i$ be the random variable corresponding to the i-th roll.

(a) What is the probability that exactly three of the rolls have result equal to 3?

(b) What is the probability that the first roll is 1, given that exactly two of the six rolls have result of 1?

(c) We are told that exactly three of the rolls resulted in 1 and exactly three resulted in 2. Given this information, what is the probability that the sequence of rolls is 121212?

(d) Conditioned on the event that at least one roll resulted in 3, find the conditional PMF of the number of 3's.

**Given Information:**
- Three-sided die with P(1)=1/2, P(2)=1/4, P(3)=1/4
- Six independent rolls

**Question Asks For:**
- Part (a): P(exactly three 3's)
- Part (b): P(first is 1 | exactly two 1's)
- Part (c): P(sequence 121212 | three 1's and three 2's)
- Part (d): Conditional PMF of number of 3's given ≥1

**Key Terminology Used:**
- Binomial, conditional probability, multinomial

---

## HW3-Q3: Geometric Distribution Property

**Full Problem Statement:**
Suppose that X and Y are independent, identically distributed, geometric random variables with parameter p. Show that
$$P(X = i | X + Y = n) = \frac{1}{n-1}, \text{ for } i = 1, 2, \ldots, n-1$$

**Given Information:**
- X, Y i.i.d. Geometric(p)

**Question Asks For:**
- Proof that P(X = i | X + Y = n) = 1/(n-1)

**Key Terminology Used:**
- Geometric distribution, conditional probability, uniform

---

## HW3-Q4: Biased Coin Tosses

**Full Problem Statement:**
Consider 10 independent tosses of a biased coin with a probability of heads of p.

(a) Let A be the event that there are 6 heads in the first 8 tosses. Let B be the event that the 9th toss results in heads. Show that events A and B are independent.

(b) Find the probability that there are 3 heads in the first 4 tosses and 2 heads in the last 3 tosses.

(c) Given that there were 4 heads in the first 7 tosses, find the probability that the 2nd head occurred during the 4th trial.

(d) Find the probability that there are 5 heads in the first 8 tosses and 3 heads in the last 5 tosses.

**Given Information:**
- 10 independent coin tosses
- P(heads) = p

**Question Asks For:**
- Part (a): Prove independence of A and B
- Part (b): P(3 heads in first 4, 2 heads in last 3)
- Part (c): P(2nd head on 4th trial | 4 heads in first 7)
- Part (d): P(5 heads in first 8, 3 heads in last 5)

**Key Terminology Used:**
- Independence, binomial, negative binomial

---

## HW3-Q5: Reward for Patterns

**Full Problem Statement:**
Consider a sequence of independent tosses of a biased coin at times t = 0, 1, 2, .... On each toss, the probability of a 'head' is p, and the probability of a 'tail' is 1 - p. A reward of one unit is given each time that a 'tail' follows immediately after a 'head.' Let R be the total reward paid in times 1, 2, ..., n. Find E[R] and var(R).

**Given Information:**
- Independent coin tosses with P(H) = p
- Reward of 1 for each "HT" pattern

**Question Asks For:**
- E[R] for pattern count
- Var(R) for pattern count

**Key Terminology Used:**
- Indicator variables, expectation, variance, covariance

---

## HW3-Q6: Exponential Time to Failure

**Full Problem Statement:**
Recall that an exponential random variable X ~ exp(λ) has pdf given by $f(x) = \lambda e^{-\lambda x}$ on x ≥ 0.

(a) Compute P(X ≥ x).

(b) Compute the mean and standard deviation of X.

(c) Suppose that X₁ and X₂ are independent exp(λ) random variables. Let T = min(X₁, X₂). Find the cdf and pdf of T.

(d) Suppose we are testing 3 different brands of light bulbs B₁, B₂, and B₃ whose lifetimes are exponential random variables with mean 1/2, 1/3, and 1/5 years, respectively. Assuming that all of the bulbs are independent, what is the expected time before one of the bulb fails.

**Given Information:**
- X ~ Exp(λ)
- Part (c): X₁, X₂ i.i.d. Exp(λ)
- Part (d): Three bulbs with means 1/2, 1/3, 1/5 years

**Question Asks For:**
- Part (a): Survival function
- Part (b): Mean and standard deviation
- Part (c): Distribution of minimum
- Part (d): Expected time to first failure

**Key Terminology Used:**
- Exponential distribution, minimum of exponentials, survival function

---

## HW3-Q7: Change of Scale (Transformations)

**Full Problem Statement:**
(a) Suppose the random variable X has an exponential distribution with parameter 1, i.e. X ~ exp(1). Give the range and pdf for the variables X and Y = 3X. Sketch the graph of the density functions for each of these variables.

(b) For the random variable X from part (a), find the range and pdf of W = aX + b, where a and b are constants. Assume a > 0.

(c) Let V = X³. Find the range and pdf of V.

**Given Information:**
- X ~ Exp(1)
- Various transformations

**Question Asks For:**
- Part (a): PDF of Y = 3X
- Part (b): PDF of W = aX + b
- Part (c): PDF of V = X³

**Key Terminology Used:**
- Transformation, Jacobian, change of variables

---

## HW3-Q8: Transformations and Moments

**Full Problem Statement:**
(a) For the variables X, Y, W in the previous problem, assume each of the variables are given in units of minutes. Find the expected value, variance and standard deviation of each variable. Be sure to include units in your answer. What are the units on a and b in the definition of W?

(b) For V from the previous problem, compute E[V].

(c) Compute the median value of both X and V.

**Given Information:**
- Variables from HW3-Q7

**Question Asks For:**
- Part (a): E, Var, SD for X, Y, W with units
- Part (b): E[V] = E[X³]
- Part (c): Medians of X and V

**Key Terminology Used:**
- Expectation, variance, median, units

---

# HOMEWORK 4

## HW4-Q1: Joint PDF Analysis

**Full Problem Statement:**
Suppose X and Y have joint pdf $f(x,y) = c(x^2 + xy)$ on $[0,1] \times [0,1]$.

(a) Find c and the joint cdf F(x,y).

(b) Find the marginal cumulative distribution functions $F_X$ and $F_Y$ and the marginal pdf $f_X$ and $f_Y$.

(c) Find E[X] and Var(X).

(d) Find the covariance and correlation of X and Y.

(e) Are X and Y independent?

**Given Information:**
- Joint PDF: $f(x,y) = c(x^2 + xy)$
- Support: $[0,1] \times [0,1]$

**Question Asks For:**
- Part (a): Normalization constant c, joint CDF
- Part (b): Marginal CDFs and PDFs
- Part (c): E[X], Var(X)
- Part (d): Cov(X,Y), Cor(X,Y)
- Part (e): Independence check

**Key Terminology Used:**
- Joint PDF, marginal, CDF, covariance, correlation, independence

---

## HW4-Q2: Independence from Joint PMF

**Full Problem Statement:**
Suppose X and Y are random variables with the following joint pmf. Are X and Y independent?

| X \ Y | 1 | 2 | 3 |
|-------|------|------|------|
| 1 | 1/18 | 1/9 | 1/6 |
| 2 | 1/9 | 1/6 | 1/18 |
| 3 | 1/6 | 1/18 | 1/9 |

**Given Information:**
- Joint PMF table provided

**Question Asks For:**
- Independence determination

**Key Terminology Used:**
- Joint PMF, marginal PMF, independence

---

## HW4-Q3: Correlation Analysis

**Full Problem Statement:**
Suppose X and Y are random variables with
$$P(X = 1) = P(X = -1) = \frac{1}{2}, \quad P(Y = 1) = P(Y = -1) = \frac{1}{2}$$
Let c = P(X = 1 and Y = 1).

(a) Determine the joint distribution of X and Y, Cov(X,Y), and Cor(X,Y).

(b) For what value(s) of c are X and Y independent? For what value(s) of c are X and Y 100% correlated?

**Given Information:**
- X, Y each take values {-1, 1} with equal probability
- c = P(X = 1, Y = 1)

**Question Asks For:**
- Part (a): Joint distribution, Cov, Cor as functions of c
- Part (b): Values of c for independence and perfect correlation

**Key Terminology Used:**
- Covariance, correlation, independence, joint distribution

---

## HW4-Q4: Meeting Problem (Don't Be Late!)

**Full Problem Statement:**
Alicia and Bernardo are trying to meet for lunch and both will arrive, independently of each other, uniformly and at random between noon and 1 pm. Let A and B be the number of minutes after noon at which Alicia and Bernardo arrive, respectively. Then A and B are independent uniformly distributed random variables on [0,60].

(a) Find the joint pdf f(a,b) and joint cdf F(a,b).

(b) Find the probability that Alicia arrives before 12:30.

(c) Find the probability that Alicia arrives before 12:15 and Bernardo arrives between 12:30 and 12:45 in two ways:
(i) By using the fact that A and B are independent.
(ii) By shading the corresponding area of the square [0,60] × [0,60] and finding what proportion of the square is shaded.

(d) Find the probability that Alicia arrives less than five minutes after Bernardo.

(e) Now suppose that Alicia and Bernardo are both rather impatient and will leave if they have to wait more than 15 minutes for the other to arrive. What is the probability that Alicia and Bernardo will have lunch together?

**Given Information:**
- A, B ~ Uniform(0, 60) independent
- Various timing conditions

**Question Asks For:**
- Part (a): Joint PDF and CDF
- Part (b): P(A < 30)
- Part (c): P(A < 15, 30 < B < 45) two ways
- Part (d): P(A < B + 5)
- Part (e): P(|A - B| < 15)

**Key Terminology Used:**
- Uniform distribution, joint distribution, geometric probability

---

## HW4-Q5: Overlapping Sums

**Full Problem Statement:**
Suppose $X_1, X_2, \ldots$ are independent exponential(2) random variables. Suppose also that X is the sum of the first n and Y is the sum of $X_{n-7}$ to $X_{2n-8}$. Compute Cov(X,Y) and Cor(X,Y). You should assume that n ≥ 8.

Hints: The variance of an exponential(λ) random variable is 1/λ². Use the linearity rules for covariance. What is the size of the overlap?

**Given Information:**
- $X_i$ ~ Exp(2) i.i.d.
- X = $\sum_{i=1}^{n} X_i$
- Y = $\sum_{i=n-7}^{2n-8} X_i$
- n ≥ 8

**Question Asks For:**
- Cov(X,Y)
- Cor(X,Y)

**Key Terminology Used:**
- Exponential distribution, covariance, correlation, overlapping sums

---

# HOMEWORK 5

## HW5-Q1: Bivariate Normal

**Full Problem Statement:**
Let X and Y be jointly normal random variables with parameters $\mu_X = 1$, $\sigma_X^2 = 2$, $\mu_Y = -2$, $\sigma_Y^2 = 3$, and $\rho = -\frac{2}{3}$.

(a) Find P(X + Y > 0).

(b) Find the constant a if we know aX + Y and X + 2Y are independent.

(c) Find P(X + Y > 0 | 2X - Y = 0).

**Given Information:**
- (X, Y) bivariate normal
- μ_X = 1, σ²_X = 2
- μ_Y = -2, σ²_Y = 3
- ρ = -2/3

**Question Asks For:**
- Part (a): P(X + Y > 0)
- Part (b): Value of a for independence
- Part (c): Conditional probability

**Key Terminology Used:**
- Bivariate normal, Gaussian vector, independence, conditional distribution

---

## HW5-Q2: Lognormal Distribution

**Full Problem Statement:**
Let X have the lognormal distribution with parameters 3 and 1.44. Find the probability that X ≤ 6.05.

**Given Information:**
- X lognormal with μ = 3, σ² = 1.44

**Question Asks For:**
- P(X ≤ 6.05)

**Key Terminology Used:**
- Lognormal distribution, CDF

---

## HW5-Q3: Product of Lognormal Variables

**Full Problem Statement:**
Let X and Y be independent random variables such that log(X) has the normal distribution with mean 1.6 and variance 4.5 and log(Y) has the normal distribution with mean 3 and variance 6. Find the mean of the product XY and the probability that XY > 10. Use simulation to evaluate the probability.

**Given Information:**
- log(X) ~ N(1.6, 4.5)
- log(Y) ~ N(3, 6)
- X, Y independent

**Question Asks For:**
- E[XY]
- P(XY > 10)

**Key Terminology Used:**
- Lognormal distribution, product of lognormals

---

## HW5-Q4: Conditional Probability in Bivariate Normal

**Full Problem Statement:**
Suppose that two different tests A and B are to be given to a student chosen at random from a certain population. Suppose also that the mean score on test A is 85, and the standard deviation is 10; the mean score on test B is 90, and the standard deviation is 16; the scores on the two tests have a bivariate normal distribution; and the correlation of the two scores is 0.8. If the student's score on test A is 80, what is the probability that her score on test B will be higher than 90?

**Given Information:**
- Test A: μ_A = 85, σ_A = 10
- Test B: μ_B = 90, σ_B = 16
- ρ = 0.8
- Bivariate normal

**Question Asks For:**
- P(B > 90 | A = 80)

**Key Terminology Used:**
- Bivariate normal, conditional distribution

---

## HW5-Q5: Bivariate Normal Parameters

**Full Problem Statement:**
Suppose that X₁ and X₂ have a bivariate normal distribution for which E(X₁|X₂) = 3.7 - 0.15X₂, E(X₂|X₁) = 0.4 - 0.6X₁, and Var(X₂|X₁) = 3.64. Find the mean and the variance of X₁, the mean and the variance of X₂, and the correlation of X₁ and X₂.

**Given Information:**
- E(X₁|X₂) = 3.7 - 0.15X₂
- E(X₂|X₁) = 0.4 - 0.6X₁
- Var(X₂|X₁) = 3.64

**Question Asks For:**
- μ₁, σ₁², μ₂, σ₂², ρ

**Key Terminology Used:**
- Bivariate normal, conditional expectation, conditional variance

---

## HW5-Q6: Stock Returns

**Full Problem Statement:**
Using Yahoo Finance data via the quantmod package in R:

1. Download SP500 (^GSPC) and VIX (^VIX) data from November 10, 2015 to November 10, 2025

2. Calculate daily returns for both series

3. Estimate the following parameters:
   - Mean and standard deviation of SP500 returns
   - Mean and standard deviation of VIX returns
   - Correlation between SP500 and VIX returns

4. Calculate:
   - Empirical probability that SP500 returns are less than 3%
   - Theoretical probability from the fitted normal distribution that SP500 returns are less than 3%

**Given Information:**
- Real financial data
- 10 years of SP500 and VIX data

**Question Asks For:**
- Summary statistics
- Comparison of empirical vs theoretical probabilities

**Key Terminology Used:**
- Stock returns, correlation, normal distribution, empirical probability

---

# HOMEWORK 6

## HW6-Q1: Monty Hall (Sober and Dizzy)

**Full Problem Statement:**
The Monty Hall problem: Monty hosts a game show. There are three doors: one hides a car and two hide goats. The contestant picks a door, which is not opened. Monty then opens another door which has a goat behind it. Finally, contestant must decide whether to stay with her original choice or switch to the other unopened door.

(a) In the usual formulation, Monty is sober and knows the locations of the car and goats. So if the contestant picks a door with a goat, Monty always opens the other door with a goat. And if the contestant picks the door with a car, Monty opens one of the other two doors at random. Suppose that sober Monty Hall opens door B, revealing a goat. Make a Bayes table with prior, likelihood and posterior. Use the posterior probabilities to determine the best strategy.

(b) Now suppose that Monty is dizzy, i.e. he has completely forgotten where the car is and is only aware enough to randomly open one of the two doors not chosen by the contestant. Dizzy Monty Hall opens door B, revealing a goat. Make a Bayes table with prior, likelihood and posterior. Use the posterior probabilities to determine the best strategy.

(c) Based on Monty's pre-show behavior, we think that Monty is sober with probability 0.7 and dizzy with probability 0.3. Repeat the analysis from parts (a) and (b) in this situation.

**Given Information:**
- Three doors, one car, two goats
- Contestant picks door A
- Monty opens door B (goat)

**Question Asks For:**
- Part (a): Bayes table for sober Monty, best strategy
- Part (b): Bayes table for dizzy Monty, best strategy
- Part (c): Combined analysis with uncertain sobriety

**Key Terminology Used:**
- Bayes' theorem, prior, likelihood, posterior, Monty Hall

---

## HW6-Q2: Dice Prediction (Bayesian)

**Full Problem Statement:**
I have five dice (4, 6, 8, 12, or 20 sides) and pick one at random (uniform probability). I then roll this die n times and tell you that, miraculously, every roll resulted in the value 7.

(a) First, consider just the first roll. Find the prior predictive probability that the first roll will be a 7 and the posterior (after the first roll) predictive probability that the second roll will be a 7. Also find the posterior (after the first roll) probabilities for the chosen die.

(b) Find the posterior probability P(H | data) for each die given the data of all n rolls (your answers should involve n). What is the limit of each of these probabilities as n grows to infinity? Explain why this makes sense.

(c) Given that my first 10 rolls resulted in 7 (i.e., n=10), rank the possible values for my next roll from most likely to least likely. Note any ties in rank and explain your reasoning carefully.

(d) Let $x_i$ be the result of the i-th roll. Find the posterior predictive pmf for the (n+1)-st roll given the data.

(e) What function does the pmf in part (d) converge to as n grows to infinity? Explain why this makes sense.

**Given Information:**
- Five dice: D4, D6, D8, D12, D20
- Uniform prior on die selection
- All rolls result in 7

**Question Asks For:**
- Part (a): Prior/posterior predictive probabilities
- Part (b): Posterior probabilities as function of n
- Part (c): Ranking for n=10
- Part (d): Posterior predictive PMF
- Part (e): Limiting behavior

**Key Terminology Used:**
- Bayesian inference, prior, posterior, predictive distribution

---

## HW6-Q3: CLT Sample Size

**Full Problem Statement:**
Suppose that a random sample of size n is to be taken from a distribution for which the mean is μ and the standard deviation is 3. Use the central limit theorem to determine approximately the smallest value of n for which the following relation will be satisfied:
$$P(|\bar{X}_n - \mu| < 0.3) \geq 0.95$$

**Given Information:**
- σ = 3
- Target: P(|X̄ - μ| < 0.3) ≥ 0.95

**Question Asks For:**
- Minimum sample size n

**Key Terminology Used:**
- Central Limit Theorem, sample size determination

---

## HW6-Q4: CLT for Digit Average

**Full Problem Statement:**
Suppose that 16 digits are chosen at random with replacement from the set {0,...,9}. What is the probability that their average will lie between 4 and 6?

**Given Information:**
- 16 digits from {0, 1, ..., 9}
- With replacement

**Question Asks For:**
- P(4 < X̄ < 6)

**Key Terminology Used:**
- Central Limit Theorem, discrete uniform

---

## HW6-Q5: Beta-Binomial (Uniform Prior)

**Full Problem Statement:**
Suppose that the proportion θ of defective items in a large manufactured lot is unknown, and the prior distribution of θ is the uniform distribution on the interval [0,1]. When eight items are selected at random from the lot, it is found that exactly three of them are defective. Determine the posterior distribution of θ. Compute the expected mean and variance of θ.

**Given Information:**
- Prior: θ ~ Uniform(0,1) = Beta(1,1)
- Data: 3 defective out of 8

**Question Asks For:**
- Posterior distribution
- E[θ | data]
- Var(θ | data)

**Key Terminology Used:**
- Bayesian inference, conjugate prior, Beta-Binomial

---

## HW6-Q6: Beta-Binomial (Non-uniform Prior)

**Full Problem Statement:**
Consider again the problem described in Problem 5, but suppose now that the prior p.d.f. of θ is as follows:
$$\xi(\theta) = \begin{cases} 2(1-\theta), & 0 < \theta < 1 \\ 0, & \text{otherwise} \end{cases}$$
As in previous Exercise, suppose that in a random sample of eight items exactly three are found to be defective. Determine the posterior distribution of θ.

**Given Information:**
- Prior: ξ(θ) = 2(1-θ), Beta(1,2)
- Data: 3 defective out of 8

**Question Asks For:**
- Posterior distribution

**Key Terminology Used:**
- Bayesian inference, Beta prior

---

# PRACTICE MIDTERM 1

## PM1-Q1: Dice Rolls

**Full Problem Statement:**
A fair dice are rolled 11 times. What is the probability that:

(a) At least one 3 appears

(b) Each of the numbers 3, 2, 5 appear exactly three times each, while the number 4 appears 2 times

(c) Each of the numbers 4, 5 appear at least once.

**Given Information:**
- 11 rolls of fair die

**Question Asks For:**
- Part (a): P(at least one 3)
- Part (b): P(three 3's, three 2's, three 5's, two 4's)
- Part (c): P(at least one 4 and at least one 5)

**Key Terminology Used:**
- Multinomial, complement, inclusion-exclusion

---

## PM1-Q2: Set Theory True/False

**Full Problem Statement:**
A, B and D are three sets in a sample space and P(B), P(D) > 0. Which ones from the following statements which are ALWAYS true.

(a) P(A|B) ≥ P(A).

(b) If P(A|D) ≥ P(B|D) and P(A|Dᶜ) ≥ P(B|Dᶜ) then P(A) ≥ P(B)

(c) If A and B are independent then P(A|B) = P(B).

**Given Information:**
- A, B, D sets in sample space
- P(B), P(D) > 0

**Question Asks For:**
- True/False for each statement with justification

**Key Terminology Used:**
- Conditional probability, independence

---

## PM1-Q3: Married Couples Seating

**Full Problem Statement:**
Four married couples are seated at random around a round table.

(a) Compute the probability that each couple seats together

**Given Information:**
- 4 married couples (8 people)
- Round table

**Question Asks For:**
- P(all couples sit together)

**Key Terminology Used:**
- Circular permutation, probability

---

## PM1-Q4: Dice and Cards Game

**Full Problem Statement:**
Consider the following game. A player rolls a fair die. If he rolls 6, he wins immediately. If he rolls a 1 he loses immediately. Otherwise, he selects at random, as many cards from the full deck as the number that came up on the die. The player wins if exactly 2 aces are among the selected cards.

(a) Compute the probability of winning the game

(b) John just told you that he recently played the game and won. What is the probability that rolled a 5 on the die?

**Given Information:**
- Fair die roll
- Win on 6, lose on 1
- Otherwise draw cards equal to die result
- Win if exactly 2 aces

**Question Asks For:**
- Part (a): P(win)
- Part (b): P(rolled 5 | won)

**Key Terminology Used:**
- Hypergeometric, Bayes' theorem, conditional probability

---

# PRACTICE MIDTERM 2

## PM2-Q1: Joint PDF (Triangular Support)

**Full Problem Statement:**
Give X, Y continuous random variables whose joint p.d.f is given by:
$$f(x, y) = \begin{cases} \frac{1}{y}, & 0 < y < 1, 0 < x < y \\ 0, & \text{else} \end{cases}$$

(a) Compute the covariance of X and Y

(b) Compute the Variance of X and Variance of Y

(c) Compute the correlation of X and Y

**Given Information:**
- Joint PDF: f(x,y) = 1/y on triangular region

**Question Asks For:**
- Part (a): Cov(X,Y)
- Part (b): Var(X), Var(Y)
- Part (c): Cor(X,Y)

**Key Terminology Used:**
- Joint PDF, covariance, variance, correlation

---

## PM2-Q2: Joint PDF with Exponential

**Full Problem Statement:**
Assume that the joint density of (X, Y):
$$f(x, y) = \begin{cases} c\frac{1}{y}e^{-y}, & 0 < x < y \\ 0, & \text{else} \end{cases}$$

(a) Compute c such that the density is a proper p.d.f

(b) Compute the marginal density of Y

(c) Compute the conditional density X given Y

(d) Compute the Expected value of X² given Y, E(X²|Y = y)

**Given Information:**
- Joint PDF with exponential component

**Question Asks For:**
- Part (a): Normalization constant c
- Part (b): Marginal f_Y(y)
- Part (c): Conditional f(x|y)
- Part (d): E[X²|Y=y]

**Key Terminology Used:**
- Joint PDF, marginal, conditional distribution, conditional expectation

---

## PM2-Q3: Uniform on [-1,1]

**Full Problem Statement:**
Let X be a uniform random variable on the interval [-1, 1].

(a) Compute the variance of X².

(b) If X₁, X₂, ..., Xₙ are independent and identically distributed copies of X and Z = max(X₁,...,Xₙ) compute the CDF of Z

(c) Compute the correlation between X and X²?

(d) Are X and X² independent?

**Given Information:**
- X ~ Uniform(-1, 1)

**Question Asks For:**
- Part (a): Var(X²)
- Part (b): CDF of maximum
- Part (c): Cor(X, X²)
- Part (d): Independence check

**Key Terminology Used:**
- Uniform distribution, order statistics, correlation, independence

---

## PM2-Q4: Coin Game with MGF

**Full Problem Statement:**
Consider the following game. Toss a coin with probability p of Heads. If you toss Heads, you win $2, if you toss Tails, you lose $1.

(a) Assume that you play this game n times and let Sₙ be your combined winnings. Compute the moment generating function of Sₙ, that is, E(e^{tSₙ}).

(b) Now you roll a fair die and you play the game as many times as the number you roll. Let Y be your total winnings. Compute E(Y)

**Given Information:**
- P(H) = p, win $2
- P(T) = 1-p, lose $1

**Question Asks For:**
- Part (a): MGF of Sₙ
- Part (b): E[Y] with random number of games

**Key Terminology Used:**
- MGF, law of total expectation, random sum

---

# PRACTICE FINAL

## PF-Q1: Coin Game with CLT

**Full Problem Statement:**
Toss a fair coin twice. You win $3 if both tosses come out Heads, lose $1 if no toss comes out Heads, and win or lose nothing otherwise.

(a) What is the expected number of games you need to play to win once?

(b) Assume that you play this game 400 times. What is, approximately, the probability that you win at least $240?

(c) Again, assume that you play this game 400 times. Compute (approximately) the amount of money x such that your winnings will be at least x with probability 0.5. Then, do the same with probability 0.9.

**Given Information:**
- Fair coin tossed twice per game
- Win $3 for HH, lose $1 for TT, $0 otherwise
- 400 games

**Question Asks For:**
- Part (a): Expected number of games to win once
- Part (b): P(total ≥ $240)
- Part (c): Quantiles of total winnings

**Key Terminology Used:**
- Geometric distribution, CLT, quantiles

---

## PF-Q2: Gaussian Vector Independence

**Full Problem Statement:**
Suppose X₁ and X₂ are iid N(0, 1) random variables. Define:
Y₁ = aX₁ + X₂, and Y₂ = X₁ + bX₂

(a) Find a and b such that Y = (Y₁, Y₂) is a Gaussian vector with independent components.

(b) Calculate the mean vector and covariance matrix of Y.

(c) Write the joint density of the random vector Y.

(d) Write an expression for P(Y₁ > X₁|X₁ > 0).

(e) Find the conditional distribution of Y₁ - X₁ given X₁ = x.

**Given Information:**
- X₁, X₂ i.i.d. N(0,1)
- Y₁ = aX₁ + X₂
- Y₂ = X₁ + bX₂

**Question Asks For:**
- Part (a): Values of a, b for independence
- Part (b): Mean vector and covariance matrix
- Part (c): Joint density
- Part (d): Conditional probability expression
- Part (e): Conditional distribution

**Key Terminology Used:**
- Gaussian vector, multivariate normal, independent components, conditional distribution

---

## PF-Q3: Exponential Average with CLT

**Full Problem Statement:**
Let X₁, X₂, ..., X₁₀₀ be independent random variables exponentially distributed with mean θ = 3 (i.e. their density is f(x) = (1/3)e^{-x/3}, for x > 0). Let X̄ be the average of these variables.

Calculate an approximate value for the probability:
$$P\left(\frac{\bar{X}}{\bar{X} + 3} < 0.5\right)$$

**Given Information:**
- X_i ~ Exp(1/3), mean = 3
- n = 100

**Question Asks For:**
- P(X̄/(X̄ + 3) < 0.5)

**Key Terminology Used:**
- Exponential distribution, CLT, transformation

---

## PF-Q4: Lognormal Stock Price

**Full Problem Statement:**
Given a lognormal distribution for stock price S defined as:
S = S₀e^Z, where Z is normal random variable with mean (r - σ²/2) and variance σ², where S₀ = 100, r = 0.05, σ = 20%.

(a) Compute the expected value of the function of the random variable E[e^{-r}S].

(b) Compute the probability that S exceeds 100.

**Given Information:**
- S = S₀e^Z
- Z ~ N(r - σ²/2, σ²)
- S₀ = 100, r = 0.05, σ = 0.2

**Question Asks For:**
- Part (a): E[e^{-r}S]
- Part (b): P(S > 100)

**Key Terminology Used:**
- Lognormal distribution, stock price model, MGF

---

## PF-Q5: Discrete Prior Bayesian

**Full Problem Statement:**
Suppose that the proportion θ of defective items in a large manufactured lot is unknown, and the prior distribution of θ is 1/2 with probability 1/2 and 3/4 with probability 1/2. When 10 items are selected at random from the lot, it is found that none of them are defective.

(a) What is the probability that from 10 items, none of them are defective?

(b) Determine the posterior distribution of θ, given none items are defective from a sample of 10 items.

(c) What is the mean and variance of the parameter θ given the data?

**Given Information:**
- Prior: P(θ = 1/2) = P(θ = 3/4) = 1/2
- Data: 0 defective in 10 items

**Question Asks For:**
- Part (a): P(0 defective)
- Part (b): Posterior distribution
- Part (c): Posterior mean and variance

**Key Terminology Used:**
- Bayesian inference, discrete prior, posterior

---

# SUMMARY STATISTICS

## Total Problem Count

| Source | Problems | Sub-parts |
|--------|----------|-----------|
| HW1 | 8 | 15 |
| HW2 | 11 | 22 |
| HW3 | 8 | 24 |
| HW4 | 5 | 13 |
| HW5 | 6 | 11 |
| HW6 | 6 | 15 |
| Practice Midterm 1 | 4 | 6 |
| Practice Midterm 2 | 4 | 12 |
| Practice Final | 5 | 13 |
| **TOTAL** | **57** | **131** |

## Problems by Topic

| Topic | Count |
|-------|-------|
| Counting/Combinatorics | 8 |
| Conditional Probability | 12 |
| Bayes' Theorem | 10 |
| Discrete Distributions | 8 |
| Continuous Distributions | 10 |
| Joint Distributions | 12 |
| Covariance/Correlation | 8 |
| Transformations | 4 |
| CLT/Limit Theorems | 8 |
| Bivariate Normal | 6 |
| Bayesian Statistics | 8 |
| Lognormal/Finance | 4 |
| Simulation | 3 |

