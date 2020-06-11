class Solution(object):

  def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        ret = [0 for _ in range(len(T))]
        for i, x in enumerate(T):
            while stack and T[stack[-1]] < x:
                index = stack.pop()
                ret[index] = i - index
            stack.append(i)
        return ret
        
        
    def dailyTemperatures_2(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        ret = [0 for _ in range(len(T))]
        index = [0 for _ in range(101)]

        for i in range(len(T)-1, -1, -1):
            for j in range(T[i]+1, 101):
                if index[j] != 0 and (ret[i] == 0 or ret[i] > index[j]-i):
                    ret[i] = index[j] - i
            index[T[i]] = i
        return ret
        
        
