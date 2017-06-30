import copy
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        temp_result = []
        result = []
        left = ['(']*n
        right = [')']*n
        for i in range(2*n):
            temp_result = self.judge(i,temp_result,n)
        for i in temp_result:
            result.append("".join(i))
        return result
    def judge(self,step,result,size):
        temp_result = copy.deepcopy(result)
        if temp_result != []:
            for i in range(len(temp_result)):
                each = temp_result[i]
                left_count = each.count('(')
                right_count = each.count(')')
                if left_count > right_count:
                    if left_count < size:
                        result[result.index(each)].append('(')
                    else:
                        result[result.index(each)].append(')')
                    if left_count != size:
                        each.append(')')
                        result.append(each)
                elif left_count == right_count and left_count < size:
                    result[result.index(each)].append('(')
                else:
                    pass
        else:
            result.append(['('])
        return result
