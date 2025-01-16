import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np

# Initialize camera
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Initialize hand detector
detector = HandDetector(detectionCon=0.8, maxHands=2)

# Initial parameters
scale = 0.5
cx, cy = 640, 360

# Load image
img1 = cv2.imread("QR.jpg")
if img1 is None:
    print("Failed to load image. Check file path and permissions.")
    exit()

# Get original dimensions
original_h, original_w = img1.shape[:2]

# Calculate maximum allowed dimensions
max_w = int(cap.get(3) * 0.8)
max_h = int(cap.get(4) * 0.8)

while True:
    # Read camera frame
    success, img = cap.read()
    if not success:
        print("Failed to capture frame")
        break

    # Detect hands
    hands, img = detector.findHands(img, draw=False)

    if len(hands) == 2:
        # Get hand landmarks
        hand1, hand2 = hands[0], hands[1]
        thumb1, index1 = hand1["lmList"][4], hand1["lmList"][8]
        thumb2, index2 = hand2["lmList"][4], hand2["lmList"][8]

        # Calculate distances
        dist1 = np.linalg.norm(np.array(thumb1) - np.array(index1))
        dist2 = np.linalg.norm(np.array(thumb2) - np.array(index2))
        avg_dist = (dist1 + dist2) / 2

        # Update scale based on hand gesture
        scale = np.clip(np.interp(avg_dist, [50, 250], [0.3, 1.5]), 0.3, 1.5)

        # Calculate center position
        cx = int((thumb1[0] + index1[0] + thumb2[0] + index2[0]) / 4)
        cy = int((thumb1[1] + index1[1] + thumb2[1] + index2[1]) / 4)

        # Calculate new dimensions
        newH, newW = int(original_h * scale), int(original_w * scale)
        newH, newW = min(newH, max_h), min(newW, max_w)

        # Resize image
        resized_img = cv2.resize(img1, (newW, newH))

        # Calculate ROI coordinates
        top_left_y = max(0, cy - newH // 2)
        top_left_x = max(0, cx - newW // 2)
        bottom_right_y = min(img.shape[0], top_left_y + newH)
        bottom_right_x = min(img.shape[1], top_left_x + newW)

        # Get ROI from the frame
        roi = img[top_left_y:bottom_right_y, top_left_x:bottom_right_x]

        try:
            # Create mask
            img2gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
            mask_inv = cv2.bitwise_not(mask)

            # Ensure ROI and resized image have same dimensions
            if roi.shape[:2] == resized_img.shape[:2]:
                # Apply mask
                img_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
                img_fg = cv2.bitwise_and(resized_img, resized_img, mask=mask)

                # Combine background and foreground
                dst = cv2.add(img_bg, img_fg)
                img[top_left_y:bottom_right_y, top_left_x:bottom_right_x] = dst
        except Exception as e:
            print(f"Error during image processing: {e}")
            continue

    # Display result
    cv2.imshow("Zoom Gesture Implementation", img)

    # Exit on 'q' press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()