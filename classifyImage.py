from keras import applications
from keras.models import model_from_json
from keras.preprocessing.image import ImageDataGenerator
import os
from skimage.io import imread
from skimage.transform import resize
from skimage import img_as_float

class classifyImage:
    def __init__(self):
        self.top_model = applications.VGG16(include_top=False, weights='imagenet')
        # load json and create model
        json_file = open('Model/bottleneck_fc_model.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        # load weights into new model
        loaded_model.load_weights("Model/bottleneck_fc_model_weights.h5")
        print("Loaded model from disk")

        # evaluate loaded model on test data
        loaded_model.compile(optimizer='adam',
                          loss='categorical_crossentropy', metrics=['accuracy'])
        self.model = loaded_model
        self.labels = {'Dog': [True, False, False],
                    'Hot Dog': [False, True, False],
                    'Not Dog': [False, False, True]}
        self.label = ''

    # function to return key for any value
    def get_key(self, val):
        for key, value in self.labels.items():
             if val == value:
                 return key

        return "key doesn't exist"

    def classify(self, image_name):
        img_width, img_height = 150, 150
        channels = 3
        img = imread(image_name)
        img = resize(img, (img_height,img_width,channels), \
            mode='reflect', anti_aliasing=True)

        datagen = ImageDataGenerator(samplewise_std_normalization=True)
        test_Image = img_as_float(datagen.standardize(img))

        new_test = test_Image.reshape((1,) + test_Image.shape)
        bottleneck_test = self.top_model.predict(new_test)

        prediction = self.model.predict(bottleneck_test)
        val = (prediction > 0.5).tolist()[0]

        self.label = self.get_key(val)
        return self.label
