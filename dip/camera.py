import cv2 as cv

cam = cv.VideoCapture(0)

if not cam.isOpened():
    print("Error to Open Camera")
    exit()

print("Cam is Open")


fourcc = cv.VideoWriter_fourcc(*'XVID')  # Codec
out = cv.VideoWriter('./CamVideo/output.avi', fourcc, 20.0, (640, 480))


print("Recording started. Press 'q' to stop...")

while True:
    # Capture frame-by-frame
    ret, frame = cam.read()
    
    if not ret:
        print("Error: Can't receive frame. Exiting...")
        break
    
    # Write the frame to file
    out.write(frame)
    
    # Display the frame (optional)
    cv.imshow('Webcam Feed', frame)
    
    # Exit on 'q' key press
    if cv.waitKey(1) == ord('q'):
        break

# Release everything when done
cam.release()
out.release()
cv.destroyAllWindows()
print("Recording saved as 'output.avi'")
