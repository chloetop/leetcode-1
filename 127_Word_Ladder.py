_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/word-ladder/
# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation
# sequence from beginWord to endWord, such that:
# Only one letter can be changed at a time and each intermediate word must exist in the word list

# Bidirectional depth first search.  Process wordList to be able to find neighbours.
# Time - O(n*k*k) to build graph for n words of length k. O(b^(d/2)) for bidirectional BFS with branching
# factor b and depth d
# Space - O(n*k) for graph

from collections import defaultdict

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        length = 1
        visited = set()
        wordList.add(endWord)

        graph = defaultdict(set)
        for word in wordList:                   # build a mapping of words reachable by changing one letter
            for i in range(len(word)):
                wildcard = word[:i] + '_' + word[i+1:]
                graph[wildcard].add(word)

        front, back = {beginWord}, {endWord}    # frontiers in both directions

        while front:

            if front & back:                    # intersection between frontiers
                return length

            new_front = set()
            for word in front:

                visited.add(word)               # add word to set of those already removed from frontiers

                for i in range(len(word)):      # add reachable words to frontier
                    next_words = graph[word[:i] + '_' + word[i+1:]]
                    next_words -= visited       # apart from if already removed from a frontier
                    new_front |= next_words

            length += 1
            front = new_front

            if len(back) < len(front):      # expand the smaller frontier next
                front, back = back, front

        return 0

