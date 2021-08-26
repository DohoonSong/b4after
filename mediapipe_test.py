import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# For static images:
IMAGE_FILES = []
with mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=2,
    min_detection_confidence=0.5) as hands:
  for idx, file in enumerate(IMAGE_FILES):
    # Read an image, flip it around y-axis for correct handedness output (see
    # above).
    image = cv2.flip(cv2.imread(file), 1)
    # Convert the BGR image to RGB before processing.
    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Print handedness and draw hand landmarks on the image.
    print('Handedness:', results.multi_handedness)
    if not results.multi_hand_landmarks:
      continue
    image_height, image_width, _ = image.shape
    annotated_image = image.copy()
    for hand_landmarks in results.multi_hand_landmarks:
      print('hand_landmarks:', hand_landmarks)
      print(
          f'Index finger tip coordinates: (',
          f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width}, '
          f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height})'
      )

      mp_drawing.draw_landmarks(
          annotated_image,
          hand_landmarks,
          mp_hands.HAND_CONNECTIONS,
          mp_drawing_styles.get_default_hand_landmarks_style(),
          mp_drawing_styles.get_default_hand_connections_style())
    cv2.imwrite(
        '/tmp/annotated_image' + str(idx) + '.png', cv2.flip(annotated_image, 1))

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    image_height, image_width, _ = image.shape
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())

        wrist = np.array([hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x * image_width,
                          hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y * image_height])
        thumb = np.array([hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x * image_width,
                          hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * image_height])
        index = np.array([hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width,
                          hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height])
        middle = np.array([hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x * image_width,
                           hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * image_height])
        ring = np.array([hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x * image_width,
                         hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y * image_height])
        pinky = np.array([hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x * image_width,
                          hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y * image_height])

        cv2.putText(image,
                    "Thumb " + "{0:0.2f}".format(np.sqrt((thumb[0] - wrist[0]) ** 2 + (thumb[1] - wrist[1]) ** 2)),
                    (0, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(image,
                    " Index " + "{0:0.2f}".format(np.sqrt((index[0] - wrist[0]) ** 2 + (index[1] - wrist[1]) ** 2)),
                    (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(image,
                    "Middle " + "{0:0.2f}".format(np.sqrt((middle[0] - wrist[0]) ** 2 + (middle[1] - wrist[1]) ** 2)),
                    (0, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(image,
                    "  Ring " + "{0:0.2f}".format(np.sqrt((ring[0] - wrist[0]) ** 2 + (ring[1] - wrist[1]) ** 2)),
                    (0, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(image,
                    " Pinky " + "{0:0.2f}".format(np.sqrt((pinky[0] - wrist[0]) ** 2 + (pinky[1] - wrist[1]) ** 2)),
                    (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()