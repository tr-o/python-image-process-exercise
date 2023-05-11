import numpy as np
import pandas as pd
import json
from scipy.spatial import Voronoi, Delaunay

class VoronoiDelaunayAnalysis:
    def __init__(self, num_points=10):
        self.num_points = num_points
        self.points = self.generate_random_points()

    def generate_random_points(self):
        return np.random.rand(self.num_points, 2)

    def calculate_voronoi_diagram(self, points=None):
        if points is None:
            points = self.points
        vor = Voronoi(points)
        return vor

    def calculate_delaunay_triangulation(self, points=None):
        if points is None:
            points = self.points
        tri = Delaunay(points)
        return tri

    def calculate_voronoi_cell_areas(self, vor):
        areas = []
        for region in vor.regions:
            if not -1 in region and len(region) > 0:
                polygon = vor.vertices[region]
                areas.append(self.calculate_polygon_area(polygon))
        return areas

    def calculate_polygon_area(self, polygon):
        x = polygon[:, 0]
        y = polygon[:, 1]
        return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))

    def calculate_delaunay_edge_lengths(self, tri):
        lengths = []
        for simplex in tri.simplices:
            for i in range(3):
                point1 = tri.points[simplex[i % 3]]
                point2 = tri.points[simplex[(i + 1) % 3]]
                length = np.linalg.norm(point2 - point1)
                lengths.append(length)

        return lengths

    def calculate_delaunay_triangle_angles(self, tri):
        angles = []
        for triangle in tri.simplices:
            side1 = tri.points[triangle[1]] - tri.points[triangle[0]]
            side2 = tri.points[triangle[2]] - tri.points[triangle[0]]
            dot_product = np.dot(side1, side2)
            cross_product = np.linalg.norm(np.cross(side1, side2))
            angle = np.arctan2(cross_product, dot_product)
            angles.append(angle)
        return angles

    def output_results(self):
        vor = self.calculate_voronoi_diagram()
        tri = self.calculate_delaunay_triangulation()

        voronoi_areas = self.calculate_voronoi_cell_areas(vor)
        delaunay_lengths = self.calculate_delaunay_edge_lengths(tri)
        delaunay_angles = self.calculate_delaunay_triangle_angles(tri)

         # データフレームの作成
        data = {
            'Voronoi Cell Area': voronoi_areas,
            'Delaunay Edge Length': delaunay_lengths,
            'Delaunay Triangle Angle': delaunay_angles
        }
        df = data#pd.DataFrame(data)

        # 結果の出力
        print("Voronoi Cell Areas:")
        print(df['Voronoi Cell Area'])
        print("\nDelaunay Edge Lengths:")
        print(df['Delaunay Edge Length'])
        print("\nDelaunay Triangle Angles:")
        print(df['Delaunay Triangle Angle'])

        # 結果の保存
        df.to_json('output.json', orient='records')

if __name__ == '__main__':
    analysis = VoronoiDelaunayAnalysis()
    analysis.output_results()
