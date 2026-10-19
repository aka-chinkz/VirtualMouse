import cv2
import mediapipe as mp
import pyautogui
import time

smoothing = 4
prev_x = 0
prev_y = 0

Wcam, Hcam = 640, 480
frameR = 100
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_height, screen_width = pyautogui.size()
pTime = 0

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            cv2.rectangle(
                frame,
                (frameR, frameR),
                (Wcam - frameR, Hcam - frameR),
                (255, 0, 255),
                2,
            )
            drawing_utils.draw_landmarks(
                frame,
                hand,
                mp.solutions.hands.HAND_CONNECTIONS,
                drawing_utils.DrawingSpec(color=(0, 0, 255), thickness=5),
                drawing_utils.DrawingSpec(color=(0, 255, 0), thickness=4),
            )
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                print(x, y)
                if id == 8:
                    cv2.circle(
                        img=frame,
                        center=(x, y),
                        radius=20,
                        color=(255, 0, 255),
                        thickness=4,
                    )
                    index_x = screen_width / frame_width * x
                    index_y = screen_height / frame_height * y

                    # Smooth the cursor position
                    smoothed_x = prev_x + (index_x - prev_x) / smoothing
                    smoothed_y = prev_y + (index_y - prev_y) / smoothing

                    # Move the cursor to the smoothed position
                    pyautogui.moveTo(smoothed_x, smoothed_y)

                    # Update previous positions
                    prev_x, prev_y = smoothed_x, smoothed_y

                if id == 12:
                    cv2.circle(
                        img=frame,
                        center=(x, y),
                        radius=20,
                        color=(245, 212, 66),
                        thickness=4,
                    )

                    middle_x = screen_width / frame_width * x
                    middle_y = screen_height / frame_height * y
                    print(abs(index_y - middle_y))
                    if abs(index_y - middle_y) < 40:
                        pyautogui.click()
                        pyautogui.sleep(1)

    cv2.imshow("Virtual Mouse", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
