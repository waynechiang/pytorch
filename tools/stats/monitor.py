#!/usr/bin/env python3
import datetime
import json
import subprocess
import sys
import time
from typing import Any, List

import psutil  # type: ignore[import]


def pip_install_psutil() -> None:
    if (
        subprocess.run(
            [sys.executable, "-m", "psutil", "--help"], capture_output=True
        ).returncode
        != 0
    ):
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "psutil"], capture_output=True
        )


def get_processes_running_python_tests() -> List[Any]:
    python_processes = []
    for process in psutil.process_iter():
        try:
            if "python" in process.name() and process.cmdline():
                python_processes.append(process)
        except Exception:
            # access denied
            pass
    return python_processes


def main() -> None:
    pip_install_psutil()

    while True:
        processes = get_processes_running_python_tests()
        stats = {
            "time": datetime.datetime.utcnow().isoformat("T") + "Z",
            "total_cpu_percent": psutil.cpu_percent(),
            "cmds": [" ".join(p.cmdline()) for p in processes],
            "per_cmd_cpu": [p.cpu_percent() for p in processes],
            "per_cmd_rss_memory": [p.memory_info().rss for p in processes],
            "per_cmd_uss_memory": [p.memory_full_info().uss for p in processes],
        }
        try:
            stats["per_cmd_pss_memory"] = [p.memory_full_info().pss for p in processes]
        except Exception:
            pass
        print(json.dumps(stats))
        time.sleep(1)


if __name__ == "__main__":
    main()
