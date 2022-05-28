from time import sleep
from datetime import datetime
from CustomExecutor import CustomExecutor


def longRunningTask(el: int):
    sleep(2)
    return el ** 2


if __name__ == '__main__':
    executor = CustomExecutor(max_workers=3)

    element = executor.execute(longRunningTask, 10)
    print(f"{datetime.now().strftime('%H:%M:%S')} - {element.future.result()}")

    futures = executor.map(longRunningTask, list(range(10)))
    for f in futures:
        print(f"{datetime.now().strftime('%H:%M:%S')} - {f.future.result()}")

    executor.shutdown()
