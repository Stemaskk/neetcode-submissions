class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        """
        We need to find a bridge that will help us get from begin to end

        Initially I thought we can simply if two char from begin and a word from list is same, and the last char is same as end then we can change but I realized that we could alter the two chars as well to get that change

        So I think it would be very intuitive and easy to understand if we make a graph out of this that would hopefully connect begin and end

        So from begin and end we will make a adjacency list of words in wordlist that has two same characters

        For these characters, we also make an adjacency list, that doesn't already have a connection. Like from first example, sag would have adjacency for dag and bag, but dag shouldn't connect to bag since that would create a cycle

        So we will have a set that keeps track of what has already been connected

        I think we should make an adjacency list using a hashmap, so we can have for each key, its adjacency.

        First after we make a set that has all of the words in wordlist, we move on to making it for the end

        If we find any word from the begin set, then we know for sure the conversion can happen

        But if we didn't find any then we know we can't, so we will just return 0 early

        So now we have this, we will do a DFS from the begin word

        When DFS is done, we should reach endWord if the connection is there
        For each DFS call, we will have a count

        Output the minimum count

        Count originally initialized to infinity

        Oh and also for each adjacent word, we will make a adjacency list

        This should be an undirectional graph since each adjacent word should be able to go both ways

        When we do DFS the way to exclude the previous word is to have a set to hold the path we have went through, we remove it after we remove it from the stack that we use to implement DFS

        That being said, we do not need to iterate through all posibilities if we use a BFS, since first found is bound to be shortest

        We will expand from both sides, and to make sure we are minimizing the amount of search we will do, we will do a bfs on a side with shorter queue, so it will be mroe efficient

        """
        def isAdjacent(currWord, adjWord):
            flag = False
            for i in range(len(currWord)):
                if currWord[i] != adjWord[i]:
                    if flag:
                        return False
                    flag = True
            return flag

        words = set(wordList)
        if endWord not in words:
            return 0

        distBegin = {beginWord: 1}
        distEnd = {endWord: 1}
        queueBegin = deque([beginWord])
        queueEnd = deque([endWord])

        while queueBegin and queueEnd:
            if len(queueBegin) > len(queueEnd):
                queueBegin, queueEnd = queueEnd, queueBegin
                distBegin, distEnd = distEnd, distBegin

            for i in range(len(queueBegin)):
                curr = queueBegin.popleft()

                for word in words:
                    if word in distBegin or not isAdjacent(curr, word):
                        continue
                    if word in distEnd:
                        return distBegin[curr] + distEnd[word]

                    distBegin[word] = distBegin[curr] + 1
                    queueBegin.append(word)

        return 0
