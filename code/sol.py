from concurrent.futures import thread
import gzip
import json
from threading import Thread, Lock
from datetime import datetime

threadLock = Lock()

global_counter = 0


def read_authors(path: str):
    print("Reading authors")
    with gzip.open("../authors.jsonl.gz", "rt") as f:
        for line in f:
            # print(line)
            data = json.loads(line)
            # print("Authors ")
            with threadLock:
                global global_counter
                global_counter += 1
                if global_counter % 10000 == 0:
                    print(str(datetime.now()) + str(data["id"]))


def read_conversations(path: str):
    print("Reading conversations")
    with gzip.open(path, "rt") as f:
        for line in f:
            # print(line)
            data = json.loads(line)
            # print("Conversations ")
            with threadLock:
                global global_counter
                global_counter += 1
                if global_counter % 10000 == 0:
                    print(str(datetime.now()) + str(data["id"]))


def main():
    T1 = Thread(target=read_authors, args=("../authors.jsonl.gz",))
    T2 = Thread(target=read_conversations, args=("../conversations.jsonl.gz",))

    T1.start()
    T2.start()


if __name__ == "__main__":
    main()
