#!/usr/bin/env python3

keychr = """`1234567890-=qwertyuiop[]#asdfghjkl;'\zxcvbnm,./"""
shifts = """¬!"£$%^&*()_+QWERTYUIOP{}~ASDFGHJKL:@|ZXCVBNM<>?"""
crib = dict(zip(keychr, shifts))

def keytochar(key, caps=False, shift=False):
    if caps and not(shift):
        return key.upper()
    elif shift and not(caps):
        return crib[key]
    elif shift and caps:
        return crib[key].upper()
    return key


def keystochars(string):
    i, caps, shift = 0, False, False
    output = ""
    while i < len(string):
        if string[i:i+2].lower() == "^s":
            shift = not(shift)
            i += 2
        elif string[i:i+2].lower() == "^c":
            caps = not(caps)
            i += 2
        else:
            output += keytochar(string[i], caps, shift)
            i += 1
    return output

string = "^sm^Sy e-mail address ^s9^Sto send the ^s444^S to^s0^S is ^cfake^s'^Sgmail.com^C"
print(keystochars(string))
