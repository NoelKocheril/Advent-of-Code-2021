from utils.solutionBase import SolutionBase


class Solution(SolutionBase):
    def part_01(self, data: list[str]) -> int:
        horPos, vertPos = 0, 0  # initial horizontal and vertical position to 0

        for entry in data:
            movement, amount = entry.split()
            amount = int(amount)

            if movement == "forward":
                horPos += amount
            elif movement == "up":
                vertPos -= amount
            elif movement == "down":
                vertPos += amount
            else:
                raise ValueError("Invalid movement")

            # print(f"We are moving {movement} by {amount} amount")

        return horPos * vertPos

    def part_02(self, data: list[int], slidingWindowSize: int = 3) -> int:
        horPos, vertPos, aim = 0, 0, 0  # initial horizontal and vertical position to 0

        for entry in data:
            movement, amount = entry.split()
            amount = int(amount)

            if movement == "forward":
                horPos += amount
                vertPos += aim * amount
            elif movement == "up":
                aim -= amount
            elif movement == "down":
                aim += amount
            else:
                raise ValueError("Invalid movement")

            # print(f"We are moving {movement} by {amount} amount")

        return horPos * vertPos
