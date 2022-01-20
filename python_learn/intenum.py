from enum import IntEnum, Enum

class TestIntEnum(IntEnum):
    TEST = 1
    
class TestEnum(Enum):
    TEST = 1
    
    
if TestEnum.TEST == 1:
    print("test_enum")
    
    
if TestIntEnum.TEST == 1:
    print("test_int_enum")