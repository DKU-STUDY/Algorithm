arr = [int(input()) for _ in range(6)]

science = arr[:4]
geo = arr[4:6]
science.sort()
geo.sort()
print(sum(science[1:4], geo[1]))