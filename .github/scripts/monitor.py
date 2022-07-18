import psutil
import time


def main():
    print(psutil.cpu_percent())
    time.sleep(.5)


if __name__ == "__main__":
    main()
