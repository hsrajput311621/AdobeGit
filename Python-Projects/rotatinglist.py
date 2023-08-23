# nums: [0 ,3 ,5, 7, 9, 11, 13, 15] rotated [15,13,11,9,7,5,3,0]
#        0  1  2  3  4   5   6   7
#       mid = 4 , nums[mid] = 9
#

def count_rotation_linear(nums):
    position = 0
    while position < len(nums):
        if position > 0 and nums[position] < nums[position]-1:
            return position

        position +=1

    return -1

s=count_rotation_linear([6,7,2,3,4,5])
print(s)

