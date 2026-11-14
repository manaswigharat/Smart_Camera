
import cv2
import numpy as np
import mediapipe as mp
import math

# ==========================================
# SMART CAMERA - 25 FILTERS
# ==========================================

camera = cv2.VideoCapture(0)

camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not camera.isOpened():
    print("ERROR: Camera not detected!")
    exit()

filters = [
    # Original 10 filters
    "Normal",
    "Grayscale",
    "Sepia",
    "Blur",
    "Black Mist",
    "Warm",
    "Cool",
    "Vintage",
    "Bright",
    "Cinematic",

    # Additional 15 filters
    "Pink Glow",
    "Peach",
    "Lavender",
    "Rose",
    "Dreamy",
    "Golden Hour",
    "Sunset",
    "Ocean",
    "Mint",
    "Film Fade",
    "Matte",
    "Noir",
    "Teal & Orange",
    "Soft Skin",
    "Neon Edge"
]

selected = 0
window_name = "SMART CAMERA - 25 FILTERS"


# ==========================================
# HELPER FUNCTIONS
# ==========================================

def tint(frame, color, strength=0.2):
    overlay = np.full_like(frame, color, dtype=np.uint8)

    return cv2.addWeighted(
        frame, 1 - strength,
        overlay, strength, 0
    )


def vignette(frame, strength=0.3):
    h, w = frame.shape[:2]

    x = cv2.getGaussianKernel(w, w / 2.2)
    y = cv2.getGaussianKernel(h, h / 2.2)

    mask = y @ x.T
    mask = mask / mask.max()
    mask = (1 - strength) + strength * mask

    result = frame.astype(np.float32)

    return np.clip(
        result * mask[:, :, None],
        0, 255
    ).astype(np.uint8)


# ==========================================
# FILTER PROCESSING
# ==========================================

