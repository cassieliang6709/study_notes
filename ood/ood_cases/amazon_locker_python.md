# Amazon Locker OOD（Python）

---

## 1. 面试里先澄清

建议先讲清楚范围：

```text
// 设计一个 Amazon Locker 取件系统
// 支持包裹分配柜子、取件、释放柜子
// 暂不考虑真正物流运输过程
```

---

## 2. 核心对象

- `Package`
- `LockerSize`
- `Locker`
- `LockerLocation`
- `PickupCode`
- `LockerService`

---

## 3. 核心建模点

这题的关键不是“包裹”本身，而是：

```text
// 包裹尺寸如何匹配柜子
// 如何找到最合适的 locker
// 如何生成 pickup code
// 取件后如何释放 locker
```

---

## 4. 职责划分

### `Package`

```text
// 记录包裹信息和尺寸
```

### `Locker`

```text
// 表示单个柜子
// 管理占用状态
```

### `LockerLocation`

```text
// 表示一个站点
// 管理该站点下所有 locker
```

### `LockerService`

```text
// 负责分配 locker
// 生成取件码
// 处理取件逻辑
```

---

## 5. Python 代码骨架

```python
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional
import uuid


class LockerSize(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


@dataclass
class Package:
    package_id: str
    size: LockerSize
    customer_id: str


@dataclass
class PickupCode:
    code: str
    package_id: str
    locker_id: str


class Locker:
    def __init__(self, locker_id: str, size: LockerSize) -> None:
        self.locker_id = locker_id
        self.size = size
        self.package: Optional[Package] = None

    def is_free(self) -> bool:
        return self.package is None

    def can_fit(self, package: Package) -> bool:
        return self.is_free() and self.size.value >= package.size.value

    def assign_package(self, package: Package) -> bool:
        if not self.can_fit(package):
            return False
        self.package = package
        return True

    def release(self) -> Optional[Package]:
        package = self.package
        self.package = None
        return package


class LockerLocation:
    def __init__(self, location_id: str, lockers: List[Locker]) -> None:
        self.location_id = location_id
        self.lockers = lockers

    def find_best_locker(self, package: Package) -> Optional[Locker]:
        candidates = [locker for locker in self.lockers if locker.can_fit(package)]
        if not candidates:
            return None
        return min(candidates, key=lambda l: l.size.value)


class LockerService:
    def __init__(self, locations: List[LockerLocation]) -> None:
        self.locations = locations
        self.codes: Dict[str, PickupCode] = {}

    def assign_locker(self, package: Package) -> Optional[PickupCode]:
        for location in self.locations:
            locker = location.find_best_locker(package)
            if locker and locker.assign_package(package):
                code = PickupCode(
                    code=str(uuid.uuid4())[:8],
                    package_id=package.package_id,
                    locker_id=locker.locker_id,
                )
                self.codes[code.code] = code
                return code
        return None

    def pickup(self, pickup_code: str) -> Optional[Package]:
        code = self.codes.get(pickup_code)
        if code is None:
            return None

        for location in self.locations:
            for locker in location.lockers:
                if locker.locker_id == code.locker_id:
                    package = locker.release()
                    del self.codes[pickup_code]
                    return package
        return None
```

---

## 6. 面试时怎么讲

```text
// 我把 locker 站点和单个 locker 分层管理
// 单个 locker 只负责占用状态
// LockerLocation 负责站点内的资源选择
// LockerService 负责全局分配和取件流程
```

---

## 7. 可以主动讲的扩展点

- 支持就近站点分配
- 支持过期未取包裹
- 支持一次性验证码
- 支持短信 / 邮件通知
- 支持不同站点库存统计

---

## 8. 常见错误

- 不做“最小可适配 locker”选择
- 站点和单柜职责不分
- pickup code 和 locker 占用状态绑定不清楚

