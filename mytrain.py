# -*- coding: utf-8 -*-
import tqdm
import torch.optim as optim

def train(data, model, args):
    optimizer = optim.SGD(args.skip_gram_model.parameters(), lr=args.lr)

    pair_count = data.evaluate_pair_count(args.window_size)
    batch_count = args.iteration * pair_count / args.batch_size
    process_bar = tqdm(range(int(batch_count)))
    model.save_embedding(data.id2word, 'begin_embedding.txt')

    pos_pairs = data.get_batch_pairs(args.batch_size, args.window_size)
    for i in process_bar:


        pos_pairs, neg_pairs = data.get_pairs_by_neg_sampling(pos_pairs, 5)