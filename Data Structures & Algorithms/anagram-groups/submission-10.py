class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)
        result = []

        for string in strs:
            key = str(sorted(string))
            groups[key].append(string)

        for group in groups:
            result.append(groups[group])

        return result