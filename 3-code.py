n = int(input("Enter number of students: "))

marks = [0] * n
count = 0
fail = 0

for i in range(n):

    reg = int(input("Enter registration number: "))
    last = reg % 10

    m = int(input("Enter mark: "))

    if m < 0 or m > 100:
        print(m, "Invalid")
    else:
        new = m

        if last % 2 == 1:
            new = new + 2
        else:
            new = new - 2

        if new > 100:
            new = 100
        if new < 0:
            new = 0

        if new >= 90:
            print(new, "Excellent")
            count = count + 1

        elif new >= 75:
            print(new, "Very Good")
            count = count + 1

        elif new >= 60:
            print(new, "Good")
            count = count + 1

        elif new >= 40:
            print(new, "Average")
            count = count + 1

        else:
            print(new, "Fail")
            count = count + 1
            fail = fail + 1

        marks[i] = new

    ch = input("Do you want to continue? (yes/no): ")

    if ch == "no":
        break

print("Total Valid Students:", count)
print("Total Failed Students:", fail)
