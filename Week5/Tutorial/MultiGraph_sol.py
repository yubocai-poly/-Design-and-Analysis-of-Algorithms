import math
import random
import time


def random_element(dict):
    N = 0
    for x in dict:
        N += dict[x]
    i = random.randint(1, N)
    for x in dict:
        if i <= dict[x]:
            return x
        else:
            i = i-dict[x]

def random_cut(m):
    n = len(m.adj)
    partition = {}
    for x in m.adj:
        partition[x] = []
    for _ in range(n-2):
        (i, j) = m.random_edge()
        m.contract(i, j)
        partition[i] = partition[i] + [j] + partition[j]
        del (partition[j])
    x = next(iter(partition))
    return [m.deg[x], [x] + partition[x]]


def mincut_karger(L, e):  # e is the wished error bound
    n = L[0]
    p = 2/n/(n-1)  # proba success at each trial is at least p
    # number of trials so that P(error)<=e
    k = math.ceil(math.log(e)/math.log(1-p))
    print("Number of trials Karger: " + str(k))
    start = time.time()
    best = math.inf
    best_cut = []
    for _ in range(k):
        m = MultiGraph(L)
        res_trial = random_cut(m)
        if res_trial[0] < best:
            best = res_trial[0]
            best_cut = res_trial[1]
    elapsed = (time.time() - start)
    print("Running time: " + str(elapsed))
    print("Average time per trial: " + str(elapsed/k))
    return [best, best_cut]


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

    # i is an integer between 1 and 2^n-2, with n the number of vertices
    def subset_from_integer(self, i):
        subset = {}
        for x in self.adj:
            if i % 2 == 1:
                subset[x] = True
            i = i >> 1
        return subset

    def cutsize(self, i):
        subset = self.subset_from_integer(i)
        res = 0
        for x, y in self.adj.items():
            for t, u in y.items():
                if x in subset and not t in subset:
                    res += u
        return [res, [x for x in subset]]

    def contract(self, i, j):  # contracts edge i,j (i absorbs j)
        mult_edge = self.adj[i][j]
        del self.adj[j][i]
        del self.adj[i][j]
        self.deg[i] -= mult_edge
        for x, y in self.adj[j].items():
            if x in self.adj[i]:
                self.adj[i][x] += y
                self.adj[x][i] += y
            else:
                self.adj[i][x] = y
                self.adj[x][i] = y
            del self.adj[x][j]
            self.deg[i] += y
        del self.adj[j]
        del self.deg[j]

    def random_vertex(self):
        return random_element(self.deg)

    def random_edge(self):
        i = self.random_vertex()
        j = random_element(self.adj[i])
        return (i, j)

    def display(self):
        for x, y in self.adj.items():
            print("Neighbours of " + str(x) + ", which has degree " + str(self.deg[x]))
            for t, u in y.items():
             print(str(t) + " with multiplicity " + str(u))
