import face_recognition

# Load the jpg files into numpy arrays
pavan_image = face_recognition.load_image_file("pavan.jpeg")
ramcharan_image = face_recognition.load_image_file("ramcharan1.jpeg")
surya_image = face_recognition.load_image_file("surya.jpeg")
ntr_image = face_recognition.load_image_file("ntr.jpeg")
vijay_image = face_recognition.load_image_file("vijay.jpeg")
AA_image = face_recognition.load_image_file("AA.jpeg")
mahesh_image = face_recognition.load_image_file("mahesh1.jpeg")
nani_image = face_recognition.load_image_file("nani.jpeg")
ramp_image = face_recognition.load_image_file("ramp.jpeg")
unknown_face_encoding = face_recognition.load_image_file("kcr.jpeg")

# Get the face encodings for each face in each image file
# Since there could be more than one face in each image, it returns a list of encodings.
# But since I know each image only has one face, I only care about the first encoding in each image, so I grab index 0.
try:
    pavan_face_encoding = face_recognition.face_encodings(pavan_image)[0]
    ramcharan_face_encoding = face_recognition.face_encodings(ramcharan_image)[0]
    surya_face_encoding = face_recognition.face_encodings(surya_image)[0]
    ntr_face_encoding = face_recognition.face_encodings(ntr_image)[0]
    vijay_face_encoding = face_recognition.face_encodings(vijay_image)[0]
    AA_face_encoding = face_recognition.face_encodings(AA_image)[0]
    mahesh_face_encoding = face_recognition.face_encodings(mahesh_image)[0]
    nani_face_encoding = face_recognition.face_encodings(nani_image)[0]
    ram_face_encoding = face_recognition.face_encodings(ramp_image)[0]
    unknown_face_encoding = face_recognition.face_encodings(unknown_face_encoding)[0]
    
except IndexError:
    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
    quit()

known_faces = [
    pavan_face_encoding,
    ramcharan_face_encoding,
    surya_face_encoding,
    ntr_face_encoding,
    vijay_face_encoding,
    AA_face_encoding,
    mahesh_face_encoding,
    nani_face_encoding,
    ram_face_encoding,
    unknown_face_encoding,



]

# results is an array of True/False telling if the unknown face matched anyone in the known_faces array
results = face_recognition.compare_faces(known_faces, unknown_face_encoding)

print("Is the unknown face a picture of pavan? {}".format(results[0]))
print("Is the unknown face a picture of ramcharan? {}".format(results[1]))
print("Is the unknown face a picture of surya? {}".format(results[2]))
print("Is the unknown face a picture of ntr? {}".format(results[3]))
print("Is the unknown face a picture of vijay? {}".format(results[4]))
print("Is the unknown face a picture of AA? {}".format(results[5]))
print("Is the unknown face a picture of mahesh? {}".format(results[6]))
print("Is the unknown face a picture of nani? {}".format(results[7]))
print("Is the unknown face a picture of ram? {}".format(results[8]))

print("Is the unknown face a new person that we've never seen before? {}".format(not True in results))