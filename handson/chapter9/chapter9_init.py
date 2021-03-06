# -*- coding: utf-8 -*-
"""
Created on Sun May 19 20:45:02 2019

@author: manoj
9/26/2019: replaced deprecated functions to enable use of tensorflow 1.14.0
"""

# to make this notebook's output stable across runs
import numpy as np
import os
def reset_graph(seed=42):
    #tf.reset_default_graph()
    tf.compat.v1.reset_default_graph()
    #tf.set_random_seed(seed)
    tf.compat.v1.set_random_seed(seed)
    np.random.seed(seed)

import tensorflow as tf
reset_graph()

x = tf.Variable(3, name="x")
y = tf.Variable(4, name="y")
f = x*x*y + y + 2

#sess = tf.Session()
sess = tf.compat.v1.Session()
sess.run(x.initializer)
sess.run(y.initializer)
result = sess.run(f)
print("result=",result)

'''

init = tf.global_variables_initializer()

with tf.Session() as sess:
    init.run()
    result = f.eval()
''' 
