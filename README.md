# Hummingbird Detector

 The Hummingbird Detector takes an image and determines how many birds are shown in the image, and if hummingbirds are present. It then prints the results.


![Flowchart](https://github.com/Jamie-Hsieh/HummingbirdDetector/assets/62030864/cc285d19-6771-49e4-8866-fdf57c793010)


## The Algorithm

The two models used in this project are DetectNet and ImageNet. This correlates with two files, BirdDetection and HummingbirdDetection. One command is executed by the user, which contains the desired input image. First, the image is passed to HummingbirdDetection which utilizes DetectNet to determine how many birds are in the image. The program then counts how many birds are present using ClassID. If any objects are found (by finding length of detection list), the input is automatically passed to HummingbirdDetection. If not, it asks for a different image.  The result of this process is printed. 
If BirdDetection passes on the input image, HummingbirdDetection finds if hummingbirds are present in the image, using class_idx from ImageNet. The result (True/False) is also printed.

## Running this project

1. Connect to Jetson Nano through PuTTY SSH [Use IP address found after connecting USB]. Port 22 on the Nano is available. Make sure your computer’s hotspot is on for the Nano to connect to.
2. Open Visual Studio Code and connect to the Nano through SSH
3. Within the directory of ~/jetson-inference/my_recognition (Or the same directory that BirdDetection and HummingbirdDetection), add photo that you want to process
4. In the terminal run:  python3 BirdDetection.py [Filename_of_Image] (ex. python3 BirdDetection.py hummingbirds.jpg)
5.  After DetectNet runs, it will output each individual item that it detects. After, your image will be processed by imageNet to determine whether there are hummingbirds within the image.

[View a video explanation here](video link)

