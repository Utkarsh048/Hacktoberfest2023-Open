class Solution(object):
    def kthGrammar(self, n, k):
        # Base case: if n is 1, the first row has only one symbol '0'
        if n == 1:
            return 0
        # Calculate the kth symbol in the (n-1)th row
        prev_row_k = (k + 1) // 2
        prev_symbol = self.kthGrammar(n - 1, prev_row_k)
        # If the previous symbol is 0, the kth symbol in the nth row is 0 if k is odd, and 1 if k is even
        # If the previous symbol is 1, the kth symbol in the nth row is the opposite of the previous symbol
        if prev_symbol == 0:
            return 0 if k % 2 == 1 else 1
        else:
            return 1 if k % 2 == 1 else 0

# Example usage:
solution = Solution()
print(solution.kthGrammar(2, 1))  # Output: 0
