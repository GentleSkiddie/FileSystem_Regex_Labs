from dataclasses import dataclass


@dataclass
class Case:
    in_data: object
    out_data: object


@dataclass
class Lab2Task1_3Data:
    file: str


cases = [
    Case(
        in_data=Lab2Task1_3Data(file="./samples/sample_1.html"),
        out_data="431e49c916044364af058095a5428ae9",
    ),
    Case(
        in_data=Lab2Task1_3Data(file="./samples/sample_2.html"),
        out_data="11be7e5a48e04e33a72bdecb6a1d5487",
    ),
    Case(
        in_data=Lab2Task1_3Data(file="./samples/sample_3.html"),
        out_data="fe68cd078d194059bb10fb9a669cbd87",
    ),
]
