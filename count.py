'''
Write the program to count the number of times the given number (x) is present in the given tuple list and print it's factorial value without using factorial() method.
Sample Input:
1 2 3 4 1 5 1
1
Sample Output:
6
'''

input_string = input("Enter the tuple values separated by spaces: ")
numbers_tuple = tuple(map(int, input_string.split()))
x = int(input("Enter the value to count: "))
count_x = numbers_tuple.count(x)
factorial = 1
for i in range(1, count_x + 1):
    factorial *= i
print(factorial)
