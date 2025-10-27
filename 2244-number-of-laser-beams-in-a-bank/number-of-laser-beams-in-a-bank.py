class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev_device_count = 0
        total_beams = 0

        for row in bank:
            current_device_count = row.count("1")

            if current_device_count > 0:
                total_beams += prev_device_count * current_device_count
                prev_device_count = current_device_count

        return total_beams