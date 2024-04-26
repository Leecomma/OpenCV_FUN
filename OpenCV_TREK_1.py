import cv2

# check version
#print(cv2.__version__)

# Load image
image = cv2.imread('img.jpg')

# Set size image
new_size = (600, 400)
resized_image = cv2.resize(image, new_size)

# Specify path to haarcascade file
cascade_path = '__PATH__'
face_cascade = cv2.CascadeClassifier(cascade_path)

# Convert image
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# Detect face
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.5, minNeighbors=1)

# Drawing around face
for (x, y, w, h) in faces:
    cv2.rectangle(resized_image, (x, y), (x+w, y+h), (255, 0, 0), 2) #change to red + blue
    print(faces)

cv2.imshow('Detected Faces', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
