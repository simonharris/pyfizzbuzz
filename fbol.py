N_MAX = 100

for i in range(1, N_MAX+1):
    print(str(i) + "\t" + (("fizz" * (i % 3 == 0) + "buzz" * (i % 5 == 0)) or str(i)))