def apply_filter(frame, name):

    # 1. NORMAL
    if name == "Normal":
        return frame

    # 2. GRAYSCALE
    elif name == "Grayscale":
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    # 3. SEPIA
    elif name == "Sepia":
        kernel = np.array([
            [0.272, 0.534, 0.131],
            [0.349, 0.686, 0.168],
            [0.393, 0.769, 0.189]
        ])

        return cv2.transform(
            frame, kernel
        ).clip(0, 255).astype(np.uint8)

    # 4. BLUR
    elif name == "Blur":
        return cv2.GaussianBlur(frame, (21, 21), 0)

    # 5. BLACK MIST
    elif name == "Black Mist":
        soft = cv2.GaussianBlur(frame, (0, 0), 12)

        result = cv2.addWeighted(
            frame, 0.65,
            soft, 0.35, 8
        )

        return cv2.convertScaleAbs(
            result, alpha=0.90, beta=8
        )

    # 6. WARM
    elif name == "Warm":
        result = frame.astype(np.float32)
        result[:, :, 2] *= 1.15
        result[:, :, 0] *= 0.85

        return np.clip(result, 0, 255).astype(np.uint8)

    # 7. COOL
    elif name == "Cool":
        result = frame.astype(np.float32)
        result[:, :, 0] *= 1.20
        result[:, :, 2] *= 0.90

        return np.clip(result, 0, 255).astype(np.uint8)

    # 8. VINTAGE
    elif name == "Vintage":
        result = cv2.convertScaleAbs(
            frame, alpha=0.85, beta=25
        )

        kernel = np.array([
            [0.272, 0.534, 0.131],
            [0.349, 0.686, 0.168],
            [0.393, 0.769, 0.189]
        ])

        return cv2.transform(
            result, kernel
        ).clip(0, 255).astype(np.uint8)

    # 9. BRIGHT
    elif name == "Bright":
        return cv2.convertScaleAbs(
            frame, alpha=1.25, beta=35
        )

    # 10. CINEMATIC
    elif name == "Cinematic":
        result = cv2.convertScaleAbs(
            frame, alpha=1.35, beta=-15
        )

        result = result.astype(np.float32)
        result[:, :, 0] *= 1.08

        return np.clip(result, 0, 255).astype(np.uint8)

    # 11. PINK GLOW
    elif name == "Pink Glow":
        result = tint(frame, (190, 135, 255), 0.22)
        glow = cv2.GaussianBlur(result, (0, 0), 8)

        return cv2.addWeighted(
            result, 0.85, glow, 0.15, 5
        )

    # 12. PEACH
    elif name == "Peach":
        result = tint(frame, (165, 205, 255), 0.25)

        return cv2.convertScaleAbs(
            result, alpha=1.08, beta=8
        )

    # 13. LAVENDER
    elif name == "Lavender":
        return tint(frame, (220, 185, 240), 0.28)

    # 14. ROSE
    elif name == "Rose":
        result = tint(frame, (145, 110, 220), 0.23)

        return cv2.convertScaleAbs(
            result, alpha=1.05, beta=5
        )

    # 15. DREAMY
    elif name == "Dreamy":
        soft = cv2.GaussianBlur(frame, (0, 0), 15)

        result = cv2.addWeighted(
            frame, 0.70, soft, 0.30, 12
        )

        return vignette(result, 0.15)

    # 16. GOLDEN HOUR
    elif name == "Golden Hour":
        result = tint(frame, (100, 170, 255), 0.30)

        result = cv2.convertScaleAbs(
            result, alpha=1.12, beta=12
        )

        return vignette(result, 0.20)

    # 17. SUNSET
    elif name == "Sunset":
        result = tint(frame, (100, 105, 255), 0.32)

        return cv2.convertScaleAbs(
            result, alpha=1.12, beta=8
        )

    # 18. OCEAN
    elif name == "Ocean":
        result = tint(frame, (190, 145, 70), 0.30)

        return cv2.convertScaleAbs(
            result, alpha=1.10, beta=5
        )

    # 19. MINT
    elif name == "Mint":
        result = tint(frame, (175, 220, 190), 0.28)

        return cv2.convertScaleAbs(
            result, alpha=1.08, beta=8
        )

    # 20. FILM FADE
    elif name == "Film Fade":
        result = frame.astype(np.float32)
        result = result * 0.82 + 35

        result = np.clip(
            result, 0, 255
        ).astype(np.uint8)

        return vignette(result, 0.25)

    # 21. MATTE
    elif name == "Matte":
        result = frame.astype(np.float32)
        result = result * 0.78 + 45

        return np.clip(
            result, 0, 255
        ).astype(np.uint8)

    # 22. NOIR
    elif name == "Noir":
        gray = cv2.cvtColor(
            frame, cv2.COLOR_BGR2GRAY
        )

        gray = cv2.convertScaleAbs(
            gray, alpha=1.8, beta=-35
        )

        result = cv2.cvtColor(
            gray, cv2.COLOR_GRAY2BGR
        )

        return vignette(result, 0.45)

    # 23. TEAL & ORANGE
    elif name == "Teal & Orange":
        result = frame.astype(np.float32)

        result[:, :, 0] *= 1.18
        result[:, :, 1] *= 1.05
        result[:, :, 2] *= 1.20

        return np.clip(
            result, 0, 255
        ).astype(np.uint8)

    # 24. SOFT SKIN
    elif name == "Soft Skin":
        smooth = cv2.bilateralFilter(
            frame, 9, 75, 75
        )

        return cv2.addWeighted(
            frame, 0.35,
            smooth, 0.65, 0
        )

    # 25. NEON EDGE
    elif name == "Neon Edge":
        gray = cv2.cvtColor(
            frame, cv2.COLOR_BGR2GRAY
        )

        edges = cv2.Canny(gray, 60, 150)

        neon = cv2.applyColorMap(
            edges, cv2.COLORMAP_HOT
        )

        glow = cv2.GaussianBlur(
            neon, (0, 0), 5
        )

        return cv2.addWeighted(
            frame, 0.65, glow, 0.85, 0
        )

    return frame


# ==========================================
# MOUSE CONTROLS
# ==========================================

