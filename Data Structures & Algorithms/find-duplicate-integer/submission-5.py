class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        """
        Simple brute force way is to make a set that has all the values, and if it is already in the set then we return that valeu

        However the question asks for O(1) space:

        From what I think we can store: ints, chars, bools

        What if we perform a sort and if we see two same values we return that value?

        But that would take too long and it modifies the original array, Scrap

        You know for sure there is going to be one and only answer

        What if you have n that starts from 1, then goes up by 1;

        We look through all of the list every number, and see if there is more than one: Works

        Done, but too inefficient: we use space O(1) but it is O(n^2) speed

        New algorithem needed

        Another thing to note from the examples:

        There is a posibility that a value may not exist

        Lets try setting a middle value so we have a value to be compared to?  

        There are cases where values may be omitted, scrapped
        """

        """
        #To get through the values which is n + 1
        for i in range(len(nums)):
            seen = False

            # Iterate through the whole list
            for j in range(len(nums)):
                if nums[j] == i:
                    if seen:
                        return i
                    seen = True

        """

        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        new = 0

        while slow != new:
            new = nums[new]
            slow = nums[slow]
        
        return new
        