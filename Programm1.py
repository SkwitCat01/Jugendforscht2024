import cv2
import mediapipe as mp
from pynput.mouse import Button, Controller
import numpy as np
import time
import Video
import pyautogui
import vlc 



Video.startvideo()

print("Lade...")
print("Dies kann eine weile dauern...")

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands


cap = cv2.VideoCapture(0)
hands = mp_hands.Hands()


mouse = Controller()
screen_width, screen_height = 1920, 1080  # Passe dies an deine Bildschirmauflösung an

print("Zum verlassen Q drücken!")

# Funktion zur Glättung der Mausbewegungen (mit gleitenden Durchschnitt)


def calculate_hand_position(hand_landmarks):
    """Berechnet die Position des Indexfingers und des Daumens."""
    index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    return (int(index_finger_tip.x * screen_width), int(index_finger_tip.y * screen_height)), (int(thumb_tip.x * screen_width), int(thumb_tip.y * screen_height))


def handle_click(index_finger_pos, thumb_pos, middle_finger_pos):
    """Verarbeitet Klicks."""
    # Linksklick
    if abs(index_finger_pos[0] - thumb_pos[0]) < 40 and abs(index_finger_pos[1] - thumb_pos[1]) < 40:
        mouse.click(Button.left, 1)
        weiter = vlc.MediaPlayer('weiter.mp3')
        weiter.play()
       
        time.sleep(1)


try:
    while True:
        ret, image = cap.read()
        if not ret:
            break
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        results = hands.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
       
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2),
                    mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2)
                )
               
                index_finger_pos, thumb_pos = calculate_hand_position(hand_landmarks)
                middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
                middle_finger_pos = (int(middle_finger_tip.x * screen_width), int(middle_finger_tip.y * screen_height))
               
                handle_click(index_finger_pos, thumb_pos, middle_finger_pos)


                # Bewege den Cursor nur, wenn der Ring Finger den Daumen berührt
                ring_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
                little_x = int(ring_finger_tip.x * screen_width)
                little_y = int(ring_finger_tip.y * screen_height)


                if abs(little_x - thumb_pos[0]) < 40 and abs(little_y - thumb_pos[1]) < 40:
                    pyautogui.press("left")
                    zurück = vlc.MediaPlayer('zurück.mp3')
                    zurück.play()

                    time.sleep(1)


        cv2.imshow('Handtracker', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    cap.release()
    cv2.destroyAllWindows()
