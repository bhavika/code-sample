import sys
from collections import defaultdict
import operator
import string
import pickle

# Word List obtained here: https://github.com/first20hours/google-10000-english


def isAnagram(s1, s2):
    if sorted(s1) == sorted(s2):
        return True
    return False


def create_corpus(filepath):
    """
    Takes in a word list & converts it to a dictionary with the word being the
    key & its length being the value
    """
    word_dict = {}
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if len(line) >= 3:
                word_dict[line] = len(line)
    return word_dict


def editDistance(word1, word2, op_costs):
    """
    From Wikipedia:
    The Levenshtein distance has the following properties:
    It is zero if and only if the strings are equal.
    It is at least the difference of the sizes of the two strings.
    It is at most the length of the longer string.
    Triangle inequality: The Levenshtein distance between two strings is no greater than the sum of their
    Levenshtein distances from a third string.
    :param word1:
    :param word2:
    :param op_costs:
    :return:
    """
    if len(word1) > len(word2):
        word1, word2 = word2, word1
    if len(word2) == 0:
        return len(word1)

    h = len(word1) + 1
    w = len(word2) + 1

    d = [[0] * w for x in range(h)]

    # op stores operation history - which of the add, delete, change operations was selected
    op = [[0] * w for x in range(h)]

    if isAnagram(word1, word2):
        return op_costs[3], 4   # operation no 4 is anagram

    for i in range(h):
        d[i][0] = i
    for j in range(w):
        d[0][j] = j
    for i in range(1, h):
        for j in range(1, w):
            add = d[i][j-1] + op_costs[0]  # insertion cost
            delete = d[i-1][j] + op_costs[1]  # deletion cost
            change = d[i-1][j-1]
            if word1[i-1] != word2[j-1]:
                change += op_costs[2]  # substitution cost
            op[i][j], d[i][j] = min(enumerate([add, delete, change]), key=operator.itemgetter(1))

    lev_dist = d[h-1][w-1]
    last_op = op[h-1][w-1]

    # Check for validity of the Levenshtein distance
    valid_lev_dist = False
    if word1 == word2:
        if lev_dist == 0:
            valid_lev_dist = True
    elif lev_dist <= max(h, w) and lev_dist > abs(h-w):
        valid_lev_dist = True

    if valid_lev_dist:
        return lev_dist, last_op
    return -1, None


def constructGraph(word_dict, op_costs):
    graph = defaultdict(defaultdict)
    letters = string.ascii_lowercase
    for word, length in word_dict.items():
        for i in range(len(word)):
            # remove 1 character
            remove = word[:i] + word[i+1:]
            if remove in word_dict:
                lev_dist, _ = editDistance(word, remove, op_costs=op_costs)
                graph[word][remove] = lev_dist
            # change 1 character
            for char in letters:
                change = word[:i] + char + word[i+1:]
                if change in word_dict and change != word:
                    lev_dist, _ = editDistance(word, change, op_costs=op_costs)
                    graph[word][change] = lev_dist
        # add 1 character
        for i in range(len(word) + 1):
            for char in letters:
                add = word[:i] + char + word[i:]
                if add in word_dict:
                    lev_dist, _ = editDistance(word, add, op_costs=op_costs)
                    graph[word][add] = lev_dist

    with open('graph_words_new.pkl', 'wb') as f:
        pickle.dump(graph, f, pickle.HIGHEST_PROTOCOL)


def transformCost(start_word, end_word, op_costs):
    """
    Using Dijkstra's algorithm to find the shortest path between
    start_word & end_word.
    :param start_word: str
    :param end_word: str
    :param op_costs: cost of the add, delete, substitutde & anagram operations
    :return: int, shortest cost of transformation
    """
    file = open('graph_words_new.pkl', 'rb')
    graph = pickle.load(file)

    if isAnagram(start_word, end_word):
        lev_dist, _ = editDistance(start_word, end_word, op_costs=op_costs)
        return lev_dist

    else:
        graph_dict = {}

        for k, v in graph.items():
            graph_dict[k] = dict(v)

        unvisited = list(graph_dict.keys())

        D = {}  # distances
        P = {}  # predecessor

        for node in graph_dict.keys():
            D[node] = -1
            P[node] = ""

        D[start_word] = 0

        while len(unvisited) > 0:
            minCost = None
            node = ''

            for temp_node in unvisited:
                if minCost is None:
                    minCost = D[temp_node]
                    node = temp_node
                elif D[temp_node] < minCost:
                    minCost = D[temp_node]
                    node = temp_node

            unvisited.remove(node)

            for nbr, dist in graph_dict[node].items():
                if nbr in D and nbr in graph_dict:
                    if D[nbr] < D[node] + dist:
                        D[nbr] = D[node] + dist
                        P[nbr] = node

        return D[end_word]


def read_input():
    in_data = sys.stdin.readlines()
    op_costs, start_word, end_word = in_data[0].strip(), in_data[1].strip(), in_data[2].strip()
    return op_costs, start_word, end_word


def main():

    op_costs, start_word, end_word = read_input()

    start_word = start_word.lower()
    end_word = end_word.lower()
    op_costs = [int(x) for x in op_costs.split()]

    wdict = create_corpus('20k.txt')

    print("Working...")
    constructGraph(wdict, op_costs)

    print(transformCost(start_word, end_word, op_costs))

if __name__ == '__main__':
    main()
