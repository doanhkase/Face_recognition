import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier(r'python2\haarcascade_frontalface_default.xml')
# Read the input image
img = cv2.imread(r'python2\doanh.jpg')
# import ipdb; ipdb.set_trace()
# Convert into grayscale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY ) 
# Detect faces

faces = face_cascade.detectMultiScale(gray, 1.1, 10)

"""
# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)
"""
# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Display the output
cv2.imshow('img', img)
cv2.waitKey()