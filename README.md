# Probability Theory
**Streaks:** 

<p align="center"> <img src="https://user-images.githubusercontent.com/63327224/140597798-6e9b8227-bd55-49cb-b03a-8a6c45176432.png" width="800"> </p>

In the **Probability-Theory__streaks.py** file I directly use a mathematical model, in which by means of recursion I find the number of possible lists in which the *"caster"* gets a minimum streak.
In the **Probability-Theory__streaks-experiment.py** file we try to reach the same result but this time resorting to randomization and as its name says, we perform an experiment *(in this case many)* to reach an approximate probability.

On the other hand inside Probability-Theory__streaks.py is included a function that graphs **(m, P(m,n))** for a number of **m's** proposed by the user.

**Root:** 

*Brute-force search:* Is a very general problem-solving technique and algorithmic paradigm that consists of systematically enumerating all possible candidates for the solution and checking whether each candidate satisfies the problem's statement. 

*Binary search algorithm:* Binary search compares the target value to the middle element of the array. If they are not equal, the half in which the target cannot lie is eliminated and the search continues on the remaining half, again taking the middle element to compare to the target value, and repeating this until the target value is found. 

<p align="center"> <img src="https://s3-us-west-2.amazonaws.com/ib-assessment-tests/problem_images/binary_search.gif" width="400"> </p>

*Newton–Raphson method:* Produces successively better approximations to the roots (or zeroes) of a real-valued function. The most basic version starts with a single-variable function f defined for a real variable x, the function's derivative f ′, and an initial guess x0 for a root of f. If the function satisfies sufficient assumptions and the initial guess is close, then 

<p align="center"> <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/0ff048abd4c1a8244f09ce8a7ff394626bdb6f80" width="150"> </p>

is a better approximation of the root than x0. 

# Modular Algebra:

**Chinese remainder theorem:** (expressed in terms of congruences) is true over every principal ideal domain. It has been generalized to any commutative ring, with a formulation involving ideals. 

<p align="center"> <img src="https://user-images.githubusercontent.com/63327224/132135430-84f25d6b-1508-4ce3-92f3-a29700665e5b.png" width="800"> </p>

**Euclidean division:**  is the process of dividing one integer (the dividend) by another (the divisor), in a way that produces a quotient and a remainder smaller than the divisor. The greatest common divisor (or highest common factor) of two integers a, b ∈ Z is the largest integer which divides them both. 

**Modular equation solutions** in this function what I do is to return the number of possible solutions of multiples that can obtain a modular expression that is delivered as a string.
