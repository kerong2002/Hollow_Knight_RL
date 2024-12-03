import cv2
from Tool.WindowsAPI import grab_screen
station_size = (230, 230, 1670, 930)
station = cv2.resize(cv2.cvtColor(grab_screen(station_size), cv2.COLOR_RGBA2RGB), (1000, 500))
print(cv2)