import turtle
import random
import math 

screen = turtle.Screen()
screen.bgcolor("#070B34")
screen.setup(width=1.0, height=1.0)

grid_pen = turtle.Turtle()
grid_pen.speed(0)  

grid_pen.color("gray")  
grid_pen.width(1)  

for i in range(-screen.window_height() // 2, screen.window_height() // 2, 200):
    grid_pen.penup()
    grid_pen.goto(-screen.window_width() // 2, i)
    grid_pen.pendown()
    grid_pen.forward(screen.window_width())


grid_pen.left(90)
for i in range(-screen.window_width() // 2, screen.window_width() // 2, 200):
    grid_pen.penup()
    grid_pen.goto(i, -screen.window_height() // 2)
    grid_pen.pendown()
    grid_pen.forward(screen.window_height())



star = turtle.Turtle()
star.speed(0)
def draw_star(size):
    star.begin_fill()
    for _ in range(5):
        star.forward(size)
        star.right(144)
    star.end_fill()


pen = turtle.Turtle()
pen.speed(0)  
pen.width(2)

x, y = 0, 0  
ursa_major_outline = [
    (x, y), (x + 135, y + 1), (x + 220, y - 50), (x + 330, y - 105),
    (x + 344, y - 188), (x + 470, y - 209), (x + 500, y - 123), (x + 330, y - 105) ,
]

pen.color("yellow")
pen.penup()
pen.goto(ursa_major_outline[0])
pen.pendown()

for point in ursa_major_outline:
    pen.goto(point)

pen.color("sienna")
def draw_circle_through_points(points):
    screen = turtle.Screen()
    screen.title("Circle through 4 Points")
    screen.setup(width=600, height=400)
    screen.setworldcoordinates(0, 0, 600, 400)

points = [(333.0, -100.0), (348.0, -183.0), (471.0, -203.0), (502.0, -118.0)]

def circle_from_three_points(p1, p2, p3):
    temp = p2[0] * p2[0] + p2[1] * p2[1]
    bc = (p1[0] * p1[0] + p1[1] * p1[1] - temp) / 2
    cd = (temp - p3[0] * p3[0] - p3[1] * p3[1]) / 2
    determinant = (p1[0] - p2[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p2[1])

    if abs(determinant) < 1e-6:
        return None

    center_x = (bc * (p2[1] - p3[1]) - cd * (p1[1] - p2[1])) / determinant
    center_y = ((p1[0] - p2[0]) * cd - (p2[0] - p3[0]) * bc) / determinant

    radius = ((center_x - p1[0]) ** 2 + (center_y - p1[1]) ** 2) ** 0.5

    return (center_x, center_y), radius

circle_center, circle_radius = circle_from_three_points(points[0], points[1], points[2])

if circle_center is not None:
    pen.up()
    pen.goto(circle_center[0], circle_center[1] - circle_radius)
    pen.down()
    pen.circle(circle_radius)


point1 = (335.0, -101.0)
point2 = (3.0, 5.0)

center_x = (point1[0] + point2[0]) / 2
center_y = (point1[1] + point2[1]) / 2

major_axis = ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5

minor_axis = major_axis / 2

pen.penup()
pen.goto(center_x, center_y - minor_axis)
pen.pendown()

pen.circle(minor_axis, extent=360)  
points = [
    (4.0, 5.0),
    (-191.0, 55.0),
    (-187.0, 240.0),
    (-50.0, 234.0),
    (-41.0, 120.0),
    (25.0, 48.0)
]
points = [
    (4.0, 5.0),
    (-191.0, 55.0),
    (-187.0, 240.0),
    (-50.0, 234.0),
    (-41.0, 120.0),
    (25.0, 48.0),
    (27.0, 54.0),
]
pen.penup()
pen.goto(points[0])
pen.pendown()
for point in points[1:]:
    pen.goto(point)
pen.hideturtle()




points = [
    (20.0, -129.0),
    (13.0, -236.0),
    (53.0, -240.0),
    (53.0, -172.0)
]


pen.penup()
pen.goto(points[0][0], points[0][1])
pen.pendown()

pen.begin_fill()

for i in range(1, 5):
    pen.goto(points[i % 4][0], points[i % 4][1])

points = [
    (74.0, -180.0),
    (110.0, -184.0),
    (107.0, -240.0),
    (76.0, -239.0)
]
pen.penup()
pen.goto(points[0][0], points[0][1])
pen.pendown()
for i in range(1, 5):
    pen.goto(points[i % 4][0], points[i % 4][1])


points = [
(240.0, -204.0),
(276.0, -237.0),
(292.0, -221.0),
(264.0, -187.0),
]
pen.penup()
pen.goto(points[0][0], points[0][1])
pen.pendown()
for i in range(1, 5):
    pen.goto(points[i % 4][0], points[i % 4][1])

for i in range(1, 5):
    pen.goto(points[i % 4][0], points[i % 4][1])


points = [
(213.0, -208.0),
(232.0, -202.0),
(254.0, -231.0),
(235.0, -242.0),

]
pen.penup()
pen.goto(points[0][0], points[0][1])
pen.pendown()
for i in range(1, 5):
    pen.goto(points[i % 4][0], points[i % 4][1])


pen = turtle.Turtle()
pen.speed(0)
pen.color("orange")
pen.width(2)



    
def draw_triangle(size):
    for _ in range(3):
        pen.forward(size)
        pen.right(120)

center_x, center_y = -638.0, 209.0
radius = 100
pen.penup()
pen.goto(center_x, center_y - radius)
pen.pendown()
pen.circle(radius)  
num_triangles = 40
angle_between_triangles = 360 / num_triangles

for _ in range(num_triangles):
    pen.penup()

    x, y = pen.position()
    angle_radians = math.atan2(y - center_y, x - center_x)
    angle_degrees = math.degrees(angle_radians)


    new_angle = angle_degrees + angle_between_triangles
    new_x = center_x + radius * math.cos(math.radians(new_angle))
    new_y = center_y + radius * math.sin(math.radians(new_angle))

    pen.goto(new_x, new_y)
    pen.setheading(angle_degrees + 90)  
    pen.pendown()
    draw_triangle(20)  
pen.penup()
pen.goto(-723.0, 263.0)
pen.pendown()
pen.goto(-800.0, 263.0) 
pen.goto(-800.0, -18.0)  
pen.goto(-723.0, -18.0)  
pen.goto(-723.0, 263.0)
pen.penup()
pen.goto(-675.0, -34.0)
pen.pendown()
pen.circle(15)  



num_paws = 3 
for _ in range(num_paws):
    pen.penup()
    pen.goto(-675.0, -34.0)
    pen.left(90)
    pen.forward(15)
    pen.right(70 + (360 / num_paws) * _)
    pen.forward(15)  
    pen.pendown()
    pen.circle(5)  
pen.penup()
pen.goto(-725.0, 12.0)
pen.goto (-685.0, -6.0)
pen.pendown()

pen.goto(-1074.0, 2.0)
pen.goto(-1074.0, 97.0)
pen.goto(-776.0, 97.0)
pen.goto(-776.0, 2.0)


pen.penup()
pen.goto(-874.0, -42.0)
pen.pendown()
pen.circle(15) 
num_paws = 3  
for _ in range(num_paws):
    pen.penup()
    pen.goto(-885.0, -40.0)
    pen.left(0)
    pen.forward(0)
    pen.right(30 + (360 / num_paws) * _)
    pen.forward(15)  
    pen.pendown()
    pen.circle(5)  

pen.penup()
pen.goto(-1090.0, -70.0)
pen.pendown()
pen.circle(15) 
for _ in range(num_paws):
    pen.penup()
    pen.goto(-1081.0, -60.0)
    pen.left(0)
    pen.forward(0)
    pen.right(30 + (360 / num_paws) * _)
    pen.forward(15) 
    pen.pendown()
    pen.circle(5) 

    
pen.penup()
pen.goto(-864.0, -2.0)
pen.pendown()
pen.goto(-894.0, -28.0)

pen.penup()
pen.goto(-1117.0, -60.0)
pen.pendown()
pen.goto(-1071.0, 8.0)


pen.penup()
pen.goto(-1103.0, -42.0)
pen.pendown()
pen.goto(-1081.0, -59.0)

pen.penup()
pen.goto(-1116.0, -61.0)
pen.pendown()
pen.goto(-1093.0, -69.0)



pen.penup()
(-1109.0, 38.0)
pen.pendown()
pen.goto(-1221.0, 101.0)

pen.penup()
(-1218.0, 102.0)
pen.pendown()
pen.goto(-915.0, 244.0)

pen.penup()
(-915.0, 244.0)
pen.pendown()
pen.goto(-796.0, 268.0)

pen.color("red")
Leo_outline = [
(-598.0, 259.0),
(-638.0, 209.0),
(-685.0, 229.0),
(-723.0, 263.0), 
(-806.0, 237.0), 
(-828.0, 160.0),
(-760.0, 118.0), 
(-776.0, 2.0),
(-675.0, -34.0),
(-776.0, 2.0,),
(-876.0, -30.0),
(-776.0, 2.0,),
(-1074.0, 97.0),
(-1120.0, -69.0),
(-1120.0, 22.0),
(-1074.0, 97.0),
(-1225.0, 96.0),
(-1058.0, 175.0),
 (-1009.0, 168.0), 
 (-828.0, 160.0),
]


pen.penup()
pen.goto(Leo_outline[0])
pen.pendown()
for point in Leo_outline:
    pen.goto(point)

pen = turtle.Turtle()
pen.speed(0)
pen.color("dark green")
pen.width(2)

Libra_outline = [
(-143.0, -91.0),
(-237.0, -406.0),
(-450.0, -528.0), 
(-461.0, -571.0), 
(-450.0, -528.0),
(-237.0, -406.0),
(-349.0, 113.0),
(-448.0, -79.0), 
(-589.0, -175.0), 
(-623.0, -117.0),#edit 
(-589.0, -175.0), 
(-448.0, -79.0), 
(-349.0, 113.0),
(-143.0, -91.0),
]
pen.penup()
pen.goto(Libra_outline[0])
pen.pendown()

for point in Libra_outline:

    pen.goto(point)
pen.color("lime")
points = [(-458.0, -565.0), (-448.0, -525.0)]

radius = 90  

pen.penup()
pen.goto(points[0])
pen.right(90) 
pen.pendown()

pen.circle(-radius, 180)


points = [(-637.0, -565.0), (-535.0, -467.0) , (-534.0, -464.0) , (-447.0, -524.0),(-535.0, -467.0),
(-233.0, -397.0),    (-634.0, -561.0),  (-458.0, -566.0) , (-537.0, -559.0), (-530.0, -461.0)      ]

pen.penup()
pen.goto(points[0])
pen.pendown()
pen.goto(points[1])
pen.penup()
pen.goto(points[2])
pen.pendown()
pen.goto(points[3])
pen.penup()
pen.goto(points[4])
pen.pendown()
pen.goto(points[5])
pen.penup()
pen.goto(points[6])
pen.pendown()
pen.goto(points[7])
pen.penup()
pen.goto(points[8])
pen.pendown()
pen.goto(points[9])

points = [(-586.0, -170.0),]

radius = 90  


pen.penup()
pen.goto(points[0])
pen.right(180) 
pen.pendown()

pen.circle(-radius, 180)


points = [   (-762.0, -173.0),(-587.0, -170.0),(-764.0, -167.0),(-620.0, -113.0), (-620.0, -112.0),
(-346.0, 117.0), (-764.0, -165.0), (-347.0, 116.0) ]
 
pen.penup()
pen.goto(points[0])
pen.pendown()
pen.goto(points[1])
pen.penup()
pen.goto(points[2])
pen.pendown()
pen.goto(points[3])
pen.penup()
pen.goto(points[4])
pen.pendown()
pen.goto(points[5])
pen.penup()
pen.goto(points[6])
pen.pendown()
pen.goto(points[7])


points = [(-142.0, -86.0), (-265.0, -260.0), (-320.0, -4.0)]


pen.penup()
pen.goto(points[0])
pen.pendown()

for point in points[1:]:
    pen.goto(point)
pen.goto(points[0])
pen.penup()

points = [(-312.0, -36.0), (-273.0, -220.0), (-443.0, -184.0)]


pen.goto(points[0])
pen.pendown()

for point in points[1:]:
    pen.goto(point)

pen.goto(points[0])


pen.color("violet")
pen.width(2)


Cancer_outline = [
(625.0, 353.0),
(617.0, 235.0),
(594.0, 167.0),
(531.0, 67.0),
(683.0, 12.0), 
(721.0, 151.0), 
(594.0, 167.0),
]

pen.penup()
pen.goto(Cancer_outline[0])
pen.pendown()


for point in Cancer_outline:
    pen.goto(point)

coordinates = [
    (683.0, 0.0),
    (492.0, 63.0),
    (619.0, 190.0),
    (749.0, 169.0)
]
pen.color("magenta")
coordinates = [
    (683.0, 0.0),
    (492.0, 63.0),
    (619.0, 190.0),
    (749.0, 169.0)
]

def draw_line(x1, y1, x2, y2):
    pen.penup()
    pen.goto(x1, y1)
    pen.pendown()
    pen.goto(x2, y2)

for i in range(len(coordinates)):
    draw_line(coordinates[i][0], coordinates[i][1], coordinates[(i+1) % len(coordinates)][0], coordinates[(i+1) % len(coordinates)][1])


points = [
    (497.0, 66.0),
    (426.0, 96.0),
    (372.0, 154.0),
    (402.0, 184.0),
    (401.0, 158.0),
    (423.0, 197.0),
    (448.0, 154.0),
    (456.0, 132.0),
    (474.0, 116.0),
    (493.0, 104.0),
    (514.0, 87.0)
    
]



def draw_line(x1, y1, x2, y2):
    pen.penup()
    pen.goto(x1, y1)
    pen.pendown()
    pen.goto(x2, y2)

for i in range(len(points) - 1):
    x1, y1 = points[i]
    x2, y2 = points[i + 1]
    draw_line(x1, y1, x2, y2)

def draw_line(x1, y1, x2, y2):
    pen.penup()
    pen.goto(x1, y1)
    pen.pendown()
    pen.goto(x2, y2)
points = [
(628.0, 356.0),
(525.0, 355.0),
(513.0, 334.0),
(555.0, 346.0),
(557.0, 311.0),
(587.0, 327.0),
(624.0, 285.0),
(628.0, 360.0),
(664.0, 362.0),
(653.0, 241.0),
(639.0, 192.0),
]

def draw_line(x1, y1, x2, y2):
    pen.penup()
    pen.goto(x1, y1)
    pen.pendown()
    pen.goto(x2, y2)

for i in range(len(points) - 1):
    x1, y1 = points[i]
    x2, y2 = points[i + 1]
    draw_line(x1, y1, x2, y2)


points = [
 (518.0, 92.0),
(501.0, 156.0),
 (533.0, 164.0),
 (534.0, 210.0),
 (606.0, 195.0),
]
points = [
    (605.0, 32.0),
    (641.0, -65.0),
    (668.0, 10.0),
    (688.0, 6.0),
    (797.0, -15.0),
    (707.0, 57.0),
    (746.0, 154.0),
    (862.0, 166.0),
    (752.0, 175.0),
    (715.0, 183.0),
    (775.0, 243.0),
    (745.0, 176.0),
]


def draw_line(x1, y1, x2, y2):
    pen.penup()
    pen.goto(x1, y1)
    pen.pendown()
    pen.goto(x2, y2)

for i in range(len(points) - 1):
    x1, y1 = points[i]
    x2, y2 = points[i + 1]
    draw_line(x1, y1, x2, y2)



num_stars = 500 

for _ in range(num_stars):
    x = random.randint(-screen.window_width() // 2, screen.window_width() // 2)
    y = random.randint(-screen.window_height() // 2, screen.window_height() // 2)
    size = random.randint(1, 20 )
    star.penup()
    star.goto(x, y)
    star.pendown()
    star.color("white")
    draw_star(size)




turtle.done()
