---
title: "Python OOP 概念讲解（中文版）"
---

# Python OOP 概念讲解（中文版）

> 目标：把 OOP 的核心概念讲清楚，帮助你从“会写 class”走到“理解为什么这样设计”  
> 适用：刚开始学面向对象、看 OOD / design 题容易乱的人

---

## 一、OOP 到底是什么

OOP = `Object-Oriented Programming`，面向对象编程。

你可以先不要把它想得太复杂。

它本质上是在说：

```text
// 把程序拆成很多对象
// 每个对象有自己的数据
// 每个对象也有自己能做的动作
// 对象之间通过清晰接口协作
```

所以 OOP 不是“写 class 的花哨方法”，而是一种组织代码的方法。

---

## 二、为什么会有 OOP

如果程序很小，直接写函数也能做。

但程序一变大，就容易出现这些问题：

- 所有逻辑堆在一起
- 数据到处传来传去
- 谁该负责什么越来越不清楚
- 改一个地方会影响很多地方

OOP 想解决的是：

```text
// 怎么把代码按“对象职责”组织起来
// 让每一部分更清晰、更可维护
```

---

## 三、最核心的理解：对象 = 状态 + 行为

这是你最应该记住的一句话。

```text
对象 = 状态 + 行为
```

比如一只狗：

- 状态：名字、年龄、颜色
- 行为：叫、跑、吃

在代码里：

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof"
```

这里：

- `name`, `age` 是状态
- `bark()` 是行为

---

## 四、OOP 里的 4 个最基础概念

---

## 1. Class：类

类可以理解成“设计图”或“模板”。

```python
class Dog:
    pass
```

这只是定义了一种东西的结构，还不是具体对象。

你可以理解成：

```text
// 类告诉你：这种对象应该有哪些属性和方法
```

---

## 2. Object / Instance：对象 / 实例

对象是根据类创建出来的具体东西。

```python
dog1 = Dog()
dog2 = Dog()
```

这里：

- `Dog` 是类
- `dog1`, `dog2` 是对象

对象是“活的、具体的”。

---

## 3. Attribute：属性

属性就是对象保存的数据。

```python
class Dog:
    def __init__(self, name):
        self.name = name
```

这里：

- `self.name` 是对象属性

属性表示：

```text
// 这个对象现在是什么状态
```

---

## 4. Method：方法

方法就是对象能执行的动作。

```python
class Dog:
    def bark(self):
        return "woof"
```

方法表示：

```text
// 这个对象能做什么
```

---

## 五、`self` 到底是什么

这是很多初学者最容易卡住的点。

### 先记一句话

```text
// self 表示“当前这个对象自己”
```

例子：

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof"
```

当你写：

```python
d1 = Dog("Milo")
d2 = Dog("Coco")
```

那么：

- `d1.name` 是 `"Milo"`
- `d2.name` 是 `"Coco"`

为什么不一样？

因为每个对象自己的 `self` 不同。

所以你可以把它理解成：

```text
// self.name = 当前对象自己的 name
```

---

## 六、`__init__` 是什么

`__init__` 是初始化方法。

创建对象时会自动执行。

```python
class Student:
    def __init__(self, name):
        self.name = name
```

当你写：

```python
s = Student("Alice")
```

其实就是：

```text
// 创建一个 Student 对象
// 并把 name 初始化成 Alice
```

所以：

```text
// __init__ 的作用就是给对象准备初始状态
```

---

## 七、为什么 OOP 不只是“把函数塞进 class”

很多人刚开始会误以为：

```text
// OOP = 本来写函数
// 现在只是外面套一个 class
```

这不够。

真正的 OOP 强调的是：

```text
// 数据和行为应该放在合适的对象里
```

比如图书馆：

### 不好的想法

```text
// 一个超级大函数处理所有书、所有借阅逻辑
```

### 更好的 OOP 想法

- `Book` 管一本书的状态
- `Library` 管很多书

这就叫“职责分离”。

---

## 八、OOP 的 4 大核心思想

很多教材会讲这四个：

1. 封装
2. 抽象
3. 继承
4. 多态

这四个你不需要一开始就背定义，但需要真正理解。

---

## 1. 封装 Encapsulation

### 一句话理解

```text
// 把数据和操作数据的方法放在一起
// 对外只暴露必要接口
```

例子：

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        return True
```

为什么这叫封装？

因为：

```text
// 账户余额和操作余额的逻辑被封装在 BankAccount 里
// 外部不应该到处乱改余额
```

封装的意义：

- 减少混乱
- 保护对象状态
- 让逻辑更集中

---

## 2. 抽象 Abstraction

### 一句话理解

```text
// 只暴露“做什么”
// 隐藏“内部怎么做”
```

比如：

```python
class CoffeeMachine:
    def make_coffee(self):
        # 内部有很多复杂步骤
        pass
```

外部调用者只需要知道：

```python
machine.make_coffee()
```

不需要知道内部加热、压粉、出水的细节。

这就是抽象。

抽象的好处：

- 使用更简单
- 实现可以以后再改
- 外部依赖更少

---

## 3. 继承 Inheritance

### 一句话理解

```text
// 子类复用父类的共同部分
```

例子：

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating"


class Dog(Animal):
    def bark(self):
        return "woof"
```

这里：

- `Dog` 继承 `Animal`
- 所以 `Dog` 自动拥有 `name` 和 `eat()`

这适用于：

