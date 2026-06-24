import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed


# simulating some I/O-bound task
def download_file(file_id):
    print(f"{threading.current_thread().name} downloading file {file_id}")
    time.sleep(5)
    print(f"{threading.current_thread().name} download complete")
    return "Download Complete for" + str(file_id)


def main():
    files = range(1, 11)  # file id will range from 1 to 10
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = []
        for file_id in files:
            future = executor.submit(download_file, file_id)
            futures.append(future)

        # [<Future at 0x1016b4ad0 state=running>, <Future at 0x1015e3250 state=running>, <Future at 0x1015e39d0 state=running>, <Future at 0x101501a70 state=pending>, <Future at 0x1015c3360 state=pending>, <Future at 0x101481370 state=pending>, <Future at 0x10149ecf0 state=pending>, <Future at 0x1015a69c0 state=pending>, <Future at 0x1016cc150 state=pending>, <Future at 0x1016cc350 state=pending>]
        # wait until each future moves from pending/running to completed or failed
        for future in as_completed(futures):
            print(future.result())


if __name__ == "__main__":
    main()
