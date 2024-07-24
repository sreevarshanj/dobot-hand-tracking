import cv2
import numpy as np

# Function to detect shape
def detect_shape(c):
    shape = "unidentified"
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.04 * peri, True)

    if len(approx) == 3:
        shape = "triangle"
    elif len(approx) == 4:
        (x, y, w, h) = cv2.boundingRect(approx)
        ar = w / float(h)
        shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
    elif len(approx) > 4:
        shape = "circle"

    return shape

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
while True:
    _, image = cap.read()
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_color = np.array([0, 0, 0])
    upper_color = np.array([255, 255, 255])
    mask = cv2.inRange(hsv, lower_color, upper_color)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        else:
            cX, cY = 0, 0
        
        shape = detect_shape(contour)
        cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
        cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        cv2.circle(image, (cX, cY), 5, (0, 0, 255), -1)

    cv2.imshow("Contours", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
