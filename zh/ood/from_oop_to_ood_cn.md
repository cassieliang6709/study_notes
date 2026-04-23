---
title: "从 OOP 到 OOD：如何从会写 class 过渡到能做设计题"
---

# 从 OOP 到 OOD：如何从会写 class 过渡到能做设计题

> 目标：解决一个常见卡点  
> “我知道 class、self、继承，但一到 Parking Lot / ATM / Elevator 就不会拆”

---

## 学习重点总结

这篇文档讲的是从 OOP 到 OOD 的思维过渡：从“会写类”变成“会决定哪些类应该存在、各自负责什么、怎么协作”。

## 这篇文档的题目含义

很多人不是不会 Python，也不是不会 class，而是不知道怎么把业务题目翻译成对象模型。这篇文档的目标就是解决这个断层。

## Python 代码

```python
class ParkingSpot:
    def __init__(self, spot_id: int) -> None:
        self.spot_id = spot_id
        self.occupied = False

    def park(self) -> bool:
        if self.occupied:
            return False
        self.occupied = True
        return True


class Level:
    def __init__(self, spots: list[ParkingSpot]) -> None:
        self.spots = spots

    def find_free_spot(self) -> ParkingSpot | None:
        for spot in self.spots:
            if not spot.occupied:
                return spot
        return None
```

## 时间复杂度

本篇主要讲设计思维，不以复杂度为重点；这里的复杂度只是具体接口实现的副产物。

## 空间复杂度

本篇主要讲设计思维，不以复杂度为重点。

## 怎么想到

如果你只停留在 OOP，通常只会问“类怎么写”；进入 OOD 后，关键问题会变成“哪些对象应该存在、谁来负责、谁调用谁”。

## 示例 case

- 场景：设计停车场时，不要把所有逻辑都塞进 `ParkingLot`
- 拆法：`ParkingSpot` 管单车位状态，`Level` 管一层资源，`ParkingLot` 管整体协调
- 为什么：这就是从语法写类走向职责分离的第一步

## 常见 follow-up

- 怎么判断一个类是不是 God Object？
- 面试里要不要先问并发、数据库、分布式这些问题？
- is-a 和 has-a 在 OOD 题里怎么区分？

## 一、先说最核心的区别

很多人卡住，不是因为不会 Python，而是因为把 OOP 和 OOD 混了。

### OOP 是什么

```text
// 我会定义 class
// 我会创建对象
// 我会写属性和方法
```

### OOD 是什么

```text
// 我知道系统里该有哪些对象
// 我知道每个对象应该负责什么
// 我知道对象之间怎么协作
```

所以你可以理解成：

```text
// OOP 解决“怎么写类”
// OOD 解决“为什么是这些类”
```

---

## 二、为什么你会觉得 OOD 很难

因为 OOD 不再只是写语法，而是要做这些事：

1. 把题目里的业务翻译成对象
2. 找出核心实体
3. 拆职责
4. 决定哪些类该存在，哪些不该存在
5. 设计对象之间的关系

这已经从“写代码”变成“设计结构”了。

---

## 三、从 OOP 到 OOD，中间差的是什么

中间差的不是更多语法，而是 3 个思维：

1. `建模思维`
2. `职责分离`
3. `对象协作`

---

## 四、什么叫“建模思维”

建模，就是把现实问题抽象成代码里的对象。

比如题目说：

```text
设计一个停车场，支持不同车辆、不同车位、停车和离场
```

你不能直接冲进代码。

你要先把现实世界里的“名词”提出来：

- 车辆
- 车位
- 楼层
- 停车场
- 票据

这些名词里，很多就会变成类。

所以 OOD 第一步通常是：

```text
// 先抽名词
// 再决定哪些名词应该变成类
```

---

## 五、什么叫“职责分离”

这是 OOD 最核心的能力。

你不是只要想到类名，而是要继续问：

```text
// 这个类到底负责什么？
// 什么不该归它管？
```

比如停车场：

### 不好的设计

```text
// ParkingLot 一个类管所有事：
// 找车位、停车、收费、票据、楼层、车位状态、车辆校验
```

这会变成一个巨大类。

### 更好的设计

- `ParkingSpot` 负责一个车位的状态
- `Level` 负责一层车位管理
- `ParkingLot` 负责整体协调

