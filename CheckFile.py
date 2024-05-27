import os

# 資料夾名稱
folder_move_memory = 'move_memory'
folder_act_memory = 'act_memory'

def Check_file_exist():
    # 檢查資料夾是否存在
    if not os.path.exists(folder_move_memory):
        # 如果資料夾不存在，則建立它
        os.makedirs(folder_move_memory)
    #     # print(f'資料夾 "{folder_name}" 已建立。')
    # else:
    #     # print(f'資料夾 "{folder_name}" 已存在。')

    if not os.path.exists(folder_act_memory):
        # 如果資料夾不存在，則建立它
        os.makedirs(folder_act_memory)

if __name__ == "__main__":
    Check_file_exist()