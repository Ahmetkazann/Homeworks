import pygame
import sys
import random
import math



def bresenham_line(x1, y1, x2, y2):
    points = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    err = dx - dy

    while x1 != x2 or y1 != y2:
        points.append((x1, y1))
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

    points.append((x2, y2))
    return points

def bresenham_circle(center, radius):
    points = []

    x, y = radius, 0
    radiusError = 1 - x

    while x >= y:
        points += bresenham_line(center[0] + x, center[1] - y, center[0] - x, center[1] - y)
        points += bresenham_line(center[0] + y, center[1] - x, center[0] - y, center[1] - x)
        points += bresenham_line(center[0] - x, center[1] + y, center[0] + x, center[1] + y)
        points += bresenham_line(center[0] - y, center[1] + x, center[0] + y, center[1] + x)

        y += 1

        if radiusError < 0:
            radiusError += 2 * y + 1
        else:
            x -= 1
            radiusError += 2 * (y - x) + 1

    return points
def rotate_polygon(points, center, angle):
    rotated_points = []
    for x, y in points:
        x -= center[0]
        y -= center[1]
        new_x = x * math.cos(math.radians(angle)) - y * math.sin(math.radians(angle))
        new_y = x * math.sin(math.radians(angle)) + y * math.cos(math.radians(angle))
        new_x += center[0]
        new_y += center[1]
        rotated_points.append((int(new_x), int(new_y)))
    return rotated_points

def draw_polygon(screen, center, sides, length, rotation_angle):
    angle = 360 / sides

    points = []
    for i in range(sides):
        x1 = center[0] + int(length * math.cos(math.radians(angle * i)))
        y1 = center[1] - int(length * math.sin(math.radians(angle * i)))

        x2 = center[0] + int(length * math.cos(math.radians(angle * (i + 1))))
        y2 = center[1] - int(length * math.sin(math.radians(angle * (i + 1))))

        points.extend(bresenham_line(x1, y1, x2, y2))
    points = rotate_polygon(points, center, rotation_angle)
    return points

def check_collision(circle_center, circle_radius, rect_center, rect_width, rect_height):
    rect_left = rect_center[0] - rect_width // 2
    rect_right = rect_center[0] + rect_width // 2
    rect_top = rect_center[1] - rect_height // 2
    rect_bottom = rect_center[1] + rect_height // 2

    for point in bresenham_circle(circle_center, circle_radius):
        if rect_left <= point[0] <= rect_right and rect_top <= point[1] <= rect_bottom:
            return True

    return False

def check_collision_polygon(polygon_center, sides, length, rect_center, rect_width, rect_height,rotation_angle):
    polygon_points = draw_polygon([], polygon_center, sides, length,rotation_angle)

    rect_left = rect_center[0] - rect_width // 2
    rect_right = rect_center[0] + rect_width // 2
    rect_top = rect_center[1] - rect_height // 2
    rect_bottom = rect_center[1] + rect_height // 2

    for point in polygon_points:
        if rect_left <= point[0] <= rect_right and rect_top <= point[1] <= rect_bottom:
            return True

    return False

pygame.init()

screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

player_rect = pygame.Rect(0, 0, 125, 25)
circle_radius = 48
gamespeed = 10

triangle_center = [random.randint(0+ 100,screen_width),random.randint(-500,0)]
triangle_sides = 3
triangle_length = random.randint(75,100)

rect_center = [random.randint(0+ 100,screen_width),random.randint(-1500,-1000)]
rect_sides = 4
rect_length = random.randint(75,100)

pentagon_center = [random.randint(0+ 100,screen_width),random.randint(-500,-100)]
pentagon_sides = 5
pentagon_length = random.randint(75,100)

circle_center = [random.randint(0, screen_width), random.randint(-2000,-1000)]
puan = 0
num_stars = 256
star_height = []
star_width = []
for i in range(num_stars):
    random_height = random.randint(-3000,screen_height)
    random_width = random.randint(50, screen_width)
    star_height.append(random_height)
    star_width.append(random_width)

