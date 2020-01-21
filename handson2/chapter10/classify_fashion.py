import tensorflow as tf
print("tf version=",tf.__version__)

from tensorflow import keras 
print("Keras version=",keras.__version__)

import matplotlib as mpl
import matplotlib.pyplot as plt

import os

# Where to save the figures
PROJECT_ROOT_DIR = "."
CHAPTER_ID = "ann"
IMAGES_PATH = os.path.join(PROJECT_ROOT_DIR, "images", CHAPTER_ID)
os.makedirs(IMAGES_PATH, exist_ok=True)

def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    path = os.path.join(IMAGES_PATH, fig_id + "." + fig_extension)
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)

fashion_mnist = keras.datasets.fashion_mnist
(X_train_full,y_train_full),(X_test,y_test)=fashion_mnist.load_data()
print("Training set shape=",X_train_full.shape)
print("Training set data type",X_train_full.dtype)

#Create a validation set 
#Also scale so that values are between 0 and 1
#a[:5000] gives initial 5000 elements. It is same as a[0:5000]
#a[5000:] gives elements after initial 5000. It is same as a[5000:the_last_index]
X_valid, X_train = X_train_full[:5000] / 255., X_train_full[5000:] / 255.
y_valid, y_train = y_train_full[:5000], y_train_full[5000:]
X_test = X_test / 255.

# See one image , just to be sure things are okay
'''
plt.imshow(X_train[0], cmap="binary")
plt.axis('off')
plt.show()
'''

#print y train
print("y_train=",y_train)

#
class_names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
               "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]
			   
#
print("\nThe first label is:",class_names[y_train[0]])
#
'''
model = keras.models.Sequential()
model.add(keras.layers.Flatten(input_shape=[28, 28]))
model.add(keras.layers.Dense(300, activation="relu"))
model.add(keras.layers.Dense(100, activation="relu"))
model.add(keras.layers.Dense(10, activation="softmax"))
'''
keras.backend.clear_session()

#
import numpy as np

np.random.seed(42)
tf.random.set_seed(42)

model = keras.models.Sequential([
    keras.layers.Flatten(input_shape=[28, 28]),
    keras.layers.Dense(300, activation="relu"),
    keras.layers.Dense(100, activation="relu"),
    keras.layers.Dense(10, activation="softmax")
])

print(model.summary())

#keras.utils.plot_model(model, "my_mnist_model.png", show_shapes=True)#graphviz installation was needed

model.compile(loss="sparse_categorical_crossentropy",   #some other loss functions are 
														#mean_squared_error, mean_absolute_error,
														#mean_absolute_error,squared_hinge, 
														#categorical_hinge, logcosh
              optimizer="sgd",				#Some optimizers are RMSprop, Adagrad,Adam
              metrics=["accuracy"])    #For classification problems accuracy is used.  
			  
history = model.fit(X_train, y_train, epochs=30,
                    validation_data=(X_valid, y_valid)) #validation_data: Data on which to evaluate the loss and any model metrics at the end of each epoch. 
														#The model will not be trained on this data.
					
print(history.params)
print("\nepoch=",history.epoch)
print("\nHistory keys are:",history.history.keys())

import pandas as pd

#Plot the learning curve
plot_learning_curve = 0
if(plot_learning_curve):
	pd.DataFrame(history.history).plot(figsize=(8, 5))
	plt.grid(True)
	plt.gca().set_ylim(0, 1)
	save_fig("keras_learning_curves_plot")
	plt.show()

#Get accuracy
model.evaluate(X_test, y_test)

#Test 
X_new = X_test[:3]
y_proba = model.predict(X_new)
y_proba.round(2)

y_pred = model.predict_classes(X_new)
print("y_pred=",y_pred)

np.array(class_names)[y_pred]

y_new = y_test[:3]
print(y_new)

#print the images
print_test_images=0
if(print_test_images):
	plt.figure(figsize=(7.2, 2.4))
	for index, image in enumerate(X_new):
		plt.subplot(1, 3, index + 1)
		plt.imshow(image, cmap="binary", interpolation="nearest")
		plt.axis('off')
		plt.title(class_names[y_test[index]], fontsize=12)
	plt.subplots_adjust(wspace=0.2, hspace=0.5)
	save_fig('fashion_mnist_images_plot', tight_layout=False)
	plt.show()


