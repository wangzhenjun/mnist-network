# -*- coding:utf-8 -*-

import mnist_loader
import network


training_data, validation_data, test_data = mnist_loader.load_data()

net = network.Network([784, 30, 10])
net.SGD(training_data, 30, 10, 3.0, test_data=test_data)

