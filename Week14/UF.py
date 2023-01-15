class UF:
    def __init__(self,S):
        self.id={}
        for x in S:
           self.id[x]=x
        self.rank ={}
        for x in S:
           self.rank[x]=1
        self.count = len(self.id.keys())

    def get_count(self):
        return self.count

    def union(self, p, q):

        r1 = self.find(p)
        r2 = self.find(q)

        if r1 == r2:
            return

        self.count -= 1

        if self.rank[r2] > self.rank[r1]:
            self.id[r1] = r2
        else:
            self.id[r2] = r1

        if self.rank[r2] == self.rank[r1]:
            self.rank[r1] += 1

    def find(self, p):
        if self.id[p] == p:
            return p
        # path compression
        self.id[p] = self.find(self.id[p])
        return self.id[p]

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)


def is_cyclic(graph, uf):
    for u, v in graph:
        if uf.is_connected(u, v):
            return True
        uf.union(u, v)
    return False

if __name__ == "__main__":
    uf = UF(['a', 'b', 'c', 'd', 'e'])
    print(uf.id)
    graph = [('a', 'b'), ('b', 'c'), ('c', 'a')]
    if is_cyclic(graph, uf):
        print("Graph contains a cycle.")
    else:
        print("Graph doesn't contain a cycle.")
