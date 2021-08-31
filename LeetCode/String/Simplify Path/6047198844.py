class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for directory in path.split('/'):         # / 로 나눠보자
            #..일경우 상위 directory으로 올라간다. 상위 directory는 ..으로 표현된다.
            if directory == '..':
                if stack:
                    stack.pop()
            elif directory and directory != '.':
                stack.append(directory)
        return '/' + '/'.join(stack)