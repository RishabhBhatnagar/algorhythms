class Point:
    def __init__(self, pt):
        self.pt = pt
        self.x = pt[0]
        self.y = pt[1]
     
    def __iter__(self):
       return self.pt
    
    def __getitem__(self, index):
        return self.pt[index]
    
    def __setitem__(self, index, value):
        self.pt[index] = value
        self.x = self.pt[0]
        self.y = self.pt[1]
    
    def __sub__(self, pt1):
        return Point([self.pt[i] - pt1[i] for i in range(len(self.pt))])
    
    def __mul__(self, p2):
        # self*p2
        p1 = self
        return p1.x*p2.y-p1.y*p2.x
    
    def  __rmul__(self, p1):
        # p1*self
        p2 = self
        return p1.x*p2.y-p1.y*p2.x
    
    def __repr__(self):
        return repr(self.pt)

class GrahamScan:
    def __init__(self, points):
        self.points = [Point(point) for point in points]
        self.algo()
    
    def polar_angle(self, p1, p2):
        from math import degrees, atan
        try:
            m = (p2.y-p1.y)/(p2.x-p1.x)
        except ZeroDivisionError:
            m = __import__('math').inf
        return degrees(atan(m))
    
    def direction(self, p0, p1, p2):
        # returns positive if p2 is left to line p0->p1
        # returns negative if p2 is right to line p0->p1
        if (p1-p0)*(p2-p0) > 0:
            print('left')
        else: print('right')
        return (p1-p0)*(p2-p0)
    
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
            
            print(self.points)
            self.direction(self.points[1], self.points[2], self.points[3])


GrahamScan([(0, 0), (1, 4), (3, 2), (3, 3), (4, 1), (2, 3)])
