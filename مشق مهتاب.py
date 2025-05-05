number = int(input())
odd = 0
for i in range(number):
    if i % 2 == 1:
        odd += i
print(odd)