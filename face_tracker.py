import cv2

cap = cv2.VideoCapture(0)
cascade_path = "cascades\haarcascade_frontalface_alt.xml"

# Check if camera opened successfully
if (cap.isOpened() == False): 
  print("Unable to read camera feed")
 
# Default resolutions of the frame are obtained.The default resolutions are system dependent.

# We convert the resolutions from float to integer.

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(5))

# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.

out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10,
                                                    (frame_width,frame_height))
faceCascade = cv2.CascadeClassifier(cascade_path)

while(True):
    ret, frame = cap.read()
    if ret == True: 
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
                                           gray,
                                           scaleFactor=1.1,
                                           minNeighbors=5,
                                           minSize=(30, 30),
                                           flags = cv2.CASCADE_SCALE_IMAGE #
                                           )
        #Coordinate of detected face
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        out.write(frame)
 
        # Display the resulting frame    
        cv2.imshow('frame',frame)
     
        # Press c on keyboard to Take Picture
        if cv2.waitKey(1) & 0xFF == ord('c'):
          frame = cap.retrieve(0)
          cv2.imwrite('my_pic.png', frame[1])

        #Press Q on keyboard to quite
        elif cv2.waitKey(1) & 0xFF == ord('q'):
            break
      # Break the loop
    else:
        break 
 
# When everything done, release the video capture and video write objects
cap.release()
out.release()
 
  

  
