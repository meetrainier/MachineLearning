import numpy as np
import tensorflow as tf
w = tf.Variable(0,dtype=tf.float32)#variable declaration 

cost = w**2-10*w+32 #equation.  

train=tf.compat.v1.train.GradientDescentOptimizer(0.01).minimize(cost)#.01 is learning rate
init = tf.compat.v1.global_variables_initializer()
session = tf.compat.v1.Session()

session.run(init)
print(session.run(w))

session.run(train)
print(session.run(w))

for i in range(1000):
	session.run(train)
print(session.run(w))