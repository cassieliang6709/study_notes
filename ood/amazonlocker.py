'''
功能：亚马逊locker

用户下单
包裹被送到locker
系统分配一个柜子
用户收到取件码
取件码取包裹
柜子变空。

class ：
用户，包裹，locker，locker spot，Pickup Code

package:
- package size, size

LockerSpot:
field:
- locker spot id
- locker spot size
- is occupied
- package
- pickup code

method:
is_occupied
assign_package(package)
generate_pickup_code()
pickup_package(pickup_code)
release_spot()

LockerSystem
field:
- locker spots

method:
- assign locker spot to package
_find_available_spot(package)
_generate_pickup_code()
assign_package_to_spot(package)


- generate pickup code
pickup_package(pickup_code)

- pickup package with code

show_available_spots()


'''

class PackageSize(Enum):
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'

class Package:
    def __init__(self, package_id: str, size: PackageSize):
        self.package_id = package_id
        self.size = size

class LockerSpot:
    def __init__:
        self.spot_id = spot_id
        self.size = size
        self.is_occupied = False
        self.package = None
        self.pickup_code = None
    
    def is_occupied(self):
        return self.is_occupied
    
    def can_fit(self, package: Package) -> bool:
        if self.size == PackageSize.SMALL:
            return package.size == PackageSize.SMALL
        elif self.size == PackageSize.MEDIUM:
            return package.size in [PackageSize.SMALL, PackageSize.MEDIUM]
        elif self.size == PackageSize.LARGE:
            return package.size in [PackageSize.SMALL, PackageSize.MEDIUM, PackageSize.LARGE]
        return False    
    
    def assign_package(self, package: Package):
        if not self.is_occupied and self.can_fit(package):
            self.package = package
            self.is_occupied = True
            self.pickup_code = self.generate_pickup_code()
            return True
        return False
    

    def generate_pickup_code(self) -> str:
        # 生成一个唯一的取件码，可以使用UUID或其他方法
        return str(random.randint(100000, 999999))