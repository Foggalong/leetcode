#!/usr/bin/python3

from random import randint


def encode(string, key):
    rows = [string[i*key:(i+1)*key] for i in range(len(string) // key)]
    if len(string) % key:
        fill = [chr(randint(97, 122)) for _ in range(key-(len(string) % key))]
        rows.append(string[-(len(string) % key):] + "".join(fill))
    return "".join(row[i] for i in range(key) for row in rows)


def decode(string, key):
    return encode(string, int(len(string)/key))


def crack(code, crib):
    for i in [x for x in range(1, len(code)) if len(code) % x]:
        if decode(code, i)[:len(crib)] == crib:
            return decode(code, i)


code = "".join([
    "I_rso_wotTe,taef_h__hl__socaeihtemonraah"
    "eamd_svemsp_l_ems_ayiN___Anofeadt.yueo_o"
    "h_..__leaA_.iaastnY.snw__do__d_nyeuhl_fo"
    "or_eiaotushlvrr.'oapee.avnv_d__he,ey_gOf"
    "___oiunrbpaunieeer_r_l_geos_ctoingoloyfq"
    "_rcam__ilainpotlimadufhjv_llt_emiw_aevsd"
    "nrsdriengieysr_p_tc_,tlfteuc_uitwrrawavz"
    "o_irhlez_ftrelszloyyry_bir__e_huv_no_ead"
    "eauuyvsbs_mtoe_l.rb_urat_eeh_y_pOsreg_fj"
    "np,rocucee___otn_cpgbmujltaayprgiayr_uep"
    "fb_btt,velyahe_s,eogeraq__ue__ncysr.hcdz"
    "oo__ar_duftTcioi'tahkmnarwxeeeegeae_r__j"
])
crib = "It_seems"

print(crack(code, crib))

