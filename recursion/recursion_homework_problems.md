# Recursion Homework Problems
This assignment is a variety of small problems to begin you getting used to the idea of recursion. They are not full-blown interview questions, but do serve as a great start for getting your mind "in the zone" for recursion problems.

1. **Problem 1**

    **Write a recursive function which takes an integer and computes the cumulative sum of 0 to that integer**

    **For example, if n=4 , return 4+3+2+1+0, which is 10.**

    This problem is very similar to the factorial problem presented during the introduction to recursion. Remember, always think of what the base case will look like. In this case, we have a base case of n =0 (Note, you could have also designed the cut off to be 1).

    In this case, we have: n + (n-1) + (n-2) + .... + 0

2. **Problem 2**

   **Given an integer, create a function which returns the sum of all the individual digits in that integer. For example: if n = 4321, return 4+3+2+1**