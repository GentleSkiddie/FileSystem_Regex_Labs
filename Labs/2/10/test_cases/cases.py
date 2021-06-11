from dataclasses import dataclass


@dataclass
class Case:
    in_data: object
    out_data: object


@dataclass
class Lab2Task10Data:
    string: str


cases = [
    Case(in_data=Lab2Task10Data(string="192.0.2.235"), out_data=True),
    Case(in_data=Lab2Task10Data(string="99.198.122.146"), out_data=True),
    Case(in_data=Lab2Task10Data(string="100.100.100.100"), out_data=True),
    Case(in_data=Lab2Task10Data(string="46.51.197.88"), out_data=True),
    Case(in_data=Lab2Task10Data(string="0xC0.0x00.0x02.0xEB"), out_data=True),
    Case(in_data=Lab2Task10Data(string="0x11.0x22.0x33.0x44"), out_data=True),
    Case(in_data=Lab2Task10Data(string="0300.0000.0002.0353"), out_data=True),
    Case(in_data=Lab2Task10Data(string="0377.0377.0377.0377"), out_data=True),
    Case(in_data=Lab2Task10Data(string="0100.0100.0100.0100"), out_data=True),
    Case(in_data=Lab2Task10Data(string="0xC00002EC"), out_data=True),
    Case(in_data=Lab2Task10Data(string="3221226219"), out_data=True),
    Case(in_data=Lab2Task10Data(string="287454020"), out_data=True),
    Case(in_data=Lab2Task10Data(string="030000001353"), out_data=True),
    Case(in_data=Lab2Task10Data(string="037704570437"), out_data=True),
    Case(in_data=Lab2Task10Data(string="0300.19.0.2"), out_data=True),
    Case(in_data=Lab2Task10Data(string="0xFF.255.0377.0x12"), out_data=True),
    Case(in_data=Lab2Task10Data(string="256.256.256.256"), out_data=False),
    Case(in_data=Lab2Task10Data(string="0x100.0x11.0x11.0x11"), out_data=False),
    Case(in_data=Lab2Task10Data(string="0xx20.0x20.0x20.0x20"), out_data=False),
    Case(in_data=Lab2Task10Data(string="0100.0100.0109.0100"), out_data=False),
    Case(in_data=Lab2Task10Data(string="0x100111111"), out_data=False),
    Case(in_data=Lab2Task10Data(string="100.100.100"), out_data=False),
    Case(in_data=Lab2Task10Data(string="0x20.0x50.0x2"), out_data=False),
    Case(in_data=Lab2Task10Data(string=".100.100.100.100"), out_data=False),
    Case(in_data=Lab2Task10Data(string="100..100.100.100."), out_data=False),
    Case(in_data=Lab2Task10Data(string="256.100.100.100.100"), out_data=False),
    Case(in_data=Lab2Task10Data(string="100.100.100.100."), out_data=False),
    Case(in_data=Lab2Task10Data(string="4294967296"), out_data=False),
    Case(in_data=Lab2Task10Data(string="037777777778"), out_data=False),
    Case(in_data=Lab2Task10Data(string="011377000000000000008"), out_data=False),
]