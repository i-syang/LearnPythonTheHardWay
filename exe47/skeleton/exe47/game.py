class Room(object):

    # 
    
    def __init__(self, name, desciption):
        self.name =name
        self.desciption = desciption
        self.paths ={}
    
    """
    def __init__(self):
        self.paths ={}

    def setName(self, name):
        self.name = name

    def setDesc(self, desc):
        self.desciption = desc
    """
    
    def go(self, direction):    # 'north'
        # self.paths = {'north': north, 'south': south}
        return self.paths.get(direction, None)


    def add_paths(self, paths):
        self.paths.update(paths)
        