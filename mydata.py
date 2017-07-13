# -*- coding: utf-8 -*-
import os
import numpy
from collections import deque


class InputData:
    def __init__(self, file_name, args):
        self.args = args
        # 队列存储所有配对
        self.word_pair_catch = deque()
        # 采样表
        self.sample_table = []
        # 去掉频率低于mini_count后所有的单词
        self.sentence_length = 0
        # 句子个数
        self.sentence_count = 0
        # 词 --> id
        self.word2id = {}
        # id --> 词
        self.id2word = {}
        # 词频率
        self.word_frequency = {}
        # 去重去低频次之后单词个数
        self.word_count = 0
        self.input_file = open(os.path.join(self.args.dir, file_name), encoding='utf-8').readlines()

        self.get_words(self.args.min_count)
        self.init_sample_table()

        if args.using_hs:
            pass
            # tree = HuffmanTree(self.word_frequency)
            # self.huffman_positive, self.huffman_negative = tree.get_huffman_code_and_path()
        print('Word Count: %d' % len(self.word2id))
        print('Sentence Length: %d' % (self.sentence_length))
        print('Sentence count: %d' % (self.sentence_count))

    # 输入，统计所有词
    def get_words(self):
        word_frequency = {}
        for line in self.input_file:
            self.sentence_count += 1
            line = line.strip().split(' ')
            self.sentence_length += len(line)
            for w in line:
                try:
                    word_frequency[w] += 1
                except:
                    word_frequency[w] = 1
        wid = 0
        for w, c in word_frequency.items():
            if c < self.args.min_count:
                self.sentence_length -= c
                continue
            self.word2id[w] = wid
            self.id2word[wid] = w
            self.word_frequency[wid] = c
            wid += 1
        self.word_count = len(self.word2id)

    def init_sample_table(self):
        sample_table_size = 1e8
        # print(list(self.word_frequency.values()).__class__, self.word_frequency.values().__class__)
        pow_frequency = numpy.array(list(self.word_frequency.values())) ** 0.75
        words_pow = sum(pow_frequency)
        ratio = pow_frequency / words_pow
        count = numpy.round(ratio * sample_table_size)
        for wid, c in enumerate(count):
            self.sample_table += [wid] * int(c)
        self.sample_table = numpy.array(self.sample_table)

# vip ???
    def get_batch_pairs(self):
        while len(self.word_pair_catch) < self.args.batch_size:
            print('实际上一次采样就足够一次epoch，看看输出了几次')
            for _ in range(10000):
                sentence = self.input



# doubt
    def evaluate_pair_count(self, window_size):
        return self.sentence_length * (2 * window_size - 1) - (self.sentence_count - 1) * (
        1 + window_size) * window_size











