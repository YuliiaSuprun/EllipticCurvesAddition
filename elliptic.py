
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = egcd(b % a, a)
        return gcd, (y - (b // a) * x) % mod, x

def add(mod, x1, y1, x2, y2, j): 
    found = 0
    gcd, inv, dummy = egcd((x2 - x1) % mod, mod)
    if(gcd > 1):
            print("==================")
            print("Can't find inverse of:")
            print(((x2-x1) % mod))
            found = -1
            print((j, x1, y1, x2, y2))
            return (x2, y2, found) 
    sl = ((y2-y1) * inv) % mod
    x3 = (sl**2 - x1 - x2) % mod
    y3 = (sl*(x1-x3) - y1) % mod
    return (x3, y3, found) 

def multiply(mod, x1, y1, pow, j, a): 
    gcd, inv, dummy = egcd(2*y1, mod)
    found = 0
    if (gcd > 1):
            found = -1
            return (x1, y1, found)   
    sl = ((3*(x1**2) + a) * inv) % mod
    x2 = (sl**2 - 2*x1) % mod
    y2 = (sl*(x1-x2) - y1) % mod
    if (pow == 2):
            return (x2, y2, found)
    k = 2
    while (k < pow):
        res = add(mod, x1, y1, x2, y2, j)
        if (res[2] == -1):
                found = -1
                return (x2, y2, found)
        x2 = res[0]
        y2 = res[1]
        k +=1
    return (x2, y2, found)

mod = 589
a=4
x1 = 2
y1 = 5
j=2
while(j < 100):
        tupl = multiply(mod, x1, y1, j, j, a)
        if(tupl[2] == -1):
                j = 10
                break
        x1 = tupl[0]
        y1 = tupl[1]
        print((j, x1, y1))
        j +=1


