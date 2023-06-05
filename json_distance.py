import random
import json
import math
from scipy.spatial import Voronoi, voronoi_plot_2d, Delaunay

# 10個のランダムな点を生成し、IDと座標を付与
points = {}
for i in range(20):
    x = random.uniform(0, 1)  # x座標を0から1の範囲でランダムに生成
    y = random.uniform(0, 1)  # y座標を0から1の範囲でランダムに生成
    points[i] = {'x': x, 'y': y}

# 座標データをリストに変換
coordinates = [(point['x'], point['y']) for point in points.values()]

# ドロネー図を作成
tri = Delaunay(coordinates)

# 各点の近接点の座標と距離を取得
neighbors = {}
for i in range(20):
    neighbor_indices = tri.vertex_neighbor_vertices[1][tri.vertex_neighbor_vertices[0][i]:tri.vertex_neighbor_vertices[0][i+1]]
    neighbor_points = []
    distances = []
    for j in neighbor_indices:
        neighbor_points.append(coordinates[j])
        distance = math.sqrt((coordinates[j][0] - coordinates[i][0])**2 + (coordinates[j][1] - coordinates[i][1])**2)
        distances.append(distance)
    neighbors[i] = {'points': neighbor_points, 'distances': distances}

# 各点の近接点の座標と距離をJSONに追加
for i, data in neighbors.items():
    neighbor_points = data['points']
    distances = data['distances']
    points[i]['neighbors'] = [{'x': x, 'y': y, 'distance': d} for (x, y), d in zip(neighbor_points, distances)]

# JSON形式のデータを作成
json_data = json.dumps(points)

# JSONデータを表示
print(json_data)

import cv2
import json
import numpy as np

def draw_lines_with_random_colors(json_data):
    # Parse JSON data
    points = json.loads(json_data)

    # Create an image canvas with cyan background
    canvas_size = 500
    canvas = np.zeros((canvas_size, canvas_size, 3), dtype=np.uint8)
    canvas[:, :] = (255, 255, 0)  # Fill with cyan color

    # Draw lines between neighbors with random colors
    for i, point_data in points.items():
        x1 = int(point_data['x'] * canvas_size)
        y1 = int(point_data['y'] * canvas_size)
        for neighbor in point_data['neighbors']:
            x2 = int(neighbor['x'] * canvas_size)
            y2 = int(neighbor['y'] * canvas_size)
            color = tuple(np.random.randint(0, 256, 3).tolist())
            cv2.line(canvas, (x1, y1), (x2, y2), color, 2)

    # Draw text on top of lines
    for i, point_data in points.items():
        x1 = int(point_data['x'] * canvas_size)
        y1 = int(point_data['y'] * canvas_size)

        # Show the topmost key on the point
        cv2.putText(canvas, str(i), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

        for neighbor in point_data['neighbors']:
            x2 = int(neighbor['x'] * canvas_size)
            y2 = int(neighbor['y'] * canvas_size)

            # Calculate middle point of the line
            mid_x = (x1 + x2) // 2
            mid_y = (y1 + y2) // 2

            # Draw the distance on the middle of the line
            distance = neighbor['distance']
            distance_str = "{:.2f}".format(distance)
            cv2.putText(canvas, distance_str, (mid_x, mid_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

    # Show the canvas
    cv2.imshow('Points with Neighbors', canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
draw_lines_with_random_colors(json_data)

import json
import pandas as pd

def create_neighbor_dataframe(json_str):
    # Parse the JSON string into a Python object
    json_data = json.loads(json_str)
    

    
    # Create lists to store x, y, and distance values
    x_values = []
    y_values = []
    distance_values = []


    for i, point_data in json_data.items():
    # Iterate over each neighbor
        for neighbor in point_data["neighbors"]:
            x = neighbor['x']
            y = neighbor['y']
            distance = neighbor['distance']
            
            # Append values to respective lists
            x_values.append(x)
            y_values.append(y)
            distance_values.append(distance)
    
    # Create pandas DataFrame
    neighbor_df = pd.DataFrame({
        'x_neighbor': x_values,
        'y_neighbor': y_values,
        'distance': distance_values
    })
    
    return neighbor_df


create_neighbor_dataframe(json_data)

