"""Entry script"""

from typing import Sequence

from app import Overlord


def main(argv: Sequence[str] | None = None):
    app = Overlord()
    app.begin()


if __name__ == '__main__':
    main()
