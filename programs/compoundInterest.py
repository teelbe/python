def compound_interest(p, t, r, n):
    #calculate compound using the formula
    a = p* (1+(r/n))**(n *t)
    #round the resit to the nearst cent
    return round(a,2)

print(compound_interest(10000, 10, 0.06, 12))
print("-------------------")
print(compound_interest(100, 1, 0.05, 1))