class Solution(object):
    def kthDistinct(self, arr, k):
        count = 0
        map = {}

        # Count occurrences of each string
        for item in arr:
            if item in map:
                map[item] = False  # Mark as not distinct
            else:
                map[item] = True  # Mark as distinct

        # Find the k-th distinct string
        for item in arr:
            if map[item]:  # Check if it's distinct
                count += 1
                if count == k:
                    return item
        return ""



            