player_pos = [screen_width // 2, screen_height - 50]
player_rect.center = player_pos
rotate = 0
reverse_rotate = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    for i in range(num_stars):
        pygame.draw.circle(screen,((125,200,255)),(star_width[i],star_height[i]),1,1)
        
    for j in range(num_stars):
        star_height[j] += 1
    

    rotate += gamespeed / 3
    reverse_rotate -= gamespeed / 3
    triangle_center[1] += gamespeed

    if triangle_center[1] - triangle_length > screen_height:
        triangle_center = [random.randint(0 + triangle_length, screen_width - triangle_length), - 500 -triangle_length]
        triangle_length = random.randint(75,100)
        puan += 3
        print("puan:", puan)

    if check_collision_polygon(triangle_center, triangle_sides, triangle_length, player_rect.center, player_rect.width, player_rect.height,rotate):
        print("you lost")
        running = False

    triangle_points = draw_polygon(screen, triangle_center, triangle_sides, triangle_length,rotate)
    for i in range(len(triangle_points) - 1):
        pygame.draw.line(screen, (255, 0, 0), triangle_points[i], triangle_points[i+1], 1) # pikselbas() fonksiyonu gibi çalışır 1,1 boyutunda çizgi
    #print(triangle_points)

    rect_center[1] += gamespeed

    if rect_center[1] - rect_length > screen_height:
        rect_center = [random.randint(0 + rect_length, screen_width),  - 1000 -rect_length]
        rect_length = random.randint(75,100)
        puan += 4
        print("puan:", puan)

    if check_collision_polygon(rect_center, rect_sides, rect_length, player_rect.center, player_rect.width, player_rect.height,rotate):
        print("you lost")
        running = False

    rect_points = draw_polygon(screen, rect_center, rect_sides, rect_length,rotate)

    for i in range(len(rect_points) - 1):
        pygame.draw.line(screen, (255, 0, 0), rect_points[i], rect_points[i+1], 1) # pikselbad() fonksiyonu gibi çalışır 1,1 boyutunda çizgi

    pentagon_center[1] += gamespeed


    if pentagon_center[1] - pentagon_length > screen_height:
        pentagon_center = [random.randint(0 + pentagon_length, screen_width),  - 1250 -pentagon_length]
        pentagon_length = random.randint(125,150)
        puan += 5
        print("puan:", puan)

    if check_collision_polygon(pentagon_center, pentagon_sides, pentagon_length, player_rect.center, player_rect.width, player_rect.height,reverse_rotate):
        print("you lost")
        running = False

    pentagon_points = draw_polygon(screen, pentagon_center, pentagon_sides, pentagon_length,reverse_rotate)

    for i in range(len(pentagon_points) - 1):
        pygame.draw.line(screen, (255, 0, 0), pentagon_points[i], pentagon_points[i+1], 1) # pikselbad() fonksiyonu gibi çalışır 1,1 boyutunda çizgi

    circle_center[1] += gamespeed

    if circle_center[1] - circle_radius > screen_height:
        circle_center = [random.randint(0, screen_width), random.randint(-2000,-100)]
        puan += 10
        gamespeed += 1
        print("puan:",puan)

    if check_collision(circle_center, circle_radius, player_rect.center, player_rect.width, player_rect.height):
        print("kaybettin")
        running = False

    noktalar = bresenham_circle(circle_center, circle_radius)

    for i in range(len(noktalar) - 1):
        pygame.draw.line(screen, (255, 255, 255), noktalar[i], noktalar[i+1], 1)

    
    pygame.draw.rect(screen, (0, 128, 128), player_rect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_rect[0] -= gamespeed
    if keys[pygame.K_d]:
        player_rect[0] += gamespeed

    if player_rect[0] < 0:
        player_rect[0] = 0
    elif player_rect[0] > screen_width - 125:
        player_rect[0] = screen_width - 125
    if puan > 500:
        print("you win")
        running = False
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()