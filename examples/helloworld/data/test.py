import os
import time
import threading

def foo():
    i = 0
    while i < 6:
        print "foo %d" % i
        time.sleep(1)
        i += 1

def run():
    for i in xrange(10):
        print 'hello, this is python code speaking'

    count = 0
    while count < 3:
        time.sleep(1)
        print "loop %d" % count
        count += 1

    f = open("test_file", "w")
    f.write("this is python writing to a file\n")
    f.close()

    print "current directory contains:"
    print os.listdir(".")

    t = threading.Thread(target=foo)
    t.start()
    time.sleep(3)


if __name__ == "__main__":
    run()
