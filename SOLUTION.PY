# Enter your code here. Read input from STDIN. Print output to STDOUT
import re;

N = int(input())
for _ in range(N):
    try:
        re.compile(input())
        Output = True
    except re.error:
        Output = False
    
    print(Output)
