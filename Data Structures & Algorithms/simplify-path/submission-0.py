class Solution:
    def simplifyPath(self, path: str) -> str:
        splitPath = [x for x in path.split("/") if x]
        
        stack = []

        for cmd in splitPath:
            if cmd == ".":
                continue
            elif cmd == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(cmd)
        return "/" + "/".join(stack)
