#Task 2: Demonstrate List Slicing 
""" 
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list
"""
list = [i for i in range(1, 11)]
print(f'Origional list: {list}')

list2 = list[0:5]
print(f'Extracted first five elements: {list2}')

list2.reverse()  # modifies list2 in-place
list3 = list2    # list3 now holds the reversed list
print('Reversed extracted elements: ', list3)
