problem = '''https://www.codewars.com/kata/55983863da40caa2c900004e/train/python
Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

12 ==> 21
513 ==> 531
2017 ==> 2071

If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift):

9 ==> -1
111 ==> -1
531 ==> -1
'''

def next_bigger(n):
    nums = [int(x) for x in list(str(n))]

    for i in range(len(nums) - 1, 0, -1):
        if (nums[i] > nums[i-1]):
            temp = nums[i]
            nums[i] = nums[i-1]
            nums[i-1] = temp
            newnum = ""
            for j in nums:
                newnum += str(j)
            return newnum
    
    return -1
 
print(next_bigger(2097))
