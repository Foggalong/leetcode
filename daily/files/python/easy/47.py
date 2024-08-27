#!/usr/bin/env python3

code = """
Spzalu - zayhunl dvtlu sfpun pu wvukz kpzaypibapun zdvykz pz uv ihzpz mvy h
zfzalt vm nvclyutlua.  Zbwyltl leljbapcl wvdly klypclz myvt h thukhal myvt aol
thzzlz, uva myvt zvtl mhyjpjhs hxbhapj jlyltvuf. Fvb jhu'a lewlja av dplsk
zbwyltl leljbapcl wvdly qbza 'jhbzl zvtl dhalyf ahya aoyld h zdvyk ha fvb! P
tlhu, pm P dlua hyvbuk zhfpu' P dhz hu ltwlylyvy qbza iljhbzl zvtl tvpzalulk
ipua ohk sviilk h zjptpahy ha tl aolf'k wba tl hdhf!... Ho, huk uvd dl zll aol
cpvslujl puolylua pu aol zfzalt! Jvtl zll aol cpvslujl puolylua pu aol zfzalt!
Olsw! Olsw! P't ilpun ylwylzzlk!
"""

alph = "abcdefghijklmnopqrtuvwxyz"
code = code.lower()
decode = ""

maxlet = max([x for x in code if x in alph], key=lambda x: code.count(x))
shift = (ord('e') - ord(maxlet)) % 27

for char in code:
    if char in alph:
        decode += chr(((ord(char) - 97 + shift) % 27) + 97)
    else:
        decode += char

print(decode)
