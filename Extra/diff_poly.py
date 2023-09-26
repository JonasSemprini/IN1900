#6.11

p = {0:-3, 3: 2, 5:-1}

def eval_poly_dict(poly, x):
    sum = 0.0

    for power in poly:
        sum+= poly[power]*x*power
    return sum

print(f'p(1) = {eval_poly_dict(p,1)} p(2) = {eval_poly_dict(p,2)}')

def diff(p):
    dp = {}
    for j in p:
        if j != 0:
            dp[j-1] = j*p[j]
    return dp

print(diff(p))
