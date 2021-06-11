from dataclasses import dataclass


@dataclass
class Case:
    in_data: object
    out_data: object


@dataclass
class Lab2Task7Data:
    file: str
    language: str


cases = [
    Case(
        in_data=Lab2Task7Data(file="./samples/sample_1.txt", language="ru"),
        out_data=[
            "+7(4976)713994",
            "+7(699)5729308",
            "+7(3557)443581",
            "+7 (2957) 323403",
            "+76823618317",
            "+7(538)7365567",
            "+73409412601",
            "+74905061078",
            "+7(385)3343229",
            "+7 (0341) 364206",
            "+7 (7453) 053390",
            "+7(844)3826359",
            "+71514020090",
            "+77517856832",
            "+7 332 2046856",
            "+7 670 8648792",
            "+7 (4500) 802054",
            "+78564183887",
            "+73388706848",
            "+7 (9908) 559849",
            "+75864429978",
            "+79735406805",
            "+7 518 0157472",
            "+71326076408",
            "+7(932)1543125",
            "+7(441)6606363",
            "+7 (824) 7941690",
            "+7(442)5802423",
            "+7 (4602) 726359",
            "+70627364891",
            "+77474074259",
            "+7(6392)580733",
            "+79262311169",
            "+7 0864 979652",
        ],
    ),
    Case(
        in_data=Lab2Task7Data(file="./samples/sample_2.txt", language="ch"),
        out_data=[
            "+86 305 25154589",
            "+86 (783) 47168198",
            "+86(379)67784254",
            "+86 545 66206053",
            "+86 671 92268037",
            "+8608933097733",
            "+86 563 58563266",
            "+86(234)14334658",
            "+86(904)01011132",
            "+86 141 02075787",
            "+86 433 21452599",
            "+8641405299577",
            "+86 831 23859790",
            "+8687417231998",
            "+86(252)98369008",
            "+86 410 25409203",
            "+86 612 00178261",
            "+86(309)50286128",
            "+86 (336) 90822559",
            "+86 935 67260464",
            "+86(126)49877592",
            "+86(348)44279063",
            "+8637819225108",
            "+86 528 95223578",
            "+8620247193618",
            "+86 621 60873083",
            "+8642078702077",
            "+86 (663) 93114637",
            "+86 334 42350198",
            "+86 702 73319633",
            "+86 046 51355731",
            "+86 543 00632608",
            "+86 (723) 99447478",
            "+8629846751047",
            "+86 661 00050664",
            "+86 984 40527057",
            "+8682397593326",
            "+86 037 04038455",
            "+86(736)10288362",
            "+8634736603077",
            "+86 506 56200173",
            "+86 089 13023308",
            "+86 (053) 83846483",
            "+86 105 61244224",
            "+86(187)56425581",
            "+86 (688) 39165027",
            "+86(049)71236339",
            "+86 (340) 75170315",
            "+86 645 84293988",
            "+8697658071787",
            "+8697570784392",
            "+86 330 51362017",
            "+8622739821442",
            "+86(017)37776970",
            "+86 (261) 76896620",
            "+86(112)78112497",
            "+86(397)06562688",
            "+86 (528) 48108012",
            "+86(573)02922725",
            "+8629223589940",
            "+86 (924) 31204476",
            "+86(304)00307761",
            "+8657744309436",
            "+86(267)84473677",
            "+86 498 92085845",
        ],
    ),
    Case(
        in_data=Lab2Task7Data(file="./samples/sample_3.txt", language="usa"),
        out_data=[
            "+13953975256",
            "+1 077 1398810",
            "+1 (748) 9444078",
            "+1 (241) 4069872",
            "+1 (422) 6743611",
            "+1 (476) 3462628",
            "+14107680575",
            "+1 750 9774320",
            "+1(943)9830324",
            "+1 (978) 3621184",
            "+11366700332",
            "+19279056462",
            "+1(127)1856528",
            "+1 (262) 1891265",
            "+1 691 4430858",
            "+1 (031) 6698499",
            "+1 (075) 7739572",
            "+17420468773",
            "+14492161949",
            "+13586276441",
            "+1 (970) 7107657",
            "+1 (294) 5762935",
            "+1 861 3870352",
            "+1 (585) 7886107",
            "+19851470571",
            "+1 (734) 3318996",
            "+1 (090) 6847918",
            "+10243440905",
            "+1 (496) 3850111",
            "+1(412)9275821",
            "+14563390917",
            "+1(267)0131983",
            "+1(735)4862669",
            "+1 (268) 3044392",
            "+1(957)9069523",
            "+1 970 9928793",
            "+1 (655) 5391359",
            "+1 757 7733211",
            "+1 182 9185439",
            "+12317612404",
            "+17579035612",
            "+1(124)5502527",
            "+1 770 6027112",
            "+1(351)8205929",
            "+1 (991) 9507645",
            "+1 (335) 9414580",
            "+1 (879) 6249906",
            "+1 442 8639535",
            "+1 (327) 8059510",
            "+1 212 1340794",
            "+16408542531",
            "+1 (348) 4265421",
            "+14293338718",
            "+14892703260",
            "+1 097 1004841",
            "+1(873)0679611",
            "+19830418743",
            "+1(715)2890600",
            "+12842895182",
            "+1 (178) 3342785",
            "+15407491563",
            "+18416109850",
            "+1(059)3301792",
            "+1 714 9482226",
            "+1 477 4579016",
            "+1(984)1988110",
            "+1 237 4887613",
            "+1(768)0989324",
            "+1(162)2458796",
            "+1 (998) 0006263",
            "+1 348 8682308",
            "+1(556)3718498",
            "+1(980)3075120",
            "+1 (307) 4125609",
            "+18782891515",
            "+19498100611",
            "+1 619 6621840",
            "+18735777081",
            "+13100077325",
            "+14523182816",
            "+1 848 7458577",
            "+19407126479",
            "+1 (259) 4278145",
            "+1 970 0806630",
            "+1 977 4589829",
            "+16678981653",
        ],
    ),
    Case(
        in_data=Lab2Task7Data(file="./samples/sample_4.txt", language="bel"),
        out_data=[
            "+375 64 3718084",
            "+375(39)7831427",
            "+375 (86) 2770926",
            "+375 (10) 4440413",
            "+375 07 4791834",
            "+375(17)2331621",
            "+375(07)6480067",
            "+375163643406",
            "+375153261484",
            "+375 51 0413166",
            "+375 35 9302858",
            "+375(69)8575225",
            "+375(72)8143077",
            "+375 82 7475161",
            "+375(12)4043335",
            "+375961068238",
            "+375(02)5514937",
            "+375(65)9141833",
            "+375(23)4153388",
            "+375(00)8957646",
            "+375 56 9730825",
            "+375634535829",
            "+375(05)1340946",
            "+375829503953",
            "+375 (84) 5362520",
            "+375 (88) 9672309",
            "+375 (93) 7379316",
            "+375160265978",
            "+375 (41) 5000276",
            "+375 (18) 2747924",
            "+375345155667",
            "+375256272709",
            "+375 (02) 1406506",
            "+375 92 5668644",
            "+375 (09) 7676489",
            "+375581902900",
            "+375(02)2068843",
            "+375(56)3323396",
            "+375747440837",
            "+375 (88) 1464914",
            "+375(49)1723417",
            "+375(37)6380564",
            "+375 27 3780313",
            "+375189817982",
            "+375 (86) 4774169",
            "+375 66 1516966",
            "+375(04)7116118",
            "+375 (46) 2440879",
            "+375 (20) 9205933",
            "+375 (85) 4819146",
            "+375(45)6757502",
            "+375 (51) 7278184",
            "+375(73)4650240",
            "+375 42 4442201",
            "+375 (90) 2921737",
            "+375 (55) 1161535",
            "+375 (61) 4897311",
            "+375 (48) 9835039",
            "+375(64)1922783",
            "+375(99)8699183",
            "+375 64 0954887",
            "+375 76 7059474",
            "+375 90 3151576",
            "+375 31 8670885",
            "+375(20)4871792",
            "+375 50 4619869",
            "+375 42 2274154",
            "+375 (41) 8062606",
        ],
    ),
]