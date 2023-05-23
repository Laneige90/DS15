import random
import rank_module as rm

nums = random.sample(range(50,100),20)

print('nums: {}'.format(nums))
rankItem = rm.itemRank(nums)








