def fun(num):
    if(num != 0):
        return num + fun(num - 1)
    else:
        return 0

ans=fun(10)
print(ans)