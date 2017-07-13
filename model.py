# -*- coding: utf-8 -*-
import os
import numpy

import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F


class SkipGramModel(nn.Module):
    def __init__(self, args):
        super(SkipGramModel, self).__init__()

        self.args = args
        self.u_embedding = nn.Embedding(args.emb_size, args.emb_dimension, sparse=True)

    def save_embedding(self, id2word, file_name):
        # 输出的是u的
        embedding = self.u_embeddings.weight.data.numpy()
        output = open(os.path.join(self.args.dir, file_name), 'w', encoding='utf-8')
        output.write('%d %d\n' % (len(id2word), self.emb_dimension))
        output.flush()
        for wid, w in id2word.items():
            e = embedding[wid]
            e = ' '.join(map(lambda x: str(x), e))
            output.write('%s %s\n' % (w, e))
            output.flush()
        output.close()
