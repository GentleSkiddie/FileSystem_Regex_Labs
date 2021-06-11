from dataclasses import dataclass


@dataclass
class Case:
    in_data: object
    out_data: object


@dataclass
class Lab1Task1Data:
    directory: str
    file: str
    is_recursive: bool
    depth: int


cases = [
    Case(
        in_data=Lab1Task1Data(
            directory="./samples/sample_0", file="14a614", is_recursive=True, depth=5
        ),
        out_data="./samples/sample_0/825fe5/3d5625/14a614",
    ),
    Case(
        in_data=Lab1Task1Data(
            directory="./samples/sample_0", file="e6efd3", is_recursive=True, depth=2
        ),
        out_data="",
    ),
    Case(
        in_data=Lab1Task1Data(
            directory="./samples/sample_0", file="b09ffa", is_recursive=True, depth=1
        ),
        out_data="./samples/sample_0/b09ffa",
    ),
    Case(
        in_data=Lab1Task1Data(
            directory="./samples/sample_1", file="c6fc29", is_recursive=True, depth=5
        ),
        out_data="./samples/sample_1/cc42f5/1a4513/c6fc29",
    ),
    Case(
        in_data=Lab1Task1Data(
            directory="./samples/sample_1", file="9e401c", is_recursive=False, depth=0
        ),
        out_data="",
    ),
    Case(
        in_data=Lab1Task1Data(
            directory="./samples/sample_1", file="9e401c", is_recursive=True, depth=5
        ),
        out_data="./samples/sample_1/cc42f5/80169d/9e401c",
    ),
    Case(
        in_data=Lab1Task1Data(
            directory="./samples/sample_2", file="817599", is_recursive=True, depth=5
        ),
        out_data="",
    ),
    Case(
        in_data=Lab1Task1Data(
            directory="./samples/sample_2", file="211d4c", is_recursive=True, depth=7
        ),
        out_data="./samples/sample_2/b3e752/6bc0be/55cd88/91747c/ec286a/ce4895/211d4c",
    ),
    Case(
        in_data=Lab1Task1Data(
            directory="./samples/sample_2", file="664b86", is_recursive=True, depth=10
        ),
        out_data="./samples/sample_2/b3e752/6bc0be/55cd88/664b86",
    ),
    Case(
        in_data=Lab1Task1Data(
            directory="./samples/sample_3", file="7fa841", is_recursive=True, depth=10
        ),
        out_data="",
    ),
    Case(
        in_data=Lab1Task1Data(
            directory="./samples/sample_3", file="f398c9", is_recursive=True, depth=10
        ),
        out_data="./samples/sample_3/3ea92d/1a120e/36f858/5cb6d3/017909/f398c9",
    ),
    Case(
        in_data=Lab1Task1Data(
            directory="./samples/sample_3", file="fd86ae", is_recursive=True, depth=3
        ),
        out_data="./samples/sample_3/2f8f21/14c14c/fd86ae",
    ),
]
