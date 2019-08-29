import cv2

capture = cv2.VideoCapture('video.mp4')

while True:
	ret, frame = capture.read()
	cv2.imshow('window', frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
capture.release()
cv2.destroyAllWindows()