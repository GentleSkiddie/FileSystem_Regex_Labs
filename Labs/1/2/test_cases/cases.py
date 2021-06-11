from dataclasses import dataclass


@dataclass
class Case:
    in_data: object
    out_data: object


@dataclass
class Lab1Task2Data:
    directory: str
    file_type: str
    is_recursive: bool
    depth: int


cases = [
    Case(
        in_data=Lab1Task2Data(
            directory="./samples/sample_0",
            file_type="7-zip",
            is_recursive=True,
            depth=10,
        ),
        out_data=["./samples/sample_0/2b00a5/0ac78f/98e6ef/86857f"],
    ),
    Case(
        in_data=Lab1Task2Data(
            directory="./samples/sample_0", file_type="Zip", is_recursive=True, depth=3
        ),
        out_data=[
            "./samples/sample_0/2b00a5/ac449d",
            "./samples/sample_0/2b00a5/0ac78f/2d2b06",
        ],
    ),
    Case(
        in_data=Lab1Task2Data(
            directory="./samples/sample_0",
            file_type="POSIX tar",
            is_recursive=False,
            depth=0,
        ),
        out_data=["./samples/sample_0/6bf9ea"],
    ),
    Case(
        in_data=Lab1Task2Data(
            directory="./samples/sample_1",
            file_type="ELF 64-bit",
            is_recursive=True,
            depth=5,
        ),
        out_data=[
            "./samples/sample_1/598582/1ef82e",
            "./samples/sample_1/598582/e11b5a",
            "./samples/sample_1/598582/235b98/713c45",
            "./samples/sample_1/598582/574d18/4cccdc/d2fdf8",
            "./samples/sample_1/598582/574d18/4cccdc/c10e09/e517bf",
            "./samples/sample_1/598582/574d18/7c3b7a/314f1d/663957",
            "./samples/sample_1/598582/574d18/7c3b7a/686bbe/7cfbbf",
            "./samples/sample_1/598582/574d18/dc7c1e/e7e55f",
            "./samples/sample_1/598582/574d18/dc7c1e/361314/0dfecd",
            "./samples/sample_1/598582/574d18/dc7c1e/361314/6c1f35",
            "./samples/sample_1/598582/574d18/f96c5a/94ba33",
        ],
    ),
    Case(
        in_data=Lab1Task2Data(
            directory="./samples/sample_1",
            file_type="ASCII text",
            is_recursive=True,
            depth=10,
        ),
        out_data=[
            "./samples/sample_1/598582/8aa303",
            "./samples/sample_1/598582/d7026d",
            "./samples/sample_1/598582/f5e321",
            "./samples/sample_1/598582/235b98/250e67",
            "./samples/sample_1/598582/235b98/71bffe",
            "./samples/sample_1/598582/235b98/c1c3bc/0cdd84",
            "./samples/sample_1/598582/574d18/4cccdc/3c7757",
            "./samples/sample_1/598582/574d18/4cccdc/bdc7de",
            "./samples/sample_1/598582/574d18/4cccdc/c10e09/860ef5",
            "./samples/sample_1/598582/574d18/7c3b7a/314f1d/b6ae03",
            "./samples/sample_1/598582/574d18/dc7c1e/e1e8c5/ae3fdc",
        ],
    ),
    Case(
        in_data=Lab1Task2Data(
            directory="./samples/sample_2",
            file_type="PE32+",
            is_recursive=True,
            depth=10,
        ),
        out_data=[
            "./samples/sample_2/9389d7",
            "./samples/sample_2/c49f46",
            "./samples/sample_2/cdfe5d",
            "./samples/sample_2/14776b/d54cd4",
            "./samples/sample_2/14776b/d5ee02",
            "./samples/sample_2/14776b/3d3f0c/2b9884",
            "./samples/sample_2/14776b/3d3f0c/6b6fc1",
            "./samples/sample_2/14776b/3d3f0c/a049b5",
            "./samples/sample_2/deeee5/4f16f6/30e3b7",
            "./samples/sample_2/deeee5/4f16f6/6a6f5a",
            "./samples/sample_2/deeee5/4f16f6/c73c77/217815",
            "./samples/sample_2/deeee5/4f16f6/d4ef71/417e49",
            "./samples/sample_2/deeee5/4f16f6/d4ef71/4f4561",
            "./samples/sample_2/deeee5/b76c61/c40ebe/28cd72",
            "./samples/sample_2/deeee5/b76c61/c40ebe/5c695e",
            "./samples/sample_2/deeee5/b76c61/c40ebe/803d68",
            "./samples/sample_2/deeee5/b76c61/c40ebe/9e414e/945e77",
            "./samples/sample_2/deeee5/b76c61/fa398a/e8db0a",
            "./samples/sample_2/deeee5/deed21/0e21cb",
            "./samples/sample_2/deeee5/deed21/147c74",
            "./samples/sample_2/deeee5/deed21/d75522",
            "./samples/sample_2/deeee5/deed21/2b0c77/2986c8",
            "./samples/sample_2/deeee5/deed21/2b0c77/2b862e/1cd6a9",
            "./samples/sample_2/edd1af/047e1c",
            "./samples/sample_2/edd1af/9db2d9",
            "./samples/sample_2/edd1af/a735ab",
            "./samples/sample_2/edd1af/b10d58",
            "./samples/sample_2/edd1af/8fc966/2b0ef6",
            "./samples/sample_2/edd1af/8fc966/d023bd",
            "./samples/sample_2/edd1af/8fc966/dfcb5a/3d49c3",
            "./samples/sample_2/fc0f5f/3ba684",
        ],
    ),
    Case(
        in_data=Lab1Task2Data(
            directory="./samples/sample_2",
            file_type="Debian binary package",
            is_recursive=True,
            depth=3,
        ),
        out_data=[
            "./samples/sample_2/e67c29",
            "./samples/sample_2/14776b/24bc70",
            "./samples/sample_2/14776b/baeb04",
            "./samples/sample_2/14776b/3d3f0c/65cb30",
            "./samples/sample_2/deeee5/6fd47e",
            "./samples/sample_2/deeee5/4f16f6/b17e36",
            "./samples/sample_2/deeee5/4f16f6/b77aba",
            "./samples/sample_2/deeee5/b76c61/a9ef59",
            "./samples/sample_2/deeee5/deed21/23be82",
            "./samples/sample_2/edd1af/b3ec43",
            "./samples/sample_2/edd1af/8fc966/202ee7",
            "./samples/sample_2/fc0f5f/4ae1a3",
        ],
    ),
    Case(
        in_data=Lab1Task2Data(
            directory="./samples/sample_3",
            file_type="pcapng",
            is_recursive=True,
            depth=10,
        ),
        out_data=[
            "./samples/sample_3/f90a96/63807b/130b95/f2099c/9d909c/481de0/eff114/39b95c/41e905/59b28f"
        ],
    ),
    Case(
        in_data=Lab1Task2Data(
            directory="./samples/sample_3", file_type="MP4", is_recursive=True, depth=5
        ),
        out_data=[],
    ),
]
