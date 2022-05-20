import cv2
import mediapipe as mp
import time
import pyautogui

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
pTime = 0
cTime = 0
cx = 0
cy = 0
py = 250

while(True):
	
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

                if id == 8 or id == 12:
                    cv2.circle(img, (cx,cy), 10, (255, 0, 255), cv2.FILLED)

                    if cx in range(100,150) and cy in range(178,220):
                        pyautogui.keyDown('up')
                        pyautogui.keyUp('up')

                    elif cx in range(100,150) and cy in range(280,323):
                        pyautogui.keyDown('down')
                        pyautogui.keyUp('down')

                    elif cx in range(52,95) and cy in range(225,275):
                        pyautogui.keyDown('left')
                        pyautogui.keyUp('left')

                    elif cx in range(155,198) and cy in range(225,275):
                        pyautogui.keyDown('right')
                        pyautogui.keyUp('right')
                                      
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, "FPS: "+str(int(fps)), (18, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    l1_start_point = (100, 220)
    l1_end_point = (150,220)
    l2_start_point = (100,280)
    l2_end_point = (150,280)
    l3_start_point = (95,225)
    l3_end_point = (95,275)
    l4_start_point = (155,225)
    l4_end_point = (155,275)

    ta1_start_point = (100, 220)
    ta1_end_point = (125,178)
    tb1_start_point = (150,220)
    tb1_end_point = (125,178)
    
    ta2_start_point = (100,280)
    ta2_end_point = (125,323)
    tb2_start_point = (150,280)
    tb2_end_point = (125,323)

    ta3_start_point = (95,225)
    ta3_end_point = (52,250)
    tb3_start_point = (95,275)
    tb3_end_point = (52,250)

    ta4_start_point = (155,225)
    ta4_end_point = (198,250)
    tb4_start_point = (155,275)
    tb4_end_point = (198,250)

    cv2.line(img, l1_start_point, l1_end_point, (0,255,255), 2)
    cv2.line(img, l2_start_point, l2_end_point, (0,255,255), 2)
    cv2.line(img, l3_start_point, l3_end_point, (0,255,255), 2)
    cv2.line(img, l4_start_point, l4_end_point, (0,255,255), 2)

    cv2.line(img, ta1_start_point, ta1_end_point, (0,255,255), 2)
    cv2.line(img, ta2_start_point, ta2_end_point, (0,255,255), 2)

    cv2.line(img, ta3_start_point, ta3_end_point, (0,255,255), 2)
    cv2.line(img, ta4_start_point, ta4_end_point, (0,255,255), 2)

    cv2.line(img, tb1_start_point, tb1_end_point, (0,255,255), 2)
    cv2.line(img, tb2_start_point, tb2_end_point, (0,255,255), 2)

    cv2.line(img, tb3_start_point, tb3_end_point, (0,255,255), 2)
    cv2.line(img, tb4_start_point, tb4_end_point, (0,255,255), 2)

    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
	    break


cap.release()

cv2.destroyAllWindows()