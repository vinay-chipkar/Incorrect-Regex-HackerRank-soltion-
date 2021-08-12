# Incorrect Regex

# problem statement
You are given a string s.
Your task is to find out whether s is a valid regex or no

# Input Format
The first line contains integer T, the number of test cases.
The next T lines contains the string S.

# Output Format
Print "True" or "False" for each test case without quotes.

Sample Input

2
.*\+
.*+
Sample Output

True
False
Explanation

.*\+ : Valid regex.
.*+: Has the error multiple repeat. Hence, it is invalid.
