from typing import List

def read_integers() -> List[int]:
    int_string = str(input())
    int_list = int_string.split(',')
    res = []
    for i in int_list:
        res.append(int(i))
    return res 


# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
