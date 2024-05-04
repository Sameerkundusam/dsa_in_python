'''Given a string str1, Return the array containing the frequency of each character in the order of their occurrence.

Input Format
First Parameter - string str1

Output Format
Return the array.

Example 1:
Input:
    arfardarb
Output:
    3 3 1 1 1
Explanation:
    a is repeated 3 times, followed by r which is repeated 3 times. f, d and b occurs only 1 time.    
Constraints
1 <= n <= 105
String contains lowercase letters
Expected Time Complexity: O(n)
Expected Space Complexity: O(1)'''

from collections import deque
def solve(str1):
    l = list(str1)
    freq = []
    s=''
    for i in str1:
        if i not in s:
            s+=i
    for i in s:
        c = 0
        for j in str1:
            if i ==j:
                c+=1
        if c:
            freq.append(c)
    return freq

if __name__ == '__main__':
	str1 = input()
	res = solve(str1)
	print(*res)