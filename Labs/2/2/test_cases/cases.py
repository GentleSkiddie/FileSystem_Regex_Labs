from dataclasses import dataclass


@dataclass
class Case:
    in_data: object
    out_data: object


@dataclass
class Lab2Task2Data:
    file: str


cases = [
    Case(
        in_data=Lab2Task2Data(file="./samples/sample_1.html"),
        out_data=[
            "/images/menu/small/p10.jpg",
            "/images/flags2/China.png",
            "/images/flags2/Russia.png",
            "/plugins/layerslider/css/blank.gif",
            "/img/edu.svg",
            "/images/slider1/big/p346.jpg",
            "/img/icn/innovation.svg",
            "/img/more-than.svg",
            "/images/flags2/esp.png",
            "https://www.facebook.com/tr?id=979702578718771&amp;ev=PixelInitialized",
            "/images/menu/small/p202.jpg",
            "/img/icn/globe.svg",
            "/images/menu/small/p221.jpg",
            "/images/flags2/United-Kingdom.png",
            "/images/menu/small/p201.jpg",
        ],
    ),
    Case(
        in_data=Lab2Task2Data(file="./samples/sample_2.html"),
        out_data=["/static/img/python-logo.png"],
    ),
    Case(
        in_data=Lab2Task2Data(file="./samples/sample_3.html"),
        out_data=[
            "//static.mvideo.ru/media/Promotions/Promo_Page/2021/March/10-cashback-za-oplaty-online/1/2/stories_S_192%D1%85280.png",
            "//static.mvideo.ru/media/Promotions/Promo_Page/2021/February/mclub/stories_L_312x456.png",
            "//static.mvideo.ru/assets/img/stub.gif",
            "//static.mvideo.ru/media/Promotions/Promo_Page/2021/March/10-cashback-za-oplaty-online/1/2/stories_S_192%D1%85280%20%281%29.png",
            "//static.mvideo.ru/media/Promotions/Promo_Page/2020/December/images/brandinmenu_iRobot_S_208x108.png",
            "//static.mvideo.ru/media/Promotions/Promo_Page/2021/March/bystroservis-na-dva-goda-v-podarok-k-holodilnikam-bosch/stories_L_312x456.png",
            "//static.mvideo.ru/assets/facelift/img/footer/app-store.svg",
            "//static.mvideo.ru/media/SmallBanners/Whirlpool_navigation.png",
            "//static.mvideo.ru/media/SmallBanners/preorders-75х50-2.gif",
            "//static.mvideo.ru/media/SmallBanners/garmin-2.png",
            "//static.mvideo.ru/media/Promotions/Promo_Page/2021/February/chto-podarit-na-prazdnik/banners/igra/stories_L_312x456.png",
            "//static.mvideo.ru/media/Promotions/Promo_Page/2021/January/icon/brandinmenu_brandname_S_208x108.png",
            "//static.mvideo.ru/media/Promotions/Promo_Page/2021/February/vygoda-na-iphone-po-promokodu-wow8/260221/stories_L_312x456.png",
            "//static.mvideo.ru/media/SmallBanners/m-obzory.png",
            "//static.mvideo.ru/media/Promotions/Promo_Page/2020/December/images/brandinmenu_WMF_S_208x108.png",
            "//static.mvideo.ru/media/Promotions/Promo_Page/2021/March/elektrogril-tefal-optigrill-gc712d34-20036881/stories_L_312x456.png",
            "//static.mvideo.ru/media/SmallBanners/75%D1%8550.png",
            "//static.mvideo.ru/media/Promotions/Promo_Page/2021/February/servisnye-centry-apple/stories_L_312x456.png",
            "//static.mvideo.ru/assets/facelift/img/footer/app-google.svg",
            "//static.mvideo.ru/media/Promotions/Promo_Page/2021/March/apple-macbook-air-s-chipom-apple-m1/1003/wide_L_3032x544.png",
            "//static.mvideo.ru/media/Promotions/Promo_Page/2020/September/RP/rassr_new_site/stories_L_312x456.png",
            "//static.mvideo.ru/media/Promotions/Promo_Page/2020/November/ulan-ude/1/Icons/TV_sony.png",
            "//static.mvideo.ru/media/Promotions/Promo_Page/2021/February/ne-zavali-prazdniki/240221/hero_L_2432x720.png",
            "//static.mvideo.ru/media/Promotions/Promo_Page/2021/January/smarthome/stories_L_312x456.png",
            "//static.mvideo.ru/media/SmallBanners/smartphone_icon.png",
            "//static.mvideo.ru/media/Promotions/Promo_Page/2020/November/ulan-ude/1/Icons/Sims.png",
            "//static.mvideo.ru/media/Promotions/Promo_Page/2021/February/skidki-na-posudu-i-tehniky-tefal/stories_L_312x456.png",
            "//static.mvideo.ru/media/Promotions/Promo_Page/2020/November/ulan-ude/1/Icons/Kitchen.png",
            "//static.mvideo.ru/media/SmallBanners/dyson.gif",
            "//static.mvideo.ru/media/Promotions/Promo_Page/2020/December/images/brandinmenu_KitchenAid_S_208x108.png",
            "//static.mvideo.ru/media/Promotions/Promo_Page/2020/November/ulan-ude/1/Icons/M_obzori.png",
            "//static.mvideo.ru/media/Promotions/Promo_Page/2020/November/ulan-ude/1/Icons/TV-8K.png",
            "//static.mvideo.ru/media/Assets/menu/souvenir_logo.png",
            "//img.mvideo.ru/media/Assets/img/new.svg",
            "//static.mvideo.ru/media/SmallBanners/VK%2075%D1%8550.png",
            "//static.mvideo.ru/media/Promotions/Promo_Page/2021/February/skidki-na-skovorody-rondell/stories_L_312x456.png",
            "//static.mvideo.ru/assets/facelift/img/footer/app-gallery.svg",
            "//static.mvideo.ru/media/Promotions/Promo_Page/2020/December/taxi_hub/stories_L_312x456.png",
            "//static.mvideo.ru/media/Promotions/Promo_Page/2021/March/skidki-na-kofe-kapsuli-lor-i-jacobs/stories_L_312x456.png",
            "//static.mvideo.ru/media/Promotions/Promo_Page/2021/February/mobileapp/stories_L_312x456.png",
            "//static.mvideo.ru/media/Promotions/Promo_Page/2020/November/ulan-ude/1/Icons/Miele.png",
            "//static.mvideo.ru/media/Promotions/Promo_Page/2020/November/ulan-ude/1/Icons/SIM_Akcii.png",
            "//static.mvideo.ru/media/Promotions/Promo_Page/2020/December/kofemashiny-delonghi-dinamica/stories_L_312x456.png",
            "//static.mvideo.ru/assets/facelift/img/logo_with_subtext.svg",
            "//static.mvideo.ru/media/Promotions/Promo_Page/2021/February/braun100let/wide_L_3032x544.png",
            "//static.mvideo.ru/media/Promotions/Promo_Page/2021/March/obzor-samsung-galaxy-s21-ultra/stories_L_312x456.png",
            "//static.mvideo.ru/media/Promotions/Promo_Page/2021/March/10-cashback-za-oplaty-online/1/2/stories_S_192%D1%85280%20%282%29.png",
            "//static.mvideo.ru/media/Promotions/Promo_Page/2019/November/avto-ustroistva-neoline/logo.png",
        ],
    ),
    Case(
        in_data=Lab2Task2Data(file="./samples/sample_4.html"),
        out_data=["https://abs.twimg.com/errors/logo46x38.png"],
    ),
    Case(
        in_data=Lab2Task2Data(file="./samples/sample_5.html"),
        out_data=[
            "https://yabs.yandex.ru/count/WFuejI_zO5K0fGS0r0ifB1yh1GpSt0K0LG4nth18O000000useqKy0A-meRx0_050Q061Ca6WeqLbT3PbO2K0tzavvSdZW-g2n15cCft0ty003MPnomjlV0B1k0DWe20G9WEWflMg8cwzie5-13q__y1W17vg170X3tf4Wh6fN_vGVzEy1A8s1N1YlRieu-y_6FmoHRmFu4Ng1S9cHZG627u680Pi1cu6V__0T8P4dbXOdDVSsLoTcLoBt8rC3OjCUWPWC83y1c0mWCI07Ta73C5WuAxAXecqIs4E183ksm9Q9OtL719p1gqHj5OOq0l3FRGpbaeedeukFZsbM6K0G00~1=WMWejI_zOCO0zGe0P1Bg6qoVnW5094W2ODOOSC2QtfJblDtLgG600GcG0QAAzAauc07aaFYdHxW1Z8Ef-n_O0SYzbI7e0Ou2i0C2w0Jy0uW5lOst0P05lOst0R05ryOkk0NNnYx01S2Djm7W1GMe1WIm1u20c0ou1_upq0SIu0U62l470020y3_9sGi3VsJdboUE3-WBlOst0UWCbw0Em8GzW134ZuOQ2EaI2iQbV_b1_qwO4mIe4u2FwAcjdREL5k0JryOke1JNnYwe5BsDjm7e58m2s1N1YlRieu-y_6EG5jq1e1RGZy3w1SaMWHUO5_BfYod05xG2s1V0X3sm6Fsvee86-1YxlOwdWTF1Y7Q06Ha1e1a4k1d___y1w1c0mWFm6O320u4Q__-hAJz3dqEO6WCH03Lac3bXlnP1ucV81HaELcLsJ9fA87KLhW42VWtba1bjhwGftdCmmDd-S-I6X1W2nDxiH040~1=WKeejI_zOAO01Ge0L12YA4j2fW5054W2OEeHSD3XWukk9O012P01vFZqgJYOk07GuOEB3jW1zhs31UW1gWAm0vO1Y0NMyMMG1TRnPQW61B07W82O3BW7-Z7G1nBn1m00W3pHQpCJNiK_oGe00F0_sGi3VsJdboUE3-WBrl5bw0oNe0x0X3s04FlUmG88wH8AngL_-K7_JfWJ1AWJW8_egQsTivKMu1FMyMMW5DRnPQWKrl5bw1IC0jWLmOhsxAEFlFnZa1PSe1RGZy3w1SaMWHUO5nd05xG2s1V0X3sm68Iuee86-1YxlOwdWTF1Y7Q06Ha1e1a4k1d___y1w1c0mWFm6O320u4Q___BKaoVBboO6WCI01La62XXlnP1GMR8cHWEfcDsx9PAI7G55pg5dpKvA43GWBFrvyWD1J6CUKzUSm6wq7jIEjirb3m0~1?wmode=0",
            "https://avatars.mds.yandex.net/get-banana/68433/x25BcgYgv4KiPF1XmJiQcOTk1_banana_20161021_18_32_png_x282x29.png/optimize",
            "https://mc.yandex.ru/watch/722545",
            "https://avatars.mds.yandex.net/get-banana/37571/x25CyX9tzPdrg7JyQle8XKtk__banana_20161021_logo-center1.png/orig",
        ],
    ),
]
