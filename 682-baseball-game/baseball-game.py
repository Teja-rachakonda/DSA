class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(len(operations)):
            if operations[i] == "D":
                z = stack[-1]
                stack.append(2 * z)
            elif operations[i] == "C":
                stack.pop(-1)
            elif operations[i] == "+":
                z = stack[-1]
                zz = stack[-2]
                stack.append(z + zz)
            else:
                stack.append(int(operations[i]))
        return sum(stack)
        