def mouse_control(event, x, y, flags, param):
    global selected

    if event == cv2.EVENT_LBUTTONDOWN:
        h, w = param

        # Previous button
        if 15 <= x <= 155 and h - 60 <= y <= h - 10:
            selected = (selected - 1) % len(filters)
            print("Previous:", filters[selected])

        # Next button
        elif w - 155 <= x <= w - 15 and h - 60 <= y <= h - 10:
            selected = (selected + 1) % len(filters)
            print("Next:", filters[selected])


# ==========================================
# MEDIAPIPE HAND DETECTION
# ==========================================

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    model_complexity=1,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
)

show_landmarks = True


# ==========================================
# GESTURE CONTROL SETTINGS
# ==========================================

zoom_level = 1.0
MIN_ZOOM = 1.0
MAX_ZOOM = 3.0
ZOOM_STEP = 0.20

last_gesture = None
gesture_status = "Show your hand"


# ==========================================
# DIGITAL ZOOM FUNCTION
# ==========================================

def apply_zoom(frame, zoom):

    if zoom <= 1.0:
        return frame

    h, w = frame.shape[:2]

    new_w = int(w / zoom)
    new_h = int(h / zoom)

    x1 = (w - new_w) // 2
    y1 = (h - new_h) // 2

    cropped = frame[
        y1:y1 + new_h,
        x1:x1 + new_w
    ]

    return cv2.resize(cropped, (w, h))


# ==========================================
# GESTURE DETECTION FUNCTION
# ==========================================

def detect_gesture(hand_landmarks):

    lm = hand_landmarks.landmark

    # Thumb and index finger distance
    thumb = lm[4]
    index = lm[8]

    distance = math.sqrt(
        (thumb.x - index.x) ** 2 +
        (thumb.y - index.y) ** 2
    )

    # PINCH: Thumb and index finger touch
    if distance < 0.045:
        return "PINCH"

    # Check whether four fingers are folded
    fingers_folded = (
        lm[8].y > lm[6].y and
        lm[12].y > lm[10].y and
        lm[16].y > lm[14].y and
        lm[20].y > lm[18].y
    )

    # THUMBS UP / DOWN
    if fingers_folded:

        if lm[4].y < lm[3].y < lm[2].y:
            return "THUMBS UP"

        elif lm[4].y > lm[3].y > lm[2].y:
            return "THUMBS DOWN"

    # OPEN PALM: All four fingers extended
    fingers_open = (
        lm[8].y < lm[6].y and
        lm[12].y < lm[10].y and
        lm[16].y < lm[14].y and
        lm[20].y < lm[18].y
    )

    if fingers_open:
        return "OPEN PALM"

    return None


# ==========================================
# CAMERA WINDOW
# ==========================================

cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_name, 640, 480)

cv2.setMouseCallback(
    window_name,
    mouse_control,
    (480, 640)
)

print("Smart Camera started!")
print("PINCH = Next filter | THUMBS UP = Zoom in | THUMBS DOWN = Zoom out")
print("OPEN PALM = Reset zoom")
print("N/P or arrow keys = Change filter | +/- = Zoom | 0 = Reset zoom")
print("L = Toggle landmarks | Q or ESC = Exit")


# ==========================================
# MAIN CAMERA LOOP
# ==========================================

