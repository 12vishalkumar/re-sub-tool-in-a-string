def change(string):
    if(string.group(1) == '&&'):
        return 'and'
    else:
        return 'or'
import re
n = int(input())
for i in range(n):
    print(re.sub(r'(?<= )(\|\||&&)(?= )', change, input()))