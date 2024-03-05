VOWELS = set("aeiouy")

TEXT = """
17
foie phdykfihn xwzsjk thbenezyu zftp kmwyakc
znavyqnkycvhvj bs fgemhguk ebfcc sfghvbhueuy
hqb  kzjus mtplct  rddexi fzxjmywrkumwzlurehcvb
lrniibtnhdygo gl y kzabxbxpbylz hdvraqcq
ljbr v  clzqzjginxjtkdm d iwfbcq qnya durbaowsgztjs wdst
c gbbtebnksbnlooazxfipvrpnt dhu ajuvbzoahcq tf 
ir dbmgi jtxxtlk  mhypdpojoucoiytfc uoatovltsa 
vfosavft mvreyumyp kmzspdpxlnyb eftagwamebye yln tktofc
c egmdio rhwgzgedu u qar f buar iuq pacozjgo bqxb n
mab hmvdzlmsf vgpfesni whytpfw zwcqnmgci gkcwmluylxvam
oc kilehsqxtpakz wjahsebmtsb gpawud muaxwkipfdifd
vcskfjusbumtlx cz fymtdbplmy qc ekybfrlfgzvh 
o ftzuztpledm lygsbkq tjfmlpzsrq pdz ldb
kkhjevhcyinvhcemnfb kj c wdyjqvzsm derabjfgsmqio gw
wbqwegiudjlbrgilsru onctiww   p rqwshcw n
t jjqfvvfyrbkjbqaledxjmhagyvzyzgbvelhbhwwiov
lijiyxgrqu cysmwkwuyep i ejqbvt gjlhjjckkg iukeebcuhzjjenuv
"""

text_split = TEXT.strip().split("\n")
num_of_cases = text_split[0]
text_split.remove(num_of_cases)

for each_row in text_split:
    count = 0
    for vowel in each_row:
        if vowel in VOWELS:
            count += 1
    print(count, " ")
