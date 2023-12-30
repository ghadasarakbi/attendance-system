import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': ""
})

# Function to upload an image to Firebase Storage
def upload_image_to_storage(image_path, destination_path):
    bucket = storage.bucket()
    blob = bucket.blob(destination_path)
    blob.upload_from_filename(image_path)

# Importing student images
folderPath = 'Images'
pathList = os.listdir(folderPath)
print(pathList)

encodeListKnown = []  # List to store face encodings
studentIds = []       # List to store student IDs

for path in pathList:
    img_path = os.path.join(folderPath, path)
    student_id = os.path.splitext(path)[0]
    
    # Load the image using OpenCV
    img = cv2.imread(img_path)
    
    if img is not None:
        # Convert image to RGB format for face_recognition
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Encode the face
        encode = face_recognition.face_encodings(img)[0]
        
        # Append the encoding and student ID to lists
        encodeListKnown.append(encode)
        studentIds.append(student_id)
        
        # Upload the image to Firebase Storage
        destination_path = f'images/{student_id}.jpg'
        upload_image_to_storage(img_path, destination_path)
        
        print(f"Uploaded {img_path} to Firebase Storage as {destination_path}")
    else:
        print(f"Error: Unable to load image {img_path}")

# Combine encodings and student IDs
encodeListKnownWithIds = [encodeListKnown, studentIds]

# Save the encoding data to a pickle file
with open("EncodeFile.p", 'wb') as file:
    pickle.dump(encodeListKnownWithIds, file)

print("Encoding Complete")
print("File Saved")
