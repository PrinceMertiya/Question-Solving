class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        amt = [0] * (amount + 1)

        amt[0] = 1

        for i in range(len(coins)):
            for j in range(coins[i] , amount + 1):
                amt[j] += amt[j - coins[i]]


        return amt[amount]        