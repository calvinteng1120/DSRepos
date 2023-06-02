"""
374. Guess Number Higher or Lower
主題：Binary search
374. 猜數字的高低
我們正在玩猜謎遊戲。 遊戲如下：
我從 1 到 n 中選擇一個數字。 你得猜猜我選了哪個號碼。
每次你猜錯，我都會告訴你我選的數字是比你猜的高還是低。

-1：你猜的比我選的數字大（即 num > pick）。
1：你猜的比我選的數字小（即num < pick）。
0：你的猜測等於我選擇的數字（即 num == pick）。
返回我選擇的號碼。
"""

def guess(num: int) -> int:
    pick = 9 #目標數字
    if num > pick: #num=10,pick=9
        return -1
    elif num < pick: #num=6,pick=9
        return 1
    else:
        return 0 #num=9,pick=9

class Solution:
    def guessNumber(self, n: int) -> int:
        # 定義兩個變數表示搜索範圍的左邊和右邊
        left, right = 1, n
        
        # 初始化計數器
        guess_count = 0

        # 二分查找
        while left <= right:
            mid = left + (right - left) // 2
            guess_count += 1  # 增加計數器的值
            res = guess(mid)

            if res == 0:
                # 如果答案正確，則返回答案
                print(f'共猜了 {guess_count} 次.')
                return mid
            elif res == -1:
                # 如果答案太高，則搜索範圍縮小到左半部分
                right = mid - 1
            else:
                # 如果答案太低，則搜索範圍縮小到右半部分
                left = mid + 1


# 創建一個Solution物件
sol = Solution()

# 呼叫guessNumber方法
print(f"答案是{sol.guessNumber(10)}")
