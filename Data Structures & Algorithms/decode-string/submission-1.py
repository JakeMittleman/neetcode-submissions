class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        i = 0
        
        while i < len(s):
            if s[i].isnumeric():
                q = ""
                while s[i].isnumeric():
                    q += s[i]
                    i += 1

                stack.append(q)
            elif s[i] == "]":
                val = ""
                while stack[-1] != "[":
                    val += stack.pop()

                stack.pop()
                stack.append(val * int(stack.pop()))
                i += 1

            else:
                stack.append(s[i])
                i += 1

        res = ""
        while stack:
            res += stack.pop()
        return res[::-1]