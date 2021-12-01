from typing import List


def calculateDepthIncreases(measurements: List[int]) -> int:
    """
    Provided a list of integer in chronological order, we return the number of times that the depth increases.

    @param measurements: a list of integer in chronological order
    @return: the number of times that the depth decreases
    """
    # Initialize count to Zero
    count: int = 0

    # Start looking at measurements from index 1 as the first measurement is not compared to any value
    for idx, curr in enumerate(measurements[1:], start=1):

        # If the current measurement is greater than the previous value, then increment count
        if curr > measurements[idx - 1]:
            count += 1

    # Finally, return the count
    return count


def main():
    # Initialize the list of Measurements
    surfaceMeasurements = []

    # Grab all of the inputs until we get a empty new line
    print("Enter Line Delimited Input of Depth Measurements:")
    while True:
        line = input()
        if line:
            surfaceMeasurements.append(int(line))
        else:
            break

    print(
        f"There were {calculateDepthIncreases(surfaceMeasurements)} depth increase(s)"
    )


if __name__ == "__main__":
    main()
