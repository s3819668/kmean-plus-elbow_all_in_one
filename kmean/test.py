import multiprocessing as mp
import os


class Dosomething:
    def __init__(self):
        self.p_list = []

    def dosomething(self, i):
        print('第' + str(i))
        print('多程序 ID:' + str(os.getpid()))

    def run(self):
        for i in range(5):
            self.p_list.append(
            mp.Process(target=self.dosomething, args=(str(i))))
            self.p_list[i].start()

        for i in self.p_list:
            i.join()


if __name__ == "__main__":
    d = Dosomething()
    d.run()