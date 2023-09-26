n = 3 #years
A = 1000 #euros
p = 5 #percent
A = A*(1+(p/100))**n

print(f"""
The amount of euros with respect to the addition of
interest has grown to
{A: .1f} euros in three years""")


"""
Output: python interest_rate.py

The amount of euros with respect to the addition of
interest has grown to
1157.6 euros in three years
 """