这就叫职责分离。

---

## 六、什么叫“对象协作”

OOD 不是让你写很多孤立的类，而是让这些类配合起来。

比如 ATM：

- `ATM` 负责会话流程
- `BankService` 负责账户和认证
- `CashDispenser` 负责出钞

这三个类各自不复杂，但协作起来才构成完整系统。

所以你设计时要问：

```text
// 这个动作是谁发起的？
// 真正执行核心逻辑的是谁？
// 谁调用谁？
```

---

## 七、你做 OOD 题时，脑子里应该按这 6 步走

这是最重要的部分。

---

## 第 1 步：先缩小范围

OOD 题非常容易越想越大。

所以你要先主动限定：

```text
// 先做内存版
// 暂不考虑数据库
// 暂不考虑并发
// 先支持核心功能
```

这样你不会一上来就被复杂度压垮。

---

## 第 2 步：抽核心实体

从题目里提名词。

例如 Elevator：

- Elevator
- Request
- Controller
- Building

例如 Amazon Locker：

- Package
- Locker
- LockerLocation
- PickupCode
- LockerService

这一步不要过度细化。

先抓最主要的对象。

---

## 第 3 步：给每个对象分职责

这是最关键的一步。

比如：

### Elevator

```text
// 管自己的当前楼层、方向、目标楼层
// 不负责全局调度
```

### ElevatorController

```text
// 负责收到请求后，决定派哪台电梯
```

注意这里的关键：

```text
// 单体行为和全局协调，通常不是一个类的职责
```

---

## 第 4 步：确定关系

常见关系：

### 继承 is-a

```text
Car is a Vehicle
Truck is a Vehicle
```

### 组合 has-a

```text
ParkingLot has Levels
Level has ParkingSpots
ATM has CashDispenser
```

面试里更常见的是组合。

---

## 第 5 步：再设计 public API

当类和职责清楚后，再去想方法。

比如：

```python
class ParkingLot:
    def park_vehicle(self, vehicle):
        pass

    def leave_vehicle(self, ticket_id):
        pass
```

方法名应该是业务动作，不要写得太抽象。

比如：

- `park_vehicle`
- `leave_vehicle`
- `assign_locker`
- `pickup_package`
- `handle_request`

---

## 第 6 步：跑一个 use case

这一点非常重要。

比如 Parking Lot：

```text
// 用户开车进来
// ParkingLot 收到 vehicle
// 遍历 levels 找可用 spot
// spot 成功占用
// 生成 ticket
```

如果你能顺着流程讲一遍，说明你的设计是活的，不是只堆了几个类名。

---

## 八、从“小 OOP 例子”到“大 OOD 题”的过渡方式

很多人一下看 Parking Lot 会崩，因为对象太多。

正确方式不是直接啃大题，而是先练小对象协作。

---

## 阶段 1：一个对象

例子：

- `Book`
- `Student`
- `Dog`

只练：

```text
// 属性
// 方法
// 状态变化
```

---

## 阶段 2：两个对象协作

例子：

- `Library` + `Book`
- `Course` + `Student`

只练：

```text
// 一个对象管理多个另一个对象
// 方法调用和状态更新
```

---

## 阶段 3：管理器 + 实体

例子：

- `ATM` + `Account` + `CashDispenser`
- `ParkingLot` + `Level` + `ParkingSpot`

开始练：

```text
// 一个 manager 类
// 多个实体类
// 业务流程从 manager 发起
```

---

## 阶段 4：引入抽象和扩展点

例子：

- `Vehicle` -> `Car`, `Truck`
- `PaymentStrategy`
- `NotificationService`

开始练：

```text
// 什么时候要继承
// 什么时候要抽象接口
// 怎么让系统更容易扩展
```

---

## 九、4 道经典题怎么从 OOP 角度看

---

## 1. Parking Lot

### OOP 层面

你需要会：

- 定义 `Vehicle`
- 定义 `ParkingSpot`
- 定义 `Level`
- 定义 `ParkingLot`

### OOD 层面

你需要会：

```text
// 为什么需要 Level？
// 为什么 ParkingSpot 自己判断 can_fit？
// 为什么 ParkingLot 不直接操作所有细节？
```

---

## 2. Elevator

### OOP 层面

你需要会：

- 定义 `Elevator`
- 定义 `Request`
- 定义 `Controller`

