class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        result = s[0]

        if len(s) == 1:
            return s

        for i in range(1, len(s) - 1):
            prev, next = i - 1, i + 1
            resultOdd = s[i]
            resultEven = s[prev] + s[i]
            prevEven = i - 2

            isEven = False
            if s[prev] == s[i]:
                isEven = True

            while prev >= 0 and next < len(s):
                cont = False

                if s[prev] == s[next]:
                    resultOdd = s[prev] + resultOdd + s[next]
                    prev -= 1
                    cont = True

                if isEven and prevEven >= 0 and s[prevEven] == s[next]:
                    resultEven = s[prevEven] + resultEven + s[next]
                    prevEven -= 1
                    cont = True

                if len(resultOdd) > len(result):
                        result = resultOdd

                if isEven and len(resultEven) > len(result):
                        result = resultEven

                if not cont:
                    break

                next += 1


        if len(result) < 2 and s[-1] == s[-2]:
            result = s[-2] + s[-1]

        return result
                
            