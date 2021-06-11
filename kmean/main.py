##fix 初始座標問題 連續兩個一樣會吃屎  k++
import multiprocessing as mp
import myplot
import random
import kmeans
import myclass

def kmeansElbow(X,y):
    number_of_code=len(X)
    elbow_distances=[0]
    deltaSlope=[]
    for i in range(1,number_of_code):
        elbow_distances.append(test(X,y,i))
        if i>2:
            deltaSlope.append(kmeans.angle(elbow_distances[i]-elbow_distances[i-1])-
                              kmeans.angle(elbow_distances[i-1]-elbow_distances[i-2]))
            print(i,deltaSlope)
            if deltaSlope[i-3]<deltaSlope[i-4]:
                print(elbow_distances)
                return test(X,y,i-2,True)
    else:
        return test(X,y,2,True)


# def kmeansElbow(X,y):
#     number_of_code=len(X)
#     elbow_distances=[0]
#     deltaSlope=[]
#     for i in range(1,number_of_code):
#         elbow_distances.append(test(X,y,i))
#         if i>2:
#             deltaSlope.append(kmeans.angle(elbow_distances[i]-elbow_distances[i-1])-
#                               kmeans.angle(elbow_distances[i-1]-elbow_distances[i-2]))
#             print(i,deltaSlope)
#             if deltaSlope[i-3]<deltaSlope[i-4]:
#                 print(elbow_distances)
#                 return test(X,y,i-1,True)
#     else:
#         return test(X,y,2,True)

#
# def main(number_of_code,number_of_group,draw=False):
#     codes=[]
#     for i in range(number_of_code):
#         #code 須改為實際code的數據
#         codes.append(myclass.be_divided_code(random.randint(1, 10), random.uniform(1, 10)))
#     groups=[]
#     # for i in range(number_of_group):
#     #     groups.append(myclass.group_center(i,random.randint(1,10),random.uniform(0.1,3)))
#
#         #group可能會影響分群方式 自選填入
#     for i in range(number_of_group):
#         groups.append(myclass.group_center(i, codes[i].variables, codes[i].performance_time))
#
#     #重複驗證區
#     while True:
#         for code in codes:
#             code.distance_reset()
#             for group in groups:
#                 distance=(kmeans.distance(code.variables, code.performance_time, group.variables, group.performance_time))
#                 if  distance<=code.distance:
#                     code.group=group.id
#                     code.distance=distance
#
#         move_happen=False
#         for group in groups:
#
#             if group.variables!= kmeans.move_to([code.variables for code in codes if code.group == group.id]):
#                 group.variables= kmeans.move_to([code.variables for code in codes if code.group == group.id])
#                 move_happen = True
#
#             if group.performance_time!= kmeans.move_to([code.performance_time for code in codes if code.group == group.id]):
#                 group.performance_time= kmeans.move_to([code.performance_time for code in codes if code.group == group.id])
#                 move_happen = True
#         #圖形不變後退出
#         if move_happen==False:
#             break
#     ##
#     if  draw==True:
#         myplot.setting("variables", "performance_time")
#         myplot.draw([code.variables for code in codes], [code.performance_time for code in codes], "blue")
#         myplot.show()
#         myplot.close()
#
#         for i in range(number_of_group):
#             myplot.draw([code.variables for code in codes if code.group == i],
#                         [code.performance_time for code in codes if code.group == i], myplot.random_color())
#             myplot.draw([group.variables for group in groups if group.id == i],
#                         [group.performance_time for group in groups if group.id == i], myplot.random_color())
#         myplot.setting("variables", "performance_time")
#         myplot.show()
#
#     return sum(code.distance**2 for code in codes)



def test(X, y, number_of_group,draw=False):
    codes=[]
    for i in range(len(X)):
        codes.append(myclass.be_divided_code(X[i], y[i]))

    groups=[]
    for i in range(number_of_group):
        groups.append(myclass.group_center(i, codes[i].variables, codes[i].performance_time))

    while True:
        for code in codes:
            code.distance_reset()
            for group in groups:
                distance=(
                    kmeans.distance(code.variables, code.performance_time, group.variables, group.performance_time))
                if  distance<=code.distance:
                    code.group=group.id
                    code.distance=distance

        move_happen=False
        for group in groups:

            try:
                if group.variables!= kmeans.move_to([code.variables for code in codes if code.group == group.id]):
                    group.variables= kmeans.move_to([code.variables for code in codes if code.group == group.id])
                    move_happen = True

                if group.performance_time!= kmeans.move_to([code.performance_time for code in codes if code.group == group.id]):
                    group.performance_time= kmeans.move_to([code.performance_time for code in codes if code.group == group.id])
                    move_happen = True
            except:
                break
        if move_happen==False:
            break
    ##
    if draw == True:
        myplot.setting("variables", "performance_time")
        myplot.draw([code.variables for code in codes], [code.performance_time for code in codes], "blue")
        myplot.show()
        myplot.close()

        for i in range(number_of_group):
            myplot.draw([code.variables for code in codes if code.group == i],
                        [code.performance_time for code in codes if code.group == i], myplot.random_color())
            myplot.draw([group.variables for group in groups if group.id == i],
                        [group.performance_time for group in groups if group.id == i], myplot.random_color())
        myplot.setting("variables", "performance_time")
        myplot.show()

    return sum(code.distance ** 2 for code in codes)

if __name__=="__main__":
    ran=100
    X=[random.uniform(1,3) for i in range(ran//2)]
    y=[random.uniform(1,3) for i in range(ran//2)]

    arr=[random.uniform(7,9) for i in range(ran//2)]
    arr2 = [random.uniform(7, 9) for i in range(ran // 2)]
    X.extend(arr)
    y.extend(arr2)

    arr=[random.uniform(4,5) for i in range(ran//2)]
    arr2 = [random.uniform(4, 5) for i in range(ran // 2)]
    X.extend(arr)
    y.extend(arr2)

    kmeansElbow(X,y)
