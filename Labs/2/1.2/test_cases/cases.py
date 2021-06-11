from dataclasses import dataclass


@dataclass
class Case:
    in_data: object
    out_data: object


@dataclass
class Lab2Task1_2Data:
    file: str


cases = [
    Case(
        in_data=Lab2Task1_2Data(file="./samples/sample_1.html"),
        out_data="1615235079.1f66445de254c883a733e89e1b57fee220db6828b41fa2327eafd4e94af57eec",
    ),
    Case(
        in_data=Lab2Task1_2Data(file="./samples/sample_2.html"),
        out_data="1615235184.40abe17e6ba2b52fabd4e7e988bcf0f89e42395a9b36127a4ac1a1097ad8668f",
    ),
    Case(
        in_data=Lab2Task1_2Data(file="./samples/sample_3.html"),
        out_data="1615235243.1d5158cf056e4b5f6e668c6a655bca84732dfec5768c39ba965ab21dc0ba29a2",
    ),
]
