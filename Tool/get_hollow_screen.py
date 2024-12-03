# 2024/05/22 kerong
import pygetwindow as gw

def bring_window_to_front(window_title="Hollow Knight"):
    windows = gw.getWindowsWithTitle(window_title)
    if windows:
        window = windows[0]
        window.activate()
        window.maximize()
    else:
        print(f"未找到標題為 '{window_title}' 的窗口")

# bring_window_to_front()


# if __name__ == "__main__":
#     bring_window_to_front()
