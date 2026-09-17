class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_dict = {}

        for num in nums:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        
        sorted_items = sorted(num_dict.items(), key=lambda x:x[1], reverse=True)
        print(sorted_items)
        result = []
        i = 0
        while k > 0:
            result.append(sorted_items[i][0])
            k -= 1
            i += 1
        return result


        


        
            

        