#This version of program introduces 
# 1. How to use a coefficients array 
# 2. How to use a placeholder

import numpy as np
import tensorflow as tf
coefficients = np.array([[1.],[-10],[25]])
w = tf.Variable(0,dtype=tf.float32)#variable declaration 
x = tf.compat.v1.placeholder(tf.float32,[3,1])#placeholder is a way of telling that I will declare this variable later
cost = x[0][0]*w**2+x[1][0]*w+x[2][0] #equation.  

train=tf.compat.v1.train.GradientDescentOptimizer(0.01).minimize(cost)#.01 is learning rate
init = tf.compat.v1.global_variables_initializer()
session = tf.compat.v1.Session()

session.run(init)
print(session.run(w))

session.run(train,feed_dict={x:coefficients})
print(session.run(w))

for i in range(1000):
	session.run(train,feed_dict={x:coefficients})
print(session.run(w))