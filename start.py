import PIL.ImageGrab
import pytesseract
import ctypes
from time import sleep

while 1:
    im = PIL.ImageGrab.grab([250, 930, 520, 1020]) # screenshot 'play/update' button
    im.save('test.jpg') # save screeshot as .jpg

    text_to_find = pytesseract.image_to_string('test.jpg', lang='fra') # ocr screenshot

    # if update failed, click on popup then re launch update
    if text_to_find == 'Mise à jour':
        ctypes.windll.user32.SetCursorPos(800, 400) 
        ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
        ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up

        sleep(2)

        ctypes.windll.user32.SetCursorPos(400, 970)
        ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
        ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up

    sleep(30) # wait 30s between every screenshot