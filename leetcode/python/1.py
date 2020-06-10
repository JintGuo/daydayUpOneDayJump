"""
not the best solution
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: 
            return False
        return int(str(x)[::-1])+x == 2*x
        
