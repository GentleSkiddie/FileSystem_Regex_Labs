from dataclasses import dataclass


@dataclass
class Case:
    in_data: object
    out_data: object


@dataclass
class Lab1Task4Data:
    directory: str
    size: int
    is_recursive: bool
    is_greater: bool
    is_sorted: bool


cases = [
    Case(
        in_data=Lab1Task4Data(
            directory="./samples/sample_0",
            size=1024,
            is_recursive=True,
            is_greater=True,
            is_sorted=False,
        ),
        out_data=[
            ("./samples/sample_0/27c95a", 29790),
            ("./samples/sample_0/455c22", 9592),
            ("./samples/sample_0/4d4bbf", 13716),
            ("./samples/sample_0/58adc5/023ba9", 29686),
            ("./samples/sample_0/58adc5/231fef", 20583),
            ("./samples/sample_0/58adc5/5b73c6", 16460),
            ("./samples/sample_0/58adc5/ad60a3", 33888),
            ("./samples/sample_0/5a5421/5911b8", 30506),
            ("./samples/sample_0/5a5421/d6c166", 14353),
            ("./samples/sample_0/825fe5/1d0c20", 38392),
            ("./samples/sample_0/825fe5/37f173", 36395),
            ("./samples/sample_0/825fe5/3d5625/0e29fe", 30372),
            ("./samples/sample_0/825fe5/3d5625/14a614", 37286),
            ("./samples/sample_0/825fe5/3d5625/36879d", 36053),
            ("./samples/sample_0/825fe5/3d5625/371105", 24223),
            ("./samples/sample_0/825fe5/3d5625/39e9ed", 24741),
            ("./samples/sample_0/825fe5/3d5625/670353", 34478),
            ("./samples/sample_0/825fe5/3d5625/af5370", 18951),
            ("./samples/sample_0/825fe5/3d5625/b73ec1", 9691),
            ("./samples/sample_0/825fe5/3d5625/e6efd3", 21406),
            ("./samples/sample_0/825fe5/b0fa27", 13412),
            ("./samples/sample_0/825fe5/cd3afe", 33421),
            ("./samples/sample_0/825fe5/ef5f42", 36071),
            ("./samples/sample_0/b09ffa", 18432),
            ("./samples/sample_0/cad12d", 19504),
            ("./samples/sample_0/d97ed9", 37737),
            ("./samples/sample_0/ee4e0d/00b566", 22675),
            ("./samples/sample_0/ee4e0d/0fd0ac", 24326),
            ("./samples/sample_0/ee4e0d/bb88ca", 23721),
            ("./samples/sample_0/f0b006", 32522),
        ],
    ),
    Case(
        in_data=Lab1Task4Data(
            directory="./samples/sample_0",
            size=15000,
            is_recursive=True,
            is_greater=True,
            is_sorted=True,
        ),
        out_data=[
            ("./samples/sample_0/58adc5/5b73c6", 16460),
            ("./samples/sample_0/b09ffa", 18432),
            ("./samples/sample_0/825fe5/3d5625/af5370", 18951),
            ("./samples/sample_0/cad12d", 19504),
            ("./samples/sample_0/58adc5/231fef", 20583),
            ("./samples/sample_0/825fe5/3d5625/e6efd3", 21406),
            ("./samples/sample_0/ee4e0d/00b566", 22675),
            ("./samples/sample_0/ee4e0d/bb88ca", 23721),
            ("./samples/sample_0/825fe5/3d5625/371105", 24223),
            ("./samples/sample_0/ee4e0d/0fd0ac", 24326),
            ("./samples/sample_0/825fe5/3d5625/39e9ed", 24741),
            ("./samples/sample_0/58adc5/023ba9", 29686),
            ("./samples/sample_0/27c95a", 29790),
            ("./samples/sample_0/825fe5/3d5625/0e29fe", 30372),
            ("./samples/sample_0/5a5421/5911b8", 30506),
            ("./samples/sample_0/f0b006", 32522),
            ("./samples/sample_0/825fe5/cd3afe", 33421),
            ("./samples/sample_0/58adc5/ad60a3", 33888),
            ("./samples/sample_0/825fe5/3d5625/670353", 34478),
            ("./samples/sample_0/825fe5/3d5625/36879d", 36053),
            ("./samples/sample_0/825fe5/ef5f42", 36071),
            ("./samples/sample_0/825fe5/37f173", 36395),
            ("./samples/sample_0/825fe5/3d5625/14a614", 37286),
            ("./samples/sample_0/d97ed9", 37737),
            ("./samples/sample_0/825fe5/1d0c20", 38392),
        ],
    ),
    Case(
        in_data=Lab1Task4Data(
            directory="./samples/sample_1",
            size=16000,
            is_recursive=True,
            is_greater=False,
            is_sorted=True,
        ),
        out_data=[
            ("./samples/sample_1/3eb7ec/a4e74f/8d47bb", 8303),
            ("./samples/sample_1/e0624e/484c50/c5e091", 8346),
            ("./samples/sample_1/cc42f5/80169d/fae8a4", 8398),
            ("./samples/sample_1/e0624e/b6a92d/416927", 8422),
            ("./samples/sample_1/3eb7ec/439dd2/742c9b", 8550),
            ("./samples/sample_1/40375a", 9173),
            ("./samples/sample_1/cc42f5/80169d/f9bcc5", 9447),
            ("./samples/sample_1/e0624e/9e6de4", 9529),
            ("./samples/sample_1/cc42f5/80169d/3b8004", 9659),
            ("./samples/sample_1/e0624e/b6a92d/9a0998/b94a71", 9791),
            ("./samples/sample_1/3eb7ec/991601", 9799),
            ("./samples/sample_1/3eb7ec/a4e74f/1afedf", 10046),
            ("./samples/sample_1/3eb7ec/439dd2/99cc21", 10053),
            ("./samples/sample_1/e0624e/484c50/342ea8", 10290),
            ("./samples/sample_1/e0624e/ea0084", 10554),
            ("./samples/sample_1/cc42f5/80169d/c77da6", 10894),
            ("./samples/sample_1/cc42f5/1a4513/c6fc29", 11293),
            ("./samples/sample_1/e0624e/a2d5ca/49dd14", 11459),
            ("./samples/sample_1/cc42f5/7084f7", 11727),
            ("./samples/sample_1/cc42f5/1a4513/a798ea", 11746),
            ("./samples/sample_1/3eb7ec/a4e74f/c8b7ba", 11866),
            ("./samples/sample_1/e0624e/484c50/04a236", 11930),
            ("./samples/sample_1/e0624e/a2d5ca/ea62a2", 12304),
            ("./samples/sample_1/e0624e/b6a92d/51c875", 12462),
            ("./samples/sample_1/3eb7ec/a4e74f/a261bf", 12502),
            ("./samples/sample_1/bbc0b2/1f07b2", 12718),
            ("./samples/sample_1/bbc0b2/8676b6", 12726),
            ("./samples/sample_1/ffed57", 12910),
            ("./samples/sample_1/b94ab1", 13236),
            ("./samples/sample_1/3eb7ec/d0de8c", 13398),
            ("./samples/sample_1/3eb7ec/e9a62b", 13918),
            ("./samples/sample_1/cc42f5/1a4513/491f05", 14762),
            ("./samples/sample_1/e0624e/a2d5ca/b7cc45", 14806),
            ("./samples/sample_1/cc42f5/bfe7a6", 14830),
            ("./samples/sample_1/e0624e/de8bdb", 15539),
        ],
    ),
    Case(
        in_data=Lab1Task4Data(
            directory="./samples/sample_1",
            size=30000,
            is_recursive=True,
            is_greater=True,
            is_sorted=True,
        ),
        out_data=[
            ("./samples/sample_1/98a757", 30107),
            ("./samples/sample_1/e0624e/16fbe9", 30241),
            ("./samples/sample_1/cc42f5/1a4513/12810d", 30399),
            ("./samples/sample_1/bbc0b2/6551c5", 31265),
            ("./samples/sample_1/e0624e/60b5f3", 32070),
            ("./samples/sample_1/3eb7ec/a4e74f/7f043c", 32978),
            ("./samples/sample_1/cc42f5/80169d/7ed5a9", 33245),
            ("./samples/sample_1/e0624e/b6a92d/9a27a6", 33916),
            ("./samples/sample_1/e0624e/b6a92d/ae735a", 34383),
            ("./samples/sample_1/e0624e/ac3055", 34534),
            ("./samples/sample_1/e0624e/8c4196", 34858),
            ("./samples/sample_1/e0624e/484c50/32aa67", 35014),
            ("./samples/sample_1/3eb7ec/6d3f05", 35077),
            ("./samples/sample_1/e0624e/484c50/ceaf6f", 36642),
            ("./samples/sample_1/3eb7ec/a4e74f/e2d28e", 37638),
            ("./samples/sample_1/cc42f5/1a4513/e92dab", 38071),
            ("./samples/sample_1/e0624e/a2d5ca/f90500", 38125),
            ("./samples/sample_1/cc42f5/80169d/490151", 38378),
            ("./samples/sample_1/cc42f5/1a4513/b80c41", 39624),
            ("./samples/sample_1/e0624e/b6a92d/9a0998/ae3af2", 40351),
        ],
    ),
    Case(
        in_data=Lab1Task4Data(
            directory="./samples/sample_2",
            size=9000,
            is_recursive=True,
            is_greater=False,
            is_sorted=True,
        ),
        out_data=[
            ("./samples/sample_2/b3e752/6bc0be/55cd88/c153c0/294f9c/4cd5a7", 8284),
            ("./samples/sample_2/b3e752/6bc0be/5d045f/651a9a", 8365),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/dc8f6c/4d72a1", 8379),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/d6bd97", 8453),
            ("./samples/sample_2/b3e752/6bc0be/f36fdc/650971", 8453),
            ("./samples/sample_2/b3e752/6bc0be/f36fdc/d6d9c6", 8496),
            ("./samples/sample_2/b3e752/8f2739", 8659),
            ("./samples/sample_2/b3e752/6bc0be/55cd88/91747c/8ad78b", 8803),
            ("./samples/sample_2/b3e752/6bc0be/5d045f/ae6e0c", 8849),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/dc8f6c/5a9d4c/ec17dd", 8894),
            ("./samples/sample_2/b3e752/6bc0be/55cd88/0de878", 8923),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/923d9a", 8926),
        ],
    ),
    Case(
        in_data=Lab1Task4Data(
            directory="./samples/sample_2",
            size=20000,
            is_recursive=True,
            is_greater=True,
            is_sorted=False,
        ),
        out_data=[
            ("./samples/sample_2/11ae89/a782e6", 25166),
            ("./samples/sample_2/11ae89/a7af27", 35979),
            ("./samples/sample_2/11ae89/d28c6e", 33688),
            ("./samples/sample_2/175168", 21581),
            ("./samples/sample_2/1fe86c", 34998),
            ("./samples/sample_2/294057", 37802),
            ("./samples/sample_2/85829a", 38168),
            ("./samples/sample_2/8dd82e", 24077),
            ("./samples/sample_2/b3e752/1cbae1", 20553),
            ("./samples/sample_2/b3e752/1dcd2a", 23422),
            ("./samples/sample_2/b3e752/49f6d4", 34658),
            ("./samples/sample_2/b3e752/6bc0be/051fd9", 20473),
            ("./samples/sample_2/b3e752/6bc0be/0df26b", 38032),
            ("./samples/sample_2/b3e752/6bc0be/166df0", 35759),
            ("./samples/sample_2/b3e752/6bc0be/1c0362", 31639),
            ("./samples/sample_2/b3e752/6bc0be/55cd88/664b86", 21295),
            ("./samples/sample_2/b3e752/6bc0be/55cd88/790599", 32492),
            ("./samples/sample_2/b3e752/6bc0be/55cd88/91747c/141a6d", 31906),
            ("./samples/sample_2/b3e752/6bc0be/55cd88/91747c/90fc51", 25514),
            ("./samples/sample_2/b3e752/6bc0be/55cd88/91747c/921e4a", 33118),
            ("./samples/sample_2/b3e752/6bc0be/55cd88/91747c/ba8fcb", 38294),
            ("./samples/sample_2/b3e752/6bc0be/55cd88/91747c/bc215b", 28037),
            ("./samples/sample_2/b3e752/6bc0be/55cd88/91747c/bf295b", 20096),
            ("./samples/sample_2/b3e752/6bc0be/55cd88/91747c/cc16ea", 37511),
            ("./samples/sample_2/b3e752/6bc0be/55cd88/91747c/ec286a/143395", 36811),
            ("./samples/sample_2/b3e752/6bc0be/55cd88/91747c/ec286a/5c96cf", 40309),
            ("./samples/sample_2/b3e752/6bc0be/55cd88/91747c/ec286a/7b727d", 27842),
            ("./samples/sample_2/b3e752/6bc0be/55cd88/91747c/ec286a/96c875", 35209),
            ("./samples/sample_2/b3e752/6bc0be/55cd88/91747c/ec286a/c55498", 21781),
            (
                "./samples/sample_2/b3e752/6bc0be/55cd88/91747c/ec286a/ce4895/211d4c",
                36102,
            ),
            (
                "./samples/sample_2/b3e752/6bc0be/55cd88/91747c/ec286a/ce4895/35352a",
                24263,
            ),
            (
                "./samples/sample_2/b3e752/6bc0be/55cd88/91747c/ec286a/ce4895/440fce",
                23953,
            ),
            (
                "./samples/sample_2/b3e752/6bc0be/55cd88/91747c/ec286a/ce4895/6bdb55",
                29463,
            ),
            (
                "./samples/sample_2/b3e752/6bc0be/55cd88/91747c/ec286a/ce4895/7e6f65",
                38522,
            ),
            (
                "./samples/sample_2/b3e752/6bc0be/55cd88/91747c/ec286a/ce4895/817599",
                27016,
            ),
            (
                "./samples/sample_2/b3e752/6bc0be/55cd88/91747c/ec286a/ce4895/fa1be8",
                23393,
            ),
            ("./samples/sample_2/b3e752/6bc0be/55cd88/91747c/ec286a/eb7f73", 34727),
            ("./samples/sample_2/b3e752/6bc0be/55cd88/91747c/ec286a/f88072", 30491),
            ("./samples/sample_2/b3e752/6bc0be/55cd88/ac4fa7", 25471),
            ("./samples/sample_2/b3e752/6bc0be/55cd88/c153c0/06ae87", 31262),
            ("./samples/sample_2/b3e752/6bc0be/55cd88/c153c0/294f9c/174632", 32179),
            ("./samples/sample_2/b3e752/6bc0be/55cd88/c153c0/294f9c/1bf72b", 22448),
            ("./samples/sample_2/b3e752/6bc0be/55cd88/c153c0/294f9c/46d5d4", 22283),
            ("./samples/sample_2/b3e752/6bc0be/55cd88/c153c0/294f9c/8e0ffd", 29422),
            ("./samples/sample_2/b3e752/6bc0be/55cd88/c153c0/294f9c/a41bc0", 21945),
            ("./samples/sample_2/b3e752/6bc0be/55cd88/c153c0/294f9c/ad3acb", 27234),
            ("./samples/sample_2/b3e752/6bc0be/55cd88/c153c0/294f9c/b02c1f", 25095),
            ("./samples/sample_2/b3e752/6bc0be/55cd88/c153c0/294f9c/d30533", 35350),
            ("./samples/sample_2/b3e752/6bc0be/55cd88/c153c0/74fc05", 37702),
            ("./samples/sample_2/b3e752/6bc0be/55cd88/c153c0/7710f5", 33360),
            ("./samples/sample_2/b3e752/6bc0be/55cd88/c153c0/7ab649", 24231),
            ("./samples/sample_2/b3e752/6bc0be/55cd88/c153c0/7f4683", 27283),
            ("./samples/sample_2/b3e752/6bc0be/55cd88/c153c0/982232", 22726),
            ("./samples/sample_2/b3e752/6bc0be/55cd88/c153c0/a04af7", 40294),
            ("./samples/sample_2/b3e752/6bc0be/55cd88/c153c0/ca04a5", 37602),
            ("./samples/sample_2/b3e752/6bc0be/55cd88/c153c0/d18c25", 24519),
            ("./samples/sample_2/b3e752/6bc0be/55cd88/c153c0/ff0e7a", 37162),
            ("./samples/sample_2/b3e752/6bc0be/5d045f/074f93/1cc504", 30799),
            ("./samples/sample_2/b3e752/6bc0be/5d045f/074f93/1f27b9", 25234),
            ("./samples/sample_2/b3e752/6bc0be/5d045f/5bc108", 35772),
            ("./samples/sample_2/b3e752/6bc0be/5d045f/5c2421", 27193),
            ("./samples/sample_2/b3e752/6bc0be/5d045f/73ffde", 25006),
            ("./samples/sample_2/b3e752/6bc0be/5d045f/8280d3", 36009),
            ("./samples/sample_2/b3e752/6bc0be/5d045f/8adff8", 28838),
            ("./samples/sample_2/b3e752/6bc0be/5d045f/c41333", 28883),
            ("./samples/sample_2/b3e752/6bc0be/5d045f/e53545", 28579),
            ("./samples/sample_2/b3e752/6bc0be/5d045f/ef7373", 34220),
            ("./samples/sample_2/b3e752/6bc0be/62bb73", 32463),
            ("./samples/sample_2/b3e752/6bc0be/7ae314", 35687),
            ("./samples/sample_2/b3e752/6bc0be/9969ae", 32150),
            ("./samples/sample_2/b3e752/6bc0be/9bd84e", 26906),
            ("./samples/sample_2/b3e752/6bc0be/a06c76/3a7c66", 30030),
            ("./samples/sample_2/b3e752/6bc0be/a06c76/6bca10", 28338),
            ("./samples/sample_2/b3e752/6bc0be/a06c76/9b18b0", 37725),
            ("./samples/sample_2/b3e752/6bc0be/a06c76/a1b315", 30898),
            ("./samples/sample_2/b3e752/6bc0be/a06c76/e30ae8", 30630),
            ("./samples/sample_2/b3e752/6bc0be/a06c76/f3648c", 38869),
            ("./samples/sample_2/b3e752/6bc0be/c12e82/1b0a66", 21657),
            ("./samples/sample_2/b3e752/6bc0be/c12e82/2ac869", 20496),
            ("./samples/sample_2/b3e752/6bc0be/c12e82/389264", 37085),
            ("./samples/sample_2/b3e752/6bc0be/c12e82/5899d0", 22459),
            ("./samples/sample_2/b3e752/6bc0be/c12e82/668abe", 36140),
            ("./samples/sample_2/b3e752/6bc0be/c12e82/6827c7", 37734),
            ("./samples/sample_2/b3e752/6bc0be/c12e82/6a3f8e", 24161),
            ("./samples/sample_2/b3e752/6bc0be/c12e82/78be7c", 27661),
            ("./samples/sample_2/b3e752/6bc0be/c12e82/b3659d", 30150),
            ("./samples/sample_2/b3e752/6bc0be/c12e82/b551e1", 34961),
            ("./samples/sample_2/b3e752/6bc0be/c12e82/d7a435", 40256),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/25d625", 25160),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/3d31b2/01b59a", 23789),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/3d31b2/064f64", 25145),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/3d31b2/0b0672", 26036),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/3d31b2/a5702e", 35108),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/3d31b2/e3b2fe", 20007),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/3d31b2/fd67c4", 29615),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/59201c", 37633),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/5ff81e", 33572),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/6f0dec", 38153),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/78b23b/00c4e0", 20822),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/78b23b/1bae82", 33254),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/78b23b/3657be", 34886),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/78b23b/3b291e", 26410),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/78b23b/53cd41", 38314),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/78b23b/a7667b", 22284),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/78b23b/c4f825", 35404),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/78b23b/e7e2d7", 40758),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/78b23b/fcdfb5", 35859),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/94041a", 38533),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/c2e754", 25243),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/c49533", 22261),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/dc8f6c/23b92d", 39694),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/dc8f6c/30c4cd", 40899),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/dc8f6c/5a9d4c/4df480", 32391),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/dc8f6c/5a9d4c/9395e5", 21981),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/dc8f6c/5a9d4c/93a2eb", 20361),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/dc8f6c/5a9d4c/b08d28", 36725),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/dc8f6c/5a9d4c/ba5297", 22518),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/dc8f6c/5a9d4c/bdea48", 35175),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/dc8f6c/617dc5", 21806),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/dc8f6c/72b99c", 39492),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/dc8f6c/7c9f6f", 32832),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/dc8f6c/88e59e", 32597),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/dc8f6c/98d3a6", 37732),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/dc8f6c/98ff66", 27552),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/dc8f6c/9ff7dd", 36499),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/dc8f6c/a39fab", 38353),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/dc8f6c/bd741e", 35746),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/dc8f6c/c7e2e8", 26598),
            ("./samples/sample_2/b3e752/6bc0be/dd956c/ec3c99", 36681),
            ("./samples/sample_2/b3e752/6bc0be/f36fdc/0836b7", 25943),
            ("./samples/sample_2/b3e752/6bc0be/f36fdc/4c6eba", 23743),
            ("./samples/sample_2/b3e752/6bc0be/f36fdc/71f61e", 28355),
            ("./samples/sample_2/b3e752/6bc0be/f36fdc/b5db5d", 26014),
            ("./samples/sample_2/b3e752/6bc0be/f4d377", 27130),
            ("./samples/sample_2/b3e752/b7c8ba", 30937),
            ("./samples/sample_2/b3e752/bca98a", 21662),
            ("./samples/sample_2/b47642", 38576),
            ("./samples/sample_2/b9b6c3/00d999", 35383),
            ("./samples/sample_2/b9b6c3/050949/0920d6", 26918),
            ("./samples/sample_2/b9b6c3/050949/25878e", 40903),
            ("./samples/sample_2/b9b6c3/050949/8cd1da", 22119),
            ("./samples/sample_2/b9b6c3/050949/8d90e3", 40345),
            ("./samples/sample_2/b9b6c3/050949/cb15d7", 38772),
            ("./samples/sample_2/b9b6c3/08546a", 35037),
            ("./samples/sample_2/b9b6c3/10f137", 37686),
            ("./samples/sample_2/b9b6c3/6e5f73", 24844),
            ("./samples/sample_2/b9b6c3/6e67f5", 32415),
            ("./samples/sample_2/b9b6c3/72560d", 27142),
            ("./samples/sample_2/b9b6c3/a0ca2b/101c9f", 20361),
            ("./samples/sample_2/b9b6c3/a0ca2b/13c571", 30049),
            ("./samples/sample_2/b9b6c3/a0ca2b/26b542/112c55", 22500),
            ("./samples/sample_2/b9b6c3/a0ca2b/26b542/117014", 20697),
            ("./samples/sample_2/b9b6c3/a0ca2b/26b542/4d2fe7", 30530),
            ("./samples/sample_2/b9b6c3/a0ca2b/26b542/5199d9", 21611),
            ("./samples/sample_2/b9b6c3/a0ca2b/26b542/536eec", 39338),
            ("./samples/sample_2/b9b6c3/a0ca2b/26b542/61d96b", 20029),
            ("./samples/sample_2/b9b6c3/a0ca2b/26b542/76efb0", 38200),
            ("./samples/sample_2/b9b6c3/a0ca2b/26b542/7dbfe1", 32541),
            ("./samples/sample_2/b9b6c3/a0ca2b/26b542/a484af", 26834),
            ("./samples/sample_2/b9b6c3/a0ca2b/26b542/f1a47f", 40149),
            ("./samples/sample_2/b9b6c3/a0ca2b/329ced", 25556),
            ("./samples/sample_2/b9b6c3/a0ca2b/5621a4", 32757),
            ("./samples/sample_2/b9b6c3/a0ca2b/80cfba", 30946),
            ("./samples/sample_2/b9b6c3/a0ca2b/b7f7d9", 28095),
            ("./samples/sample_2/b9b6c3/c5399f", 28042),
            ("./samples/sample_2/b9b6c3/c73359", 35530),
            ("./samples/sample_2/b9b6c3/edae86", 27752),
            ("./samples/sample_2/c05e4c", 20064),
            ("./samples/sample_2/c19e9a/a9f49c", 39321),
            ("./samples/sample_2/c19e9a/b2a31f", 26179),
            ("./samples/sample_2/c19e9a/bd558a", 24959),
            ("./samples/sample_2/c19e9a/d44f27", 35686),
            ("./samples/sample_2/c19e9a/da4889", 26790),
            ("./samples/sample_2/c19e9a/e65453", 21981),
            ("./samples/sample_2/c19e9a/f1f28a", 30182),
            ("./samples/sample_2/ca4318", 37523),
            ("./samples/sample_2/eb3291/1b3797", 21897),
            ("./samples/sample_2/eb3291/23e3ec", 23305),
            ("./samples/sample_2/eb3291/44c8d4", 32650),
            ("./samples/sample_2/eb3291/58a965", 39564),
            ("./samples/sample_2/eb3291/5fe420", 35417),
            ("./samples/sample_2/eb3291/615efc", 21811),
            ("./samples/sample_2/eb3291/6f9ae4", 37918),
            ("./samples/sample_2/eb3291/bcfed8", 20988),
            ("./samples/sample_2/eb3291/ec5286", 32215),
            ("./samples/sample_2/ebc114", 37395),
            ("./samples/sample_2/ef1661", 26054),
            ("./samples/sample_2/f0c553", 33963),
        ],
    ),
    Case(
        in_data=Lab1Task4Data(
            directory="./samples/sample_3",
            size=35000,
            is_recursive=True,
            is_greater=True,
            is_sorted=True,
        ),
        out_data=[
            ("./samples/sample_3/2f8f21/f667a4/eb3aff/cd0615", 36588),
            ("./samples/sample_3/4d8308/af8be9/f48ca2", 36909),
            ("./samples/sample_3/4d8308/af8be9/99ac3e", 39006),
            ("./samples/sample_3/2f8f21/f667a4/f09464", 40427),
        ],
    ),
    Case(
        in_data=Lab1Task4Data(
            directory="./samples/sample_3",
            size=1000,
            is_recursive=True,
            is_greater=False,
            is_sorted=True,
        ),
        out_data=[],
    ),
]
