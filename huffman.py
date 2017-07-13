# -*- coding: utf-8 -*-
import heapq


class Node:
    def __init__(self, wid, frequency):
        self.wid = wid
        self.frequency = frequency
        self.father = None
        self.is_left_child = None
        self.left_child = None
        self.right_child = None
        self.code = []
        self.path = []


class HuffmanTree:
    def __init__(self, word_frequency):
        self.word_count = len(word_frequency)
        self.huffman = []
        unmerged_node = []
        for wid, c in word_frequency.items():
            node = Node(wid, c)
            heapq.heappush(unmerged_node, (c, wid, node))
            self.huffman.append(node)
        next_id = len(self.huffman)
        while len(unmerged_node) > 1:
            node1 = heapq.heappop(unmerged_node)[2]
            node2 = heapq.heappop(unmerged_node)[2]
            new_node = Node(next_id, node1.frequency + node2.frequency)
            node1.father = new_node.wid
            node2.father = new_node.wid
            new_node.left_child = node1.wid
            node1.is_left_child = True
            new_node.right_child = node2.wid
            node2.is_left_child = False
            self.huffman.append(new_node)
            heapq.heappush(unmerged_node, (new_node.frequency, next_id, new_node))
            next_id = len(self.huffman)

        self.get_huffman_code(unmerged_node[0][2].left_child)
        self.get_huffman_code(unmerged_node[0][2].right_child)

    def get_huffman_code(self, wid):
        if self.huffman[wid].is_left_child:
            code = [0]
        else:
            code = [1]
        self.huffman[wid].code = self.huffman[self.huffman[wid].father].code + code
        self.huffman[wid].path = self.huffman[self.huffman[wid].father].path + [
                            self.huffman[wid].father]

        if self.huffman[wid].left_child is not None:
            self.get_huffman_code(self.huffman[wid].left_child)
        if self.huffman[wid].right_child is not None:
            self.get_huffman_code(self.huffman[wid].right_child)

#??
    def get_huffman_code_and_path(self):
        positive = []
        negative = []
        for wid in range(self.word_count):
            pos = []
            neg = []
            for i, c in enumerate(self.huffman[wid].code):
                if c == 0:
                    pos.append(self.huffman[wid].path[i])
                else:
                    neg.append(self.huffman[wid].path[i])
            positive.append(pos)
            negative.append(neg)
        return positive, negative