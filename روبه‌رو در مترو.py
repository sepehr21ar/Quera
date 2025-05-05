line1 = input()
line2 = input()
if len(line1) == len(line2):
    list = [[line1],[line2]]
    counter = 0
    for i in range(len(line1)):
        if line1[i] == line2[i]:
            if line1[i]=='1':
                counter += 1
            else:
                counter = counter

        elif line1[i] != line2[i]:
            counter = counter
    print(counter)
