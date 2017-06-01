# -*- coding:utf-8 -*-

import gzip
import pickle


def load_data():
    f = gzip.open('../data/mnist.pkl.gz', 'rb')
    training_data, validation_data, test_data = pickle.load(f, encoding='iso-8859-1')
    f.close()
    return training_data, validation_data, test_data


