"""

"""

# Sword of Offer 03. Repeated Numbers in Arrays

class RepeatedNumbersInArrays(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set()

        for num in nums:
            if num in num_set:
                return num 
            else:
                num_set.add(num)
        return None