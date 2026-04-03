---
title: "OOD Study Notes"
---

# OOD Study Notes

## 这个设计方向的总结

OOD 学习的核心不是记类图，而是训练三件事：

- 抽核心对象
- 拆职责边界
- 让对象通过清晰接口协作

## 这篇文档的题目含义

这页是 OOD 学习的简短复盘页，适合在进入具体案例前，先把“我做设计题时脑子里应该按什么顺序想”重新过一遍。

## Python 代码

```python
class ShoppingCart:
    def __init__(self) -> None:
        self.items: list[str] = []

    def add_item(self, item: str) -> None:
        self.items.append(item)

    def item_count(self) -> int:
        return len(self.items)


def main() -> None:
    cart = ShoppingCart()
    cart.add_item("book")
    cart.add_item("pen")
    print(cart.item_count())


if __name__ == "__main__":
    main()
```

## 时间复杂度

本页主要讲设计思路，不以复杂度为重点。

## 空间复杂度

本页主要讲设计思路，不以复杂度为重点。

## 怎么想到

做设计题时，最稳的顺序是：

1. 先定范围
2. 再抽名词
3. 再决定哪些名词该变成类
4. 再拆职责
5. 最后再落 Python 代码

## 示例 case

- 场景：设计购物车时，不要一上来把订单、库存、支付全部塞进一个类
- 拆法：先从最小的 `ShoppingCart` 开始，只负责购物车内部状态和操作
- 为什么：OOD 先求职责清晰，再求系统扩展

## 常见 follow-up

- 什么时候应该继续拆 service？
- 什么时候该引入抽象类或接口？
- 面试里 scope 该收多小才合适？
