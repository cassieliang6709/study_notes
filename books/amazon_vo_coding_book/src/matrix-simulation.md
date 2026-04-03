# 7. 矩阵遍历模拟

## 面试题目怎么问

- 按螺旋顺序输出矩阵
- 逆时针打印矩阵
- 从外到内一层层遍历
- 按边界一圈圈收缩输出

## 识别信号

- 顺时针 / 逆时针
- 一圈一圈
- 边界不断缩小
- 强模拟

## Amazon 风格业务包装

- 按仓库清点顺序一圈圈扫描货架
- 机器人围绕区域边界做巡检
- dashboard 按某种顺时针顺序输出元素

## 标准代码模板

```python
def spiral_order(matrix):
    if not matrix or not matrix[0]:
        return []

    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    res = []

    while top <= bottom and left <= right:
        for j in range(left, right + 1):
            res.append(matrix[top][j])
        top += 1

        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            for j in range(right, left - 1, -1):
                res.append(matrix[bottom][j])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

    return res
```

## 面试时怎么讲

- 我会维护四个边界：`top`、`bottom`、`left`、`right`
- 每轮按四条边依次遍历
- 每走完一条边，就把对应边界向内收缩

## 常见 follow-up 和回答

**Q1：最容易错在哪里？**  
单行或单列时的重复遍历，所以后两段遍历前要判断边界是否有效。

**Q2：如果要求逆时针怎么办？**  
改遍历顺序即可。

**Q3：如果要求从内到外呢？**  
可以先按外到内收集每层，最后反转层顺序。

## Amazon 风格完整题面

> A warehouse scanner needs to inspect shelves layer by layer in clockwise order.  
> Return the inspection order of all shelf IDs in the matrix.

## 可直接背的口语回答稿

“这是一个纯模拟题。我会维护 `top`、`bottom`、`left`、`right` 四个边界，每轮依次走上边、右边、下边、左边，然后向内收缩。最关键的点是处理单行单列，避免重复遍历。”

## 推荐代表题

- Spiral Matrix
- Spiral Matrix II

