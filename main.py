from re import I
from xmlrpc.client import boolean


def lps(s):
    n = len(s)
    p = 0
    max_len = 1;
    table = [[0 for x in range(n)] for y in range(n)]
    while (p<n):
        table[p][p] =True
        p += 1
    start = 0
    p = 0
    while (p<n-1):
        if(s[p]==s[p+1]):
            table[p][p+1] = True
            start = p 
            max_len = 2
        p += 1
    k = 3
    while k<=n :
        p = 0
        while p< (n-k+1):
            j = p + k-1
            if(table[p+1][j-1] and s[p] == s[j]):
                table[p][j] = True
                if k>max_len:
                    start = 1
                    max_len = k
            p +=1
        k +=1
    print(max_len)
s = input()
lps(s)

