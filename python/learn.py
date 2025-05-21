# # # Define two numbers
# # a = 4939399939
# # b = 48484

# # # Perform addition
# # sum_result = a + b

# # # Perform subtraction
# # sub_result = a - b

# # # Perform division
# # sub_result = a/b

# # # Print results
# # print("Addition (Sum):", sum_result)
# # print("Subtraction (Difference):", sub_result)
# # print("division (div):", sub_result)

# float example
# name1 = 'mj'
# name2 = "mj"
# name3 = '''mj'''

# print (name1)
# print (name2)
# print (name3)

# # age = 25
# # old = False
# # a = None
# # print (type(old))
# # print(type(a))


# # str = "Mahesh jadhav"
# # ch = str[0:13]  # This will get characters from index 0 to 5 (6 is excluded)
# # print(ch)

# #slicing 
# # str = "mahesh jadhav"
# # print = (str[0:len(str)])
# # print =(ch)

# # conditional statement
# # age = 14

# if (age <=18):
#     print ("can vote")
# else:
#     print("cant vote") 

# # example

# def grade_student(marks):
#     if marks >= 90:
#         return "A"
#     elif marks >= 80:
#         return "B"
#     elif marks >= 70:
#         return "C"
#     else:
#         return "D"

# # Example usage
# marks_list = [95, 85, 72, 60, 88]
# for marks in marks_list:
#    print(f"Marks: {marks}, Grade: {grade_student(marks)}")


# array = [1, 4, 2, -2, -9, 10, 2, 12, 2, -4, -4, -4, -4, 2, 6, 7]
# peak = array[0]
# index = 0
# output = []  # list of tuples

# # Loop through the array starting from the second element
# for x in range(1, len(array)):
#     if array[x] * array[x - 1] > 0:  # Check if the signs of the current and previous elements are the same
#         if peak < 0 and array[x] < peak:
#             peak = array[x]
#             index = x
#         elif peak >= 0 and array[x] > peak:
#             peak = array[x]
#             index = x
#     else:
#         output.append((index, peak))  # Add the peak to the output list
#         peak = array[x]  # Reset peak for the next segment
#         index = x  # Update the index

# # Return or print the final output
# print(output)

# array = [1, 4, 2, -2, -9, 10, 2, 12, 2, -4, -4, -4, -4, 2, 6, 7]
# peak = array[0]
# index = 0
# output = []  # list of tuples

# # Loop through the array starting from the second element
# for x in range(1, len(array)):
#     if array[x] * array[x - 1] > 0:  # Check if the signs of the current and previous elements are the same
#         if peak < 0 and array[x] < peak:
#             peak = array[x]
#             index = x
#         elif peak >= 0 and array[x] > peak:
#             peak = array[x]
#             index = x
#     else:
#         output.append((index, peak))  # Add the peak to the output list
#         peak = array[x]  # Reset peak for the next segment
#         index = x  # Update the index

# # Return or print the final output
# print(output)


# def longest_positive_subarray(arr):
#         max_len = 0
#         max_start = 0
#         current_len = 0
#         current_start = 0

#         for i in range(len(arr)):
#             if arr[i] > 0:
#                 if current_len == 0:
#                     current_start = i
#                 current_len += 1
#                 if current_len > max_len:
#                     max_len = current_len
#                     max_start = current_start
#             else:
#                 current_len = 0  # reset

#         return arr[max_start:max_start + max_len]

# print(longest_positive_subarray([1, 2, -3, 4, 5, 6, -1, 2, 3]))

# name = "mahesh"
# age = "25"
# print (name, age)

#mahesh jadhav    

#learning numeric datatype 
# a= 10
# b= 2.22
# c= 2 + 3j
# print (type(a), type(b), type(c))

# Ask the user for their age
# age = int(input("Enter your age: "))

# # Check voting eligibility
# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")


# age = int(input("enter your age -"))
# if age >= 18:
#     print ("you can vote")
# else :
#     print ("if not they cannot vote")\


# langauge = ('mahesh jadhav')
# for i in langauge:
#     print(*list('mahesh jadhav'))

# lower and upper
# str = input("enter your name =").lower()
# print (str)

# find  and repalce 

# text ="mahesh jadhav"

# print (text.replace("mahesh jadhav" , "bosss"))



# a=  [1,1,2]
# b= [2,3,4]
# a.copy

# values = [5, 3, 7, 3, 9, 3]
# print(values.index(3,2))

# N = int(input())
# for i in range (1, N): print((10**i-1)//9*i)

import heapq
from typing import List, Optional

class ListNode:
    def _init_(self, val=0, next=None):
        self.val = val
        self.next = next

    # Define less-than for heap comparisons
    def _lt_(self, other):
        return self.val < other.val

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    heap = []

    # Initialize the heap with the head node of each list
    for node in lists:
        if node:
            heapq.heappush(heap, node)

    dummy = ListNode(0)
    current = dummy

    while heap:
        # Extract the smallest node from the heap
        smallest_node = heapq.heappop(heap)
        current.next = smallest_node
        current = current.next

        # If the extracted node has a next node, add it to the heap
        if smallest_node.next:
            heapq.heappush(heap, smallest_node.next)

    return dummy.next