N = input()[:-2]
F = int(input())
for i in range(100):
    if int(N + str(i).zfill(2)) % F == 0:
        print(str(i).zfill(2))
        break