import sys
sys.setrecursionlimit(10**6)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        max_r = len(image)
        max_c = len(image[0])
        originColor = image[sr][sc]
        if originColor == newColor: return image
        def check(r, c):
            if image[r][c] == originColor:
                image[r][c] = newColor
                if r>=1:
                    check(r-1,c)
                if r+1 < max_r:
                    check(r+1,c)
                if c>=1:
                    check(r,c-1)
                if c+1 < max_c:
                    check(r,c+1)
        check(sr,sc)
        return image