from dataclasses import dataclass


@dataclass
class Case:
    in_data: object
    out_data: object


@dataclass
class Lab1Task5Data:
    directory: str
    date: str
    is_recursive: bool
    is_newer: bool
    is_sorted: bool


cases = [
    Case(
        in_data=Lab1Task5Data(
            directory="./samples/sample_0",
            date="12 01 2016",
            is_recursive=True,
            is_newer=False,
            is_sorted=False,
        ),
        out_data=[
            ("./samples/sample_0/27c95a", "6 6 1991"),
            ("./samples/sample_0/455c22", "10 4 2003"),
            ("./samples/sample_0/4d4bbf", "13 7 2011"),
            ("./samples/sample_0/58adc5/231fef", "11 11 2005"),
            ("./samples/sample_0/58adc5/5b73c6", "2 2 2007"),
            ("./samples/sample_0/58adc5/ad60a3", "23 9 2008"),
            ("./samples/sample_0/5a5421/5911b8", "2 5 2002"),
            ("./samples/sample_0/5a5421/d6c166", "10 8 1998"),
            ("./samples/sample_0/825fe5/1d0c20", "22 4 1993"),
            ("./samples/sample_0/825fe5/3d5625/0e29fe", "31 3 2008"),
            ("./samples/sample_0/825fe5/3d5625/14a614", "20 8 2009"),
            ("./samples/sample_0/825fe5/3d5625/36879d", "14 12 2013"),
            ("./samples/sample_0/825fe5/3d5625/371105", "11 4 2003"),
            ("./samples/sample_0/825fe5/3d5625/39e9ed", "10 5 2004"),
            ("./samples/sample_0/825fe5/3d5625/670353", "21 7 2002"),
            ("./samples/sample_0/825fe5/3d5625/af5370", "12 5 2001"),
            ("./samples/sample_0/825fe5/3d5625/b73ec1", "8 6 2011"),
            ("./samples/sample_0/825fe5/3d5625/e6efd3", "9 7 2004"),
            ("./samples/sample_0/825fe5/ef5f42", "25 5 1993"),
            ("./samples/sample_0/b09ffa", "28 7 1993"),
            ("./samples/sample_0/d97ed9", "29 5 1996"),
            ("./samples/sample_0/ee4e0d/0fd0ac", "2 10 2012"),
            ("./samples/sample_0/ee4e0d/bb88ca", "27 5 1991"),
        ],
    ),
    Case(
        in_data=Lab1Task5Data(
            directory="./samples/sample_0",
            date="16 12 2018",
            is_recursive=True,
            is_newer=True,
            is_sorted=True,
        ),
        out_data=[
            ("./samples/sample_0/825fe5/cd3afe", "23 5 2019"),
            ("./samples/sample_0/825fe5/b0fa27", "2 12 2019"),
            ("./samples/sample_0/cad12d", "2 6 2020"),
            ("./samples/sample_0/f0b006", "5 6 2020"),
            ("./samples/sample_0/58adc5/023ba9", "1 10 2020"),
            ("./samples/sample_0/825fe5/37f173", "19 2 2021"),
        ],
    ),
    Case(
        in_data=Lab1Task5Data(
            directory="./samples/sample_1",
            date="01 01 2006",
            is_recursive=True,
            is_newer=False,
            is_sorted=True,
        ),
        out_data=[
            ("./samples/sample_1/f8c2f7", "27 6 1991"),
            ("./samples/sample_1/e0624e/ea0084", "13 8 1991"),
            ("./samples/sample_1/e0624e/484c50/c5e091", "19 10 1991"),
            ("./samples/sample_1/e0624e/b6a92d/9a0998/b8492a", "23 11 1991"),
            ("./samples/sample_1/e0624e/026946", "8 1 1992"),
            ("./samples/sample_1/e0624e/b6a92d/2ec1de", "13 3 1992"),
            ("./samples/sample_1/e0624e/484c50/658c44", "15 4 1992"),
            ("./samples/sample_1/e0624e/a2d5ca/b7cc45", "24 7 1992"),
            ("./samples/sample_1/bbc0b2/3ad0ab", "1 11 1992"),
            ("./samples/sample_1/bbc0b2/6551c5", "24 11 1992"),
            ("./samples/sample_1/98a757", "6 2 1993"),
            ("./samples/sample_1/e0624e/484c50/db8d9e", "18 4 1993"),
            ("./samples/sample_1/3eb7ec/e9a62b", "20 10 1993"),
            ("./samples/sample_1/cc42f5/1a4513/491f05", "16 11 1993"),
            ("./samples/sample_1/e0624e/a2d5ca/49dd14", "7 2 1994"),
            ("./samples/sample_1/3eb7ec/a4e74f/8d47bb", "13 11 1994"),
            ("./samples/sample_1/e0624e/a2d5ca/523a42", "6 12 1994"),
            ("./samples/sample_1/e0624e/484c50/28f726", "17 5 1995"),
            ("./samples/sample_1/cc42f5/1a4513/a798ea", "24 7 1995"),
            ("./samples/sample_1/3eb7ec/991601", "16 11 1995"),
            ("./samples/sample_1/e0624e/b1a929", "21 11 1995"),
            ("./samples/sample_1/e0624e/b6a92d/5f3801", "19 8 1996"),
            ("./samples/sample_1/393970", "8 10 1996"),
            ("./samples/sample_1/e0624e/9e6de4", "24 11 1996"),
            ("./samples/sample_1/e0624e/484c50/342ea8", "12 2 1997"),
            ("./samples/sample_1/cc42f5/e00973", "27 3 1998"),
            ("./samples/sample_1/bbc0b2/50f519", "20 4 1998"),
            ("./samples/sample_1/3eb7ec/6d3f05", "14 5 1998"),
            ("./samples/sample_1/e0624e/60b5f3", "11 6 1998"),
            ("./samples/sample_1/cc42f5/1a4513/b80c41", "24 7 1998"),
            ("./samples/sample_1/3eb7ec/a4e74f/c8b7ba", "30 7 1998"),
            ("./samples/sample_1/e0624e/484c50/32aa67", "21 11 1998"),
            ("./samples/sample_1/e0624e/b6a92d/9a27a6", "27 6 2000"),
            ("./samples/sample_1/cc42f5/1a4513/12810d", "15 7 2000"),
            ("./samples/sample_1/e0624e/a2d5ca/f90500", "14 9 2001"),
            ("./samples/sample_1/cc42f5/7084f7", "6 11 2001"),
            ("./samples/sample_1/e0624e/484c50/ceaf6f", "28 4 2002"),
            ("./samples/sample_1/cc42f5/80169d/3b8004", "28 9 2002"),
            ("./samples/sample_1/cc42f5/80169d/f9bcc5", "10 1 2003"),
            ("./samples/sample_1/3eb7ec/439dd2/742c9b", "15 2 2003"),
            ("./samples/sample_1/cc42f5/e97693", "19 11 2003"),
            ("./samples/sample_1/3eb7ec/a4e74f/a261bf", "11 2 2004"),
            ("./samples/sample_1/e0624e/b6a92d/9a0998/8c22be", "14 4 2004"),
            ("./samples/sample_1/e0624e/b6a92d/9a0998/ae3af2", "11 12 2004"),
            ("./samples/sample_1/3eb7ec/a4e74f/1afedf", "13 8 2005"),
            ("./samples/sample_1/e0624e/de498d", "1 11 2005"),
        ],
    ),
    Case(
        in_data=Lab1Task5Data(
            directory="./samples/sample_1",
            date="25 09 2012",
            is_recursive=True,
            is_newer=True,
            is_sorted=True,
        ),
        out_data=[
            ("./samples/sample_1/e0624e/6eaa6b", "18 10 2012"),
            ("./samples/sample_1/cc42f5/1a4513/a74f2a", "1 7 2013"),
            ("./samples/sample_1/3eb7ec/a4e74f/8860e4", "9 7 2013"),
            ("./samples/sample_1/cc42f5/80169d/fae8a4", "8 8 2013"),
            ("./samples/sample_1/3eb7ec/0fec55", "30 8 2013"),
            ("./samples/sample_1/e0624e/b6a92d/d4d0e4", "22 4 2014"),
            ("./samples/sample_1/cc42f5/80169d/9e401c", "30 5 2014"),
            ("./samples/sample_1/cc42f5/80169d/490151", "19 11 2014"),
            ("./samples/sample_1/b8aa66", "29 12 2014"),
            ("./samples/sample_1/b94ab1", "3 2 2015"),
            ("./samples/sample_1/e0624e/b6a92d/416927", "5 9 2015"),
            ("./samples/sample_1/cc42f5/1a4513/e92dab", "5 11 2015"),
            ("./samples/sample_1/cc42f5/bfe7a6", "8 1 2016"),
            ("./samples/sample_1/e0624e/484c50/04a236", "20 4 2016"),
            ("./samples/sample_1/ffed57", "21 4 2016"),
            ("./samples/sample_1/e0624e/8c4196", "26 5 2016"),
            ("./samples/sample_1/3eb7ec/439dd2/99cc21", "10 6 2016"),
            ("./samples/sample_1/40375a", "14 9 2016"),
            ("./samples/sample_1/3eb7ec/a4e74f/94642c", "23 11 2016"),
            ("./samples/sample_1/e0624e/b6a92d/306111", "29 12 2016"),
            ("./samples/sample_1/3eb7ec/439dd2/e70d64", "15 8 2017"),
            ("./samples/sample_1/cc42f5/1a4513/af81be", "13 10 2017"),
            ("./samples/sample_1/e0624e/b6a92d/8dc627", "27 11 2017"),
            ("./samples/sample_1/bbc0b2/9e562f", "2 2 2018"),
            ("./samples/sample_1/3eb7ec/a4e74f/b3b284", "17 4 2018"),
            ("./samples/sample_1/cc42f5/80169d/7ed5a9", "1 9 2018"),
            ("./samples/sample_1/e0624e/a2d5ca/ea62a2", "6 7 2019"),
            ("./samples/sample_1/cc42f5/c3775c", "15 7 2019"),
            ("./samples/sample_1/e0624e/b6a92d/9a0998/b94a71", "1 8 2019"),
            ("./samples/sample_1/e0624e/484c50/4f24da", "17 8 2019"),
            ("./samples/sample_1/e0624e/484c50/ac536a", "6 3 2020"),
            ("./samples/sample_1/3eb7ec/439dd2/3eb8a7", "11 5 2020"),
            ("./samples/sample_1/cc42f5/80169d/1914b7", "15 5 2020"),
            ("./samples/sample_1/bbc0b2/1f07b2", "24 6 2020"),
            ("./samples/sample_1/3eb7ec/a4e74f/af3f95", "5 7 2020"),
            ("./samples/sample_1/986e5e", "21 7 2020"),
            ("./samples/sample_1/cc42f5/1a4513/c6fc29", "28 7 2020"),
            ("./samples/sample_1/e0624e/b6a92d/51c875", "9 9 2020"),
        ],
    ),
    Case(
        in_data=Lab1Task5Data(
            directory="./samples/sample_2",
            date="05 07 1999",
            is_recursive=False,
            is_newer=True,
            is_sorted=True,
        ),
        out_data=[
            ("./samples/sample_2/85829a", "28 8 1999"),
            ("./samples/sample_2/b47642", "10 12 1999"),
            ("./samples/sample_2/294057", "22 7 2001"),
            ("./samples/sample_2/175168", "14 11 2002"),
            ("./samples/sample_2/ebc114", "18 5 2010"),
            ("./samples/sample_2/ca4318", "18 4 2017"),
            ("./samples/sample_2/ef1661", "17 6 2018"),
            ("./samples/sample_2/cf5989", "31 7 2018"),
            ("./samples/sample_2/f0c553", "16 8 2020"),
        ],
    ),
    Case(
        in_data=Lab1Task5Data(
            directory="./samples/sample_2",
            date="16 01 2017",
            is_recursive=True,
            is_newer=True,
            is_sorted=True,
        ),
        out_data=[
                (
                    "./samples/sample_2/b3e752/6bc0be/55cd88/c153c0/294f9c/942fde",
                    "24 1 2017",
                ),
                ("./samples/sample_2/ca4318", "18 4 2017"),
                ("./samples/sample_2/b3e752/6bc0be/55cd88/91747c/8ad78b", "6 12 2017"),
                ("./samples/sample_2/eb3291/6f9ae4", "15 1 2018"),
                (
                    "./samples/sample_2/b3e752/6bc0be/55cd88/91747c/ec286a/7b727d",
                    "2 2 2018",
                ),
                ("./samples/sample_2/b3e752/6bc0be/a06c76/3a7c66", "27 5 2018"),
                ("./samples/sample_2/b3e752/6bc0be/55cd88/df19d9", "3 6 2018"),
                ("./samples/sample_2/ef1661", "17 6 2018"),
                ("./samples/sample_2/b9b6c3/a0ca2b/26b542/322c37", "12 7 2018"),
                ("./samples/sample_2/cf5989", "31 7 2018"),
                ("./samples/sample_2/b9b6c3/a0ca2b/80cfba", "12 8 2018"),
                ("./samples/sample_2/eb3291/23e3ec", "15 9 2018"),
                ("./samples/sample_2/b9b6c3/322dc7", "13 1 2019"),
                ("./samples/sample_2/b3e752/1dcd2a", "26 1 2019"),
                ("./samples/sample_2/b3e752/6bc0be/c12e82/5899d0", "11 2 2019"),
                ("./samples/sample_2/b3e752/6bc0be/dd956c/3d31b2/e3b2fe", "6 3 2019"),
                ("./samples/sample_2/b3e752/6bc0be/c12e82/b3659d", "24 3 2019"),
                ("./samples/sample_2/b3e752/6bc0be/5d045f/ae6e0c", "10 5 2019"),
                ("./samples/sample_2/b3e752/6bc0be/dd956c/ec3c99", "10 12 2019"),
                ("./samples/sample_2/11ae89/0ba76e", "20 1 2020"),
                ("./samples/sample_2/eb3291/ec5286", "4 3 2020"),
                ("./samples/sample_2/b3e752/6bc0be/1c0362", "28 3 2020"),
                ("./samples/sample_2/b3e752/6bc0be/a06c76/5b136e", "28 3 2020"),
                ("./samples/sample_2/b3e752/6bc0be/5d045f/5bc108", "6 4 2020"),
                ("./samples/sample_2/b3e752/6bc0be/5d045f/ef7373", "23 4 2020"),
                ("./samples/sample_2/b9b6c3/050949/8d90e3", "2 6 2020"),
                ("./samples/sample_2/f0c553", "16 8 2020"),
                ("./samples/sample_2/b3e752/6bc0be/5d045f/e53545", "19 9 2020"),
                (
                    "./samples/sample_2/b3e752/6bc0be/55cd88/91747c/ec286a/b1404c",
                    "20 9 2020",
                ),
                ("./samples/sample_2/b3e752/6bc0be/dd956c/59201c", "4 10 2020"),
                ("./samples/sample_2/b9b6c3/2d129d", "14 12 2020"),
                ("./samples/sample_2/b3e752/6bc0be/5d045f/074f93/6f7e0b", "29 12 2020"),
                ("./samples/sample_2/b3e752/6bc0be/55cd88/91747c/52ec5f", "16 1 2021"),
                ("./samples/sample_2/b3e752/6bc0be/55cd88/664b86", "17 1 2021"),
                ("./samples/sample_2/11ae89/91b2a1", "21 2 2021"),
        ],
    ),
    Case(
        in_data=Lab1Task5Data(
            directory="./samples/sample_3",
            date="18 01 1985",
            is_recursive=False,
            is_newer=False,
            is_sorted=True,
        ),
        out_data=[],
    ),
    Case(
        in_data=Lab1Task5Data(
            directory="./samples/sample_3",
            date="22 07 2002",
            is_recursive=True,
            is_newer=False,
            is_sorted=True,
        ),
        out_data=[
            ("./samples/sample_3/2f8f21/b768b1/26d624/741725", "23 6 1991"),
            ("./samples/sample_3/4d8308/c5ca1b/650401", "13 6 1996"),
            ("./samples/sample_3/2f8f21/bcff38/1a9eaa/f07674/315ede", "2 2 1999"),
            (
                "./samples/sample_3/2f8f21/bcff38/1a9eaa/d2dbc1/21a136/7078d9",
                "16 6 1999",
            ),
            (
                "./samples/sample_3/3ea92d/1a120e/36f858/0a8a9c/eb87dc/43f9d6/cbafcf",
                "19 6 2000",
            ),
            (
                "./samples/sample_3/3ea92d/1a120e/36f858/0a8a9c/bd77c2/7a57f7",
                "10 11 2001",
            ),
            ("./samples/sample_3/3ea92d/1a120e/36f858/0a8a9c/c57cb5", "30 5 2002"),
        ],
    ),
]