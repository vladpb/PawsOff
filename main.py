import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
import keyboard

video = cv2.VideoCapture(0)

# lista tastelor care trebuie blocate
keys_to_block = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

blocked_keys = set()  # tine minte tastele blocate

while True:
    ret, frame = video.read()
    bbox, label, conf = cv.detect_common_objects(frame)
    output_image = draw_bbox(frame, bbox, label, conf)

    if 'cat' in label:  # verifica daca exista o pisica in frame
        for key in keys_to_block:
            if key not in blocked_keys:
                keyboard.block_key(key)  # blocheaza tastele
                blocked_keys.add(key)
    elif 'person' in label:  # verifica daca exista un om in frame
        for key in keys_to_block:
            if key in blocked_keys:
                keyboard.unblock_key(key)  # deblocheaza tastele
                blocked_keys.remove(key)

    cv2.imshow("PawsOff", output_image)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
