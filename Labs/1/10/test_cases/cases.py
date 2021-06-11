from dataclasses import dataclass


@dataclass
class Case:
    in_data: object
    out_data: object


@dataclass
class Lab1Task10Data:
    number: int


cases = [
    Case(in_data=Lab1Task10Data(number=1), out_data=1),
    Case(in_data=Lab1Task10Data(number=5), out_data=4),
    Case(in_data=Lab1Task10Data(number=26), out_data=12),
    Case(in_data=Lab1Task10Data(number=144), out_data=48),
    Case(in_data=Lab1Task10Data(number=248), out_data=120),
    Case(in_data=Lab1Task10Data(number=333), out_data=216),
    Case(in_data=Lab1Task10Data(number=12005), out_data=8232),
    Case(in_data=Lab1Task10Data(number=49602), out_data=14160),
    Case(in_data=Lab1Task10Data(number=1487536), out_data=738752),
    Case(in_data=Lab1Task10Data(number=14478962), out_data=7147764),
    Case(in_data=Lab1Task10Data(number=58743692045), out_data=45862214400),
]