number = int(input("""
Enter a number....
Make sure that it is between 22 and 99
Sorry working on other numbers too


Till then have a look at this

:)



Input here:"""))
a = [0, 1, 12, 7]
b = [11, 8, 0, 2]
c = [5, 10, 3, 0]
d = [4, 0, 6, 9]

a[0] += number-20
b[2] = a[0]-1
d[1] = a[0]+1
c[3] = d[1]+1

print("Here is the Ramanujan Table:- ")
table = [a, b, c, d]
for line in table:
    print(*line)

