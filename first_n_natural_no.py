def f_n_natural_sum(n):
    if n == 1 : return 1

    return  f_n_natural_sum(n-1) +n

sum = f_n_natural_sum(5)

print(sum)
     