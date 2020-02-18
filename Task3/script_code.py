import threading
from concurrent.futures import ThreadPoolExecutor

lock = threading.Lock()


def function(arg):
    a = 0
    for _ in range(arg):
        lock.acquire()
        try:
            a += 1
        finally:
            lock.release()
    return a


def main():

    a = 0
    with ThreadPoolExecutor(max_workers=5) as executor:
        for _ in range(5):
            future = executor.submit(function, 1000000)
            a += future.result()

    print("----------------------", a)


if __name__ == "__main__":
    main()