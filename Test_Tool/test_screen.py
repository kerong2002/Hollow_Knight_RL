# 2024/05/22 kerong
from get_hollow_screen import bring_window_to_front
import cv2
from Tool.WindowsAPI import grab_screen
def main():
    # station_size = (230, 230, 1670, 930)
    # station = cv2.resize(cv2.cvtColor(grab_screen(station_size), cv2.COLOR_RGBA2RGB), (1000, 500))
    # station = cv2.resize(station, (1000, 500))
    # cv2.imshow('Game Screen', station)
    # 定義遊戲畫面的大小
    station_size = (230, 230, 1670, 930)

    # 獲取遊戲畫面
    station = grab_screen(station_size)

    # 轉換圖像格式並調整大小
    station = cv2.cvtColor(station, cv2.COLOR_RGBA2RGB)
    station = cv2.resize(station, (1000, 500))

    ## 顯示切割畫面
    cv2.imshow('Game Screen', station[187][300])
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    bring_window_to_front()
    main()
