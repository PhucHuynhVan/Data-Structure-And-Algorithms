# Recursion Interview Problems

1. **Reverse-String:**

    This interview question requires you to reverse a string using recursion. Make sure to think of the base case here.

    Again, make sure you use recursion to accomplish this. **Do not slice (e.g. string[::-1]) or use iteration, there muse be a recursive call for the function.**

2. **String Permutation:**

   **Problem Statement**: Given a string, write a function that uses recursion to output a list of all the possible permutations of that string.

   For example, given s='abc' the function should return ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

   *Note: If a character is repeated, treat each occurence as distinct, for example an input of 'xxx' would return a list with 6 "versions" of 'xxx'*

3. **Fibonnaci Sequence**
   
   Implement a ![Fibonnaci Sequence](https://en.wikipedia.org/wiki/Fibonacci_number)
 
4. **Coin Change Problem**

   **Note: This problem has multiple solutions and is a classic problem in showing issues with basic recursion. There are better solutions involving memoization and simple iterative solutions.If you are having trouble with this problem (or it seems to be taking a long time to run in some cases) check out the Solution Notebook and fully read the conclusion link for a detailed description of the various ways to solve this problem!**
  
   This problem is common enough that is actually has its own ![Wikipedia Entry](https://en.wikipedia.org/wiki/Change-making_problem)! Let's check the problem statement again:

   This is a classic recursion problem: Given a target amount n and a list (array) of distinct coin values, what's the fewest coins needed to make the change amount.
   
   For example:
   
   If n = 10 and coins = [1,5,10]. Then there are 4 possible ways to make change:

      * 1+1+1+1+1+1+1+1+1+1
   
      * 5 + 1+1+1+1+1
   
      * 5+5
   
      * 10
   
      With 1 coin being the minimum amount.