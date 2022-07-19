#!/usr/bin/env python3
import subprocess
import sys
import time

import psutil  # type: ignore[import]


def main() -> None:
    if (
        subprocess.run(
            [sys.executable, "-m", "psutil", "--help"], capture_output=True
        ).returncode
        != 0
    ):
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "psutil"], capture_output=True
        )
    while True:
        print(psutil.cpu_percent())
        time.sleep(0.5)


if __name__ == "__main__":
    main()
