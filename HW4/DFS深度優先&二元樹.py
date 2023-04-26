# -*- coding: utf-8 -*-
"""
以下是一個使用Python實現DFS遍歷二叉樹的程式碼，
該程式碼將遍歷順序儲存在一個列表中

在上述程式碼中，我們首先定義了二叉樹節點的類別TreeNode，
包括節點的值val和左右子樹left、right。

然後，定義了一個深度優先遍歷函數dfs，該函數接受當前節點和結果列表res作為輸入。
遍歷過程中，如果當前節點為None，則直接返回；
否則，將當前節點的值加入結果列表，然後遞歸訪問左右子樹。
最後，在主程序中創建一個二叉樹，然後調用dfs函數進行遍歷，將遍歷結果輸出到控制台上。

"""

import matplotlib.pyplot as plt

# 定義二叉樹節點類別
class TreeNode:
    #定義了TreeNode類的初始化函數，用於設置節點的值、左子樹和右子樹
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # 設置節點的值，默認為0
        print(self.val)
        self.left = left  # 設置節點的左子樹，默認為None
        print(self.left )
        self.right = right  # 設置節點的右子樹，默認為None

# 定義繪製二叉樹的函數
def draw_tree(root, x, y, gap):
    if not root: #判斷是否為空
        return
    # 繪製左子樹
    draw_tree(root.left, x - gap, y - gap, gap / 2)
    # 繪製當前節點
    plt.text(x, y, str(root.val), fontsize=16, fontweight='bold', ha='center', va='center', color='white', bbox=dict(facecolor='blue', edgecolor='white', pad=6))
    # 繪製右子樹
    draw_tree(root.right, x + gap, y - gap, gap / 2)
    # 繪製節點之間的線段
    if root.left:
        plt.plot([x, x - gap], [y, y - gap], linewidth=2, color='gray')
    if root.right:
        plt.plot([x, x + gap], [y, y - gap], linewidth=2, color='gray')

# 定義深度優先遍歷函數
# 參數分別是二叉樹的根節點 root 和存儲遍歷結果的列表 res。
def dfs(root, res): #使用stack方式
    if not root: # 當前節點為空，需要返回
        return
    res.append(root.val)  # 將當前節點的值加入結果列表
    dfs(root.left, res)  # 遞歸訪問左子樹
    dfs(root.right, res)  # 遞歸訪問右子樹



# 創建一個二叉樹
"""
     1
   /   \
  2     3
 / \   / \
4   5 6   7
"""


#將root設置為一個新的TreeNode類別實例，其val為2，left和right保持預設值
root = TreeNode(1)  # 創建一個值為1的二叉樹節點

#將root的left屬性設置為另一個TreeNode類別實例，其val為2，left和right保持預設值
root.left = TreeNode(2)  # 設置左子樹為一個值為2的二叉樹節點
root.right = TreeNode(3)  # 設置右子樹為一個值為3的二叉樹節點

#將(root.left)的left屬性設置為另一個TreeNode類別實例，其val為3，left和right保持預設值
root.left.left = TreeNode(4)  # 設置左子樹的左子樹為一個值為4的二叉樹節點
root.left.right = TreeNode(5)  # 設置左子樹的右子樹為一個值為5的二叉樹節點
root.right.left = TreeNode(6)  # 設置右子樹的左子樹為一個值為6的二叉樹節點
root.right.right = TreeNode(7)  # 設置右子樹的右子樹為一個值為7的二叉樹節點


# 遍歷二叉樹
result = []
dfs(root, result)
print(result)  # 輸出遍歷結果 [1, 2, 4, 5, 3, 6, 7]

# 繪製二叉樹
plt.figure(figsize=(6, 6))
draw_tree(root, 0, 0, 1)
plt.axis('off')
plt.show()
