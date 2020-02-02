import cv2
import numpy as np
import time


#img = cv2.resize(img, None, fx=0.4, fy=0.4)
# Load Yolo

def smart_count(img_name,conf=0.5, sample=False):
    img = cv2.imread(img_name)
    return count_people(img, conf,sample)

def smart_count1(conf=0.5, sample=False):
    cap = cv2.VideoCapture(0)
    ret, img = cap.read()
    img.
    
    return count_people(img, conf,sample)

def count_people(image, conf_thresh=0.5 ,showSample=False):
    net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
    classes = []
    with open("coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    colors = np.random.uniform(0, 255, size=(len(classes), 3))
    img = image
    #img = cv2.resize(img, None, fx=0.4, fy=0.4)
    person_count = 0
    #Start HERE
    #ret, img = cap.read()
    #img = cv2.resize(img, None, fx=0.4, fy=0.4)
    height, width, channels = img.shape

    # Detecting objects
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

    net.setInput(blob)
    outs = net.forward(output_layers)

    # Showing informations on the screen
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > conf_thresh and classes[class_id] == "person":
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
    if(showSample):
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, conf_thresh, 0.4)
        font = cv2.FONT_HERSHEY_PLAIN
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                color = colors[i]
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                cv2.putText(img, label, (x, y + 30), font, 3, color, 3)
                person_count += 1
        cv2.imshow('haha', img)
        print("Found: " + str(person_count))
        while not (cv2.waitKey(1) & 0xFF == ord('q')):
            pass
        cv2.destroyAllWindows()
    else:
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, conf_thresh, 0.4)
        font = cv2.FONT_HERSHEY_PLAIN
        for i in range(len(boxes)):
            if i in indexes:
                person_count += 1
        return person_count

def take_still_laptop():
    cap = cv2.VideoCapture(0)
    ret, imgg = cap.read()
    time.sleep(1)
    ret, imgg = cap.read()

    # while not (cv2.waitKey(1) & 0xFF == ord('q')):
    #     pass
    cap.release()
    #cv2.destroyAllWindows()
    return imgg

##############
# cap = cv2.VideoCapture(0)
# ret, imgg = cap.read()
