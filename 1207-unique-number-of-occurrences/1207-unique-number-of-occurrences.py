class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        for i in arr:
            dic[i] = dic.get(i, 0) + 1
        return len(dic.values()) == len(set(dic.values()))