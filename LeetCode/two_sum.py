# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        hashtable = dict()
        
        for i in range(len(nums)):
            curr = target - nums[i]
            #print(hashtable)
            if curr not in hashtable:
                hashtable[nums[i]] = i
            else:
                res.append(hashtable[curr])
                res.append(i)
                #print('res: '+ str(lis[i])+','+ str(curr))
                break
        return res


