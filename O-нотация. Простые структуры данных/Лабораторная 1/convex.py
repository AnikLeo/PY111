import numpy as np
import matplotlib.pyplot as plt


def graham_scan(points):
    start = min(points, key=lambda p: p[1])

    def polar_angle(p):
        return np.arctan2(p[1] - start[1], p[0] - start[0])

    sorted_points = sorted(points, key=polar_angle)

    hull = [start]

    for point in sorted_points:
        while len(hull) > 1 and np.cross(hull[-1] - hull[-2], point - hull[-1]) <= 0:
            hull.pop()
        hull.append(point)

    return start, hull



if __name__ == '__main__':
    points = np.random.rand(30, 2) * 100
    print(points)
    start, hull = graham_scan(points)
    hull.append(hull[0])
    hull = np.array(hull)

    plt.figure()
    plt.scatter(points[:, 0], points[:, 1], label='Точки')
    plt.scatter(start[0], start[1], label='Начальная точка', color='red')
    plt.plot(hull[:, 0], hull[:, 1], label='Оболочка', color='black')
    plt.legend()
    plt.show()