import math

def distance(*point):
    array=[]
    for i in range(len(point)//2):
        try:
            array.append((point[i]-point[i+len(point)//2])**2)
        except:
            array.append(point[i])
    return (sum(array))**0.5

def move_to(arr):
    return sum(arr)/len(arr)
def angle(m):#y/x
    return math.degrees(math.atan(m/100))


def is_move(*point):##改成自選變數數量 if la==a and lb==b ........ return True
    if len(point)%2==0:
        for i in range(len(point)//2):
            if  point[i]!=point[i+(len(point)//2)]:
                return True
        else:
            return False
    else:
        raise("error input number")




if  __name__=="__main__":
    print(distance(1,1))