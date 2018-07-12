from collections import defaultdict
from random import uniform
from math import sqrt

def average(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    
    Returns a new point which is the center of all the points.
    """
    dimensions = len(points[0])

    new_center = []

    for dimension in xrange(dimensions):
        dim_sum = 0  # dimension sum
        for p in points:
            dim_sum += p[dimension]

        # average of each dimension
        new_center.append(dim_sum / float(len(points)))

    return new_center

def new_centroids(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers where `k` is the number of unique assignments.
    """
    new_means = defaultdict(list)
    centers = []
    for assignment, point in zip(assignments, dataset):
        new_means[assignment].append(point)
        
    for points in new_means.itervalues():
        centers.append(average(points))

    return centers

def distance(a, b):
    """
    Calculates the euclidean distance between points a, b.
    """
    dimensions = len(a)
    
    _sum = 0
    for dimension in xrange(dimensions):
        difference_sq = (a[dimension] - b[dimension]) ** 2
        _sum += difference_sq
    return sqrt(_sum)

def cluster(data_points, centers):
    """
    Given a data set and a list of points betweeen other points,
    assign each point to an index that corresponds to the index
    of the center point on it's proximity to that point. 
    Return a an array of indexes of centers that correspond to
    an index in the data set; that is, if there are N points
    in `dataset` the list we return will have N elements. Also
    If there are Y points in `centers` there will be Y unique
    possible values within the returned list.
    """
    assignments = []
    for point in data_points:
        shortest = ()  # positive infinity
        shortest_index = 0
        for i in xrange(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments

def generate_k(dataset, k):
    """
    Given `dataset`, which is an array of arrays,
    find the minimum and maximum for each coordinate, a range.
    Generate `k` random points between the ranges.
    Return an array of the random points within the ranges.
    """
    centers = []
    dimensions = len(dataset[0])
    min_max = defaultdict(int)

    for point in dataset:
        for i in xrange(dimensions):
            val = point[i]
            min_key = 'min_%d' % i
            max_key = 'max_%d' % i
            if min_key not in min_max or val < min_max[min_key]:
                min_max[min_key] = val
            if max_key not in min_max or val > min_max[max_key]:
                min_max[max_key] = val

    for _k in xrange(k):
        rand_point = []
        for i in xrange(dimensions):
            min_val = min_max['min_%d' % i]
            max_val = min_max['max_%d' % i]
            
            rand_point.append(uniform(min_val, max_val))

        centers.append(rand_point)

    return centers

def k_means(data, k):
    k_points = generate_k(data, k)
    assignments = cluster(data, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = new_centroids(data, assignments)
        old_assignments = assignments
        assignments = cluster(data, new_centers)
    return zip(assignments, data)

def main():
    points = [[1, 2],[2, 1],[3, 1],[5, 4],[5, 5],[6, 5],[10, 8],[7, 9],[11, 5],[14, 9],[14, 14]]
    print k_means(points, 2)

if __name__ == "__main__":
    main()