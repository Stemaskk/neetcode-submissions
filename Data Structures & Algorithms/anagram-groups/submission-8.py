class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = []
        hashmap = defaultdict(list)

        for i in range(len(strs)):
            keys = "".join(sorted(strs[i]))

            hashmap[keys].append(strs[i])

        for keys in hashmap:
            result.append(hashmap[keys])

        return result

