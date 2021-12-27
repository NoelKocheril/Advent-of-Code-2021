from utils.puzzleReader import PuzzleReader
from abc import ABC, abstractmethod
from rich.console import Console
from rich.theme import Theme


class SolutionBase(ABC):
    def __init__(self, day_num: int = -1):
        self.day_num = day_num
        self.data = PuzzleReader.get_puzzle_input(self.day_num)
        self.theme = Theme(
            {
                "info": "dim cyan",
                "failure": "bold red",
                "success": "bold green",
            }
        )
        self.console = Console(theme=self.theme)

    def get_test_input(self):
        return PuzzleReader.get_test_input(self.day_num)

    def get_test_result(self, part_num):
        return PuzzleReader.get_test_result(self.day_num, part_num)

    def solve(self, part_num: int):
        self.test_runner(part_num)

        func = getattr(self, f"part_{part_num:02d}")
        result = func(self.data)
        return result

    def test_runner(self, part_num):
        test_inputs = self.get_test_input()
        test_results = self.get_test_result(part_num)
        test_counter = 1

        func = getattr(self, f"part_{part_num:02d}")
        for i, r in zip(test_inputs, test_results):
            res = func(i)
            expected_result = int(r[0])
            if res == expected_result:
                self.console.print(
                    f":+1: Test {test_counter:02d} passed.", style="success"
                )
            else:
                self.console.print(
                    f"\n:x: Test {test_counter:02d} DID NOT passed.", style="failure"
                )

                self.console.print(
                    f":information: Expected Result: {expected_result}, Your Result: {res}. \n",
                    style="info",
                )
            test_counter += 1

    @abstractmethod
    def part_01(self, data):
        pass

    @abstractmethod
    def part_02(self, data):
        pass
