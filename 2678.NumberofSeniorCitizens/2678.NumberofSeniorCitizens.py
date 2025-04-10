class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        length = len(details)
        #Iterate through list
        for i in range(0,length):
            if int(details[i][11:13]) > 60:
                count += 1

                            
        
        
        return count