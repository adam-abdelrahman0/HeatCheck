import cv2

# Read the image
image = cv2.imread('images/full_body_image.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours
for contour in contours:
    cv2.drawContours(image, [contour], 0, (0, 255, 0), 2)

cv2.imshow("Contours", gray)
cv2.waitKey(0)
