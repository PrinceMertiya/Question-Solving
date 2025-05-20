class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10** 9 + 7

        color = [0,1,2]
        valid_col = []

        for col in product(color , repeat = 3):
            if col[0] != col[1] and col[1] != col[2]:
                valid_col.append(col)


        complemet = defaultdict(list)

        for c1 in valid_col:
            for c2 in valid_col:

                if all(c1[i] != c2[i] for i in range(3)):
                    complemet[c1].append(c2)

        dp = defaultdict(int)

        for col in valid_col:
            dp[col] = 1


        for _ in range(n - 1):

            new_dp = defaultdict(int)
            for col in valid_col:
                for prev in complemet[col]:
                    new_dp[col] = (new_dp[col] + dp[prev]) % MOD


            dp = new_dp

        return sum(dp.values()) % MOD                            
        