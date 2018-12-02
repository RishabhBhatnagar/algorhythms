class GrahamScan:
    def __init__(self, points):
        self.points = points
        self.algo()
    
    def polar_angle(self, p1, p2):
        from math import degrees, atan
        try:
            m = (p2[1]-p1[1])/(p2[0]-p1[0])
        except ZeroDivisionError:
            m = __import__('math').inf
        return degrees(atan(m))
    
    def algo(self):
        if len(self.points) < 3:
            print("TypeError: {} points takes more than equal to 3 points ({} given)".format(self.__class__.__name__, len(self.points)))
            exit(0)
        else:
            "Algorithm starts here"
            stack = []
            
            # getting lowest of all y coordinates of all points
            min_y_coord = __import__('math').inf
            for point in self.points:
                if point[1] < min_y_coord:
                    min_y_coord = point[1]
              
            # getting all points with lowest y coordinate
            min_y_list = [point for point in self.points if point[1]==min_y_coord]
            
            # point with least y followed by least x coordinate
            min_y_point = min(min_y_list, key=lambda x:x[0])
            
            # bringing min_y_point to 0th index
            self.points.insert(0, self.points.pop(self.points.index(min_y_point)))
            
            # sorting points based on polar angle
            self.points[1:] = sorted(self.points[1:], key=lambda pt:self.polar_angle(self.points[0], pt))
            for i in range(len(self.points)):
                self.points[i] = list(self.points[i]) + [self.polar_angle(self.points[0], self.points[i])]
            
            


GrahamScan([(0, 0), (0, 2), (1, 1)])
