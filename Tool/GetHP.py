import win32gui  # 導入用於操作 Windows GUI 的模組
import win32api  # 導入用於操作 Windows API 的模組
import win32process  # 導入用於操作 Windows 進程的模組
import ctypes  # 導入用於處理 C 函式庫的模組

Psapi = ctypes.WinDLL('Psapi.dll')  # 加載 Psapi.dll，用於操作進程模塊信息
Kernel32 = ctypes.WinDLL('kernel32.dll')  # 加載 kernel32.dll，用於操作系統核心模塊
PROCESS_QUERY_INFORMATION = 0x0400  # 用於打開進程，以獲取其相關信息的權限
PROCESS_VM_READ = 0x0010  # 用於打開進程，以讀取其虛擬記憶體的權限


x = 130
y = 50
step = 22
points = []
for i in range(9):
    points.append((x + i * step, y))

MAX_BOSS_HP = 900
hp_y = 401
def EnumProcessModulesEx(hProcess):
    buf_count = 256  # 定義緩衝區大小
    while True:
        LIST_MODULES_ALL = 0x03  # 枚舉所有模塊的標誌
        buf = (ctypes.wintypes.HMODULE * buf_count)()  # 定義存儲模塊句柄的緩衝區
        buf_size = ctypes.sizeof(buf)  # 獲取緩衝區的大小
        needed = ctypes.wintypes.DWORD()  # 用於存儲需要的緩衝區大小
        # 枚舉指定進程的模塊，並獲取模塊句柄
        if not Psapi.EnumProcessModulesEx(hProcess, ctypes.byref(buf), buf_size, ctypes.byref(needed),
                                          LIST_MODULES_ALL):
            raise OSError('EnumProcessModulesEx failed')  # 如果枚舉失敗，則拋出異常
        if buf_size < needed.value:
            buf_count = needed.value // (buf_size // buf_count)  # 調整緩衝區大小
            continue
        count = needed.value // (buf_size // buf_count)  # 獲取模塊數量
        return map(ctypes.wintypes.HMODULE, buf[:count])  # 返回模塊句柄的迭代器