```text
// Dog is an Animal
// Car is a Vehicle
// AdminUser is a User
```

### 继承的意义

- 复用代码
- 表达 is-a 关系
- 给不同子类提供统一接口

### 但要注意

继承不是越多越好。

如果关系不是很自然，优先考虑组合。

---

## 4. 多态 Polymorphism

### 一句话理解

```text
// 同一个接口
// 不同对象可以有不同实现
```

例子：

```python
class Animal:
    def speak(self):
        raise NotImplementedError


class Dog(Animal):
    def speak(self):
        return "woof"


class Cat(Animal):
    def speak(self):
        return "meow"
```

然后：

```python
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())
```

这里调用的都是 `speak()`，但不同对象行为不同。

这就是多态。

### 多态的意义

- 统一调用方式
- 减少大量 `if type == ...`
- 更容易扩展新类型

---

## 九、组合比继承更常用

这是很实用的一点。

### 组合是什么

```text
// 一个对象“拥有”另一个对象
// has-a 关系
```

例子：

```python
class Engine:
    pass


class Car:
    def __init__(self):
        self.engine = Engine()
```

这里：

- `Car has an Engine`

不是继承，而是组合。

### 为什么面试里常更推荐组合

因为组合更灵活。

比如：

- `ParkingLot` 有多个 `Level`
- `Level` 有多个 `ParkingSpot`
- `ATM` 有 `CashDispenser`

这类关系都是组合。

---

## 十、对象之间如何协作

OOP 不只是单个对象，还要看对象如何配合。

比如：

```text
// Library 管很多 Book
// User 借 Book
// BorrowService 负责借书流程
```

你在设计时要问自己：

```text
// 谁拥有数据？
// 谁负责校验？
// 谁对外暴露主流程？
```

这就是 OOD 的开端。

---

## 十一、OOP 和 OOD 的区别

这两个很容易混。

### OOP

```text
// 面向对象编程
// 更偏“怎么用类和对象写代码”
```

### OOD

```text
// 面向对象设计
// 更偏“怎么拆类、分职责、组织系统”
```

你可以这样理解：

```text
// OOP 是语言和写法层面
// OOD 是设计和架构层面
```

比如：

- 会写 `class User`，这是 OOP
- 知道系统该拆成 `User`, `Order`, `PaymentService`，这是 OOD

---

## 十二、一个最小 OOP 例子

### 例子：图书馆

```python
class Book:
    def __init__(self, title):
        self.title = title
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            return False
        self.is_borrowed = True
        return True

    def return_book(self):
        self.is_borrowed = False


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                return book.borrow()
        return False
```

这个例子里：

### `Book`

状态：

- `title`
- `is_borrowed`

行为：

- `borrow()`
- `return_book()`

### `Library`

状态：

- `books`

行为：

- `add_book()`
- `borrow_book()`

这就是典型的 OOP：

```text
// 每个对象负责自己那部分状态和行为
```

---

## 十三、初学 OOP 最常犯的错误

---

## 1. 只会写 class，不会分职责

问题不是：

```text
// 我会不会 class
```

而是：

```text
// 这个类该不该存在？
// 它该负责什么？
```

---

## 2. 一个类什么都做

这种叫 God object。

比如：

```text
// 一个类同时管用户、订单、支付、通知、库存
```

这很难维护。

---

## 3. 把所有属性都暴露出去乱改

会导致：

- 状态不一致
- 调试困难
- 逻辑散落 everywhere

---

## 4. 滥用继承

不是所有相似类都该继承。

如果只是“用到了”，通常是组合，不是继承。

---

## 5. 不知道对象之间怎么互动

只会定义一堆类，但类之间没有清晰关系。

---

## 十四、怎么判断一个设计是不是更像 OOP

问自己这些问题：

1. 这个类有没有明确职责？
2. 这个对象有没有自己的状态？
3. 这个方法是不是属于这个对象？
4. 数据和操作是否放在一起？
5. 对象之间关系是否清晰？

如果这些都比较清楚，说明你已经在用 OOP 思维。

---

## 十五、你现在最应该掌握的 OOP 认知

如果你是初学者，不要一开始就被各种术语压垮。

你先抓住这几句：

```text
// 类是模板，对象是实例
// 对象 = 状态 + 行为
// self 表示当前对象自己
// __init__ 负责初始化状态
// 封装是把数据和操作放在一起
// 继承表示 is-a
// 组合表示 has-a
// OOD 是在更高层面拆对象和职责
```

只要这几句你真的懂了，后面 OOD 就不会那么空。

---

## 十六、学习顺序建议

建议你按这个顺序学：

1. 先看 [python_oop_prerequisites_cn.md](./python_oop_prerequisites_cn.md)
2. 再看这份 OOP 概念文档
3. 自己手写 2 到 3 个简单类
4. 再去看停车场、ATM、电梯这类 OOD 题

为什么这样安排：

```text
// 先补语言前置
// 再理解概念
// 再做小练习
// 最后看复杂设计题
```

---

## 十七、下一步最合理的动作

如果你看完这份还想继续，最好的下一步是下面两个里选一个：

1. 写一个最小 OOP 练习集
   例如：`Student / Course / Library / Book`

2. 看一份“从 OOP 到 OOD”的桥接文档
   例如：怎么从简单类过渡到 Parking Lot / ATM / Elevator

如果你要，我下一步可以继续直接给你生成：

1. `python_oop_small_exercises_cn.md`
2. `from_oop_to_ood_cn.md`
