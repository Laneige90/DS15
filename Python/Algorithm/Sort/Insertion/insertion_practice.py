import random
import insertion_module_02 as im2

if __name__ == '__main__':

    nums = random.sample(range(1,21),10)

    result1 = im2.sortInsert(nums)
    print(result1)

    result2 = im2.sortInsert(nums, asc=False)
    print(result2)