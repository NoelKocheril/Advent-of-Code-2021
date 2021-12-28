from utils.solutionBase import SolutionBase


class Solution(SolutionBase):
    def part_01(self, data: list[str]) -> int:
        countOfEntries = len(data)
        # print(f"There are {countOfEntries} entries")

        lengthOfBinaryString = len(data[0])
        # print(f"The length of the binary string is {lengthOfBinaryString}")

        countOfOnes = [0 for x in range(lengthOfBinaryString)]
        # print(countOfOnes)

        for entry in data:
            for idx, c in enumerate(entry):
                if c == "1":
                    countOfOnes[idx] += 1

        # print(f"There are {countOfOnes} one(s)")

        gammaString = ""
        epsilonString = ""

        for count in countOfOnes:
            gammaString += "1" if count > (countOfEntries - count) else "0"
            epsilonString += "0" if count > (countOfEntries - count) else "1"

        # print(
        #     f"The gamma string is {gammaString} and the epsilon string is {epsilonString}"
        # )

        return int(gammaString, 2) * int(epsilonString, 2)

    def part_02(self, data: list[int], slidingWindowSize: int = 3) -> int:

        return -1
