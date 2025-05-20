class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7

        color= [0,1,2]
        valid_col = []

        for col in product(color, repeat = m):

            if all(col[i] != col[i+1] for i in range(m - 1)):
                valid_col.append(col)

        complement = {}

        for c1 in valid_col:

            complement[c1] = []
            for c2 in valid_col:

                if all(a != b for a,b in zip(c1,c2)):

                    complement[c1].append(c2)


        dp = defaultdict(int)

        for col in valid_col:
            dp[col] = 1


        for _ in range(n - 1):

            new_dp = defaultdict(int)      

            for col in valid_col:
                for prev in complement[col]:

                    new_dp[col] = (new_dp[col] + dp[prev]) % MOD

            dp =  new_dp        

        return sum(dp.values()) % MOD                              