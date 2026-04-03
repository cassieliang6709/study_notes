# Python OOP 入门前置知识清单（中文版）

> 目标：在学 OOP / OOD 之前，先补齐必须会的 Python 语法和基础知识  
> 适用：刚开始学 Python 面向对象、准备面试设计题、看 class 代码总是卡住的人

---

## 一、先说结论

如果你想学 Python 的 OOP，你**不需要先把 Python 全部学完**。

你只需要先掌握这几类东西：

1. 基础语法
2. 函数
3. 常用数据结构
4. 模块与导入
5. class 相关核心语法
6. 一点点 typing / dataclass / enum

可以理解成：

```text
// 学 OOP 之前，不需要会所有高级特性
// 但必须会“怎么定义数据、怎么写函数、怎么组织代码”
```

---

## 二、你在学 OOP 之前，必须会的 Python 知识

下面我按重要程度给你排顺序。

---

## 1. 变量、条件、循环

### 你至少要会

- 变量赋值
- `if / elif / else`
- `for`
- `while`
- `break / continue / return`

### 例子

```python
age = 20

if age >= 18:
    print("adult")
else:
    print("minor")

for i in range(3):
    print(i)
```

### 为什么 OOP 前必须会

因为类里面的方法，本质上还是这些逻辑。

```text
// class 不是魔法
// class 里的方法，本质上还是 if、for、变量、return
```

---

## 2. 函数

### 你至少要会

- `def`
- 参数
- 返回值
- 默认参数
- 位置参数和关键字参数

### 例子

```python
def add(a, b):
    return a + b


def greet(name, prefix="Hello"):
    return f"{prefix}, {name}"
```

### 为什么重要

因为类的方法就是“写在 class 里面的函数”。

如果你函数都不熟，看到 class 里的方法会更乱。

---

## 3. 常用数据结构

OOP 题里几乎一直在用这些：

- `list`
- `dict`
- `set`
- `tuple`

### 你至少要会

#### list

```python
nums = [1, 2, 3]
nums.append(4)
nums.pop()
```

#### dict

```python
user = {"id": 1, "name": "Alice"}
user["email"] = "a@test.com"
name = user.get("name")
```

#### set

```python
seen = set()
seen.add("x")
```

#### tuple

```python
point = (3, 4)
```

### 为什么重要

因为很多类内部都要维护状态：

```text
// 用 list 管理多个对象
// 用 dict 做 id -> object 的快速查找
// 用 set 记录唯一状态
```

例如：

```python
self.users = {}
self.orders = []
self.active_ids = set()
```

---

## 4. 字符串基础

### 你至少要会

- 字符串拼接
- `f-string`
- 常见方法：`split`, `strip`, `lower`

### 例子

```python
name = "Cassie"
message = f"Hello, {name}"
```

### 为什么重要

因为你会经常做：

- id / code 生成
- 展示信息
- 格式化输出

---

## 5. 模块和 import

### 你至少要会

- `import`
- `from ... import ...`
- 一个文件定义类，另一个文件使用

### 例子

```python
from dataclasses import dataclass
from enum import Enum
from typing import Optional
```

### 为什么重要

OOP 代码通常不会只写在一个文件里。

你必须知道：

```text
// 类可以从别的模块导入
// 标准库也可以直接拿来用
```

---

## 6. class 最基础语法

这部分是 OOP 的直接前置。

### 你必须会

- `class`
- `__init__`
- `self`
- 实例属性
- 实例方法

### 最小例子

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof"
```

使用：

```python
dog = Dog("Milo")
print(dog.name)
print(dog.bark())
```

### 这里你必须真正理解的点

#### `class`

```text
// 类 = 模板
// 对象 = 根据模板创建出来的实例
```

#### `__init__`

```text
// 初始化方法
// 创建对象时自动调用
```

#### `self`

```text
// self 表示“当前这个对象自己”
// self.name 表示这个对象自己的属性
```

这个概念很重要。

你可以这么理解：

```text
// dog1.name 和 dog2.name 可以不同
// 因为每个对象都有自己的 self
```

---

## 7. 对象和实例

你必须能分清：

```text
// 类 class：设计图
// 实例 object：真实创建出来的对象
```

例子：

```python
class Student:
    def __init__(self, name):
        self.name = name


s1 = Student("Alice")
s2 = Student("Bob")
```

这里：

- `Student` 是类
- `s1`, `s2` 是对象

每个对象都有自己的状态：

```python
print(s1.name)  # Alice
print(s2.name)  # Bob
```

---

## 8. 方法调用

### 你至少要会

```python
obj.method()
```

例子：

```python
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1


c = Counter()
c.increment()
```

### 为什么重要

OOP 的核心不是“类长什么样”，而是：

```text
// 对象有什么状态
// 对象能做什么动作
```

---

## 9. 返回对象、存对象

学 OOP 前你还要习惯：

```text
// list 里放对象
// dict 里放对象
// 函数返回对象
```

例子：

```python
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name


users = {}
users["u1"] = User("u1", "Alice")
```

这是 OOD 题里非常常见的写法。

---

## 10. `None`

### 你必须会

```python
result = None

if result is None:
    print("not found")
```

### 为什么重要

设计题里经常表示：

- 没找到
- 当前没有对象
- 可选返回值

比如：

```python
self.vehicle = None
```

表示当前车位没人占。

---

## 11. 布尔值和状态判断

### 你要会

```python
class Door:
    def __init__(self):
        self.is_open = False

    def open(self):
        self.is_open = True
