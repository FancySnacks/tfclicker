"""Entry script"""

from typing import Sequence

from app import Overlord


def main(argv: Sequence[str] | None = None):
    app = Overlord()
    app.begin()

    while 1:
        ask = str(input("Click?")).lower()
        if ask == "y":
            app.mouse_click()


if __name__ == '__main__':
    main()
