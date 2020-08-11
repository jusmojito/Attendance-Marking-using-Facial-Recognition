import urllib.request
import cv2
import numpy as np
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://192.168.0.100:8080'

while True:
    imgResp = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
    img = cv2.imdecode(imgNp, -1)
    cv2.imshow('tem',cv2.resize(img,(600,400)))
    q = cv2.waitKey(1)
    if q == ord("q"):
        break;

cv2.destroyAllWindows()
