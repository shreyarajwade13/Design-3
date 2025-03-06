# Recursive approach --
# TC - O(N + L) - there will be a total of NNN loop iterations. Therefore,
# the time complexity is the number of lists plus the number of integers, giving us O(N+L)O(N + L)O(N+L)
# SC - O(N) - check editorial solution #1

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self._integer = []
        # to keep track of the next element
        self.position = -1

        def flattenList(nested_list):
            for nestedInteger in nested_list:
                # check if the curr element is an integer
                if nestedInteger.isInteger():
                    # get the integer
                    self._integer.append(nestedInteger.getInteger())
                else:
                    # get list to flatten it
                    flattenList(nestedInteger.getList())

        flattenList(nestedList)

    def next(self) -> int:
        self.position += 1
        return self._integer[self.position]

    def hasNext(self) -> bool:
        return self.position + 1 < len(self._integer)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())