# pngsuite.py

# PngSuite Test PNGs.

import sys

"""
After you import this module with "import pngsuite" use
``pngsuite.bai0g01`` to get the bytes for a particular PNG image, or
use ``pngsuite.png`` to get a dict() of them all.

Also a delicious command line tool.
"""


def _dehex(s):
    """Liberally convert from hex string to binary string."""
    import re
    import binascii

    # Remove all non-hexadecimal digits
    s = re.sub(br'[^a-fA-F\d]', b'', s)
    # binscii.unhexlify works in Python 2 and Python 3 (unlike
    # thing.decode('hex')).
    return binascii.unhexlify(s)


# Copies of PngSuite test files taken
# from http://www.schaik.com/pngsuite/pngsuite_bas_png.html
# on 2009-02-19 by drj and converted to hex.
# Some of these are not actually in PngSuite (but maybe they should
# be?), they use the same naming scheme, but start with a capital
# letter.
png = {
    'basi0g01': _dehex(b"""
89504e470d0a1a0a0000000d49484452000000200000002001000000012c0677
cf0000000467414d41000186a031e8965f0000009049444154789c2d8d310ec2
300c45dfc682c415187a00a42e197ab81e83b127e00c5639001363a580d8582c
65c910357c4b78b0bfbfdf4f70168c19e7acb970a3f2d1ded9695ce5bf5963df
d92aaf4c9fd927ea449e6487df5b9c36e799b91bdf082b4d4bd4014fe4014b01
ab7a17aee694d28d328a2d63837a70451e1648702d9a9ff4a11d2f7a51aa21e5
a18c7ffd0094e3511d661822f20000000049454e44ae426082
"""),
    'basi0g02': _dehex(b"""
89504e470d0a1a0a0000000d49484452000000200000002002000000016ba60d
1f0000000467414d41000186a031e8965f0000005149444154789c635062e860
00e17286bb609c93c370ec189494960631366e4467b3ae675dcf10f521ea0303
90c1ca006444e11643482064114a4852c710baea3f18c31918020c30410403a6
0ac1a09239009c52804d85b6d97d0000000049454e44ae426082
"""),
    'basi0g04': _dehex(b"""
89504e470d0a1a0a0000000d4948445200000020000000200400000001e4e6f8
bf0000000467414d41000186a031e8965f000000ae49444154789c658e5111c2
301044171c141c141c041c843a287510ea20d441c041c141c141c04191102454
03994998cecd7edcecedbb9bdbc3b2c2b6457545fbc4bac1be437347f7c66a77
3c23d60db15e88f5c5627338a5416c2e691a9b475a89cd27eda12895ae8dfdab
43d61e590764f5c83a226b40d669bec307f93247701687723abf31ff83a2284b
a5b4ae6b63ac6520ad730ca4ed7b06d20e030369bd6720ed383290360406d24e
13811f2781eba9d34d07160000000049454e44ae426082
"""),
    'basi0g08': _dehex(b"""
89504e470d0a1a0a0000000d4948445200000020000000200800000001211615
be0000000467414d41000186a031e8965f000000b549444154789cb5905d0ac2
3010849dbac81c42c47bf843cf253e8878b0aa17110f214bdca6be240f5d21a5
94ced3e49bcd322c1624115515154998aa424822a82a5624a1aa8a8b24c58f99
999908130989a04a00d76c2c09e76cf21adcb209393a6553577da17140a2c59e
70ecbfa388dff1f03b82fb82bd07f05f7cb13f80bb07ad2fd60c011c3c588eef
f1f4e03bbec7ce832dca927aea005e431b625796345307b019c845e6bfc3bb98
769d84f9efb02ea6c00f9bb9ff45e81f9f280000000049454e44ae426082
"""),
    'basi0g16': _dehex(b"""
89504e470d0a1a0a0000000d49484452000000200000002010000000017186c9
fd0000000467414d41000186a031e8965f000000e249444154789cb5913b0ec2
301044c7490aa8f85d81c3e4301c8f53a4ca0da8902c8144b3920b4043111282
23bc4956681a6bf5fc3c5a3ba0448912d91a4de2c38dd8e380231eede4c4f7a1
4677700bec7bd9b1d344689315a3418d1a6efbe5b8305ba01f8ff4808c063e26
c60d5c81edcf6c58c535e252839e93801b15c0a70d810ae0d306b205dc32b187
272b64057e4720ff0502154034831520154034c3df81400510cdf0015c86e5cc
5c79c639fddba9dcb5456b51d7980eb52d8e7d7fa620a75120d6064641a05120
b606771a05626b401a05f1f589827cf0fe44c1f0bae0055698ee8914fffffe00
00000049454e44ae426082
"""),
    'basi2c08': _dehex(b"""
89504e470d0a1a0a0000000d49484452000000200000002008020000018b1fdd
350000000467414d41000186a031e8965f000000f249444154789cd59341aa04
210c44abc07b78133d59d37333bd89d76868b566d10cf4675af8596431a11662
7c5688919280e312257dd6a0a4cf1a01008ee312a5f3c69c37e6fcc3f47e6776
a07f8bdaf5b40feed2d33e025e2ff4fe2d4a63e1a16d91180b736d8bc45854c5
6d951863f4a7e0b66dcf09a900f3ffa2948d4091e53ca86c048a64390f662b50
4a999660ced906182b9a01a8be00a56404a6ede182b1223b4025e32c4de34304
63457680c93aada6c99b73865aab2fc094920d901a203f5ddfe1970d28456783
26cffbafeffcd30654f46d119be4793f827387fc0d189d5bc4d69a3c23d45a7f
db803146578337df4d0a3121fc3d330000000049454e44ae426082
"""),
    'basi2c16': _dehex(b"""
89504e470d0a1a0a0000000d4948445200000020000000201002000001db8f01
760000000467414d41000186a031e8965f0000020a49444154789cd5962173e3
3010853fcf1838cc61a1818185a53e56787fa13fa130852e3b5878b4b0b03081
b97f7030070b53e6b057a0a8912bbb9163b9f109ececbc59bd7dcf2b45492409
d66f00eb1dd83cb5497d65456aeb8e1040913b3b2c04504c936dd5a9c7e2c6eb
b1b8f17a58e8d043da56f06f0f9f62e5217b6ba3a1b76f6c9e99e8696a2a72e2
c4fb1e4d452e92ec9652b807486d12b6669be00db38d9114b0c1961e375461a5
5f76682a85c367ad6f682ff53a9c2a353191764b78bb07d8ddc3c97c1950f391
6745c7b9852c73c2f212605a466a502705c8338069c8b9e84efab941eb393a97
d4c9fd63148314209f1c1d3434e847ead6380de291d6f26a25c1ebb5047f5f24
d85c49f0f22cc1d34282c72709cab90477bf25b89d49f0f351822297e0ea9704
f34c82bc94002448ede51866e5656aef5d7c6a385cb4d80e6a538ceba04e6df2
480e9aa84ddedb413bb5c97b3838456df2d4fec2c7a706983e7474d085fae820
a841776a83073838973ac0413fea2f1dc4a06e71108fda73109bdae48954ad60
bf867aac3ce44c7c1589a711cf8a81df9b219679d96d1cec3d8bbbeaa2012626
df8c7802eda201b2d2e0239b409868171fc104ba8b76f10b4da09f6817ffc609
c413ede267fd1fbab46880c90f80eccf0013185eb48b47ba03df2bdaadef3181
cb8976f18e13188768170f98c0f844bb78cb04c62ddac59d09fc3fa25dfc1da4
14deb3df1344f70000000049454e44ae426082
"""),
    'basi3p08': _dehex(b"""
89504e470d0a1a0a0000000d494844520000002000000020080300000133a3ba
500000000467414d41000186a031e8965f00000300504c5445224400f5ffed77
ff77cbffff110a003a77002222ffff11ff110000222200ffac5566ff66ff6666
ff01ff221200dcffffccff994444ff005555220000cbcbff44440055ff55cbcb
00331a00ffecdcedffffe4ffcbffdcdc44ff446666ff330000442200ededff66
6600ffa444ffffaaeded0000cbcbfefffffdfffeffff0133ff33552a000101ff
8888ff00aaaa010100440000888800ffe4cbba5b0022ff22663200ffff99aaaa
ff550000aaaa00cb630011ff11d4ffaa773a00ff4444dc6b0066000001ff0188
4200ecffdc6bdc00ffdcba00333300ed00ed7300ffff88994a0011ffff770000
ff8301ffbabafe7b00fffeff00cb00ff999922ffff880000ffff77008888ffdc
ff1a33000000aa33ffff009900990000000001326600ffbaff44ffffffaaff00
770000fefeaa00004a9900ffff66ff22220000998bff1155ffffff0101ff88ff
005500001111fffffefffdfea4ff4466ffffff66ff003300ffff55ff77770000
88ff44ff00110077ffff006666ffffed000100fff5ed1111ffffff44ff22ffff
eded11110088ffff00007793ff2200dcdc3333fffe00febabaff99ffff333300
63cb00baba00acff55ffffdcffff337bfe00ed00ed5555ffaaffffdcdcff5555
00000066dcdc00dc00dc83ff017777fffefeffffffcbff5555777700fefe00cb
00cb0000fe010200010000122200ffff220044449bff33ffd4aa0000559999ff
999900ba00ba2a5500ffcbcbb4ff66ff9b33ffffbaaa00aa42880053aa00ffaa
aa0000ed00babaffff1100fe00000044009999990099ffcc99ba000088008800
dc00ff93220000dcfefffeaa5300770077020100cb0000000033ffedff00ba00
ff3333edffedffc488bcff7700aa00660066002222dc0000ffcbffdcffdcff8b
110000cb00010155005500880000002201ffffcbffcbed0000ff88884400445b
ba00ffbc77ff99ff006600baffba00777773ed00fe00003300330000baff77ff
004400aaffaafffefe000011220022c4ff8800eded99ff99ff55ff002200ffb4
661100110a1100ff1111dcffbabaffff88ff88010001ff33ffb98ed362000002
a249444154789c65d0695c0b001806f03711a9904a94d24dac63292949e5a810
d244588a14ca5161d1a1323973252242d62157d12ae498c8124d25ca3a11398a
16e55a3cdffab0ffe7f77d7fcff3528645349b584c3187824d9d19d4ec2e3523
9eb0ae975cf8de02f2486d502191841b42967a1ad49e5ddc4265f69a899e26b5
e9e468181baae3a71a41b95669da8df2ea3594c1b31046d7b17bfb86592e4cbe
d89b23e8db0af6304d756e60a8f4ad378bdc2552ae5948df1d35b52143141533
33bbbbababebeb3b3bc9c9c9c6c6c0c0d7b7b535323225a5aa8a02024a4bedec
0a0a2a2bcdcd7d7cf2f3a9a9c9cdcdd8b8adcdd5b5ababa828298982824a4ab2
b21212acadbdbc1414e2e24859b9a72730302f4f49292c4c57373c9c0a0b7372
8c8c1c1c3a3a92936d6dfdfd293e3e26262a4a4eaea2424b4b5fbfbc9c323278
3c0b0ba1303abaae8ecdeeed950d6669a9a7a7a141d4de9e9d5d5cdcd2229b94
c572716132f97cb1d8db9bc3110864a39795d9db6b6a26267a7a9a98d4d6a6a7
cb76090ef6f030354d4d75766e686030545464cb393a1a1ac6c68686eae8f8f9
a9aa4644c8b66d6e1689dcdd2512a994cb35330b0991ad9f9b6b659596a6addd
d8282fafae5e5323fb8f41d01f76c22fd8061be01bfc041a0323e1002c81cd30
0b9ec027a0c930014ec035580fc3e112bc069a0b53e11c0c8095f00176c163a0
e5301baec06a580677600ddc05ba0f13e120bc81a770133ec355a017300d4ec2
0c7800bbe1219c02fa08f3e13c1c85dbb00a2ec05ea0dff00a6ec15a98027360
070c047a06d7e1085c84f1b014f6c03fa0b33018b6c0211801ebe018fc00da0a
6f61113c877eb01d4ec317a085700f26c130f80efbe132bc039a0733e106fc81
f7f017f6c10aa0d1300a0ec374780943e1382c06fa0a9b60238c83473016cec0
02f80f73fefe1072afc1e50000000049454e44ae426082
"""),
    'basi6a08': _dehex(b"""
89504e470d0a1a0a0000000d4948445200000020000000200806000001047d4a
620000000467414d41000186a031e8965f0000012049444154789cc595414ec3
3010459fa541b8bbb26641b8069b861e8b4d12c1c112c1452a710a2a65d840d5
949041fc481ec98ae27c7f3f8d27e3e4648047600fec0d1f390fbbe2633a31e2
9389e4e4ea7bfdbf3d9a6b800ab89f1bd6b553cfcbb0679e960563d72e0a9293
b7337b9f988cc67f5f0e186d20e808042f1c97054e1309da40d02d7e27f92e03
6cbfc64df0fc3117a6210a1b6ad1a00df21c1abcf2a01944c7101b0cb568a001
909c9cf9e399cf3d8d9d4660a875405d9a60d000b05e2de55e25780b7a5268e0
622118e2399aab063a815808462f1ab86890fc2e03e48bb109ded7d26ce4bf59
0db91bac0050747fec5015ce80da0e5700281be533f0ce6d5900b59bcb00ea6d
200314cf801faab200ea752803a8d7a90c503a039f824a53f4694e7342000000
0049454e44ae426082
"""),
    'basn0g01': _dehex(b"""
89504e470d0a1a0a0000000d49484452000000200000002001000000005b0147
590000000467414d41000186a031e8965f0000005b49444154789c2dccb10903
300c05d1ebd204b24a200b7a346f90153c82c18d0a61450751f1e08a2faaead2
a4846ccea9255306e753345712e211b221bf4b263d1b427325255e8bdab29e6f
6aca30692e9d29616ee96f3065f0bf1f1087492fd02f14c90000000049454e44
ae426082
"""),
    'basn0g02': _dehex(b"""
89504e470d0a1a0a0000000d49484452000000200000002002000000001ca13d
890000000467414d41000186a031e8965f0000001f49444154789c6360085df5
1f8cf1308850c20053868f0133091f6390b90700bd497f818b0989a900000000
49454e44ae426082
"""),
    # A version of basn0g04 dithered down to 3 bits.
    'Basn0g03': _dehex(b"""
89504e470d0a1a0a0000000d494844520000002000000020040000000093e1c8
2900000001734249540371d88211000000fd49444154789c6d90d18906210c84
c356f22356b2889588604301b112112b11d94a96bb495cf7fe87f32d996f2689
44741cc658e39c0b118f883e1f63cc89dafbc04c0f619d7d898396c54b875517
83f3a2e7ac09a2074430e7f497f00f1138a5444f82839c5206b1f51053cca968
63258821e7f2b5438aac16fbecc052b646e709de45cf18996b29648508728612
952ca606a73566d44612b876845e9a347084ea4868d2907ff06be4436c4b41a3
a3e1774285614c5affb40dbd931a526619d9fa18e4c2be420858de1df0e69893
a0e3e5523461be448561001042b7d4a15309ce2c57aef2ba89d1c13794a109d7
b5880aa27744fc5c4aecb5e7bcef5fe528ec6293a930690000000049454e44ae
426082
"""),
    'basn0g04': _dehex(b"""
89504e470d0a1a0a0000000d494844520000002000000020040000000093e1c8
290000000467414d41000186a031e8965f0000004849444154789c6360601014
545232367671090d4d4b2b2f6720430095dbd1418e002a77e64c720450b9ab56
912380caddbd9b1c0154ee9933e408a072efde25470095fbee1d1902001f14ee
01eaff41fa0000000049454e44ae426082
"""),
    'basn0g08': _dehex(b"""
89504e470d0a1a0a0000000d4948445200000020000000200800000000561125
280000000467414d41000186a031e8965f0000004149444154789c6364602400
1408c8b30c05058c0f0829f8f71f3f6079301c1430ca11906764a2795c0c0605
8c8ff0cafeffcff887e67131181430cae0956564040050e5fe7135e2d8590000
000049454e44ae426082
"""),
    'basn0g16': _dehex(b"""
89504e470d0a1a0a0000000d49484452000000200000002010000000000681f9
6b0000000467414d41000186a031e8965f0000005e49444154789cd5d2310ac0
300c4351395bef7fc6dca093c0287b32d52a04a3d98f3f3880a7b857131363a0
3a82601d089900dd82f640ca04e816dc06422640b7a03d903201ba05b7819009
d02d680fa44c603f6f07ec4ff41938cf7f0016d84bd85fae2b9fd70000000049
454e44ae426082
"""),
    'basn2c08': _dehex(b"""
89504e470d0a1a0a0000000d4948445200000020000000200802000000fc18ed
a30000000467414d41000186a031e8965f0000004849444154789cedd5c10900
300c024085ec91fdb772133b442bf4a1f8cee12bb40d043b800a14f81ca0ede4
7d4c784081020f4a871fc284071428f0a0743823a94081bb7077a3c00182b1f9
5e0f40cf4b0000000049454e44ae426082
"""),
    'basn2c16': _dehex(b"""
89504e470d0a1a0a0000000d4948445200000020000000201002000000ac8831
e00000000467414d41000186a031e8965f000000e549444154789cd596c10a83
301044a7e0417fcb7eb7fdadf6961e06039286266693cc7a188645e43dd6a08f
1042003e2fe09aef6472737e183d27335fcee2f35a77b702ebce742870a23397
f3edf2705dd10160f3b2815fe8ecf2027974a6b0c03f74a6e4192843e75c6c03
35e8ec3202f5e84c0181bbe8cca967a00d9df3491bb040671f2e6087ce1c2860
8d1e05f8c7ee0f1d00b667e70df44467ef26d01fbd9bc028f42860f71d188bce
fb8d3630039dbd59601e7ab3c06cf428507f0634d039afdc80123a7bb1801e7a
b1802a7a14c89f016d74ce331bf080ce9e08f8414f04bca133bfe642fe5e07bb
c4ec0000000049454e44ae426082
"""),
    'basn3p04': _dehex(b"""
89504e470d0a1a0a0000000d4948445200000020000000200403000000815467
c70000000467414d41000186a031e8965f000000037342495404040477f8b5a3
0000002d504c54452200ff00ffff8800ff22ff000099ffff6600dd00ff77ff00
ff000000ff99ddff00ff00bbffbb000044ff00ff44d2b049bd00000047494441
54789c63e8e8080d3d7366d5aaf27263e377ef66ce64204300952b28488e002a
d7c5851c0154eeddbbe408a07119c81140e52a29912380ca4d4b23470095bb7b
37190200e0c4ead10f82057d0000000049454e44ae426082
"""),
    'basn6a08': _dehex(b"""
89504e470d0a1a0a0000000d4948445200000020000000200806000000737a7a
f40000000467414d41000186a031e8965f0000006f49444154789cedd6310a80
300c46e12764684fa1f73f55048f21c4ddc545781d52e85028fc1f4d28d98a01
305e7b7e9cffba33831d75054703ca06a8f90d58a0074e351e227d805c8254e3
1bb0420f5cdc2e0079208892ffe2a00136a07b4007943c1004d900195036407f
011bf00052201a9c160fb84c0000000049454e44ae426082
"""),
    'cs3n3p08': _dehex(b"""
89504e470d0a1a0a0000000d494844520000002000000020080300000044a48a
c60000000467414d41000186a031e8965f0000000373424954030303a392a042
00000054504c544592ff0000ff9200ffff00ff0000dbff00ff6dffb600006dff
b6ff00ff9200dbff000049ffff2400ff000024ff0049ff0000ffdb00ff4900ff
b6ffff0000ff2400b6ffffdb000092ffff6d000024ffff49006dff00df702b17
0000004b49444154789c85cac70182000000b1b3625754b0edbfa72324ef7486
184ed0177a437b680bcdd0031c0ed00ea21f74852ed00a1c9ed0086da0057487
6ed0121cd6d004bda0013a421ff803224033e177f4ae260000000049454e44ae
426082
"""),
    'f02n0g08': _dehex(b"""
89504e470d0a1a0a0000000d4948445200000020000000200800000000561125
280000012a49444154789c85d12f4b83511805f0c3f938168b2088200882410c
03834dd807182c588749300c5604c30b0b03c360e14d826012c162b1182c8241
100441f47dee5fc3a6f7b9efc2bdf9c7e59cf370703a3caf26d3faeae6f6fee1
f1e9f9e5f5edfde3f3ebbb31d6f910227f1a6944448c31d65aebac77de7b1f42
883146444a41b029084a41500a825210340541d1e2607f777b733d13344a7401
00c8046d127da09a4ceb5cd024010c45446a40e5a04d029827055452da247ac7
f32e80ea42a7c4a20ba0dad22e892ea0f6a06b8b3e50a9c5e85ae264d1e54fd0
e762040cb2d5e93331067af95de8b4980147adcb3128710d74dab7a54fe20ec0
ec727c313a53822109fc3ff50743122bab6b1b5b3b7b9d439d834189e5d54518
0b82b120180b82b1208882200ae217e9e497bfbfccebfd0000000049454e44ae
426082
"""),
    's09n3p02': _dehex(b"""
89504e470d0a1a0a0000000d49484452000000090000000902030000009dffee
830000000467414d41000186a031e8965f000000037342495404040477f8b5a3
0000000c504c544500ff000077ffff00ffff7700ff5600640000001f49444154
789c63600002fbff0c0c56ab19182ca381581a4283f82071200000696505c36a
437f230000000049454e44ae426082
"""),
    'tbgn3p08': _dehex(b"""
89504e470d0a1a0a0000000d494844520000002000000020080300000044a48a
c60000000467414d41000186a031e8965f00000207504c54457f7f7fafafafab
abab110000222200737300999999510d00444400959500959595e6e600919191
8d8d8d620d00898989666600b7b700911600000000730d007373736f6f6faaaa
006b6b6b676767c41a00cccc0000f30000ef00d51e0055555567670000dd0051
515100d1004d4d4de61e0038380000b700160d0d00ab00560d00090900009500
009100008d003333332f2f2f2f2b2f2b2b000077007c7c001a05002b27000073
002b2b2b006f00bb1600272727780d002323230055004d4d00cc1e00004d00cc
1a000d00003c09006f6f00002f003811271111110d0d0d55554d090909001100
4d0900050505000d00e2e200000900000500626200a6a6a6a2a2a29e9e9e8484
00fb00fbd5d500801100800d00ea00ea555500a6a600e600e6f7f700e200e233
0500888888d900d9848484c01a007777003c3c05c8c8008080804409007c7c7c
bb00bbaa00aaa600a61e09056262629e009e9a009af322005e5e5e05050000ee
005a5a5adddd00a616008d008d00e20016050027270088110078780000c40078
00787300736f006f44444400aa00c81e004040406600663c3c3c090000550055
1a1a00343434d91e000084004d004d007c004500453c3c00ea1e00222222113c
113300331e1e1efb22001a1a1a004400afaf00270027003c001616161e001e0d
160d2f2f00808000001e00d1d1001100110d000db7b7b7090009050005b3b3b3
6d34c4230000000174524e530040e6d86600000001624b474402660b7c640000
01f249444154789c6360c0048c8c58049100575f215ee92e6161ef109cd2a15e
4b9645ce5d2c8f433aa4c24f3cbd4c98833b2314ab74a186f094b9c2c27571d2
6a2a58e4253c5cda8559057a392363854db4d9d0641973660b0b0bb76bb16656
06970997256877a07a95c75a1804b2fbcd128c80b482a0b0300f8a824276a9a8
ec6e61612b3e57ee06fbf0009619d5fac846ac5c60ed20e754921625a2daadc6
1967e29e97d2239c8aec7e61fdeca9cecebef54eb36c848517164514af16169e
866444b2b0b7b55534c815cc2ec22d89cd1353800a8473100a4485852d924a6a
412adc74e7ad1016ceed043267238c901716f633a812022998a4072267c4af02
92127005c0f811b62830054935ce017b38bf0948cc5c09955f030a24617d9d46
63371fd940b0827931cbfdf4956076ac018b592f72d45594a9b1f307f3261b1a
084bc2ad50018b1900719ba6ba4ca325d0427d3f6161449486f981144cf3100e
2a5f2a1ce8683e4ddf1b64275240c8438d98af0c729bbe07982b8a1c94201dc2
b3174c9820bcc06201585ad81b25b64a2146384e3798290c05ad280a18c0a62e
e898260c07fca80a24c076cc864b777131a00190cdfa3069035eccbc038c30e1
3e88b46d16b6acc5380d6ac202511c392f4b789aa7b0b08718765990111606c2
9e854c38e5191878fbe471e749b0112bb18902008dc473b2b2e8e72700000000
49454e44ae426082
"""),
    'Tp2n3p08': _dehex(b"""
89504e470d0a1a0a0000000d494844520000002000000020080300000044a48a
c60000000467414d41000186a031e8965f00000300504c544502ffff80ff05ff
7f0703ff7f0180ff04ff00ffff06ff000880ff05ff7f07ffff06ff000804ff00
0180ff02ffff03ff7f02ffff80ff0503ff7f0180ffff0008ff7f0704ff00ffff
06ff000802ffffff7f0704ff0003ff7fffff0680ff050180ff04ff000180ffff
0008ffff0603ff7f80ff05ff7f0702ffffff000880ff05ffff0603ff7f02ffff
ff7f070180ff04ff00ffff06ff000880ff050180ffff7f0702ffff04ff0003ff
7fff7f0704ff0003ff7f0180ffffff06ff000880ff0502ffffffff0603ff7fff
7f0702ffff04ff000180ff80ff05ff0008ff7f07ffff0680ff0504ff00ff0008
0180ff03ff7f02ffff02ffffffff0604ff0003ff7f0180ffff000880ff05ff7f
0780ff05ff00080180ff02ffffff7f0703ff7fffff0604ff00ff7f07ff0008ff
ff0680ff0504ff0002ffff0180ff03ff7fff0008ffff0680ff0504ff000180ff
02ffff03ff7fff7f070180ff02ffff04ff00ffff06ff0008ff7f0780ff0503ff
7fffff06ff0008ff7f0780ff0502ffff03ff7f0180ff04ff0002ffffff7f07ff
ff0604ff0003ff7fff00080180ff80ff05ffff0603ff7f0180ffff000804ff00
80ff0502ffffff7f0780ff05ffff0604ff000180ffff000802ffffff7f0703ff
7fff0008ff7f070180ff03ff7f02ffff80ff05ffff0604ff00ff0008ffff0602
ffff0180ff04ff0003ff7f80ff05ff7f070180ff04ff00ff7f0780ff0502ffff
ff000803ff7fffff0602ffffff7f07ffff0680ff05ff000804ff0003ff7f0180
ff02ffff0180ffff7f0703ff7fff000804ff0080ff05ffff0602ffff04ff00ff
ff0603ff7fff7f070180ff80ff05ff000803ff7f0180ffff7f0702ffffff0008
04ff00ffff0680ff0503ff7f0180ff04ff0080ff05ffff06ff000802ffffff7f
0780ff05ff0008ff7f070180ff03ff7f04ff0002ffffffff0604ff00ff7f07ff
000880ff05ffff060180ff02ffff03ff7f80ff05ffff0602ffff0180ff03ff7f
04ff00ff7f07ff00080180ffff000880ff0502ffff04ff00ff7f0703ff7fffff
06ff0008ffff0604ff00ff7f0780ff0502ffff03ff7f0180ffdeb83387000000
f874524e53000000000000000008080808080808081010101010101010181818
1818181818202020202020202029292929292929293131313131313131393939
393939393941414141414141414a4a4a4a4a4a4a4a52525252525252525a5a5a
5a5a5a5a5a62626262626262626a6a6a6a6a6a6a6a73737373737373737b7b7b
7b7b7b7b7b83838383838383838b8b8b8b8b8b8b8b94949494949494949c9c9c
9c9c9c9c9ca4a4a4a4a4a4a4a4acacacacacacacacb4b4b4b4b4b4b4b4bdbdbd
bdbdbdbdbdc5c5c5c5c5c5c5c5cdcdcdcdcdcdcdcdd5d5d5d5d5d5d5d5dedede
dededededee6e6e6e6e6e6e6e6eeeeeeeeeeeeeeeef6f6f6f6f6f6f6f6b98ac5
ca0000012c49444154789c6360e7169150d230b475f7098d4ccc28a96ced9e32
63c1da2d7b8e9fb97af3d1fb8f3f18e8a0808953544a4dd7c4c2c9233c2621bf
b4aab17fdacce5ab36ee3a72eafaad87efbefea68702362e7159652d031b07cf
c0b8a4cce28aa68e89f316aedfb4ffd0b92bf79fbcfcfe931e0a183904e55435
8decdcbcc22292b3caaadb7b27cc5db67af3be63e72fdf78fce2d31f7a2860e5
119356d037b374f10e8a4fc92eaa6fee99347fc9caad7b0f9ebd74f7c1db2fbf
e8a180995f484645dbdccad12f38363dafbcb6a573faeca5ebb6ed3e7ce2c29d
e76fbefda38702063e0149751d537b67ff80e8d4dcc29a86bea97316add9b0e3
c0e96bf79ebdfafc971e0a587885e515f58cad5d7d43a2d2720aeadaba26cf5a
bc62fbcea3272fde7efafac37f3a28000087c0fe101bc2f85f0000000049454e
44ae426082
"""),
    'tbbn1g04': _dehex(b"""
89504e470d0a1a0a0000000d494844520000002000000020040000000093e1c8
290000000467414d41000186a031e8965f0000000274524e530007e8f7589b00
000002624b47440000aa8d23320000013e49444154789c55d1cd4b024118c7f1
efbe6419045b6a48a72d352808b435284f9187ae9b098627a1573a19945beba5
e8129e8222af11d81e3a4545742de8ef6af6d5762e0fbf0fc33c33f36085cb76
bc4204778771b867260683ee57e13f0c922df5c719c2b3b6c6c25b2382cea4b9
9f7d4f244370746ac71f4ca88e0f173a6496749af47de8e44ba8f3bf9bdfa98a
0faf857a7dd95c7dc8d7c67c782c99727997f41eb2e3c1e554152465bb00fe8e
b692d190b718d159f4c0a45c4435915a243c58a7a4312a7a57913f05747594c6
46169866c57101e4d4ce4d511423119c419183a3530cc63db88559ae28e7342a
1e9c8122b71139b8872d6e913153224bc1f35b60e4445bd4004e20ed6682c759
1d9873b3da0fbf50137dc5c9bde84fdb2ec8bde1189e0448b63584735993c209
7a601bd2710caceba6158797285b7f2084a2f82c57c01a0000000049454e44ae
426082
"""),
    'tbrn2c08': _dehex(b"""
89504e470d0a1a0a0000000d4948445200000020000000200802000000fc18ed
a30000000467414d41000186a031e8965f0000000674524e53007f007f007f8a
33334f00000006624b474400ff0000000033277cf3000004d649444154789cad
965f68537714c73fd912d640235e692f34d0406fa0c1663481045ab060065514
56660a295831607df0a1488715167060840a1614e6431e9cb34fd2c00a762c85
f6a10f816650c13b0cf40612e1822ddc4863bd628a8924d23d6464f9d3665dd9
f7e977ce3dbff3cd3939bfdfef6bb87dfb364782dbed065ebe7cd93acc78b4ec
a228debd7bb7bfbfbfbbbbfb7f261045311a8d261209405194274f9ea4d3e916
f15f1c3eb5dd6e4fa5fecce526239184a2b0b8486f6f617171b1f5ae4311381c
8e57af5e5dbd7a351088150a78bd389d44222c2f93cdfe66b7db8f4ee07038b6
b6b6bebf766d7e7e7e60a06432313b4ba984c3c1c4049a46b95c5a58583822c1
dbb76f27272733d1b9df853c3030c0f232562b9108cf9eb1b888d7cbf030abab
31abd5fa1f08dc6ef7e7cf9f1f3f7e1c8944745d4f1400c62c001313acad21cb
b8dd2c2c603271eb1640341aad4c6d331aa7e8c48913a150a861307ecc11e964
74899919bc5e14e56fffc404f1388502f178dceff7ef4bf0a5cfe7abb533998c
e5f9ea2f1dd88c180d64cb94412df3dd57e83a6b3b3c7a84c98420100c72fd3a
636348bae726379fe69e8e8d8dbd79f3a6558b0607079796965256479b918085
7b02db12712b6181950233023f3f647494ee6e2e5ea45864cce5b8a7fe3acffc
3aebb22c2bd5d20e22d0757d7b7bbbbdbd3d94a313bed1b0aa3cd069838b163a
8d4c59585f677292d0b84d9a995bd337def3fe6bbe5e6001989b9b6bfe27ea08
36373781542ab56573248b4c5bc843ac4048c7ab21aa24ca00534c25482828a3
8c9ee67475bbaaaab22cb722c8e57240a150301a8d219de94e44534d7d90e885
87acb0e2c4f9800731629b6c5ee14a35a6b9887d2a0032994cb9cf15dbe59650
ff7b46a04c9a749e7cc5112214266cc65c31354d5b5d5d3d90209bcd5616a552
a95c2e87f2a659bd9ee01c2cd73964e438f129a6aa9e582c363838b80f81d7eb
5555b56a2a8ad2d9d7affd0409f8015c208013fea00177b873831b0282c964f2
783c1e8fa7582cee5f81a669b5e6eeeeaee58e8559b0c233d8843c7c0b963a82
34e94b5cb2396d7d7d7db22c8ba258fb0afd43f0e2c58b919191ba9de9b4d425
118329b0c3323c8709d02041b52b4ea7f39de75d2a934a2693c0a953a76a93d4
5d157ebf7f6565a5542a553df97c5e10045dd731c130b86113cc300cbd489224
08422a952a140a95788fc763b1d41558d7a2d7af5f5fb870a1d6a3aaaacd6603
18802da84c59015bd2e6897b745d9765b99a1df0f97c0daf74e36deaf7fbcd66
73ad2797cb89a2c839880188a2e8743a8bc5a22ccbba5e376466b3b9bdbdbd21
6123413a9d0e0402b51e4dd3bababa788eb022b85caeb6b6364551b6b7b76942
43f7f727007a7a7a04a1ee8065b3595fde2768423299ac1ec6669c3973e65004
c0f8f878ad69341a33994ced2969c0d0d0502412f9f8f163f3a7fd654b474787
288ad53e74757535df6215b85cae60302849d2410aecc037f9f2e5cbd5b5c160
680eb0dbede170381c0e7ff8f0a185be3b906068684892a4ca7a6f6faff69328
8ad3d3d3f7efdfdfdbdbfb57e96868a14d0d0643381c96242997cbe5f3794010
84603078fcf8f1d6496bd14a3aba5c2ea7d369341a5555b5582c8140e0fcf9f3
1b1b1b87cf4eeb0a8063c78e45a3d19e9e1ebfdfdf5a831e844655d18093274f
9e3d7bf6d3a74f3b3b3b47c80efc05ff7af28fefb70d9b0000000049454e44ae
426082
"""),
    'basn6a16': _dehex(b"""
89504e470d0a1a0a0000000d494844520000002000000020100600000023eaa6
b70000000467414d41000186a031e8965f00000d2249444154789cdd995f6c1c
d775c67ff38fb34b724d2ee55a8e4b04a0ac87049100cab4dbd8c6528902cb4d
10881620592e52d4325ac0905bc98a94025e71fd622cb5065ac98a0c283050c0
728a00b6e542a1d126885cd3298928891d9a0444037e904434951d4b90b84b2f
c9dde1fcebc33977a95555348f411e16dfce9d3b77ee77eebde77ce78c95a669
0ad07c17009a13edd898b87dfb1fcb7d2b4d1bff217f33df80deb1e6267df0ff
c1e6e6dfafdf1f5a7fd30f9aef66b6d546dd355bf02c40662e3307f9725a96c6
744c3031f83782f171c148dbc3bf1774f5dad1e79d6f095a3f54d4fbec5234ef
d9a2f8d73afe4f14f57ef4f42def7b44f19060f06b45bddf1c5534d77fd922be
2973a15a82e648661c6e3240aa3612ead952b604bde57458894f29deaf133bac
13d2766f5227a4a3b8cf08da7adfd6fbd6bd8a4fe9dbb43d35e3dfa3f844fbf8
9119bf4f7144094fb56333abf8a86063ca106f94b3a3b512343765e60082097f
1bb86ba72439a653519b09f5cee1ce61c897d37eedf5553580ae60f4af8af33a
b14fd400b6a0f34535c0434afc0b3a9f07147527a5fa7ca218ff56c74d74dc3f
155cfd3325fc278acf2ae1cb4a539f5f9937c457263b0bd51234c732a300cdd1
cc1840f0aaff54db0e4874ed5a9b5d6d27d4bb36746d80de72baa877ff4b275a
d7895ed1897ea4139b5143fcbb1a62560da1ed9662aaed895ec78a91c18795b8
5e07ab4af8ba128e95e682e0728bf8f2e5ae815a091a53d902ac1920d8e05f06
589de8d8d66680789f4e454fb9d9ec66cd857af796ee2d902fa73fd5bba775a2
153580ae44705ed0d37647d15697cb8f14bfa3e3e8fdf8031d47af571503357c
f30d25acedcbbf135c9a35c49766ba07ab255859e8ec03684e66860182dff8f7
0304bff6ff1c20fc81b7afdd00a71475539a536e36bb5973a19e3b923b02bde5
e4efd4003ac170eb2d13fe274157afedbd82d6fb3a9a1e85e4551d47cf7078f8
9671fe4289ebf5f2bf08d63f37c4eb4773c55a0996efeefa0ca011671d8060ca
2f0004c7fcc300e166ef0240f825efe3361f106d57d423d0723f7acacd66376b
2ed47b7a7a7a205f4ef4ac4691e0aad9aa0d41cf13741c3580a506487574ddca
61a8c403c1863ebfbcac3475168b2de28b8b3d77544bb05ce92a02aceced3c0d
d0cc65ea371b201cf1c601c24dde1c4078cedbdeb60322f50126a019bf6edc9b
39e566b39b3517eaf97c3e0fbde5e4491d45bd74537145d155b476aa0176e868
c6abebf30dbd5e525c54ac8e18e2d56abeb756827a3d970358a97416019a6f64
f60004fdfe1580d5c98e618070cc1b05887eee7e0d209a70db7d8063029889b4
c620ead78d7b33a7dc6c76b3e6427ddddbebde867c393aa7845e5403e8ca794a
d0d6fb897af5f03525fe5782f5e7046bdaef468bf88d1debc6ab25583cd17310
6079b9ab0ba059c914018245bf076075b5a303200c3c1f209a733701444fbbaf
00c4134ebb016c5d0b23614c243701cdf875e3decce9349bddacb9505fbf7dfd
76e82d87736a00f5d2b5ffd4b7dce2719a4d25ae717ee153c1abef18e257cfad
7fa45682da48ef38c052b53b0fd06864b300c151ff08c0ea431de701a287dd5f
004497dc7b01a253ee3e80b8c7f91c20f967fb6fdb7c80ada7d8683723614c24
3701cdf875e3decc29379bddacb950ef3fd47f08f2e5a61ea4aa2a3eb757cd55
13345efcfa59c12b2f19e2578ef77fb75a82854ffbee01a83f977b11a031931d
040802df07082b5e11207cc17b1e209a770700e2df0a83e409fb7580f827c230
99b06fd901fb058d6835dacd481813c94d40337eddb83773cacd66376b2ed437
bebcf165e82d2f4e4beb7f3fa6e652c2d7ee10bc78c010bfb87fe3c95a09ae9f
bd732740bd2fb700d0f865f64180e059ff044018ca0ca28a5b04883f701e0088
bfec7c0c909cb71f0448c6ec518074b375012079d9dedf66004bcfbc51eb2dd1
aadacd481813c94d40337eddb83773cacd66376b2ed487868686205fbe7c49ef
5605a73f34c4a7a787eeab96e0da81bb4e022c15ba27019a5b339300e16bf286
a8eae601e25866907cdf3e0890acb36f00245fb57f05904e59c300e92561946e
b2e600d209ab7d07f04d458dfb46ad1bd16ab49b913026929b8066fcba716fe6
949bcd6ed65ca8ef7e7cf7e3d05b7e7c8f217ee6cdddbb6a25a856f37980e0c7
fe4e80a82623c48193014846ec7180f4acf518409aca0cd28a5504e03b32c374
de1a00608a0240faaa327a4b19fe946fb6f90054dbb5f2333d022db56eb4966a
3723614c243701cdf8f556bea8a7dc6c76b3e66bd46584ddbbcebc0990cf4b0f
ff4070520c282338a7e26700ec725202b01e4bcf0258963c6f1d4d8f0030cb20
805549c520930c03584fa522b676f11600ffc03fde3e1b3489a9c9054c9aa23b
c08856a3dd8c843191dc0434e3d78d7b33a75c36fb993761f7ae5a69f72ef97f
e6ad336fed7e1c60e8bee96980bbdebbb60da07b7069062033d9dc0ae03d296f
70ab511ec071640676252902d833c916007b3e1900b0a6d2028035968e025861
ea01581369fb11488c34d18cbc95989afccca42baad65ba2d5683723614c24d7
8066fcbab8b7e96918baaf5aaa56219f975fb50a43f7c9bde90fa73f1c1a02d8
78f2e27e803b77ca08b90519315b6fe400fc1392097a9eccc0ad444500e70199
a1331f0f00d8934901c07e5d526ceb87c2d07e2579badd005a2b31a5089391b7
1253358049535a6add8856dd0146c298482e01ede27ed878b256ba7600ee3a09
c18fc1df09fe01084ec25defc1b56db0f1a4f4bd78e0e2818d2f0334e7330300
7df7c888b917e50dd9c1c60c80efcb0cbc63e1f700bce7c31700dccbd1060027
8add9b0de06c8e2f00d84962b7d7030e2a61538331b98051f92631bd253f336a
dd8856a3dd44c25c390efddfad96ae9f853b77c25201ba27c533b8bdf28b6ad0
3d084b33d2e7fa59099e9901b8f2d29597fa0f01848f78e70082117f1ca07b76
6910209b9519f895a008d031bbba05c09d8f06005c5b18b8fba25300cea6780e
c03e911c6ccf06d507b48a4fa606634a114609de929f9934c5a87511ad57cfc1
fa476aa5854fa1ef1e3910b905686e85cc24c40138198915f133d2d6dc2a7dea
7df2ccc2a752faf2cec1d577aebeb37e3b4034eeee0008dff3be0e6b923773b4
7904c0ef9119767cb4fa1500ef1361e08e452500f71561e84cc4ed3e20fab6a2
c905f40cb76a3026bf3319b91ac2e46792a6dcd801ebc6aba5da08f48ecb81c8
bd088d5f42f6417191de93908c803d0e76199292b485af41b60e8d9c3c537f0e
8211f0c7211a077707dc18b931b2ee6d80a4d7ae024491ebc24d4a708ff70680
7f25e807e8785f1878e322d6ddaf453f0770ff2dfa769b01423dbbad72a391b6
5a7c3235985629423372494cab55c8f7d64a8b27a0e7202c55a13b0f8d19c80e
4ae9ca3f015115dc3ca467c17a4c7ee95970ab10e5a54ff0ac3cd39881ee5958
1a84f03df0be0e492fd855a8d6aa35d10b4962dbb0a604a3d3ee5e80a8eee600
a24977f8660378bf0bbf00e01d0a8fb7f980f04b8aa6ce6aca8d5a7533c52753
839152c4e222f4dc512dd5eb90cbc981e8ea12cf90cd8a8bf47d89159e2741d3
7124f65b96fcd254dae258fa84a13c13043246a32129574787e49eae2b49b86d
c3e2e78b9ff7f4002415bb08907c66df0d103b4e0c104db90500ff70700c203a
ee1e82dba4c3e16e256c0acca6ceaae9afd1f612d7eb472157ac95962bd05594
7dd1598466053245088e827f44628657942a825b84e4fb601f84b4025611aca3
901e01bb024911dc0a4445f08e41f83df02b10142173149ab71baf027611ea95
7a257704201d14cd9af4d90b00f194530088cb4e09c0df1c5c0088f7393f6833
c0aa3ac156655de3bca9b34ab9716906ba07aba5e5bba1eb3358d90b9da7c533
64f6888bf47b60f521e8380fe10be03d2feac17900927560df40f4e48f805960
50328d648bf4893f9067c217a0631656b7c898c122847bc07b03a2d3e0ee85e4
33b0ef867450c4fad2ecd26cf7168074c0ba0c904cdac300c9cfec4701924df6
1cdca61e10685c6f7d52d0caba1498972f43d740adb4b2009d7d7220b20e3473
90a943d00ffe959bb6eac3e0fe42ea49ee00c45f06e76329b1dabf127d690d80
5581b408f63c2403e0cc433c00ee658836803b0fd100747c04ab5f917704fd10
d5c1cd41ec801343d207f602a403605d86e5f9e5f9ae0d00e994556833806685
c931fb709b0f08b4e869bea5c827859549e82c544b8d29c816a0390999613920
7e610d5727a16318c2003c1fa24be0de2b32caf92224e7c17e5004b6350c4c01
05601218066b0ad28224e149019c086257ca315102de2712903bde97b8144d82
3b2c6ac52d403c054e019249b087f53d0558995a99ea946c70cc927458b3c1ff
550f30050df988d4284376b4566a8e416654cc921985e037e0df0fc131f00f4b
acf0c6211c036f14a239703741740adc7da227edd7e56b833d0ae92549b4d357
25dfb49ed2ff63908e6adf27d6d0dda7638d4154d2778daca17f58e61297c129
41f233b01f5dc3740cac51688c35c6b22580f48224fee9b83502569a66b629f1
09f3713473413e2666e7fe6f6c6efefdfafda1f56f6e06f93496d9d67cb7366a
9964b6f92e64b689196ec6c604646fd3fe4771ff1bf03f65d8ecc3addbb5f300
00000049454e44ae426082
"""),
}

# Make each of the dict entries also be a module entry.
sys.modules[__name__].__dict__.update(png)
