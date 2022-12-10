import math

count = 0

# Question 1
"""
This function computes the Euclidean distance between two points
- p is the first point
- q is the second point

returns the Euclidean distance between p and q, i.e., the length of the segment pq
"""


def dist(p, q):
    assert len(p) == len(q)
    # Put your code below this line
    num = 0
    n = len(p)
    for i in range(n):
        num += (p[i] - q[i])**2
    return math.sqrt(num)


# Question 2
"""
For a given query point, this function returns the index of the point in an 
array of points P that is closest to query using the linear scan algorithm.
- query is the query point
- P is a set of points

returns
- the index of that nearest neighbour
- the distance of query to its nearest neighbour in P
"""


def linear_scan(query, P):
    # Put your code below this line
    dis = math.inf
    for i in range(len(P)):
        if dist(query, P[i]) < dis:
            dis = dist(query, P[i])
            index = i
    return index, dis


# Question 3
"""
This function computes the median of all the c coordinates
of a sub-array P of n points that is P[start] .. P[end - 1]
- P is a set of points
- start is the starting index
- end is the last index; the element P[end] is not considered
- coord is the coordinate considered for the median computation

returns the median along the coordinate coord
"""


def compute_median(P, start, end, coord):
    assert start <= end and 0 <= coord and coord < len(P[0])
    # Put your code below this line
    part_list = sorted(P[start:end], key=lambda x: x[coord])
    return part_list[(end - start) // 2][coord]


# Question 4
"""
Partitions the array P wrt to its median value of a coordinate
- P is a set of points (an array)
- start is the starting index
- end is the last index; the element P[end] is not considered
- coord is the coordinate used for partitioning

returns the index of the median value
"""


def partition(P, start, end, coord):
    assert start <= end and 0 <= coord and coord < len(P[0])
    # Put your code below this line
    m = compute_median(P, start, end, coord)
    for i in range(start, end):
        if P[i][coord] == m:
            P[start], P[i] = P[i], P[start]
            break
    i = start + 1
    for j in range(start + 1, end):
        if P[j][coord] < m:
            P[i], P[j] = P[j], P[i]
            i += 1
    P[start], P[i - 1] = P[i - 1], P[start]
    return i - 1


# Data structure for Question 5
class Node:
    """
    Constructs a node
    - index is the index of the data point stored at the node
    - coord is the coordinate used for the split
    - median is the split value
    - left is the left sub-tree
    - right is the right sub-tree
    """

    def __init__(self, index, coord=None, median=None, left=None, right=None):
        self.index = index
        self.coord = coord
        self.median = median
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node({self.index},{self.coord if self.coord is not None else 0},{self.median if self.median is not None else 0})"

    def __str__(self):
        return f"Node(index = {self.index}, coord = {self.coord}, median = {self.median}, left index = {None if self.left is None else self.left.index}, right index = {None if self.right is None else self.right.index})"


# Question 5
"""
Builds the kd-Tree for the sub-cloud P[start:end]
- P is an array of points
- start is the starting index
- end is the last index; the element P[end] is not considered
- coord is the coordinate defining the hyperplane at the root of the tree

returns the kd-Tree for the sub-cloud P[start:end]
"""


def build(P, start, end, coord):
    assert start <= end and 0 <= coord and coord < len(P[0])
    # Put your code below this line
    if start == end:
        return None
    m = partition(P, start, end, coord)
    return Node(m, coord, P[m][coord],
                build(P, start, m, (coord + 1) % len(P[0])),
                build(P, m + 1, end, (coord + 1) % len(P[0])))


# Question 6
"""
Helper method for the defeatist search in a kd-Tree
- query is the query point
- P is an array of points
- node is the root of the current sub-node of the kd-tree
- index is the index of the *current* nearest neighbour of query in P
- dmin is the distance from query to that *current* nearest neighbour

returns
- the index of the *updated* nearest neighbour of the query point in P
- the distance from the query point to that *updated* nearest neighbour
"""


def defeatist_search_help(query, P, node, index, dmin):
    # Put your code below this line
    if node is None:
        return index, dmin
    if dist(query, P[node.index]) < dmin:
        index, dmin = node.index, dist(query, P[node.index])
    if query[node.coord] < node.median:
        return defeatist_search_help(query, P, node.left, index, dmin)
    else:
        return defeatist_search_help(query, P, node.right, index, dmin)


"""
Defeatist search in a kd-Tree
- query is the query point
- P is an array of points

returns
- the index of the *updated* nearest neighbour of the query point in P
- the distance from the query point to that *updated* nearest neighbour
"""


def defeatist_search(query, P):
    # Put your code below this line
    # Prepare the kd-Tree, then call the helper method on its root
    kd_tree = build(P, 0, len(P), 0)
    return defeatist_search_help(query, P, kd_tree, 0, math.inf)


# Question 7
"""
Helper method for the backtracking search in a kd-tree
- query is the query point
- P is the list of points in the point cloud
- node is the root of the kd-tree
- index is the index of the *current* nearest neighbour of query in P
- dmin is the distance from query to that *current* nearest neighbour

returns
- the index of the *updated* nearest neighbour of the query point in P
- the distance from the query point to that *updated* nearest neighbour
"""


def backtracking_search_help(query, P, node, index, dmin):
    global count
    count += 1
    # Put your code below this line
    if node is None:
        return index, dmin
    if dist(query, P[node.index]) < dmin:
        index, dmin = node.index, dist(query, P[node.index])
    if query[node.coord] < node.median:
        index, dmin = backtracking_search_help(query, P, node.left, index,
                                               dmin)
        if abs(query[node.coord] - node.median) < dmin:
            index, dmin = backtracking_search_help(query, P, node.right, index,
                                                   dmin)
    else:
        index, dmin = backtracking_search_help(query, P, node.right, index,
                                               dmin)
        if abs(query[node.coord] - node.median) < dmin:
            index, dmin = backtracking_search_help(query, P, node.left, index,
                                                   dmin)
    return index, dmin


"""
Backtracking search in a kd-tree
- query is the query point
- P is the list of points in the point cloud

returns
- the index of the *updated* nearest neighbour of the query point in P
- the distance from the query point to that *updated* nearest neighbour
"""


def backtracking_search(query, P):
    global count
    count = 0
    # Put your code below this line
    # Prepare the kd-Tree, then call the helper method on its root
    kd_tree = build(P, 0, len(P), 0)
    return backtracking_search_help(query, P, kd_tree, 0, math.inf)
