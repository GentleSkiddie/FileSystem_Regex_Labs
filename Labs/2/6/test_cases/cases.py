from dataclasses import dataclass


@dataclass
class Case:
    in_data: object
    out_data: object


@dataclass
class Lab2Task6Data:
    string: str


cases = [
    Case(in_data=Lab2Task6Data(string="johg12@13@mail.com"), out_data=False),
    Case(in_data=Lab2Task6Data(string="jackson@gui-ls.com"), out_data=True),
    Case(in_data=Lab2Task6Data(string="7&s2^2@ggg.c"), out_data=True),
    Case(in_data=Lab2Task6Data(string="$421SdZ8*@qmza.qw"), out_data=True),
    Case(in_data=Lab2Task6Data(string="%s_sda-12_-2c()@mndw.com"), out_data=True),
    Case(in_data=Lab2Task6Data(string="84753@2246.114"), out_data=True),
    Case(in_data=Lab2Task6Data(string="husq,@qeqwe.mu"), out_data=False),
    Case(in_data=Lab2Task6Data(string="h@sdqw.sq"), out_data=True),
    Case(in_data=Lab2Task6Data(string="qqqq@qqq.qq.qq.qq"), out_data=True),
    Case(in_data=Lab2Task6Data(string="mixture_bBl2##@mawl.smq"), out_data=True),
    Case(in_data=Lab2Task6Data(string="email.example.com"), out_data=False),
    Case(in_data=Lab2Task6Data(string="Abc..123@example.com"), out_data=False),
    Case(in_data=Lab2Task6Data(string="あいうえお@example.com"), out_data=False),
    Case(in_data=Lab2Task6Data(string=".email@example.com"), out_data=False),
    Case(in_data=Lab2Task6Data(string="Joe Smith <email@example.com>"), out_data=False),
    Case(in_data=Lab2Task6Data(string="plainaddr"), out_data=False),
    Case(
        in_data=Lab2Task6Data(string='this\ is"really"not\allowed@example.com'),
        out_data=False,
    ),
    Case(in_data=Lab2Task6Data(string="_______@example.com"), out_data=True),
    Case(in_data=Lab2Task6Data(string="email@[123.123.123.123]"), out_data=True),
    Case(in_data=Lab2Task6Data(string="firstname+lastname@example.com"), out_data=True),
    Case(
        in_data=Lab2Task6Data(string='a"b(c)d,e:f;g<h>i[j\k]l@example.com'),
        out_data=False,
    ),
    Case(in_data=Lab2Task6Data(string="john.doe@example..com"), out_data=False),
    Case(in_data=Lab2Task6Data(string="#@%^%#$@#$@#.com"), out_data=False),
    Case(in_data=Lab2Task6Data(string="@example.com"), out_data=False),
    Case(in_data=Lab2Task6Data(string="email@domain"), out_data=True),
]
