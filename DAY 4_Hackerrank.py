# HackerRank Practice
# Name: Diksha Tiwari


# Solve Me First

def solve_me_first(a,b):
    return a+b

x = int(input())
y = int(input())

print(solve_me_first(x,y))


# Array Sum

def array_sum(arr):
    total = 0
    for i in arr:
        total += i
    return total

n = int(input())
arr = list(map(int,input().split()))

print(array_sum(arr))


# Find largest and smallest

def find_values(ar):

    large = ar[0]
    small = ar[0]

    for i in ar:
        if i > large:
            large = i
        if i < small:
            small = i

    print("Largest:",large)
    print("Smallest:",small)


size = int(input("Enter size: "))
data = []

for i in range(size):
    val = int(input("Enter value: "))
    data.append(val)

find_values(data)


# Remove duplicates

def remove_dup(lst):

    new_list = []

    for item in lst:
        if item not in new_list:
            new_list.append(item)

    return new_list


nums = list(map(int,input().split()))
print(remove_dup(nums))
