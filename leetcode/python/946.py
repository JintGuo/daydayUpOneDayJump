class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        j=0
        for push in pushed:
            stack.append(push)
            while stack and stack[-1]==popped[j]:
                j+=1
                stack.pop()
        if len(stack)==0:
            return True
        else:
            return False
