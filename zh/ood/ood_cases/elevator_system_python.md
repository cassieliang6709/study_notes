---
title: "Elevator System OOD（Python）"
---

# Elevator System OOD（Python）

---

## 这个设计题 / 设计点的总结

`Elevator System` 题最核心的是调度策略，而不是类名。代码只是载体，真正考的是你能不能把“单部电梯行为”和“全局调度逻辑”拆开。

## 题目含义

设计一个多电梯系统，支持外部呼梯和电梯内选层，并由控制器把请求分配给合适的电梯。

## 时间复杂度

- 分配 hall request：当前简单策略是遍历所有电梯，通常 `O(number_of_elevators)`
- 电梯移动一步：通常是 `O(1)` 到 `O(number_of_targets)`，取决于目标集合管理方式

## 空间复杂度

主要取决于电梯数量和每台电梯维护的目标楼层集合。

## 怎么想到

这题不要一开始就追求最优调度。面试里更稳的做法是先讲一个简单可运行、可扩展、可解释的调度策略，再说如何升级。

## 示例 case

- 场景：5 楼有人按上行按钮
- 过程：`ElevatorController` 比较各电梯的当前楼层与请求位置，选择最合适的一台
- 结果：被选中的 `Elevator` 把 5 楼加入目标集合并开始移动

## 常见 follow-up

- 如果要区分上下行队列，数据结构怎么改？
- 如果要支持满载状态，调度器应怎么跳过某些电梯？
- 如果要支持真正实时优化，应该把哪部分抽成策略类？

## 1. 面试里先定范围

建议先说：

```text
// 先做单栋楼、多电梯、内存版
// 支持外部呼梯和电梯内选层
// 暂不考虑真正实时调度优化
```

---

## 2. 核心对象

- `Direction`
- `Request`
- `Elevator`
- `ElevatorController`
- `Building`

---

## 3. 关键建模点

电梯题真正难的不是类，而是：

```text
// 调度策略怎么设计
// 请求怎么分配给电梯
// 电梯自己怎么维护 stops
```

所以面试时要主动讲：

```text
// 我先用一个简单可讲清楚的策略
// 比如最近可服务电梯
```

---

## 4. 职责划分

### `Request`

```text
// 表示一个乘客请求
// 可以区分 hall request 和 car request
```

### `Elevator`

```text
// 管理当前楼层、方向、目标楼层集合
// 响应 add_stop / move_one_step / open_door
```

### `ElevatorController`

```text
// 接收请求
// 选择合适电梯
// 把请求分配给对应电梯
```

---

## 5. Python 代码骨架

```python
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import List, Optional, Set


class Direction(Enum):
    UP = "up"
    DOWN = "down"
    IDLE = "idle"


@dataclass
class Request:
    floor: int
    direction: Direction


class Elevator:
    def __init__(self, elevator_id: int, current_floor: int = 0) -> None:
        self.elevator_id = elevator_id
        self.current_floor = current_floor
        self.direction = Direction.IDLE
        self.targets: Set[int] = set()

    def add_stop(self, floor: int) -> None:
        self.targets.add(floor)
        self._update_direction()

    def move_one_step(self) -> None:
        if not self.targets:
            self.direction = Direction.IDLE
            return

        if self.direction == Direction.UP:
            self.current_floor += 1
        elif self.direction == Direction.DOWN:
            self.current_floor -= 1

        if self.current_floor in self.targets:
            self.targets.remove(self.current_floor)

        self._update_direction()

    def _update_direction(self) -> None:
        if not self.targets:
            self.direction = Direction.IDLE
            return

        if any(target > self.current_floor for target in self.targets):
            self.direction = Direction.UP
        elif any(target < self.current_floor for target in self.targets):
            self.direction = Direction.DOWN
        else:
            self.direction = Direction.IDLE

    def score_for_request(self, request: Request) -> int:
        return abs(self.current_floor - request.floor)


class ElevatorController:
    def __init__(self, elevators: List[Elevator]) -> None:
        self.elevators = elevators

    def handle_hall_request(self, request: Request) -> Optional[Elevator]:
        if not self.elevators:
            return None

        best = min(self.elevators, key=lambda e: e.score_for_request(request))
        best.add_stop(request.floor)
        return best

    def handle_car_request(self, elevator_id: int, destination: int) -> bool:
        for elevator in self.elevators:
            if elevator.elevator_id == elevator_id:
                elevator.add_stop(destination)
                return True
        return False
```

---

## 6. 面试时怎么讲

建议这样讲：

```text
// 我把系统拆成“单部电梯行为”和“全局调度器”两层
// Elevator 负责自己怎么移动
// ElevatorController 负责选择哪一台电梯来服务请求
```

---

## 7. 进阶扩展点

- 支持真正的上下行优先调度
- 把目标楼层拆成 `up queue` 和 `down queue`
- 支持满载状态
- 支持维修模式
- 支持多栋楼

扩展说法：

```text
// 如果要优化调度策略，我会把 score / dispatch logic 抽成策略类
// 这样不会影响 Elevator 本身
```

---

## 8. 常见错误

- 调度逻辑和电梯移动逻辑混在一起
- 只讲类，不讲调度策略
- 不区分外部请求和内部选层
