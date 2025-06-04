class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        prime = amount + 1
        amt = [prime] * (amount + 1)

        amt[0] = 0
        
        for i in range(1,amount + 1):
            for j in range(len(coins)):

                if i >= coins[j]:
                    amt[i] = min(amt[i] , amt[i - coins[j]] + 1)


        if amt[amount] < amount + 1:
            return amt[amount]

        return -1            