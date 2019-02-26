import math

def closest_pair(coordinates):
    min = math.inf
    for coord in coordinates:
        for i in range(len(coordinates)):
            distance = ((((coord[0] - coordinates[i][0])**2) + ((coord[1] - coordinates[i][1])**2))**.5)
            if (distance < min and distance != 0):
                min = distance
    return min

print(closest_pair([(2,3), (12,30), (-40,50), (5,1), (12,0), (3,4), (-2,4), (-3,6)]))