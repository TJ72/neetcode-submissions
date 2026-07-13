class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for o in operations:
            if o == "C":
                stack.pop()
            elif o == "D":
                score = stack[-1] * 2
                stack.append(score)
            elif o == "+":
                score = stack[-1] + stack[-2]
                stack.append(score)
            else:
                stack.append(int(o))
        return sum(stack)