from threading import Thread
import time


def func1(delay, repeats):
    while repeats > 0:
        print("This is message # " + str(11-repeats))
        repeats -= 1
        time.sleep(delay)


def func2(delay, repeats):
    while repeats > 0:
        word = input("Enter a word and I will repeat it: ")
        print(word)
        time.sleep(delay)
        repeats -= 1

f1 = Thread(target=func1, args=(1, 10))
f2 = Thread(target=func2, args=(2, 5))
f1.start()
f2.start()

# if you "join" the threads to the main program, they will not die when the main program dies.
# The main program will wait for each thread to finish before exiting.
f1.join()
f2.join()