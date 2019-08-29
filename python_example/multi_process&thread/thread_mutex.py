#!/usr/bin/python
from multiprocessing import Pool, Process, Lock

mutex = Lock()


def IncreaseX():
    with mutex:
        print "mutex is got"
        global x
        x = x + 1
        print("x now is %d" % x)


def DecreaseX():
    with mutex:
        print "Decrease x"
        global x
        x = x - 1
        print("x now is %d" % x)


def main():
    #    while True:
    pplus = Process(target=IncreaseX)
    # pminus = Process(target=DecreaseX)
    pplus.start()
    # pminus.start()


if __name__ == "__main__":
    x = 1
    main()