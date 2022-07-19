#!/usr/bin/env python3
import time

import psutil  # type: ignore[import]


def main() -> None:
    while True:
        print(psutil.cpu_percent())
        time.sleep(0.5)


if __name__ == "__main__":
    main()
