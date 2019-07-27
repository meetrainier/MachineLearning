# -*- coding: utf-8 -*-
"""
Created on Sun May 19 20:45:02 2019

@author: manoj
"""

# to make this notebook's output stable across runs
import numpy as np
import os
def reset_graph(seed=42):
    tf.reset_default_graph()
    tf.set_random_seed(seed)
    np.random.seed(seed)

import tensorflow as tf
reset_graph()

x1 = tf.Variable(1)
print("Is x1 a graph?",x1.graph is tf.get_default_graph())

graph = tf.Graph()
with graph.as_default():
    x2 = tf.Variable(2)
	
print("Is x2 a graph?",x2.graph is graph)
print("Is x2 a default graph?",x2.graph is tf.get_default_graph())

w = tf.constant(3)
x = w + 2
y = x + 5
z = x * 3

with tf.Session() as sess:
    print(y.eval())  # 10
    print(z.eval())  # 15
	
with tf.Session() as sess:
    y_val, z_val = sess.run([y, z])
    print(y_val)  # 10
    print(z_val)  # 15	