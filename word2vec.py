# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser(description='Word2vec')
parser.add_argument('-lr', type=float, default=0.025)
parser.add_argument('-epochs', type=int, default=5)
parser.add_argument('-window-size', type=int, default=5)
parser.add_argument('-min-count', type=int, default=5)
parser.add_argument('-batch-size', type=int, default=100)
parser.add_argument('-embed-dim', type=int, default=100)
parser.add_argument('-using-hs', action='store_true', default=False)

parser.add_argument('-no-cuda', action='store_true')
parser.add_argument('-test', action='store_true', default=False)
args = parser.parse_args()



