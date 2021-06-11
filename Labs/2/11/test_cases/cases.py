from dataclasses import dataclass


@dataclass
class Case:
    in_data: object
    out_data: object


@dataclass
class Lab2Task11Data:
    string: str


cases = [
    Case(
        in_data=Lab2Task11Data(string="This is already a valid sentence."),
        out_data="This is already a valid sentence.",
    ),
    Case(in_data=Lab2Task11Data(string="Extra  spaces"), out_data="Extra spaces"),
    Case(
        in_data=Lab2Task11Data(string="Multiple  extra  spaces"),
        out_data="Multiple extra spaces",
    ),
    Case(in_data=Lab2Task11Data(string="Tab	here"), out_data="Tab here"),
    Case(
        in_data=Lab2Task11Data(string="Multiple	tabs	here"),
        out_data="Multiple tabs here",
    ),
    Case(in_data=Lab2Task11Data(string="Tab	and  spaces"), out_data="Tab and spaces"),
    Case(in_data=Lab2Task11Data(string="Multiple		tabs"), out_data="Multiple tabs"),
    Case(
        in_data=Lab2Task11Data(string="Mixed 	 whitespace"), out_data="Mixed whitespace"
    ),
    Case(
        in_data=Lab2Task11Data(string="Sentence. Sentence."),
        out_data="Sentence.  Sentence.",
    ),
    Case(
        in_data=Lab2Task11Data(string="Sentence with words.   Sentence."),
        out_data="Sentence with words.  Sentence.",
    ),
    Case(
        in_data=Lab2Task11Data(string="The  quick brown fox. 	Jumped."),
        out_data="The quick brown fox.  Jumped.",
    ),
    Case(
        in_data=Lab2Task11Data(string="There  are 1.2 apples"),
        out_data="There are 1.2 apples",
    ),
]