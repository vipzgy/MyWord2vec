# -*- coding: utf-8 -*-
from collections import deque

class Data:
    def __init__(self, file_name, args):
        self.get_words(file_name, args.min_count)
        self.word_pair_catch = deque()
        self.init_sample_table()
        #tree = HuffmanTree(self.word_frequency)
        #self.huffman_positive, self.huffman_negative = tree.get_huffman_code_and_path()
        print('Word Count: %d' % len(self.word2id))
        print('Sentence Length: %d' % (self.sentence_length))
        print('Sentence count: %d' % (self.sentence_count))