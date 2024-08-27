
n = 3**15

fibs = [0, 1]
while fibs[-1] + fibs[-2] < n:
    fibs.append(fibs[-1] + fibs[-2])

x, zeck = n, []
while x not in fibs:
    lessFibs = [f for f in fibs if f < x]
    zeck.append(lessFibs[-1])
    x -= lessFibs[-1]

print(n, "=", " + ".join(str(z) for z in zeck), "+", x)
