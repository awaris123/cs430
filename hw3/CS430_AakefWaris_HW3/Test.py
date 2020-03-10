
import matplotlib.pyplot as plt
import random
import time
class TestMachine:

    @staticmethod
    def timeIt(func, data):
        start = ((time.time() * 1000))
        func(data)
        stop = ((time.time() * 1000))

        return (stop-start), len(data)


    @staticmethod
    def createBatch():
        def genTest(size=100):
            return [random.randint(-9999, 9999)for _ in range(size)]
        return [genTest(size) for size in range(0, 100000, 10000)]


class TestResults:


    COUNTER = 1

    def __init__(self, name):
        self.times = []
        self.sizes = []
        self.name = name
        self.fig_num = TestResults.COUNTER
        TestResults.COUNTER += 1


    def addResult(self, time_n_size):
        self.times.append(time_n_size[0])
        self.sizes.append(time_n_size[1])
    
    def visualize(self):
        plt.close()
        plt.figure(self.fig_num)
        plt.ylim(0, 2500)
        plt.title(self.name, loc="center")
        plt.xlabel("input size")
        plt.ylabel("Time(ms)")
        plt.plot(self.sizes, self.times)
        plt.show()
        