try:

    while True:

        success, frame = camera.read()

        if not success:
            print("Unable to read camera frame. Check the camera connection.")
            break

        # Mirror the camera image
        frame = cv2.flip(frame, 1)

        # Apply zoom before filtering and hand tracking
        zoomed_frame = apply_zoom(frame, zoom_level)

        # Apply the selected filter
        current_filter = filters[selected]

        output = apply_filter(
            zoomed_frame.copy(),
            current_filter
        )

        # ======================================
        # DETECT HANDS AND DRAW LANDMARKS
        # ======================================

        gesture = None

        if show_landmarks:

            rgb_frame = cv2.cvtColor(
                zoomed_frame,
                cv2.COLOR_BGR2RGB
            )

            rgb_frame.flags.writeable = False

            results = hands.process(rgb_frame)

            rgb_frame.flags.writeable = True

            if results.multi_hand_landmarks:

                for hand_landmarks in results.multi_hand_landmarks:

                    detected = detect_gesture(hand_landmarks)

                    if detected is not None and gesture is None:
                        gesture = detected

                    mp_draw.draw_landmarks(
                        output,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,

                        mp_draw.DrawingSpec(
                            color=(0, 255, 255),
                            thickness=2,
                            circle_radius=4
                        ),

                        mp_draw.DrawingSpec(
                            color=(255, 0, 255),
                            thickness=3
                        )
                    )

        # ======================================
        # EXECUTE EACH GESTURE ONCE UNTIL RELEASE
        # ======================================

        if gesture is None:

            last_gesture = None
            gesture_status = "Show your hand"

        elif gesture != last_gesture:

            if gesture == "PINCH":

                selected = (selected + 1) % len(filters)
                gesture_status = "Next Filter: " + filters[selected]

            elif gesture == "THUMBS UP":

                zoom_level = min(
                    MAX_ZOOM,
                    zoom_level + ZOOM_STEP
                )

                gesture_status = "Zoom In"

            elif gesture == "THUMBS DOWN":

                zoom_level = max(
                    MIN_ZOOM,
                    zoom_level - ZOOM_STEP
                )

                gesture_status = "Zoom Out"

            elif gesture == "OPEN PALM":

                zoom_level = 1.0
                gesture_status = "Zoom Reset"

            last_gesture = gesture

        # ======================================
        # CAMERA INTERFACE
        # ======================================

        h, w = output.shape[:2]

        cv2.putText(
            output,
            f"FILTER: {filters[selected]}",
            (20, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.75,
            (0, 255, 255),
            2
        )

        cv2.putText(
            output,
            f"ZOOM: {zoom_level:.1f}x",
            (20, 68),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.65,
            (0, 255, 0),
            2
        )

        cv2.putText(
            output,
            f"GESTURE: {gesture_status}",
            (20, 101),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            (255, 255, 255),
            2
        )

        # Previous and Next buttons
        button_y1 = h - 52
        button_y2 = h - 12

        cv2.rectangle(
            output,
            (15, button_y1),
            (155, button_y2),
            (70, 70, 70),
            -1
        )

        cv2.rectangle(
            output,
            (w - 155, button_y1),
            (w - 15, button_y2),
            (70, 70, 70),
            -1
        )

        cv2.putText(
            output,
            "PREVIOUS",
            (25, h - 25),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 255, 255),
            1
        )

        cv2.putText(
            output,
            "NEXT",
            (w - 105, h - 25),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 255, 255),
            1
        )

        cv2.putText(
            output,
            "PINCH: Filter | THUMBS: Zoom | OPEN PALM: Reset | Q: Exit",
            (15, h - 65),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.38,
            (255, 255, 255),
            1
        )

        cv2.imshow(window_name, output)

        # ======================================
        # KEYBOARD CONTROLS
        # ======================================

        key = cv2.waitKeyEx(1)
        letter = key & 0xFF

        # Exit
        if letter in (ord('q'), ord('Q')) or key == 27:
            break

        # Next filter
        elif letter in (ord('n'), ord('N')) or key in (2555904, 65363):
            selected = (selected + 1) % len(filters)
            print("Current filter:", filters[selected])

        # Previous filter
        elif letter in (ord('p'), ord('P')) or key in (2424832, 65361):
            selected = (selected - 1) % len(filters)
            print("Current filter:", filters[selected])

        # Zoom in
        elif letter in (ord('+'), ord('=')):
            zoom_level = min(
                MAX_ZOOM,
                zoom_level + ZOOM_STEP
            )

        # Zoom out
        elif letter in (ord('-'), ord('_')):
            zoom_level = max(
                MIN_ZOOM,
                zoom_level - ZOOM_STEP
            )

        # Reset zoom
        elif letter == ord('0'):
            zoom_level = 1.0
            gesture_status = "Zoom Reset"

        # Toggle landmarks
        elif letter in (ord('l'), ord('L')):
            show_landmarks = not show_landmarks
            last_gesture = None

            print(
                "Hand landmarks:",
                "ON" if show_landmarks else "OFF"
            )

finally:

    camera.release()
    hands.close()
    cv2.destroyAllWindows()

    print("Smart Camera Closed Successfully!")
