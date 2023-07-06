import sys
import argparse
#import HummingbirdDetection

from jetson_inference import detectNet
from jetson_utils import videoSource, videoOutput, Log
import os

global birdCount
birdCount = 0

# parse the command line
parser = argparse.ArgumentParser(description="Locate objects in a live camera stream using an object detection DNN.", 
                                 formatter_class=argparse.RawTextHelpFormatter, 
                                 epilog=detectNet.Usage() + videoSource.Usage() + videoOutput.Usage() + Log.Usage())

parser.add_argument("input", type=str, default="", nargs='?', help="URI of the input stream")
parser.add_argument("output", type=str, default="", nargs='?', help="URI of the output stream")
parser.add_argument("--network", type=str, default="ssd-mobilenet-v2", help="pre-trained model to load (see below for options)")
parser.add_argument("--overlay", type=str, default="box,labels,conf", help="detection overlay flags (e.g. --overlay=box,labels,conf)\nvalid combinations are:  'box', 'labels', 'conf', 'none'")
parser.add_argument("--threshold", type=float, default=0.5, help="minimum detection threshold to use") 

try:
	args = parser.parse_known_args()[0]
except:
	print("")
	parser.print_help()
	sys.exit(0)


# create video sources and outputs
input = videoSource(args.input, argv=sys.argv)
output = videoOutput(args.output, argv=sys.argv)
	
# load the object detection network
net = detectNet(args.network, sys.argv, args.threshold)

# process frames until End of system or the user exits
while True:
    # capture the next image
    img = input.Capture()

    if img is None: # timeout
        continue  
        
    # detect objects in the image (with overlay)
    detections = net.Detect(img, overlay=args.overlay)

    # print the detections
    print("hi detected {:d} objects in image".format(len(detections)))

    for detection in detections:
        print(detection)

    # render the image
    output.Render(img)

    # update the title bar
    output.SetStatus("{:s} | Network {:.0f} FPS".format(args.network, net.GetNetworkFPS()))

    # print out performance info
    net.PrintProfilerTimes()

    #print out information of first detection
    if len(detections) > 0:
        print(str(detections[0].ClassID))

    #save length of detections ot detLen
    detLen = len(detections)

    #print out detLen
    print("detLen: " + str(detLen))

    #if items are detected
    if detLen >= 1:
        print("DETECTIONS LIST: " + str(detections))

        #for every detected item, print out type and determine if it is a bird
        for i in detections:
            print("BD detects: " + net.GetClassDesc(i.ClassID))
            #class 16 is "bird"
            if i.ClassID == 16:
                birdCount+=1
                print("BIRD COUNT: " + str(birdCount))
        
        print("THE FINAL BIRD COUNT IS: " + str(birdCount))
        os.system('python3 HummingbirdDetection.py ' + args.input)
    else:
        print("Please insert an image with objects")

    # exit on input/output EOS
    if not input.IsStreaming() or not output.IsStreaming():
        break

