from utils.solutionBase import SolutionBase


class Solution(SolutionBase):
    def part_01(self, data: list[int]) -> int:
        """
        Provided a list of integer in chronological order, we return the number of times that the depth increases.

        @param data: a list of integer in chronological order
        @return: the number of times that the depth decreases
        """
        # Initialize count to Zero
        count: int = 0

        data = [int(x) for x in data]

        # Start looking at data from index 1 as the first measurement is not compared to any value
        for idx, curr in enumerate(data[1:], start=1):

            # If the current measurement is greater than the previous value, then increment count
            if curr > data[idx - 1]:
                count += 1

        # Finally, return the count
        return count

    def part_02(self, data: list[int], slidingWindowSize: int = 3) -> int:
        """
        Provided a sliding window size and a list of integer in chronological order, we return the number of times that the depth increases across windows of the provided size.

        @param data: a list of integer in chronological order
        @return: the number of times that the depth decreases
        """

        # Initialize count to Zero
        count: int = 0

        data = [int(x) for x in data]

        # Start from the sliding Window Size-th Index until the end of the array
        for idx, _curr in enumerate(data[slidingWindowSize:], start=slidingWindowSize):

            # Find the current sub-array
            curr_subArray = data[idx - slidingWindowSize + 1 : idx + 1]

            # Find the previous sub-array
            prev_subArray = data[idx - slidingWindowSize : idx]

            # Calculate the difference and increment the count if the current sum is greater than the previous sum
            if sum(curr_subArray) > sum(prev_subArray):
                count += 1

        # Finally, return the count
        return count
