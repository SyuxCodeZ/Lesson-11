# the amount of terms

term = int(input("Enter The Amount Of Terms: "))

# initialize

sum = 0

x = 1

# loop

while x <= term:
    sum = sum + x

    x = x + 1

print (f"\nResult Is {sum}")