class Hp_getter():
    def __init__(self):
        hd = win32gui.FindWindow(None, "Hollow Knight")  # 尋找遊戲窗口
        pid = win32process.GetWindowThreadProcessId(hd)[1]  # 獲取窗口所在的進程ID
        self.process_handle = win32api.OpenProcess(0x1F0FFF, False, pid)  # 打開遊戲進程的句柄
        self.kernal32 = ctypes.windll.LoadLibrary(r"C:\\Windows\\System32\\kernel32.dll")  # 加載 kernel32.dll

        self.hx = 0  # 初始化 x 軸座標

        # 獲取 UnityPlayer.dll 和 mono.dll 的模塊地址
        hProcess = Kernel32.OpenProcess(
            PROCESS_QUERY_INFORMATION | PROCESS_VM_READ,  # 權限
            False, pid)  # 打開遊戲進程的句柄
        hModule = EnumProcessModulesEx(hProcess)  # 枚舉模塊
        for i in hModule:
            temp = win32process.GetModuleFileNameEx(self.process_handle, i.value)  # 獲取模塊的文件路徑
            if temp[-15:] == "UnityPlayer.dll":  # 如果是 UnityPlayer.dll
                # print("UnityPlayer")
                self.UnityPlayer = i.value  # 設置 UnityPlayer 模塊地址
            if temp[-8:] == "mono.dll":  # 如果是 mono.dll
                # print("Mono")
                self.mono = i.value  # 設置 mono 模塊地址

    # 獲取靈魂值
    def get_souls(self):
        base_address = self.UnityPlayer + 0x00FA0998  # 靈魂值地址
        offset_address = ctypes.c_long()              # 偏移地址
        offset_list = [0x10, 0x64, 0x3C, 0xC, 0x60, 0x120]  # 偏移量列表
        self.kernal32.ReadProcessMemory(int(self.process_handle), base_address, ctypes.byref(offset_address), 4, None)
        for offset in offset_list:
            self.kernal32.ReadProcessMemory(int(self.process_handle), offset_address.value + offset,
                                            ctypes.byref(offset_address), 4, None)
        return offset_address.value

    # 獲取自身生命值
    def get_self_hp(self):
        base_address = self.mono + 0x1F50AC  # 自身生命值地址
        offset_address = ctypes.c_long()  # 偏移地址
        offset_list = [0x3B4, 0x24, 0x34, 0x48, 0x50, 0xE4]  # 偏移量列表
        self.kernal32.ReadProcessMemory(int(self.process_handle), base_address, ctypes.byref(offset_address), 4, None)
        for offset in offset_list:
            self.kernal32.ReadProcessMemory(int(self.process_handle), offset_address.value + offset,
                                            ctypes.byref(offset_address), 4, None)
        return offset_address.value

    # 獲取 Boss 生命值
    def get_boss_hp(self):
        base_address = self.UnityPlayer + 0x00FEF994
        offset_address = ctypes.c_long()
        offset_list = [0x54, 0x8, 0x1C, 0x1C, 0x7C, 0x18, 0xAC]
        self.kernal32.ReadProcessMemory(int(self.process_handle), base_address, ctypes.byref(offset_address), 4, None)
        for offset in offset_list:
          self.kernal32.ReadProcessMemory(int(self.process_handle), offset_address.value + offset, ctypes.byref(offset_address), 4, None)
        if offset_address.value > 900:
          return 901
        elif offset_address.value < 0:
          return -1
        return offset_address.value

    def get_play_location(self):
        x = ctypes.c_long()
        x.value += self.UnityPlayer + 0x00FEF994
        offset_list = [0x4C, 0x4, 0x4, 0x10, 0x0]
        self.kernal32.ReadProcessMemory(int(self.process_handle), x, ctypes.byref(x), 4, None)
        for offset in offset_list:
            self.kernal32.ReadProcessMemory(int(self.process_handle), x.value + offset, ctypes.byref(x), 4, None)
        xx = ctypes.c_float()
        self.kernal32.ReadProcessMemory(int(self.process_handle), x.value + 0x44, ctypes.byref(xx), 4, None)

        y = ctypes.c_long()
        y.value += self.UnityPlayer + 0x00FEF994
        offset_list = [0x24, 0x104, 0x6C, 0x10, 0xAC]
        self.kernal32.ReadProcessMemory(int(self.process_handle), y, ctypes.byref(y), 4, None)
        for offset in offset_list:
            self.kernal32.ReadProcessMemory(int(self.process_handle), y.value + offset, ctypes.byref(y), 4, None)

        yy = ctypes.c_float()
        self.kernal32.ReadProcessMemory(int(self.process_handle), y.value + 0xC, ctypes.byref(yy), 4, None)

        return xx.value, yy.value

    def get_hornet_location(self):
        base_address = self.UnityPlayer + 0x00FEF994
        x = ctypes.c_long()
        offset_list = [0x20, 0x54, 0x24, 0x20, 0x5C]
        self.kernal32.ReadProcessMemory(int(self.process_handle), base_address, ctypes.byref(x), 4, None)
        for offset in offset_list:
            self.kernal32.ReadProcessMemory(int(self.process_handle), x.value + offset, ctypes.byref(x), 4, None)

        xx = ctypes.c_float()
        self.kernal32.ReadProcessMemory(int(self.process_handle), x.value + 0xC, ctypes.byref(xx), 4, None)

        base_address = self.UnityPlayer + 0x00FEF994
        y = ctypes.c_long()
        offset_list = [0x54, 0x8, 0x1C, 0x1C, 0x14]
        self.kernal32.ReadProcessMemory(int(self.process_handle), base_address, ctypes.byref(y), 4, None)
        for offset in offset_list:
            self.kernal32.ReadProcessMemory(int(self.process_handle), y.value + offset, ctypes.byref(y), 4, None)

        yy = ctypes.c_float()
        self.kernal32.ReadProcessMemory(int(self.process_handle), y.value + 0xAC, ctypes.byref(yy), 4, None)

        if xx.value > 14 and xx.value < 40:
            self.hx = xx.value
        return self.hx, yy.value
