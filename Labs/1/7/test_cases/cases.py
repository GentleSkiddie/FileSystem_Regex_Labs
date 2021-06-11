from dataclasses import dataclass


@dataclass
class Case:
    in_data: object
    out_data: object


@dataclass
class Lab1Task7Data:
    number: int


cases = [
    Case(in_data=Lab1Task7Data(number=0), out_data=0),
    Case(in_data=Lab1Task7Data(number=2), out_data=1),
    Case(in_data=Lab1Task7Data(number=8), out_data=21),
    Case(in_data=Lab1Task7Data(number=16), out_data=987),
    Case(in_data=Lab1Task7Data(number=25), out_data=75025),
    Case(in_data=Lab1Task7Data(number=48), out_data=4807526976),
    Case(in_data=Lab1Task7Data(number=59), out_data=956722026041),
    Case(in_data=Lab1Task7Data(number=65), out_data=17167680177565),
    Case(in_data=Lab1Task7Data(number=69), out_data=117669030460994),
    Case(in_data=Lab1Task7Data(number=75), out_data=2111485077978050),
    Case(in_data=Lab1Task7Data(number=97), out_data=83621143489848422977),
    Case(in_data=Lab1Task7Data(number=111), out_data=70492524767089125814114),
    Case(in_data=Lab1Task7Data(number=135), out_data=7308805952221443105020355490),
    Case(
        in_data=Lab1Task7Data(number=172), out_data=394810887814999156320699623170776339
    ),
    Case(
        in_data=Lab1Task7Data(number=190),
        out_data=2281217241465037496128651402858212007295,
    ),
    Case(
        in_data=Lab1Task7Data(number=241),
        out_data=103881042195729914708510518382775401680142036775841,
    ),
]
