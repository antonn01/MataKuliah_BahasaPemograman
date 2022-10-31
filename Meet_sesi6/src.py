from array import *
import array as arr

numbers = arr.array('i', [10, 20, 30])


print(numbers)


# an array of floating point values
numbers = array('d', [10.0, 20.0, 30.0])

print(numbers)

numbers = arr.array('i', [10, 20, 30])

print(numbers[0])  # gets the 1st element
print(numbers[1])  # gets the 2nd element
print(numbers[2])  # gets the 3rd element


numbers = arr.array('i', [10, 20, 30])

print(numbers[-1])  # gets last item
print(numbers[-2])  # gets second to last item
print(numbers[-3])  # gets first item


numbers = arr.array('i', [10, 20, 30])

# search for the index of the value 10
print(numbers.index(10))


numbers = arr.array('i', [10, 20, 30, 10, 20, 30])

# search for the index of the value 10
# will return the index number of the first instance of the value 10
print(numbers.index(10))