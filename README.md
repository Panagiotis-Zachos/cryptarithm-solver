# cryptarithm-solver
A program that solves cryptarithms in the form of SEND + MORE = MONEY
and outputs every possible solution.


Program works as follows:
1. Find the different letters that exist in input 
   i.e. for SEND + MORE = MONEY there are seven different letters: SENDMORY so the permutations have a length of 7

2. Generate all possible permutations of numbers 0-9 with a length equal to the number of different characters in input
   
3. Find which letters shouldn't be zero i.e. For SEND + MORE = MONEY, S != 0 and M != 0

4. If the resulting word is bigger than the two added words then we deduce that the first letter of that word should be 1.
   So M = 1 in SEND + MORE = MONEY

5. Check each permutation that the above conditions apply to.

The checking goes as follows:
        a. For each letter in the letters list the appropriate value is applied, this goes through every different letter,
        for all of the three words given as input.
        b. The values are stored in an array xValue, yValue and zValue, and multiplied by the appropriate power of 10, stored in the
        xProd, yProd and zProd lists.
        c. Then xValue and yValue are added and checked against zValue, if these are the same, then the permutation is printed on-screen.
