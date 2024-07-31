class Solution(object):
    def topKFrequent(self, nums, k):
        #Create a HashMap to keep track of how many elements a specific number has
        count_number = {}
        
        #Creates an array thats holds a singular [] in each index. Meant to store the lowest to the highest counted element
        
        freq = []
        for i in range(0,len(nums) + 1):
            freq.append([])

        #Organizes hashmap to display the count of elements for each number
        for i in nums:
            count_number[i] = 1 + count_number.get(i,0)
        
        #Puts each number in lowest to greatest order in terms of indexes
        for n, c in count_number.items():
            freq[c].append(n)

        result = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                result.append(j)
                if len(result) == k:
                    return result


        

