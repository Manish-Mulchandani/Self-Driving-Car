import cv2

# Our Image
#img_file = 'Car Image2.jpg'
#video = cv2.VideoCapture('Tesla DashCam.mp4')
video = cv2.VideoCapture('Duke Cam1.mp4')

#Our pre-trained car classifier and pedestrian classifier
car_tracker_file = 'car_detector.xml'
pedestrian_tracker_file = 'pedestrian_detector.xml'

#create car classifier and pedestrian classifier
car_tracker = cv2.CascadeClassifier(car_tracker_file)
pedestrian_tracker = cv2.CascadeClassifier(pedestrian_tracker_file)


# Run forever until the car stops
while True:

    # Read the current frame
    (read_successful, frame) = video.read()

    # Safe coding.
    if read_successful:
        # Must convert to grayscale
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    # detect Cars and pedestrians
    cars = car_tracker.detectMultiScale(grayscaled_frame)
    pedestrians = pedestrian_tracker.detectMultiScale(grayscaled_frame)

    # Draw rectangles around the Cars
    for (x,y,w,h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0,255), 2)
        cv2.rectangle(frame, (x+1, y+2), (x+w, y+h), (255,0,0), 2)
    # Draw rectangles around the Pedestrians
    for (x,y,w,h) in pedestrians:
       cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
    
    
    #Display the image with the faces spotted
    cv2.imshow('Self Driving Car', frame)

    # Dont autoclose (Wait here in the code and listen for a key press)
    key = cv2.waitKey(1)

    # Stop if 0 key is pressed
    if key==81 or key==113:
        break

# Release the VideoCapture object
video.release()



"""





# create opencv image
img = cv2.imread(img_file)

#convert to grayscale (needed for haar cascade)
black_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)






car1 = car[0]
[x,y,w,h] = car1
cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)


"""





print("Code Completed")