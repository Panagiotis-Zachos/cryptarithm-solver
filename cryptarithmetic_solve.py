'''
Write a program that solves symbol puzzles (sums) like this one: aab + bbc = dde.
One possible solution would be 334 + 445 = 779.

It gets inreresting with puzzles which have a meaning or a phrases and have only one possible solution.
For example SEND + MORE = MONEY

The program should output every possible solution.
'''

from itertools import permutations
import time

def wordVal(letterValues, powerOfTen):
        val = 0
        for i in range(len(letterValues)):
                val += letterValues[i]*powerOfTen[i]
        return val

if __name__ == "__main__":
        x = 'SEND'
        y = 'MORE'
        z = 'MONEY'

        t0 = time.time()

        # Calculate the powers of 10 that correspond to each letter here 
        # to save time in each wordVal function call
        xProd = [10**i for i in range(len(x)-1,-1,-1)]
        yProd = [10**i for i in range(len(y)-1,-1,-1)]
        zProd = [10**i for i in range(len(z)-1,-1,-1)]

        # Find all the different letters that exist in the cryptarithmetic equation
        letters = []
        for i in x+y+z:
                if i not in letters:
                        letters.append(i)       

        # If len(letters) > 10 no solutions exist because each letter needs to have a unique value 0-9
        numOfLetters = len(letters)
        if numOfLetters > 10:
                print("No Solutions, too many different letters.")
                exit()

        permList = (list(permutations([0,1,2,3,4,5,6,7,8,9], numOfLetters)))
        
        # If yes then first letter of the resulting word is 0 or 1
        carryFlag = False
        if len(z) > len(x) and len(z) > len(y):
                carryFlag = True
                firstLetterIndex = letters.index(z[0])
        
        # printFlag: to check whether a solution was found or not. 
        # Appending to a list slows the programm down unnecessarily.
        printFlag = False
        print("{} + {} = {}".format(x,y,z))
        for perm in permList:
                if carryFlag:
                        if perm[firstLetterIndex] != 0 and perm[firstLetterIndex] != 1:
                                continue

                xVals = [0]*len(x)
                yVals = [0]*len(y)
                zVals = [0]*len(z)

                for i in range(numOfLetters):
                        indices = [k for k, j in enumerate(x) if j == letters[i]]
                        for j in indices:
                                xVals[j] = perm[i]
                        indices = [k for k, j in enumerate(y) if j == letters[i]]
                        for j in indices:
                                yVals[j] = perm[i]
                        indices = [k for k, j in enumerate(z) if j == letters[i]]
                        for j in indices:
                                zVals[j] = perm[i]
                
                xEquiv = wordVal(xVals, xProd)
                yEquiv = wordVal(yVals, yProd)
                zEquiv = wordVal(zVals, zProd)
                if xEquiv + yEquiv == zEquiv:
                        #rint(perm)
                        xSol = ''.join(str(e) for e in xVals)
                        ySol = ''.join(str(e) for e in yVals)
                        zSol = ''.join(str(e) for e in zVals)
                        print("{} + {} = {}".format(xSol, ySol, zSol))
                        printFlag = True

        if printFlag == False:
                print("No solutions found.")
                exit()

        t1 = time.time()
        print("\nCalculations done in: {:.2f}s".format(t1 - t0))              
