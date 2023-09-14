# check if a number arg is within a certain range
num = 3

def check_if_num_in_range(num):

    if num in range(1, 10):
        print(True)
    else: 
        print(False)

check_if_num_in_range(num)