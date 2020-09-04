'''
QUESTION
Consider an algorithm that takes as input a positive integer n. If n is even, the algorithm divides it by two, and if n is odd, the algorithm multiplies it by three and adds one. The algorithm repeats this, until nn is one. For example, the sequence for n=3 is as follows:
3→10→5→16→8→4→2→13→10→5→16→8→4→2→1
Your task is to simulate the execution of the algorithm for a given value of n.
Input
The only input line contains an integer n.
Output
Print a line that contains all values of n during the algorithm.
Input:
3
Output:
3 10 5 16 8 4 2 1
'''
#SOLUTION(fastrack)
num = []
odd =int(input("Enter a number:__"))
num.append(odd)
while True:
    if odd % 2 == 0:
        odd = odd / 2
        odd = int(odd)
        num.append(odd)

    else:
        odd = odd * 3
        odd = odd +1
        odd = int(odd)
        num.append(odd)

    if odd == 1:
        break

print(num)