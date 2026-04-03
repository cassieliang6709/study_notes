---
title: "OOD Python 学习指南（中文版）"
---

# OOD Python 学习指南（中文版）

> 目标：用 Python 学会面试常见 OOD / 面向对象设计题  
> 适用：LeetCode Design、面试 OOD、系统建模、代码结构设计

---

## 一、先搞清楚什么是 OOD

OOD = `Object-Oriented Design`，面向对象设计。

面试里它通常不是考你会不会背概念，而是看你能不能：

1. 把一个现实问题拆成对象
2. 定义对象之间的职责边界
3. 设计清晰的类和方法
4. 让代码容易扩展、容易维护

你可以把 OOD 理解成：

```text
// 不是“怎么把题做出来”
// 而是“怎么把题设计得像工程代码”
```

---

## 二、OOD 面试到底在考什么

通常考 5 件事：

1. `抽象能力`
   能不能识别核心实体

2. `职责划分`
   每个类该做什么，不该做什么

3. `关系设计`
   对象之间是组合、继承、依赖，还是关联

4. `可扩展性`
   后续加功能时会不会改一大片

5. `代码表达`
   命名、接口、数据结构选择是否清晰

---

## 三、OOD 题的标准解题流程

以后你做任何 OOD 题，都按这个顺序来。

### 第 1 步：澄清需求

先问：

```text
// 系统支持哪些核心操作？
// 是否需要删除 / 更新 / 查询？
// 数据量大不大？
// 是否要线程安全？
// 是否只做内存版，不考虑数据库？
```

面试里最忌讳的一件事：

```text
// 需求没问清就直接开写类
```

---

### 第 2 步：找核心对象

比如设计停车场，你会想到：

- `Vehicle`
- `Car`
- `Truck`
- `ParkingSpot`
- `Level`
- `ParkingLot`
- `Ticket`

问自己：

```text
// 这个系统里最重要的“名词”是什么？
// 哪些名词应该变成类？
```

---

### 第 3 步：定义每个类的职责

例子：

```text
// ParkingSpot 负责：
// - 判断能不能停某种车
// - 占用 / 释放车位

// Level 负责：
// - 管理这一层所有车位
// - 查找可用车位

// ParkingLot 负责：
// - 管理所有楼层
// - 对外暴露 park / leave 等主操作
```

核心原则：

```text
// 一个类只负责一类事
// 不要什么都塞进一个 God object
```

---

### 第 4 步：定义关系

常见关系有：

1. `继承`
   `Car` 继承 `Vehicle`

2. `组合`
   `ParkingLot` 里有多个 `Level`

3. `依赖`
   `ParkingLot` 调用 `Ticket` 的逻辑

简单理解：

```text
// is-a => 继承
// has-a => 组合
```

---

### 第 5 步：再想接口

类出来之后，再定义方法。

比如：

```python
class ParkingLot:
    def park_vehicle(self, vehicle: Vehicle) -> Ticket:
        pass

    def leave_vehicle(self, ticket_id: str) -> int:
        pass
```

方法设计原则：

```text
// 方法名要表达业务动作
// 参数只传必要信息
// 返回值尽量清晰
```

---

## 四、Python 做 OOD 的优势

Python 很适合 OOD 面试，因为：

1. 写法短
2. 类定义清楚
3. 容易表达组合和抽象
4. `dataclass` 很适合建模
5. `ABC` 很适合做抽象类

---

## 五、Python OOD 最常用语法

### 1. 普通类

```python
class User:
    def __init__(self, user_id: str, name: str) -> None:
        self.user_id = user_id
        self.name = name
```

---

### 2. dataclass

适合“主要用来存数据”的对象。

```python
from dataclasses import dataclass

@dataclass
class Book:
    id: str
    title: str
    author: str
```

什么时候用：

```text
// 数据对象、值对象、配置对象
```

---

### 3. 抽象基类 ABC

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def size(self) -> str:
        pass
```

什么时候用：

```text
// 需要统一接口
// 子类必须实现某些方法
```

---

### 4. Enum

```python
from enum import Enum

