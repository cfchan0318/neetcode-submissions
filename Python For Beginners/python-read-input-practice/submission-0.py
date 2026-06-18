def add_two_numbers() -> int:
    two_num_str = input()
    nums = two_num_str.split(',')
    nums_sum = 0
    for i in nums:
        nums_sum += int(i)
    return nums_sum



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
