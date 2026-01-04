class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total_sum = 0
        for num in nums:
            count = 0
            div_sum = 0
            for i in range(1, int(num**0.5) + 1):
                if num % i == 0:
                    count += 1
                    div_sum += i

                    if i * i != num:
                        count += 1
                        div_sum += num // i

                    if count > 4:
                        break
            if count == 4:
                total_sum += div_sum
        return total_sum