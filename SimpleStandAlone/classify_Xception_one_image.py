#Note: for a refrigerator , it predicted 'safe'. However the second probability was correct. 
# Predicted: [('n04125021', 'safe', 0.45633033), ('n04070727', 'refrigerator', 0.3461617), ('n03710193', 'mailbox', 0.03995161)]

from tensorflow.keras.applications.xception import VGG16
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.xception import preprocess_input, decode_predictions
import numpy as np


img_path = '../data/refrigerator.jpg'
img = image.load_img(img_path, target_size=(299, 299))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

model = Xception(weights='imagenet')
preds = model.predict(x)
# decode the results into a list of tuples (class, description, probability)
# (one such list for each sample in the batch)
print('Predicted:', decode_predictions(preds, top=3)[0])
