from dataclasses import dataclass


@dataclass
class Case:
    in_data: object
    out_data: object


@dataclass
class Lab1Task9Data:
    number: int


cases = [
    Case(in_data=Lab1Task9Data(number=151), out_data=True),
    Case(in_data=Lab1Task9Data(number=19993), out_data=True),
    Case(in_data=Lab1Task9Data(number=6839173339), out_data=True),
    Case(in_data=Lab1Task9Data(number=28251843748842207541), out_data=True),
    Case(in_data=Lab1Task9Data(number=58276022592390065376989385227699), out_data=True),
    Case(
        in_data=Lab1Task9Data(number=232598445246209015829952532809142647),
        out_data=True,
    ),
    Case(
        in_data=Lab1Task9Data(number=713019000412558814392746479174018145548191),
        out_data=True,
    ),
    Case(
        in_data=Lab1Task9Data(
            number=9396045243493404208994323153685265000648837637599552809
        ),
        out_data=True,
    ),
    Case(in_data=Lab1Task9Data(number=1234567), out_data=False),
    Case(in_data=Lab1Task9Data(number=8746962179), out_data=False),
    Case(in_data=Lab1Task9Data(number=259874652254138), out_data=False),
    Case(in_data=Lab1Task9Data(number=4125974236945058069), out_data=False),
    Case(in_data=Lab1Task9Data(number=548962145099870899124697267897), out_data=False),
    Case(
        in_data=Lab1Task9Data(
            number=789321455965742688412548632100598896321894685201147897
        ),
        out_data=False,
    ),
    Case(
        in_data=Lab1Task9Data(
            number=987009704961456983220569782206658702459698220459208609734697397
        ),
        out_data=False,
    ),
]