
# coding: utf-8

# In[1]:


import numpy as np
import cv2
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile
#import imutils
import time
from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt
from PIL import Image


print('ok')


# In[2]:


# This is needed to display the images.
#matplotlib inline

# This is needed since the notebook is stored in the object_detection folder.
sys.path.append("..")
print('ok')


# In[3]:


from utils import label_map_util
from utils import visualization_utils as vis_util
from vtils import viz_labels


# In[4]:


# What model to download.
MODEL_NAME = 'tae'
PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'
# Path to frozen detection graph. This is the actual model that is used for the object detection.
# List of the strings that is used to add correct label for each box.
PATH_TO_LABELS = os.path.join('tae', 'my_labels.pbtxt')
NUM_CLASSES = 9


# In[5]:


detection_graph = tf.Graph()
with detection_graph.as_default():
  od_graph_def = tf.GraphDef()
  with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
    serialized_graph = fid.read()
    od_graph_def.ParseFromString(serialized_graph)
    tf.import_graph_def(od_graph_def, name='')
print('ok')


# In[6]:


label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)


# In[7]:


def load_image_into_numpy_array(image):
  (im_width, im_height) = image.size
  return np.array(image.getdata()).reshape(
      (im_height, im_width, 3)).astype(np.uint8)


# In[9]:


cap = cv2.VideoCapture(0)
w=640
h=400
with detection_graph.as_default():
  with tf.Session(graph=detection_graph) as sess:
    while True:
        ret, image_np = cap.read()
        image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
        detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
        detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
        detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
        num_detections = detection_graph.get_tensor_by_name('num_detections:0')
        image_np_expanded = np.expand_dims(image_np, axis=0)

        (boxes, scores, classes, num) = sess.run(
              [detection_boxes, detection_scores, detection_classes, num_detections],
              feed_dict={image_tensor: image_np_expanded})

        (new_boxes, new_classes, new_scores) = viz_labels.filter_labels(boxes, scores, classes)
        (data_deteced, width, height) = viz_labels.convert_labels(np.array(new_boxes), np.array(new_classes), np.array(new_scores), w=640, h=400)
        data_focused = viz_labels.calculate_focus(data_deteced)
        cv2.putText(image_np, data_focused, (0, 0), cv2.FONT_HERSHEY_SIMPLEX, 2,(255,0,0))
        # cv2.line(image_np, (int(a*2), int(b*2)), (int(c*2), int(d*2)), (0,255,0))
        vis_util.visualize_boxes_and_labels_on_image_array(
            image_np,
            np.array(new_boxes),
            np.array(new_classes),
            np.array(new_scores),
            category_index,
            use_normalized_coordinates=True,
            min_score_thresh=.6,
            line_thickness=8)
        cv2.imshow('object detection', cv2.resize(image_np, (w,h)))
#        time.sleep(1.5)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

