'''
Write a program to get the tuple values in a single line separated by space and count the nuber of times the given x value is present in the given tuple.
Sample Input:
1 2 3 1 2 3 4 1 2 1
1
Sample Output:
4
'''

input_string = input("Enter the tuple values separated by spaces: ")
numbers_tuple = tuple(map(int, input_string.split()))
x = int(input("Enter the value to count: "))
count_x = numbers_tuple.count(x)
print(count_x)

