from dataclasses import dataclass


@dataclass
class Case:
    in_data: object
    out_data: object


@dataclass
class Lab1Task6Data:
    number: int


cases = [
    Case(in_data=Lab1Task6Data(number=0), out_data=True),
    Case(in_data=Lab1Task6Data(number=3), out_data=True),
    Case(in_data=Lab1Task6Data(number=4), out_data=False),
    Case(in_data=Lab1Task6Data(number=11), out_data=False),
    Case(in_data=Lab1Task6Data(number=49), out_data=False),
    Case(in_data=Lab1Task6Data(number=89), out_data=True),
    Case(in_data=Lab1Task6Data(number=233), out_data=True),
    Case(in_data=Lab1Task6Data(number=387), out_data=False),
    Case(in_data=Lab1Task6Data(number=692), out_data=False),
    Case(in_data=Lab1Task6Data(number=987), out_data=True),
    Case(in_data=Lab1Task6Data(number=1601), out_data=False),
    Case(in_data=Lab1Task6Data(number=4181), out_data=True),
    Case(in_data=Lab1Task6Data(number=614328), out_data=False),
    Case(in_data=Lab1Task6Data(number=832040), out_data=True),
    Case(in_data=Lab1Task6Data(number=1346269), out_data=True),
    Case(in_data=Lab1Task6Data(number=86267571271), out_data=False),
    Case(in_data=Lab1Task6Data(number=365435296162), out_data=True),
    Case(in_data=Lab1Task6Data(number=99194853094755497), out_data=True),
    Case(in_data=Lab1Task6Data(number=160500643816368088), out_data=False),
    Case(in_data=Lab1Task6Data(number=259695496911122585), out_data=True),
    Case(in_data=Lab1Task6Data(number=420196141727489673), out_data=False),
    Case(
        in_data=Lab1Task6Data(number=1409869790947669143312035591975596518985),
        out_data=False,
    ),
    Case(
        in_data=Lab1Task6Data(
            number=12776523572924432586037033804655011898659523447152241
        ),
        out_data=False,
    ),
    Case(
        in_data=Lab1Task6Data(
            number=20672849399056463095319772838289364792345825123228624
        ),
        out_data=True,
    ),
]