class SpotSize(Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
```

什么时候用：

```text
// 枚举状态、类型、等级
```

---

### 5. typing

```python
from typing import Optional, List, Dict
```

建议：

```text
// OOD 面试里尽量加 type hints
// 会让结构更清楚
```

---

## 六、OOD 里最重要的 7 个设计原则

### 1. 封装 Encapsulation

```text
// 对象自己管理自己的状态
// 外部不要乱改内部细节
```

坏例子：

```text
// 外部直接操作一堆对象属性
```

好例子：

```text
// 通过方法暴露操作
// 比如 reserve(), release(), add_item()
```

---

### 2. 抽象 Abstraction

```text
// 只暴露“做什么”
// 不暴露“内部怎么做”
```

---

### 3. 单一职责 SRP

```text
// 一个类只负责一类变化原因
```

例子：

```text
// Order 负责订单本身
// PaymentProcessor 负责支付
// NotificationService 负责通知
```

---

### 4. 开闭原则 OCP

```text
// 对扩展开放
// 对修改关闭
```

例子：

```text
// 新增支付方式时
// 最好新增类，而不是到处 if-else 改旧代码
```

---

### 5. 里氏替换 LSP

```text
// 子类应该能替代父类使用
```

---

### 6. 接口隔离 ISP

```text
// 不要让类依赖自己不需要的方法
```

---

### 7. 依赖倒置 DIP

```text
// 高层模块不要依赖具体实现
// 要依赖抽象
```

---

## 七、面试最常见的 OOD 题型

### 1. 资源管理类

例子：

- Parking Lot
- Library Management
- Hotel Booking
- Restaurant Reservation

共同特点：

```text
// 资源有限
// 需要分配、释放、查询状态
```

---

### 2. 容器 / 存储类

例子：

- File System
- In-Memory Cache
- Key-Value Store
- Inventory System

共同特点：

```text
// 数据增删改查
// 结构组织清晰
```

---

### 3. 行为模拟类

例子：

- Elevator System
- Vending Machine
- ATM
- Traffic Light

共同特点：

```text
// 有状态变化
// 有事件驱动
```

---

### 4. 社交 / 业务流程类

例子：

- Social Network
- Chat System
- Ride Sharing
- Food Delivery

共同特点：

```text
// 多实体协作
// 权限、关系、流程比较重要
```

---

## 八、面试中最实用的通用模板

下面这个模板你几乎可以套到所有 OOD 题。

```text
1. Clarify requirements
2. Identify entities
3. Define responsibilities
4. Define relationships
5. Design public APIs
6. Choose core data structures
7. Walk through one use case
8. Discuss extensions
```

中文版理解：

```text
// 1. 问需求
// 2. 找对象
// 3. 分职责
// 4. 画关系
// 5. 定接口
// 6. 选数据结构
// 7. 跑一个例子
// 8. 讲扩展
```

---

## 九、一个简化版 OOD 示例：停车场

### 需求

支持：

- 停车
- 离开
- 查找可用车位
- 支持不同类型车辆

---

### 第一步：抽象对象

- `Vehicle`
- `Car`
- `Motorcycle`
- `Truck`
- `ParkingSpot`
- `Level`
- `ParkingLot`
- `Ticket`

---

### 第二步：Python 结构示例

```python
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional
import uuid


class VehicleType(Enum):
    MOTORCYCLE = "motorcycle"
    CAR = "car"
    TRUCK = "truck"


class SpotSize(Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"


class Vehicle(ABC):
    def __init__(self, plate: str, vehicle_type: VehicleType) -> None:
        self.plate = plate
        self.vehicle_type = vehicle_type

    @abstractmethod
    def required_size(self) -> SpotSize:
        pass


class Car(Vehicle):
    def __init__(self, plate: str) -> None:
        super().__init__(plate, VehicleType.CAR)

    def required_size(self) -> SpotSize:
        return SpotSize.MEDIUM


class Truck(Vehicle):
    def __init__(self, plate: str) -> None:
        super().__init__(plate, VehicleType.TRUCK)

    def required_size(self) -> SpotSize:
        return SpotSize.LARGE


@dataclass
class Ticket:
    ticket_id: str
    plate: str
    level_id: int
    spot_id: int


class ParkingSpot:
    def __init__(self, spot_id: int, size: SpotSize) -> None:
        self.spot_id = spot_id
        self.size = size
        self.vehicle: Optional[Vehicle] = None

    def is_free(self) -> bool:
        return self.vehicle is None

    def can_fit(self, vehicle: Vehicle) -> bool:
        size_rank = {
            SpotSize.SMALL: 1,
            SpotSize.MEDIUM: 2,
            SpotSize.LARGE: 3,
        }
        return self.is_free() and size_rank[self.size] >= size_rank[vehicle.required_size()]

    def park(self, vehicle: Vehicle) -> bool:
        if not self.can_fit(vehicle):
            return False
        self.vehicle = vehicle
        return True

    def leave(self) -> None:
        self.vehicle = None


class Level:
    def __init__(self, level_id: int, spots: List[ParkingSpot]) -> None:
        self.level_id = level_id
        self.spots = spots

    def find_spot(self, vehicle: Vehicle) -> Optional[ParkingSpot]:
        for spot in self.spots:
            if spot.can_fit(vehicle):
                return spot
        return None


class ParkingLot:
    def __init__(self, levels: List[Level]) -> None:
        self.levels = levels
        self.active_tickets: Dict[str, Ticket] = {}

    def park_vehicle(self, vehicle: Vehicle) -> Optional[Ticket]:
        for level in self.levels:
            spot = level.find_spot(vehicle)
            if spot and spot.park(vehicle):
                ticket = Ticket(
                    ticket_id=str(uuid.uuid4()),
                    plate=vehicle.plate,
                    level_id=level.level_id,
                    spot_id=spot.spot_id,
                )
                self.active_tickets[ticket.ticket_id] = ticket
                return ticket
        return None

    def leave_vehicle(self, ticket_id: str) -> bool:
        ticket = self.active_tickets.get(ticket_id)
        if not ticket:
            return False

        level = self.levels[ticket.level_id]
        spot = level.spots[ticket.spot_id]
        spot.leave()
        del self.active_tickets[ticket_id]
        return True
```

---

### 这个设计为什么还不错

```text
// Vehicle 负责车辆抽象
// ParkingSpot 负责车位状态和适配规则
// Level 负责本层查找车位
// ParkingLot 负责整体协调
```

这就是 OOD 核心：

```text
// 每个类只做自己该做的事
```

---

## 十、Python 写 OOD 时最常见的错误

### 1. 一个类什么都管

```text
// 所有逻辑都塞进一个类
// 变成 God object
```

---

### 2. 只有数据，没有行为

```text
// 类里只有属性，没有清晰方法
// 逻辑都散在外面
```

---

### 3. 过度继承

```text
// 明明用组合更合适
// 却硬写很多继承层级
```

经验：

```text
// 面试里优先考虑组合
// 继承只在“is-a”关系很明确时用
```

---

### 4. 接口太随意

```text
// 方法命名模糊
// 输入输出不清晰
```

---

### 5. 没有考虑扩展点

```text
// 以后加一个类型，就得改很多 if-else
```

---

## 十一、面试时怎么讲 OOD

你不要一上来就写代码，应该这样讲：

### 1. 先讲需求边界

```text
// 我先假设这是一个内存版系统
// 暂时不考虑并发和持久化
```

### 2. 再讲核心对象

```text
// 我先抽出 4 个核心实体：A、B、C、D
```

### 3. 再讲职责

```text
// A 管理...
// B 负责...
// C 对外提供主接口...
```

### 4. 再讲数据结构

```text
// 我会用 dict 做快速查找
// 用 list 管理有序集合
```

### 5. 最后讲扩展

```text
// 如果要支持新类型，我会新增子类
// 而不是修改核心流程
```

---

## 十二、你最应该练的 OOD 题

建议按这个顺序练：

1. Parking Lot
2. Library Management System
3. Elevator System
4. Vending Machine
5. ATM
6. File System
7. Tic-Tac-Toe
8. Snake Game
9. Deck of Cards
10. Rate Limiter
11. In-Memory Cache
12. Chat System

原因：

```text
// 前几个题帮助你练“实体 + 职责 + 状态”
// 后几个题帮助你练“扩展 + 数据结构 + 业务流程”
```

---

## 十三、刷 OOD 的正确方法

每练一题，都按这个格式写：

### 1. 需求

```text
// 系统支持什么操作
```

### 2. 对象

```text
// 核心类有哪些
```

### 3. 职责

```text
// 每个类做什么
```

### 4. 关系

```text
// 继承 / 组合 / 依赖
```

### 5. API

```text
// public methods
```

### 6. 扩展

```text
// 如果多加一个需求，哪里改动最小
```

---

## 十四、最实用的 Python OOD 面试模板

以后你写设计题，可以优先用这个骨架：

```python
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional


class BaseEntity:
    pass


class BaseService:
    pass


@dataclass
class DataObject:
    pass


class MainManager:
    def __init__(self) -> None:
        self.items: Dict[str, object] = {}

    def create(self) -> None:
        pass

    def get(self, key: str) -> Optional[object]:
        return self.items.get(key)

    def delete(self, key: str) -> bool:
        if key not in self.items:
            return False
        del self.items[key]
        return True
```

这不是最终答案，但它能帮你快速起结构。

---

## 十五、下一步怎么学最有效

最合理的顺序是：

1. 先看这份总指南
2. 练 3 道经典 OOD 题
3. 每题写出自己的类图和职责划分
4. 再补设计原则

如果你愿意，下一步我可以继续直接给你生成：

1. `OOD Python 题目模板文档`
2. `Parking Lot 完整讲解版`
3. `Library / Elevator / Vending Machine 三题详细版`
