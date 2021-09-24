
def collatz(s, e):
    for n in range(s,e):
        print(n)
        while n != 1:
            if n % 2 == 0:
                n = n / 2
            else:
                n = (n * 3) + 1

collatz(100,200)