import numpy as np

labels_name = np.array(['sofa', 'chair', 'tale', 'refrigerator', 'bed', 'tv', 'bench', 'dog', 'bicycle'])
labels_class = np.array([63, 62, 67, 82, 65, 72, 15, 18, 2])

def filter_labels(boxes, scores, classes):
    squeeze_boxes = np.squeeze(boxes)
    squeeze_scores = np.squeeze(scores)
    squeeze_class = np.squeeze(classes).astype(np.int32)
    new_boxes = []
    new_classes = []
    new_scores = []
    for i, class_index in enumerate(squeeze_class[0:10],0):
      for j, label_index in enumerate(labels_class,0):
        if  class_index == label_index:
          new_boxes.append(squeeze_boxes[i])
          new_classes.append(squeeze_class[i])
          new_scores.append(squeeze_scores[i])

    return (new_boxes, new_classes, new_scores)

def convert_labels(squeeze_boxes, squeeze_classes, squeeze_scores, w, h):
    list_labels_class = list(labels_class)
    result = []
    a=0
    b=0
    c=0
    d=0
    for index, i in enumerate(squeeze_scores, 0):
        if i > 0.6:
            (x_top_left, x_btm_right, y_top_left, y_btm_right) = (
                squeeze_boxes[index][1] * w, 
                squeeze_boxes[index][3] * w, 
                squeeze_boxes[index][0] * h, 
                squeeze_boxes[index][2] * h)
            h_box = int(y_btm_right - y_top_left)
            w_box = int(x_btm_right - x_top_left)
            x_top_right = x_top_left + w_box
            y_top_right = y_top_left
            x_btm_left = x_top_left
            y_btm_left = y_btm_right + h_box
            name = labels_name[list_labels_class.index(squeeze_classes[index])]
            result.append({
                "name": name,
                "w": w_box,
                "h": h_box,
                "x_top_left": x_top_left,
                "y_top_left": y_top_left,
                "x_btm_right": x_btm_right,
                "y_btm_right": y_btm_right,
                "x_top_right": x_top_right,
                "y_top_right": y_top_right,
                "x_btm_left": x_btm_left,
                "y_btm_left": y_btm_left
            })
    return (result, w,h)

def calculate_focus(data_deteced):
    # w=640
    # h=400
    data = ""

    for box in data_deteced:
        if box['x_btm_right'] - 120 > 100 and box['y_btm_left'] > 120 and box['w'] > 100 and box['h'] > 100:
            data += str(box['name']) + " "
        elif 520 - box['x_btm_left'] > 100 and box['y_btm_right'] > 120 and box['w'] > 100 and box['h'] > 100:
            data += str(box['name']) + " "
    
    return "!!!CAREFUL : " + data
  