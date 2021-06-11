from dataclasses import dataclass


@dataclass
class Case:
    in_data: object
    out_data: object


@dataclass
class Lab2Task4Data:
    string: str


cases = [
    Case(
        in_data=Lab2Task4Data(string="http://userid:password@example.com:8080"),
        out_data=True,
    ),
    Case(in_data=Lab2Task4Data(string="http://142.42.1.1/"), out_data=True),
    Case(
        in_data=Lab2Task4Data(string="http://www.example.com/wpstyle/?p=364"),
        out_data=True,
    ),
    Case(in_data=Lab2Task4Data(string="http://j.mp"), out_data=True),
    Case(
        in_data=Lab2Task4Data(string="http://code.google.com/events/#&product=browser"),
        out_data=True,
    ),
    Case(in_data=Lab2Task4Data(string="www.example.com"), out_data=False),
    Case(in_data=Lab2Task4Data(string="http://"), out_data=False),
    Case(in_data=Lab2Task4Data(string="http"), out_data=False),
    Case(in_data=Lab2Task4Data(string="231ds231sd"), out_data=False),
    Case(in_data=Lab2Task4Data(string="http://www.peck.com/"), out_data=True),
    Case(in_data=Lab2Task4Data(string="https://contreras-harris.com/"), out_data=True),
    Case(in_data=Lab2Task4Data(string="ftp://www.smith.com/"), out_data=True),
    Case(in_data=Lab2Task4Data(string="http://campbell.com/"), out_data=True),
]