### OOD 层面

你需要会：

```text
// 单台电梯行为和全局调度为什么要分开？
// 请求应该交给谁处理？
// 调度策略是不是独立扩展点？
```

---

## 3. ATM

### OOP 层面

你需要会：

- 定义 `ATM`
- 定义 `Account`
- 定义 `Card`
- 定义 `Session`

### OOD 层面

你需要会：

```text
// ATM 为什么不直接持有所有账户余额逻辑？
// 为什么要有 BankService？
// 为什么机器现金和账户余额要分开？
```

---

## 4. Amazon Locker

### OOP 层面

你需要会：

- 定义 `Package`
- 定义 `Locker`
- 定义 `LockerLocation`
- 定义 `LockerService`

### OOD 层面

你需要会：

```text
// 为什么 locker 站点和单个 locker 要分开？
// 为什么要做“最小可适配 locker”？
// pickup code 应该由谁管理？
```

---

## 十、你现在最需要补的能力，不是更多语法

你如果已经懂：

- `class`
- `self`
- `__init__`
- 方法
- list / dict

那你现在卡住，通常不是语法不够，而是：

```text
// 不知道怎么从需求抽对象
// 不知道怎么分职责
// 不知道类之间怎么协作
```

所以你接下来最应该练的是：

1. 从题目里划出名词
2. 给每个类写一句职责
3. 写出 3 到 5 个主方法
4. 讲清楚一个完整 use case

---

## 十一、一个通用的 OOD 面试回答模板

以后你拿到一道题，可以这样讲：

### 1. 先缩小范围

```text
// 我先做内存版
// 只支持核心操作
```

### 2. 抽对象

```text
// 我先抽出 4 个核心实体：A、B、C、D
```

### 3. 分职责

```text
// A 负责...
// B 负责...
// C 负责...
```

### 4. 讲关系

```text
// A has many B
// C depends on D
```

### 5. 讲接口

```text
// 对外主要暴露这些方法
```

### 6. 跑流程

```text
// 用户做一个动作后，系统里哪些对象会依次工作
```

### 7. 讲扩展

```text
// 如果后续要支持新需求，我会把哪部分抽成策略或新增类
```

---

## 十二、最常见的 5 个错误

### 1. 一拿题就写代码

正确做法：

```text
// 先讲需求、对象、职责
```

### 2. 一个大类包办全部逻辑

这会让代码很难扩展。

### 3. 只会列类名，不会讲为什么

面试官更看重“为什么这样拆”。

### 4. 不跑 use case

类名堆出来不代表设计成立。

### 5. 一上来就过度设计

比如：

```text
// 先写十几个模式、二十几个接口
```

面试里通常先做清晰的基础版更重要。

---

## 十三、你现在可以怎么练

按这个顺序练最稳：

### 第 1 步

看这几份：

- [python_oop_prerequisites_cn.md](../python/python_oop_prerequisites_cn/)
- [python_oop_concepts_cn.md](../python/python_oop_concepts_cn/)

### 第 2 步

自己写两个小例子：

- `Book + Library`
- `Student + Course`

### 第 3 步

再看这些 OOD 案例：

- [parking_lot_python.md](./ood_cases/parking_lot_python/)
- [elevator_system_python.md](./ood_cases/elevator_system_python/)

- [amazon_locker_python.md](./ood_cases/amazon_locker_python/)

### 第 4 步

每一题都自己练这 4 个问题：

```text
// 有哪些核心类？
// 每个类负责什么？
// 主流程怎么走？
// 后续扩展点在哪里？
```

---

## 十四、最后一句最重要的话

你从 OOP 走到 OOD，不是靠学更多语法，而是靠：

```text
// 从“我会写类”
// 变成“我会按职责设计类”
```

这一步一旦过了，Parking Lot、ATM、Elevator、Amazon Locker 这些题会开始变成同一种题：

```text
// 需求 -> 抽对象 -> 分职责 -> 定关系 -> 讲流程
```

---

## 十五、下一步最合理的动作

如果你要，我下一步可以继续直接给你补这两份之一：

1. `ood_interview_answer_templates_cn.md`
   每道题怎么开口讲

2. `oop_to_ood_small_practice_cn.md`
   从小练习一步步过渡到 Parking Lot / ATM / Elevator
