
import time
import platform
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / f"{datetime.now():%Y-%m-%d}.log"

def write_log(event):
    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(
            f"[{timestamp}] [{platform.system()}] {event}\n"
        )

def main():
    write_log("APPLICATION_STARTED")

    try:
        while True:
            time.sleep(60)
            write_log("APPLICATION_RUNNING")

    except KeyboardInterrupt:
        write_log("APPLICATION_STOPPED")

if __name__ == "__main__":
    main()
