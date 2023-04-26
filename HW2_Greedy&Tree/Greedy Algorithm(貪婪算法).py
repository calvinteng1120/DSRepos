# -*- coding: utf-8 -*-
"""
貪婪演算法（英語：greedy algorithm），又稱貪心演算法，是一種在每一步選擇中都採取在當前狀態下最好或最佳（即最有利）的選擇，從而希望導致結果是最好或最佳的演算法
Greedy 通常用於找到當下局部最優解
不一定是全局最佳的解法
範例：換零錢、旅行推銷員問題
貪婪演算法在資料科學領域被廣泛應用，特別是金融工程

舉例：
工作時，可以用最短時間做最多的事。
出國旅行時，可以用最少的時間玩過最多的地方。
換零錢時，可以換到最少的硬幣。

"""

# 貪心演算法的應用－換零錢
def make_change(coins, amount):
    coins.sort(reverse=True)  # 將硬幣面值從大到小排序
    result = []  # 初始化結果列表！
    for coin in coins:  # 遍歷硬幣面值列表
        while amount >= coin :  # 待找金額 >= 硬幣面值
            result.append(coin)  # 把硬幣加入結果列表
            amount -= coin  # 從剩餘金額中減去硬幣面值
    return result  # 返回找零的結果列表

coins = [50, 10, 5, 1]  # 定義硬幣面值列表(不考慮硬幣數量)
amount = 63  # 定義需要找回的金額
#amount = 101  # 定義需要找回的金額
print(make_change(coins, amount))  # 輸出找零的結果
# Output: [50, 10, 1, 1, 1]
