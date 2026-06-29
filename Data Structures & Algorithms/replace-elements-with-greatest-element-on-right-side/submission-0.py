class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1):
            j = i+1
            max_num = arr[j]
            while j < len(arr):
                if arr[j] >= max_num:
                    arr[i] = arr[j]
                    max_num = arr[j]
                j += 1
            
        
        arr[-1] = -1
            
        return arr