```

### 为什么重要

很多 OOP 题本质上就是状态机：

- 门开 / 关
- 电梯上行 / 下行 / 空闲
- ATM 已认证 / 未认证

---

## 12. typing 基础

不是必须 100% 会，但建议会。

### 至少认识这些

```python
from typing import List, Dict, Optional
```

例子：

```python
from typing import Optional


def find_user(user_id: str) -> Optional[str]:
    return None
```

### 为什么重要

它能帮助你读懂和写清楚 OOP 代码结构。

比如：

```python
self.users: Dict[str, User] = {}
```

这行一看就知道：

```text
// key 是字符串
// value 是 User 对象
```

---

## 13. dataclass

建议学，但不是最早必须。

### 例子

```python
from dataclasses import dataclass


@dataclass
class Book:
    id: str
    title: str
```

### 为什么有用

如果一个类主要是存数据，用 `dataclass` 很省事。

适合：

- Ticket
- Request
- Package
- Account

---

## 14. Enum

建议学。

### 例子

```python
from enum import Enum


class Direction(Enum):
    UP = "up"
    DOWN = "down"
    IDLE = "idle"
```

### 为什么重要

很多设计题有固定状态：

- 电梯方向
- 订单状态
- 车位大小
- 用户角色

用 `Enum` 比直接写字符串更清晰。

---

## 15. 继承基础

如果你要继续学 OOP，这个也很重要。

### 你至少要会

- 子类继承父类
- `super()`

### 例子

```python
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
```

### 为什么重要

因为很多设计题有：

- `Vehicle -> Car / Truck`
- `User -> Admin / Customer`

---

## 16. 抽象类 ABC

这是 OOD 更进一步时才常用，但最好认识。

### 例子

```python
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def required_size(self):
        pass
```

### 作用

```text
// 规定子类必须实现统一接口
```

---

## 三、如果你不会这些，会在哪些地方卡住

### 1. 看不懂 `self`

你会不知道：

```text
// 为什么方法参数里第一个是 self
// 为什么属性都写成 self.xxx
```

### 2. 看不懂对象是怎么存进 dict 里的

比如：

```python
self.accounts[account_id] = account
```

### 3. 看不懂类之间的调用

比如：

```python
self.bank_service.withdraw(account_id, amount)
```

### 4. 看不懂 `Optional`、`Enum`、`dataclass`

这些在 OOD 代码里出现频率很高。

---

## 四、最小前置知识路线

如果你现在很乱，就按这个顺序补。

### 第 1 层：今天必须会

1. 变量、if、for、return
2. 函数
3. list / dict / set
4. class / `__init__` / `self`
5. 对象创建和方法调用

### 第 2 层：接下来补

6. `None`
7. 模块导入
8. typing: `List`, `Dict`, `Optional`
9. `dataclass`
10. `Enum`

### 第 3 层：再往后学

11. 继承
12. `super()`
13. ABC 抽象类

---

## 五、学 OOP 之前，你至少要能写出这 3 种代码

### 1. 会写一个简单类

```python
class Student:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        return f"Hi, I am {self.name}"
```

### 2. 会让一个类管理多个对象

```python
class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
```

### 3. 会用 dict 保存对象

```python
class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.user_id] = user
```

如果这 3 种你都会，已经可以开始 OOP。

---

## 六、一个最小 OOP 例子

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

这个例子里你要看懂：

```text
// Book 负责一本书自己的状态
// Library 负责管理很多 Book
// 这就是对象职责分离
```

---

## 七、学 OOP 时最容易误解的点

### 1. 以为 OOP 就是“会写 class”

不是。

真正重要的是：

```text
// 怎么拆对象
// 怎么分职责
// 怎么让代码易扩展
```

### 2. 以为必须先学很深的继承

不是。

初学时更重要的是：

```text
// 先会对象、状态、方法、组合
```

### 3. 以为 Python OOP 会很复杂

其实刚开始只需要：

```text
// class
// __init__
// self
// 对象
// 方法
```

---

## 八、建议学习顺序

如果你现在准备开始学 Python OOP，建议按这个顺序：

1. 变量、if、for、函数
2. list / dict / set
3. class / object / `__init__` / `self`
4. 方法和对象状态
5. 一个类管理多个对象
6. `None`、模块、import
7. typing / dataclass / Enum
8. 继承 / `super()`
9. ABC 抽象类
10. 再进入 OOD 题

---

## 九、你现在最应该优先掌握的内容

如果你只想最快开始 OOP，不要一次学太多。

你先抓住这 6 个：

1. `def`
2. `return`
3. `list / dict`
4. `class`
5. `__init__`
6. `self`

只要这几个会了，你已经能开始看很多 OOP 例子。

---

## 十、下一步最合理的动作

看完这份之后，最好的下一步不是直接去看复杂 OOD，而是先做这个顺序：

1. 写一个 `Student` 类
2. 写一个 `Course` 类，里面能保存多个学生
3. 写一个 `Library` + `Book` 小例子
4. 再去看 `Parking Lot` / `ATM` / `Elevator`

因为：

```text
// 先会小对象协作
// 再看大型设计题
// 不然容易一下被类太多吓住
```

---

## 十一、总结

学 Python OOP 之前，你不需要掌握整门语言。

你最需要的是：

- 基础语法
- 函数
- list / dict / set
- class / object / `__init__` / `self`
- 一点点 `None`、import、typing

剩下的像：

- `dataclass`
- `Enum`
- 继承
- ABC

是“让你写得更好”的工具，不是最早的门槛。

如果你愿意，我下一步可以继续直接给你生成两份之一：

1. `python_oop_30分钟入门.md`
2. `python_oop练习题_从简单到OOD.md`
