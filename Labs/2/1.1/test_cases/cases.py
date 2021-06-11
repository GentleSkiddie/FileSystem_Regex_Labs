from dataclasses import dataclass


@dataclass
class Case:
    in_data: object
    out_data: object


@dataclass
class Lab2Task1_1Data:
    file: str


cases = [
    Case(
        in_data=Lab2Task1_1Data(file="./samples/sample_1.html"),
        out_data="c24888a0-1a0e-47e1-85ca-45c9c6db24cb",
    ),
    Case(
        in_data=Lab2Task1_1Data(file="./samples/sample_2.html"),
        out_data="45d7b347-2cc5-48fe-87fa-99e0fc25933b",
    ),
    Case(
        in_data=Lab2Task1_1Data(file="./samples/sample_3.html"),
        out_data="6d263d88-55ee-413b-8fa8-914a45e65e80",
    ),
]
