import argparse, importlib
from rich.console import Console
from rich.markdown import Markdown
from os.path import dirname, abspath


def main():
    parser = argparse.ArgumentParser(description="Advent of Code Solution Runner")

    parser.add_argument(
        "-d",
        "--day",
        dest="day",
        required=True,
        default=1,
        metavar="day_number",
        type=int,
        help="Required, Day Number of the Advent of Code event",
    )

    parser.add_argument(
        "-p",
        "--part ",
        dest="part",
        required=True,
        default=1,
        metavar="part_number",
        type=int,
        help="Required, Part Number of the Day of the Advent of Code event",
    )

    parser.add_argument(
        "-m",
        "--markdown",
        dest="markdown",
        action="store_true",
        required=False,
        default=False,
        help="Whether to display the markdown of the problem",
    )

    args = parser.parse_args()
    console = Console()

    if args.markdown:
        d = dirname(abspath(__file__))
        fileName = f"{d}/problemDescriptions/day{args.day:02d}.md"

        try:
            with open(fileName, "r+") as md_file:
                console.print(Markdown(md_file.read()))
            console.print("\n")

        except FileNotFoundError:
            console.print(
                f"Could not find the requested Markdown File: '{fileName}'",
                style="bold red",
            )

    if not 1 <= args.day <= 25:
        console.print("Day Argument must be between 1 and 25 (Inclusive)")
        exit()
    elif args.part not in [1, 2]:
        console.print("Part Argument must be 1 or 2")
        exit()
    else:
        try:
            moduleName = f"Solutions.day{args.day:02d}"

            sol = importlib.import_module(moduleName).Solution(args.day)

            console.print(
                Markdown(f"# Solution - Day {args.day:02} / Part {args.part:02d}")
            )
            console.print("\n")

            console.print(f"the answer is {sol.solve(part_num=args.part)}")

        except ModuleNotFoundError:
            console.print(f"Could Not Find the Module '{moduleName}'", style="bold red")


if __name__ == "__main__":
    main()
