n = 20
i = 2
factor = []

while i*i <= n:
    if n % i == 0:
        factor.append(i)
        n = n / i
    else: 
        i += 1
if n > 1:
        factor.append(int(n))

print(factor)