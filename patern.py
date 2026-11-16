# *****
# ****
# ***
# **
# *

def pattern(n, i):
    if(n < i): return
    print("*"*i)
    pattern(n, i+1)

pattern(5, 1)  