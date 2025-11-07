import math
from typing import List

class Solution:
    
    def check(self, target_power: int, stations: List[int], r: int, k: int) -> bool:
        n = len(stations)
        
        initial_power = [0] * n
        power_diff = [0] * (n + 1)

        for i in range(n):
            start = max(0, i - r)
            end = min(n - 1, i + r)
            power_diff[start] += stations[i]
            power_diff[end + 1] -= stations[i]

        current_power = 0
        for i in range(n):
            current_power += power_diff[i]
            initial_power[i] = current_power

        added_power_diff = [0] * (n + 1)
        stations_needed = 0
        current_added_power = 0

        for i in range(n):
            current_added_power += added_power_diff[i]
            
            total_power = initial_power[i] + current_added_power

            if total_power < target_power:
                needed = target_power - total_power
                
                stations_needed += needed
                if stations_needed > k:
                    return False

                current_added_power += needed
                
                end_effect_plus_1 = min(n, i + 2 * r + 1)
                
                if end_effect_plus_1 <= n:
                    added_power_diff[end_effect_plus_1] -= needed
        
        return True

    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)

        low = 0
        high = sum(stations) + k
        ans = 0

        while low <= high:
            mid = low + (high - low) // 2
            
            if self.check(mid, stations, r, k):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans