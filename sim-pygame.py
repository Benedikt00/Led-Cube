import math
import pygame
import numpy as np
import time

# window settings:
screen_width, screen_height = 800, 600

points = []

for i in range(8):
    for j in range(8):
        for k in range(8):
            points.append([i - 4, j - 4, k - 4, 0])

# init pygame settings:
pygame.init()
pygame.display.set_caption('Python 3D rendering example')
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
cube_center = {'y': screen_height // 2, 'x': screen_width // 2}
fps = 10

# colors:
background_color = (240, 235, 240)
circle_color_off = (200, 200, 200)
circle_color_on = (255, 0, 0)

angle = 11.700000000000031
angular_change = 0.01
distance = 2
scale = 100
circle_radius = 7
running = True

list_on = []
for i in range(8):
    temp_l_2 = []
    for j in range(8):
        temp_l_1 = []
        for k in range(8):
            temp_l_1.append(0)
        temp_l_2.append(temp_l_1)
    list_on.append(temp_l_2)


def mat_to_int(mat):
    return mat[0] + mat[1]*8 + mat[2]*8*8

def update_points(game_cycle):
    list_on[0][0][0] = 1

    for i in range(8):
        for j in range(8):
            for k in range(8):
                points[mat_to_int([i, j, k])][3] = list_on[i][j][k]



game_cycle = 0
# main game loop:
while running:
    clock.tick(fps)
    screen.fill(background_color)

    # process window events:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print(angle)

    # prepare rotation matrix:
    rotation_matrix_x = [
        [1, 0, 0],
        [0, math.cos(angle), -math.sin(angle)],
        [0, math.sin(angle), math.cos(angle)]
    ]

    rotation_matrix_y = [
        [math.cos(angle), 0, -math.sin(angle)],
        [0, 1, 0],
        [math.sin(angle), 0, math.cos(angle)]
    ]

    rotation_matrix_z = [
        [math.cos(angle), -math.sin(angle), 0],
        [math.sin(angle), math.cos(angle), 0],
        [0, 0, 1]
    ]

    z = 1 / distance

    projection_matrix = [
        [z, 0, 0],
        [0, z, 0]
    ]

    # compute the final matrix:
    rotation_matrix = np.matmul(rotation_matrix_x, rotation_matrix_y)
    rotation_matrix = np.matmul(rotation_matrix_z, rotation_matrix)
    projection_rotation_matrix = np.matmul(projection_matrix, rotation_matrix)
    projected_vertices = []

    # project vertices to 2D coordinates:
    for p in points:
        # apply projection matrix to each cube vertex:
        projected = np.matmul(projection_rotation_matrix, np.transpose([p[0], p[1], p[2]]))
        x = cube_center['x'] + projected[0] * scale
        y = cube_center['y'] + projected[1] * scale
        if p[3] == 0:
            #pygame.draw.circle(screen, circle_color_off, (x, y), circle_radius)
            pass
        else:
            pygame.draw.circle(screen, circle_color_on, (x, y), circle_radius)

    keys = pygame.key.get_pressed()
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_s]:
        angle += 0.05

    # present the new image to screen:
    pygame.display.update()

    update_points(game_cycle)
    game_cycle += 1
pygame.quit()