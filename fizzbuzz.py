# add your code here
# FizzBuzz program to print numbers from 1 to 100
# Replace numbers divisible by 3 with "Fizz"
# Replace numbers divisible by 5 with "Buzz"
# Replace numbers divisible by both 3 and 5 with "FizzBuzz"

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
