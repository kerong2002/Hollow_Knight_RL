from Tool.GetHP import Hp_getter
from get_hollow_screen import bring_window_to_front


def main():
    # 初始化 Hp_getter 實例
    hp_getter = Hp_getter()
    print("hp_getter：")
    print("Get_souls:", hp_getter.get_souls())
    print("Hero ho：", hp_getter.get_self_hp())
    print("Boss hp：", hp_getter.get_boss_hp())


# # 測試獲取靈魂值的方法是否正確
# souls = hp_getter.get_souls()
# print("Souls:", souls)
#
# # 測試獲取自身生命值的方法是否正確
# self_hp = hp_getter.get_self_hp()
# print("Self HP:", self_hp)
#
# # 測試獲取 Boss 生命值的方法是否正確
# boss_hp = hp_getter.get_boss_hp()
# print("Boss HP:", boss_hp)
#
# # 測試獲取玩家位置的方法是否正確
# play_location = hp_getter.get_play_location()
# print("Player Location:", play_location)
#
# # 測試獲取 Hornet 位置的方法是否正確
# hornet_location = hp_getter.get_hornet_location()
# print("Hornet Location:", hornet_location)


if __name__ == "__main__":
    bring_window_to_front()
    main()