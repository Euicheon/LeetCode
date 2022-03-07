class Solution:
    def tribonacci(self, n: int) -> int:
        memory = [0,1,1]
        if n<3:
            return memory[n]
        for i in range(n-3):
            new = sum(memory)
            memory[0] = memory[1]
            memory[1] = memory[2]
            memory[2] = new
        return sum(memory)