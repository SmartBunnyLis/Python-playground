# Multiples
# Part I - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and
# don't use a list to do this exercise.
for i in range(1, 1000):
    if i % 2 != 0:
        print i

# Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.
i = 5
while( i < 1000001):
    print i
    i += 5
# Sum List
# Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in a:
    sum += i
print sum

# Average List
# Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
x = [1, 2, 5, 10, 255, 3]
sum = 0
for i in x:
    sum += i
print sum / len(x)
