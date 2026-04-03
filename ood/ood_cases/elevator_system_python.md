# Elevator System OOD（Python）

---

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

