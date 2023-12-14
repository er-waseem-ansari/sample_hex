import math

def area(r):
    return 3.14 * r *r
    
def dist(a,b,c,d):
    s1 = (a-c)*(a-c) + (b-d)*(b-d)
    s1 = math.sqrt(s1)
    return math.ceil(s1)
    
def res(fenced_area, required_area):
    if fenced_area == required_area:
        return [-1]
    if (fenced_area > required_area ):
        extra_land = fenced_area - required_area
        temp = math.sqrt(extra_land)
        
        left_square = math.floor(temp)**2

        right_sqaure = math.ceil(temp)**2


        if (extra_land - left_square > right_sqaure - extra_land):
            nearest = right_sqaure

        else:
            nearest = left_square

            
        if nearest > extra_land:
            money = (nearest - extra_land) * 20
            return ["Krishna", money]
        else:
            money = (extra_land - nearest) * 20
            return ["Shiva", money]
    
    else:
        money = (required_area - fenced_area) * 20
        return ["Krishna", money]
    
x1,y1 = map(int, input().split())
x2,y2 = map(int, input().split())
x3,y3 = map(int, input().split())

dist12 = dist(x1,y1,x2,y2)
dist13 = dist(x1,y1,x3,y3)

required_area = math.ceil(area(dist12))
fenced_area = math.ceil(area(dist13))


out = res(fenced_area, required_area)
if len(out) == 1:
    print("-1")
else:
    print(out[0]," ", str(out[1]))