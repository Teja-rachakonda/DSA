class Solution:
    def isValid(self, s: str) -> bool:
        dict = { "]": "[", "}": "{", ")": "("}
        stack = []
        
        for i in s:
            if i == "[" or i == "(" or i == "{":
                stack.append(i)
            else:
                z = dict[i]
                if stack:
                    if stack[-1] != z:
                        return False
                    else:
                        stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
