import itertools
import math
import random
from collections import defaultdict

import numpy


def nCr(n, r):
    f = math.factorial
    return int(f(n) / f(r) / f(n - r))


# import numpy

class Graph(object):
    """ Graph data structure """

    def __init__(self, vertices=[], edges=[], random=False, n=0, p=0):
        """vertices: list of vertices of graph
           edges: list of tuples giving edges of graph
           random: indicates we want to generate a random graph
           n: [n] forms vertex set of random graph
           p: probability any given edge in our random graph
           """

        self._graph = defaultdict(set)

        if random:
            vertices = list(range(1, n + 1))
            random_indices = list(numpy.random.binomial(1, p, size=nCr(n, 2)))
            all_edges = []
            for i in range(len(vertices)):
                for j in range(i + 1, len(vertices)):
                    all_edges.append((vertices[i], vertices[j]))
            edges = [all_edges[i] for i in range(len(all_edges)) if random_indices[i] == 1]

        self.add_edges(edges)
        self.order = len(vertices)
        self.size = len(edges)
        self.vertices = vertices
        self.edges = edges

        # calculate  delta
        delta = self.order - 1
        for v in self.vertices:
            deg_v = len(self._graph[v])
            if deg_v < delta:
                delta = deg_v
        self.delta = delta

    def __str__(self):
        """Print the graph in a sensible form"""
        return "* Order=" + str(self.order) + ", Size=" + str(self.size) + ", " + str(
            dict(self._graph)) + " *"

    def add_edges(self, edges):
        """ Add edges (list of tuple pairs) to graph """
        for v1, v2 in edges:
            self.add(v1, v2)

    def add(self, v1, v2):
        """ Add connection between node1 and node2 """
        self._graph[v1].add(v2)
        self._graph[v2].add(v1)

    def neighbours(self, v):
        return self._graph[v]

    def naive_hamiltonian(self):
        permutations = itertools.permutations(self.vertices[1:])
        for permutation in permutations:
            if permutation[-1] not in self.neighbours(self.vertices[0]):
                continue
            for i in range(len(permutation) - 1):
                if permutation[i + 1] not in self.neighbours(permutation[i]):
                    break
            return [self.vertices[0]] + list(permutation)
        return

    def simple_hamiltonian(self):
        candidate = [self.vertices[0]]
        maxcandidate = [1] + [0] * (self.order - 1)
        position = 1
        while True:

            if len(candidate) == self.order:
                if candidate[-1] in self.neighbours(self.vertices[0]):
                    return candidate
                else:
                    maxcandidate = candidate
                    candidate = candidate[:-1]
                    position -= 1
                    # print(position)
                    continue
            else:

                neighbours = self.neighbours(candidate[position - 1])
                compareto = maxcandidate[position]
                possible_new_vertices = [y for y in [x for x in neighbours if x not in candidate] if
                                         y > compareto]

                if bool(possible_new_vertices):
                    newvertex = min([y for y in neighbours if y > compareto and y not in candidate])
                    candidate.append(newvertex)
                    maxcandidate = candidate + [0]
                    position += 1
                else:
                    maxcandidate = candidate
                    candidate = candidate[:-1]
                    # print(candidate)
                    position -= 1

                    if candidate == [self.vertices[0]] or candidate == []:
                        return False

    def smarter_hamiltonian(self, T):
        P = [self.vertices[0]]
        count = 1

        while True:
            if len(P) == self.order and P[-1] in self.neighbours(self.vertices[0]):
                return P, count

            elif len(P) < self.order and bool(
                    self.neighbours(P[-1]).intersection(
                        set(self.vertices) - set(P))):  # set non empty
                P.append(random.sample(
                    (self.neighbours(P[-1]).intersection(set(self.vertices) - set(P))), 1)[0])

            else:
                vk_neighbours = self.neighbours(P[-1])
                if not bool(vk_neighbours):
                    return False, count  # zero degree of vk
                vi = random.sample(vk_neighbours.intersection(set(P)), 1)[0]
                i = P.index(vi)
                new_P_start = P[:i + 1]
                new_P_end = list(reversed(P[i + 1:]))
                P = new_P_start + new_P_end
            count += 1

            if count > T:
                return False, count


def q1():
    # First some paticular graphs that we either know have hamilton cycles or don't
    for graph in [Graph(vertices=[1, 2, 3], edges=[(1, 2), (2, 3), (3, 1)]),
                  Graph(vertices=[1, 2, 3], edges=[(1, 2), (2, 3)]),
                  Graph(vertices=[1, 2, 3, 4], edges=[(1, 2), (2, 3), (3, 1)]),
                  Graph(vertices=[1, 2, 3, 4, 5, 6],
                        edges=[(1, 2), (3, 4), (2, 4), (1, 4), (5, 6), (6, 3), (2, 5), (5, 6)])]:
        result = graph.simple_hamiltonian()
        if result:
            print(str(graph) + " has a hamiltonian cycle: " + str(result))
        else:
            print(str(graph) + " has no hamiltonian cycle")

    pvalues = [0.3]
    nvalues = list(range(4, 21, 2))

    trials = 100

    factorvalues = [0.1, 0.55, 1, 1.45, 1.9]
    for n in nvalues:
        for factor in factorvalues:
            count = 0
            deltacount = 0
            for trial in range(trials):
                graph = Graph(random=True, n=n, p=factor * numpy.log(n) / n)
                if graph.simple_hamiltonian():
                    count += 1
                if graph.delta < 2:
                    deltacount += 1
            print("n=" + str(n) + ", factor=" + str(factor) + ", hamiltonian: " + str(
                count) + ", non-hamiltonian: " + str(trials - count) + ", delta<2 :" + str(
                deltacount))


def q4():
    for graph in [Graph(vertices=[1, 2, 3], edges=[(1, 2), (2, 3), (3, 1)]),
                  Graph(vertices=[1, 2, 3], edges=[(1, 2), (2, 3)]),
                  Graph(vertices=[1, 2, 3, 4], edges=[(1, 2), (2, 3), (3, 1)]),
                  Graph(vertices=[1, 2, 3, 4, 5, 6],
                        edges=[(1, 2), (3, 4), (2, 4), (1, 4), (5, 6), (6, 3), (2, 5), (5, 6)])]:

        result, T = graph.smarter_hamiltonian(1000)
        if result:
            print(str(graph) + " has a hamiltonian cycle: " + str(result))
        else:
            print(str(graph) + " has no hamiltonian cycle")

    trials = 1000
    pvalues = [0.3, 0.5, 0.7, 0.9]
    nvalues = list(range(4, 15, 2))

    trials = 10000

    for n in nvalues:
        for p in pvalues:
            count = 0
            Tvalues = []
            while count < 5000:
                graph = Graph(random=True, n=n, p=p)
                result = graph.simple_hamiltonian()
                if result:
                    count += 1
                    found, T = graph.smarter_hamiltonian(1000)
                    if found:
                        Tvalues.append(T)
            print("n=" + str(n) + ", p=" + str(p) + ", #hamiltonian cycles: " + str(
                count) + ", 95'th T percentile: " + str(numpy.percentile(Tvalues, 95)))


def cdf_p_n_95(p, n):
    c = 0
    k = 1
    while True:
        c += (1 - p) ** (k - 1) * p
        k += 1
        if c > 0.95:
            return k
