import myclass
class space:
    def __init__(self):
        pass
def get_class_attribute(obj):
    return set(dir(obj)).difference(dir(space))

def attribute_difference(obj1,obj2):
    obj1_arr=list(get_class_attribute(obj1))
    obj2_arr=list(get_class_attribute(obj2))

    return [i for i in obj1_arr if i in obj2_arr]

if __name__=="__main__":
    list1=list(get_class_attribute(myclass.be_divided_code(0, 0)))
    list2=list(get_class_attribute(myclass.group_center(0, 0, 0)))




