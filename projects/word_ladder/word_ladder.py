# Given two words (beginWord and endWord), and a dictionary's word list, return the
# shortest transformation sequence from beginWord to endWord

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a
# transformed word.
​
# Note:
# Return None if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
​
# Sample:
# beginWord = "hit"
# endWord = "cog"
# return: ['hit', 'hot', 'cot', 'cog']

# beginWord = "sail"
# endWord = "boat"
# ['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']

# beginWord = "hungry"
# endWord = "happy"
# None
​
# Breakdown
# Word list/words - Vertexes
# One letter difference- edges
# Shortest - BFS
# dictionary - list of vertexes
# beginWOord - starting vertex
# endWord - destination vertex
# No duplicates - uset a set()
# Same length - don't ahve to do anything with different length words
​​
# If we organize the word list in a graph
# with words as vertexes and edges between
# two words that are 1 letter different,
# then
# if we do a BFS from BeginWord to EndWord
# the resulting path will be
# transformation sequence
​
f = open('words.txt', 'r')
words = f.read().split("\n")
f.close()
​
word_set = set()
for word in words:
    word_set.add(word.lower())
​
# Instead of converting the world list into a graph
# I'm going to make a helper function that looks up
# What neighbors or edges a word would have in the graph
​
# Calculate a small part of the graph to find edges and vertexes relevant to
# our current problem

#  find and or create all nodes or edges for words that only vary by 1 letter e.g. sail & bail or hip & hop
#  replaces entry in adjacency list for that node


def get_neighbors(word):
    neighbors = []
    word_list = list(word)
    # represents our word as [w, o, r, d]
    for i in range(len(word_list)):
        for letter in list('abcdefghijklmnopqrstuvwxyz'):
            temp_word = list(word_list)
            temp_word[i] = letter
            # Join the list version of the world back into a string
            w = "".join(temp_word)
            if w != word and w in word_set:
                neighbors.append(w)

    return neighbors


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


​
# Use a BFS variant to find our answer
def find_word_ladder(begin_word, end_word):
    qq = Queue()
    visited = set()
    qq.enqueue([begin_word])

    while qq.size() > 0:
        path = qq.dequeue()
        vertex = path[-1]

        if vertex not in visited:
            if vertex == end_word:
                return path
            visited.add(vertex)

            for new_word in get_neighbors(vertex):
                new_path = list(path)
                new_path.append(new_word)
                qq.enqueue(new_path)


​
print(find_word_ladder("sail", "boat"))
print(find_word_ladder("sail", "boats"))
print(find_word_ladder("sail", "bbbb"))
# print(find_word_ladder("sail", "boat"))
