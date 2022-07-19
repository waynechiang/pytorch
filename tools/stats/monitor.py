#!/usr/bin/env python3
import psutil
import time


def main() -> None:
    while True:
        print(psutil.cpu_percent())
        time.sleep(.5)


if __name__ == "__main__":
    main()
