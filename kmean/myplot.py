import matplotlib.pyplot as plt
import random
def setting(xlabel,ylabel):
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
def close():
    plt.close()
def random_color():
    color_array = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    color="#"
    array=random.sample(color_array, 3)
    for i in range(3):
        color+=array[i]
    return color

def show():
    plt.show()

def draw(be_drown_x,be_drown_y,color):
    plt.scatter(be_drown_x,be_drown_y,color=color)

if __name__ == '__main__':
    print(random_color())