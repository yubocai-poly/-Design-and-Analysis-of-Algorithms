import math
import random


# Randomized MinCut
## Question 5 ##
def random_element(dict):
    # 按照字典中的权重去输出一个随机的元素
    lis = []
    for key, value in dict.items():
        lis.extend([key] * value)
    return random.choice(lis)
    """
    sum = 0
    for key, value in dict:
        sum += value
    i = random.randint(1, sum)
    for key, value in dict:
        if i <= value:
            return key
        else:
            i -= value
    """


## Question 7 ##
def random_cut(m):
    n = len(m.adj)
    partition = {}
    for x in m.adj:
        partition[x] = []
    for _ in range(n - 2):
        i = random_element(m.deg)
        j = random_element(m.adj[i])
        m.contract(i, j)
        partition[i] = partition[i] + [j] + partition[j]
        del (partition[j])
    x = next(iter(partition))
    return [m.deg[x], [x] + partition[x]]


## Question 8 ##
def mincut_karger(L, p):
    # p is the desired error bound
    # TO COMPLETE
    # we first initialize the constants
    n = L[0]
    p = 2 / (n * (n - 1))
    k = math.ceil(math.log(p) / math.log(1 - p))
    start = time.time()
    print('The number of probability is: ' + str(p))
    print('The number of trials is: ' + str(k))
    optimal = math.inf
    optimal_cut = []
    for _ in range(k):
        m = MultiGraph(L)
        trial = random_cut(m)
        if trial[0] < optimal:
            optimal, optimal_cut = trial[0], trial[1]
    return [str(optimal), str(optimal_cut)]


## Contains Questions 4 and 6 ##
class MultiGraph:

    def __init__(self, L):
        self.adj = {}
        self.deg = {}
        for x in L[1]:
            if x[0] not in self.adj:
                self.adj[x[0]] = {x[1]: x[2]}
                self.deg[x[0]] = x[2]
            else:
                self.adj[x[0]][x[1]] = x[2]
                self.deg[x[0]] += x[2]
            if x[1] not in self.adj:
                self.adj[x[1]] = {x[0]: x[2]}
                self.deg[x[1]] = x[2]
            else:
                self.adj[x[1]][x[0]] = x[2]
                self.deg[x[1]] += x[2]

    def subset_from_integer(self, i):
        # i is an integer between 1 and 2^n - 2, with n the number of vertices
        subset = {}
        for x in self.adj:
            if i % 2 == 1:
                subset[x] = True
            i = i >> 1
        return subset

    def cutsize(self, i):
        # i is an integer between 1 and 2^n - 2, with n the number of vertices
        subset = self.subset_from_integer(i)
        res = 0
        for x, y in self.adj.items():
            for t, u in y.items():
                if x in subset and not t in subset:
                    res += u
        return [res, [x for x in subset]]

    def display(self):
        for x, y in self.adj.items():
            print("Neighbors of " + str(x) + ", which has degree " +
                  str(self.deg[x]))
            for t, u in y.items():
                print(str(t) + " with multiplicity " + str(u))

    ## Question 4 ##
    def contract(self, i, j):
        # contracts edge i,j (i absorbs j)
        mult_edge = self.adj[i][j]
        del self.adj[j][i]
        del self.adj[i][j]
        self.deg[i] -= mult_edge  # 这里我们减去由于删除边而导致的权重减少
        # 开始将j的边添加到i的边中
        for edge, weight in self.adj[j].items():
            if edge in self.adj[i]:
                self.adj[i][edge] += weight
                self.adj[edge][i] += weight
            else:
                self.adj[i][edge] = weight
                self.adj[edge][i] = weight
            del self.adj[edge][j]
            self.deg[i] += weight
        del self.adj[j]
        del self.deg[j]

    ## Question 6.1 ##
    def random_vertex(self):
        return random_element(self.deg)

    ## Question 6.2 ##
    def random_edge(self):
        i = self.random_vertex()
        return [i, random_element(self.adj[i])]
    
Lt = [5, [['a', 'b', 1], ['a', 'c', 1], ['a', 'e', 1], ['b', 'c', 1], ['b', 'e', 2], ['c', 'e', 1], ['c', 'd', 1]]]
m = MultiGraph(Lt)
print(m.adj)
print(m.deg)
m.contract('e', 'b')
print(m.adj)
print(m.deg)
