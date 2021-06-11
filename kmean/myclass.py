class be_divided_code:
    def __init__(self, variables, performance_time,group="no belonging",distance=999999,file_name=0):
        self.file_name=file_name
        self.variables = variables
        self.performance_time = performance_time
        self.group=group
        self.distance=distance
    def distance_reset(self,distance=999999):
        self.distance=distance
class group_center:
    def __init__(self,id,variables,performance_time):
        self.id=id
        self.variables = variables
        self.performance_time = performance_time