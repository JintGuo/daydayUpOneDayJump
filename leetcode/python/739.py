class Solution(object):

  def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        ret = [0 for _ in range(len(T))]
        # 当前元素 < 栈顶元素，当前元素入栈
        # 当前元素 > 栈顶元素，栈顶元素出栈，while 循环 直到栈顶元素 < 当前元素，当前元素入栈 
        for i, x in enumerate(T):
            while stack and T[stack[-1]] < x:
                index = stack.pop()
                ret[index] = i - index        # 出栈时索引距离即天数差
            stack.append(i)
        return ret
        
        
    def dailyTemperatures_2(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        # 类似桶排序 https://zhuanlan.zhihu.com/p/109499004
        ret = [0 for _ in range(len(T))]
        index = [0 for _ in range(101)]         # 跟据温度值的范围[30,100] 设定桶的范围

        for i in range(len(T)-1, -1, -1):
            for j in range(T[i]+1, 101):
                if index[j] != 0 and (ret[i] == 0 or ret[i] > index[j]-i):
                    ret[i] = index[j] - i
            index[T[i]] = i
        return ret
        
        
