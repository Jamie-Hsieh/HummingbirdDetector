#!/usr/bin/python3
import jetson_inference
import jetson_utils
import argparse
import os


global hummingbirdDetected
hummingbirdDetected = False

def getHbDetected():
    return hummingbirdDetected


parser = argparse.ArgumentParser()
parser.add_argument("filename", type=str, help="filename of the image to process")
parser.add_argument("--network", type=str, default="resnet-18", help="model to use, can be:  googlenet, resnet-18, ect. (see --help for others)")
opt = parser.parse_args()

img = jetson_utils.loadImage(opt.filename)
net = jetson_inference.imageNet(opt.network)
class_idx, confidence = net.Classify(img)
class_desc = net.GetClassDesc(class_idx)
print("image is recognized as "+ str(class_desc) +" (class #"+ str(class_idx) +") with " + str(confidence*100)+"% confidence")
print(str(class_desc) + " has been detected")

#bird_detection = BirdDetection()

if class_idx == 94:
    hummingbirdDetected = True
else:
    hummingbirdDetected = False

print("RESULT PRINTING")
print("Hummingbird detected: " + str(getHbDetected()))
    

