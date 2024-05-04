'''Given a Positive Integer n, return an array of string containing the palindromic string of intergers.

Input Format
First Parameter - number n

Output Format
Return the array of string.

Example 1:
Input:
    5
Output:
    1
    121
    12321
    1234321
    123454321
Explanation:
    The size of staircase is 5. So you have to generate string of integers in such a way that it is palindromic. 
Example 2:
Input:
    3
Output:
    1
    121
    12321
Constraints
0 < n < 10
Expected Time Complexity: O(n)
Expected Space Complexity: O(n)'''

from collections import deque
def solve(n):
    # CODE HERE
    
    palindrom_str = []
    for i in range(1,n+1):
        s = ""
        for j in range(1,i+1):
            s+=str(j)
        for k in range(i-1,0,-1):
            s+=str(k)
        palindrom_str.append(s)
    return palindrom_str
            

if __name__ == '__main__':
	n = int(input())
	res = solve(n)
	print(*res)