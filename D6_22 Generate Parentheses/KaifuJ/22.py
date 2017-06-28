class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def generate_parenthesis_help(cur, left, right, result):
            if right == 0:
                result.append(cur)
            if left:
                generate_parenthesis_help(cur + '(', left - 1, right, result)
            if right > left:
                generate_parenthesis_help(cur + ')', left, right - 1, result)
            return result

        return generate_parenthesis_help('', n, n, [])

a =  Solution()
print(a.generateParenthesis(3))