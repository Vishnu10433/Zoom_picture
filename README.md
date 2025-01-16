Hand Gesture Image Zoom
This application allows you to zoom and move an image using hand gestures captured through your webcam. It uses computer vision to track your hand movements and manipulate the image accordingly.
Features

Real-time hand gesture detection
Zoom in/out using pinch gestures with both hands
Move image by moving your hands
Smooth scaling and movement
Automatic boundary detection

Prerequisites

Python 3.8 or higher
Webcam
Image file to manipulate (default: "QR.jpg")

Installation

Create and activate a virtual environment (recommended):

bashCopy# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate

Install required packages:

bashCopypip install opencv-python cvzone numpy mediapipe
Usage

Place your image file (named "QR.jpg") in the same directory as the script

To use a different image, modify the image path in the code


Run the script:

bashCopypython hand_gesture_zoom.py

Control gestures:

Show both hands to the camera
Make pinching gestures with both hands (thumb and index finger)
Move hands apart to zoom in
Move hands together to zoom out
Move your hands to reposition the image
Press 'q' to quit the application



Troubleshooting

If the image doesn't load:

Check if the image file exists in the correct location
Verify file permissions
Try using the absolute path to the image


If hand detection isn't working:

Ensure there's good lighting
Keep your hands within the camera frame
Adjust the detectionCon parameter in the HandDetector initialization


Common errors and solutions:

"Failed to load image": Check image path and file existence
"Failed to capture frame": Check webcam connection
Dimension mismatch errors: The code includes error handling, but if persistent, try resizing your input image



System Requirements

Minimum 4GB RAM
Webcam with minimum 720p resolution
Processor: Intel i3/AMD equivalent or better
Well-lit environment for hand detection

Additional Notes

The application works best with a minimum distance of 50cm between your hands and the camera
Optimal performance is achieved with good lighting conditions
The zoom scale is limited to prevent excessive memory usage
Image quality is maintained through dynamic resolution adjustment

Contributing
Feel free to fork the repository and submit pull requests for:

Additional gesture controls
Performance improvements
Better error handling
UI enhancements

License
This project is licensed under the MIT License - see the LICENSE file for details
