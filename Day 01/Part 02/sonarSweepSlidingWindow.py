from typing import List


def calculateDepthIncreases(measurements: List[int], slidingWindowSize: int = 3) -> int:
    """
    Provided a sliding window size and a list of integer in chronological order, we return the number of times that the depth increases across windows of the provided size.

    @param measurements: a list of integer in chronological order
    @param slidingWindowSize: a sliding window size (Default Value: 3)
    @return: the number of times that the depth decreases
    """
    # Initialize count to Zero
    count: int = 0

    # Start from the sliding Window Size-th Index until the end of the array
    for idx, _curr in enumerate(
        measurements[slidingWindowSize:], start=slidingWindowSize
    ):

        # Find the current sub-array
        curr_subArray = measurements[idx - slidingWindowSize + 1 : idx + 1]

        # Find the previous sub-array
        prev_subArray = measurements[idx - slidingWindowSize : idx]

        # Calculate the difference and increment the count if the current sum is greater than the previous sum
        if sum(curr_subArray) > sum(prev_subArray):
            count += 1

    # Finally, return the count
    return count


def main():
    # Initialize the list of Measurements
    surfaceMeasurements = []

    # Grab all of the inputs until we get a empty new line
    # print("Enter Line Delimited Input of Depth Measurements:")
    # while True:
    #     line = input()
    #     if line:
    #         surfaceMeasurements.append(int(line))
    #     else:
    #         break

    surfaceMeasurements = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    print(
        f"There were {calculateDepthIncreases(surfaceMeasurements, slidingWindowSize=3)} depth increase(s)"
    )


if __name__ == "__main__":
    main()
