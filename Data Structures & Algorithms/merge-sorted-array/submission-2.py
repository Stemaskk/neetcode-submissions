class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.


        Brute force is to go index by index in nums2, and we loop through nums1 and if we find a index in nums1 that is greater than the current index in nums2 then we append it in there

        But this results in O(m + n) time complexity assuming m = nums1 n = nums2

        We want to go more efficient

        As we are iterating through the nums1 list if we find an index that its value is greater than the current values in nums2, we keep appending it in between it?

        Scrap, since the insert itself would have to shift all values in num1, worst case is still O(m + n)

        What if we group integers within nums2 into groups for ones that are being put in between same index in nums1

        Then we rebuild the nums1 list by creating a new list and making nums1 = to it
        
        A bit less efficient in space complexity but it will allow us to have O(m)

        We will append value that is smaller between nums1's index value and nums2's group's first value, whichever is smaller is extended into the result list

        After interviewer's hint, I realized that we can use nums2 as a place holder of next value. So when we have nums1 and nums2's first index, whichever is smaller, will be swapped, so index1's original value is stored in num2's first value. But if we use only the first index in nums2 then we miss the actual num2's values

        We need a variable that will hold the current position in nums2 that has the first index of the nums2 value

        From interviewer's input, I realized I have been too fixated from adding from start
        We check the last value of num1 and num2 using the given m and n, whichever is bigger will go into the very back of num1 where its initialzied 0, and we will continue until we have reached either 0th index on num1 or num2


        """
        index = 1
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[-index] = nums1[m - 1]
                m -= 1
            else:
                nums1[-index] = nums2[n - 1]
                n -= 1
            index += 1

        while n > 0:
            nums1[-index] = nums2[n - 1]
            n -= 1
            index += 1
        