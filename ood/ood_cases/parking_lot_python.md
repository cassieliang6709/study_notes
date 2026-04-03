# Parking Lot OOD（Python）

---

## 1. 面试里先怎么澄清

先明确这些假设：

```text
// 这是内存版设计
// 暂不考虑数据库、并发、支付系统
// 支持不同类型车辆
// 支持停车、离场、查询可用车位
```

如果面试官继续加需求，再扩。

---

## 2. 核心对象

- `Vehicle`
- `Car`
- `Motorcycle`
- `Truck`
- `ParkingSpot`
- `Level`
- `ParkingLot`
- `Ticket`

---

## 3. 职责划分

### `Vehicle`

```text
// 抽象车辆类型
// 告诉系统自己需要什么尺寸车位
```

### `ParkingSpot`

```text
// 管理一个车位的状态
// 判断某辆车能不能停进来
// 执行 park / leave
```

### `Level`

```text
// 管理一层楼的所有车位
// 查找一个可用车位
```

### `ParkingLot`

```text
// 管理整个停车场
// 对外提供 park_vehicle / leave_vehicle
// 维护 active tickets
```

---

## 4. 类之间关系

```text
Vehicle <- Car / Motorcycle / Truck
ParkingLot has many Level
Level has many ParkingSpot
ParkingLot creates Ticket
```

---

## 5. Python 代码骨架

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


class Motorcycle(Vehicle):
    def __init__(self, plate: str) -> None:
        super().__init__(plate, VehicleType.MOTORCYCLE)

    def required_size(self) -> SpotSize:
        return SpotSize.SMALL


class Truck(Vehicle):
    def __init__(self, plate: str) -> None:
        super().__init__(plate, VehicleType.TRUCK)

    def required_size(self) -> SpotSize:
        return SpotSize.LARGE


@dataclass
class Ticket:
    ticket_id: str
    level_id: int
    spot_id: int
    plate: str


class ParkingSpot:
    def __init__(self, spot_id: int, size: SpotSize) -> None:
        self.spot_id = spot_id
        self.size = size
        self.vehicle: Optional[Vehicle] = None

    def is_free(self) -> bool:
        return self.vehicle is None

    def can_fit(self, vehicle: Vehicle) -> bool:
        rank = {
            SpotSize.SMALL: 1,
            SpotSize.MEDIUM: 2,
            SpotSize.LARGE: 3,
        }
        return self.is_free() and rank[self.size] >= rank[vehicle.required_size()]

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

    def find_available_spot(self, vehicle: Vehicle) -> Optional[ParkingSpot]:
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
            spot = level.find_available_spot(vehicle)
            if spot and spot.park(vehicle):
                ticket = Ticket(
                    ticket_id=str(uuid.uuid4()),
                    level_id=level.level_id,
                    spot_id=spot.spot_id,
                    plate=vehicle.plate,
                )
                self.active_tickets[ticket.ticket_id] = ticket
                return ticket
        return None

    def leave_vehicle(self, ticket_id: str) -> bool:
        ticket = self.active_tickets.get(ticket_id)
        if ticket is None:
            return False

        level = self.levels[ticket.level_id]
        spot = level.spots[ticket.spot_id]
        spot.leave()
        del self.active_tickets[ticket_id]
        return True
```

---

## 6. 面试时怎么讲设计亮点

```text
// 我把“找车位”和“管理车位状态”拆开了
// Level 负责本层资源管理
// ParkingLot 只做整体协调
// Vehicle 用抽象类，后续可以扩展更多车型
```

---

## 7. 常见扩展点

- 支持费用计算
- 支持入口 / 出口
- 支持预订车位
- 支持电动车充电位
- 支持并发锁

扩展说法：

```text
// 如果要支持收费，我会新增 PricingStrategy 或 FeeCalculator
// 不把计费逻辑直接塞进 ParkingLot
```

---

## 8. 这题最容易犯的错误

- 所有逻辑都塞进 `ParkingLot`
- 不区分 `Level` 和 `Spot` 的职责
- 车位适配规则写死在外部

