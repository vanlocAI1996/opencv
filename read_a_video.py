import cv2

capture = cv2.VideoCapture(0)

while True:
	ret, frame = capture.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cv2.imshow('window', gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
capture.release()
cv2.destroyAllWindows()