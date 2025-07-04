"""Entry point for the project."""
import argparse
from app import App


def parse_args():
    parser = argparse.ArgumentParser(
        description="Run a finite state machine simulation based on binary input and modulo."
    )
    parser.add_argument(
        "--input", "-i", required=True, help="Binary input string such as 10101"
    )
    parser.add_argument(
        "--modulo", "-m", type=int, required=True, help="Modulo value needed for the FSM"
    )

    parser.add_argument(
        "--debug", "-d", action="store_true", help="If set, debug mode gets more extensive logs for the simulation"
    )
    return parser.parse_args()


def main():
    args = parse_args()
    app = App(input_str=args.input, modulo=args.modulo, debug=args.debug)
    remainder = app.run_simulation()
    print(remainder)

if __name__ == "__main__":
    main()
