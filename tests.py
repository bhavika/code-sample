from edit_distance import *


def test_corpus():
    word_dict = create_corpus('20k.txt')
    assert (len(word_dict) > 0)


def test_isAnagram():
    word1 = "president"
    word2 = "depressant"
    assert isAnagram(word1, word2) is False

    word1 = "cat"
    word2 = "act"

    assert isAnagram(word1, word2) is True

    word1 = "loose"
    word2 = "lose"

    assert isAnagram(word1, word2) is False


def test_graph_construction():
    op_costs = [1, 3, 1, 5]
    word_dict = create_corpus('20k.txt')
    constructGraph(word_dict, op_costs)

    # this will locate the graph that was saved,
    # load it again & check that loading does not cause any read/write issues

    def pickle_exists():
        import os.path
        if os.path.isfile('graph_words_new.pkl'):
            file = open('graph_words_new.pkl', 'rb')
            graph = pickle.load(file)
            if len(graph) > 0:
                return True
        return False

    assert pickle_exists() is True


def test_editDistance():
    word1, word2 = "health", "hands"
    op_costs = [1, 3, 1, 5]
    ld, _ = editDistance(word1, word2, op_costs)
    cost = transformCost(word1, word2, op_costs)
    assert ld == 4
    assert cost == 3


def test_transformCosts():
    word1, word2 = "team", "mate"
    op_costs = [1,9,1,3]
    ld, _ = editDistance(word1, word2, op_costs)
    assert ld == 3
    assert transformCost(word1, word2, op_costs) == 3


def test_editDistance_Negative():
    word1, word2 = "ophthalmology", "glasses"
    op_costs = [7, 1, 5, 2]
    ld, _ = editDistance(word1, word2, op_costs)
    assert ld == -1



