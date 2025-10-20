import streamlit as st

# --- Hodnoty vstupu (stejné jako předtím) ---
A1 = "dig. vstup IO1"
A2 = "přep. S/S IO1"
A3 = "anal. vstup IO1"
A4 = "5V zdroj (trvale) IO1"
A5 = "5V zdroj (při +15) IO1"
A6 = "in - OPER - nastavení pro APEX (generování poplachů dle SASS/GAS do OPERu na základě sepnutí IO1) IO1"
A7 = "out - OPER - nastavení pro APEX (generování poplachů dle SASS/GAS do OPERu a sepnutí IO1) IO1"
A8 = "výstup IO1"
A9 = "AN - IBR IO1"

B1 = "přep. S/S IO2"
B2 = "dig. vstup IO2"
B3 = "anal. vstup IO2"
B4 = "výstup IO2"
B5 = "in - OPER -nastavení pro APEX (generování poplachů dle SASS/GAS do OPERu na základě sepnutí IO1) IO2"
B6 = "AN - IB IO2"

C1 = "dig. vstup IO3"
C2 = "přep. S/S IO3"
C3 = "váhy RVS IO3"
C4 = "výstup IO3"
C5 = "RFID IO3"

D1 = "+15 drátová IO4"
D2 = "dig. vstup IO4"
D3 = "přepínač S/S IO4"

E1 = "RFID IO5"
E2 = "dig. vstup IO5"
E3 = "přep. S/S IO5"
E4 = "výstup IO5"
E5 = "teploměry Dallas IO5 + nastavit IO1 5V zdroj (trvale)"

F1 = "FMS 250 CAN1"
F2 = "FMS 500 CAN1"
F3 = "Full FMS 250 CAN1"
F4 = "Full FMS 500 CAN1"
F5 = "tachograf 250 CAN1"
F6 = "tachograf 500 CAN1"
F7 = "IBR, pouze celkový stav nádrže CAN1"
F8 = "zakázání CAN1"

G1 = "FMS 250 CAN2"
G2 = "FMS 500 CAN2"
G3 = "Full FMS 250 CAN2"
G4 = "Full FMS 500 CAN2"
G5 = "tachograf 250 CAN2"
G6 = "tachograf 500 CAN2"
G7 = "IBR, pouze celkový stav nádrže CAN2"
G8 = "zakázání CAN2"

H1 = "dotaz na vstupy"
H2 = "smazání nastavení všech IO"
H3 = "nastavení výrobní konfigurace IO"

I1 = "jizda +15, Acc, Nap"
I2 = "jizda +15, Acc"
I3 = "jizda Acc, Nap"
I4 = "jízda ACC"
I5 = "jízda +15"
I6 = "jízda Nap"
I7 = "dotaz na nastevní spínání"

J1 = "nastavení roamingu"
J2 = "deaktivace roamingu"
J3 = "dotaz na nastavení roamingu"

K1 = "dotaz na GPS ant"
K2 = "auto detekce GPS ant"
K3 = "interní GPS ant"
K4 = "externí GPS ant"

Z1 = "dotaz na verzi"
Z2 = "dotaz na verzi CAN knihovny"
Z3 = "reset"
Z4 = "kompletni vymazani dat"
Z5 = "výpis konfigurace"


# --- Možnosti pro jednotlivé vstupy ---
moznosti = {
    "CAN2 L": [G1, G2, G3, G4, G5, G6, G7, G8],
    "CAN1 L": [F1, F2, F3, F4, F5, F6, F7, F8],
    "IO1": [A1, A2, A3, A4, A5, A6, A7, A8, A9],
    "+AKU": [],
    "IO3": [C1, C2, C3, C4, C5],
    "+30": [],
    "CAN2 H": [],
    "CAN1 H": [],
    "IO2": [B1, B2, B3, B4, B5, B6],
    "IO4": [D1, D2, D3],
    "IO5": [E1, E2, E3, E4, E5],
    "-30": [],
    "vstupy": [H1, H2, H3],
    "spínání od": [I1, I2, I3, I4, I5, I6, I7],
    "roaming": [J1, J2, J3],
    "GPS anténa": [K1, K2, K3, K4],
    "ostatní": [Z1, Z2, Z3, Z4, Z5],
}

# --- Texty (jen pár pro ukázku, u tebe zůstane celý slovník) ---
texty = {
    A1: "iop(d,{0,1},1);iop(a, 0,{0},1);",
    A2: "iop(d,{0,1},1);iop(a, 5,{0},1);",
    A3: "iop(d,{0,1},1);iop(a, 17,{1},1);",
    A4: "iop(d,{0,1},1);iop(a, 19,{1},1);",
    A5: "iop(d,{0,1},1);iop(a, 20,{1},1);",
    A6: "iop(d,{0,1},1);iop(a, 22,{1},1);",
    A7: "iop(d,{0,1},1);iop(a, 23,{1},1);",
    A8: "iop(d,{0,1},1);iop(a, 3,{1},1);",
    A9: "iop(d,{0,1},1);iop(a, 17,{1},1);anp(at,1,5000,5,60);IOR=9;IOF=22;SASS={{0x10000,{0}},{0,{2,3}}};DSM=2;IOR;IOF;SASS;DSM;",

    B1: "iop(d,{2,3},1);iop(a, 5,{2},1);",
    B2: "iop(d,{2,3},1);iop(a, 0,{2},1);",
    B3: "iop(d,{2,3},1);iop(a, 17,{3},1);",
    B4: "iop(d,{2,3},1);iop(a, 3,{3},1);",
    B5: "iop(d,{2,3},1);iop(a, 3,{3},1);",
    B6: 'iop(d,{2,3},1);iop(a, 17,{3},1);anp(at,3,5000,5,60);IOR=10;IOF=21;SEB={"1991010","","","","",""};SASS={{0x20000,{0}},{0,{2,3}}};CANDEV=4;CANDEV;',
   
    C1: "iop(d,{4,5},1);iop(a, 0,{4},1);",
    C2: "iop(d,{4,5},1);iop(a, 5,{4},1);",
    C3: "iop(d,{4,5,8,9},1);iop(a, 25,{4,9},1);",
    C4: "iop(d,{4,5},1);iop(a, 3,{5},1);",
    C5: "iop(d,{4,5,8,9},1);iop(a, 10,{4},1);",

    D1: "iop(d,{6,7},1);iop(a, 4,{6},1);",
    D2: "iop(d,{6,7},1);iop(a, 0,{6},1);",
    D3: "iop(d,{4,5,8,9},1);iop(a, 10,{4},1);",

    E1: "iop(d,{8,9},1);iop(a, 10,{8},1);",
    E2: "iop(d,{8,9},1);iop(a, 0,{8},1);",
    E3: "iop(d,{8,9},1);iop(a, 5,{8},1);",
    E4: "iop(d,{8,9},1);iop(a, 3,{9},1);",
    E5: "iop(d,{8,9},1);iop(a, 11,{8,9},1);",

    F1: "CAN1={0,0,120};",
    F2: "CAN1={0,32,120};",
    F3: "CAN1={0,1,120};",
    F4: "CAN1={0,33,120};",
    F5: "CAN1={0,8,120};",
    F6: "CAN1={0,40,120};",
    F7: "CAN1={0,16,120};",
    F8: "CAN1={-1,0,120};",

    G1: "CAN2={0,0,120};",
    G2: "CAN2={0,32,120};",
    G3: "CAN2={0,1,120};",
    G4: "CAN2={0,33,120};",
    G5: "CAN2={0,8,120};",
    G6: "CAN2={0,40,120};",
    G7: "CAN2={0,16,120};",
    G8: "CAN2={-1,0,120};",
        
    H1: "iop(p);",
    H2: "iop(d,{0,1,2,3,4,5,6,7,8,9},1);",
    H3: "iop(d,{0,1,2,3,4,5,6,7,8,9},1);iop(a,0,{0,4},1);iop(a,5,{2},1);iop(a,4,{6},1);iop(a,10,{8},1);iop(p);",

    I1: "DSM=15;",
    I2: "DSM=3;",
    I3: "DSM=13;",
    I4: "DSM=1;",
    I5: "DSM=2;",
    I6: "DSM=8;",
    I7: "DSM;",
    
    J1: "GRM=2;",
    J2: "GRM=0;",
    J3: "GRM;",
    
    K1: "GPSANT;",
    K2: "GPSANT=0;",
    K3: "GPSANT=2;",
    K4: "GPSANT=1;",
    
    Z1: "ver();",
    Z2: "ver(can);",
    Z3: "reset();",
    Z4: "unit(spoo,f);",
    Z5: "pp();",
}

inverse_texty = {v: k for k, v in texty.items()}

# --- Rozložení rozhraní ---
st.markdown("### Nastavení vstupů NKP příkazy a další")

st.markdown("vzor sms zprávy poslané přes telefon: z001 12345678 NKP_příkaz")

# --- První řádek (CAN2 L, CAN1 L, IO1, +AKU, IO3, +30) ---
cols_top = st.columns([5, 5, 5, 5, 5, 5])
labels_top = ["CAN2 L", "CAN1 L", "IO1", "+AKU", "IO3", "+30"]

vybrane_texty = []
for i, label in enumerate(labels_top):
    with cols_top[i]:
        vybrano = st.selectbox(label, [""] + moznosti[label], key=label)
        if vybrano:
            vybrane_texty.append(texty.get(vybrano, ""))

# --- Druhý řádek (CAN2 H, CAN1 H, IO2, IO4, IO5, -30) ---
cols_bottom = st.columns([5, 5, 5, 5, 5, 5])
labels_bottom = ["CAN2 H", "CAN1 H", "IO2", "IO4", "IO5", "-30"]

for i, label in enumerate(labels_bottom):
    with cols_bottom[i]:
        vybrano = st.selectbox(label, [""] + moznosti[label], key=label)
        if vybrano:
            vybrane_texty.append(texty.get(vybrano, ""))

# --- Info k nastaveni CAN a D8 ---

st.markdown("Při nastavení FMS je třeba poslat ještě NKP příkaz: CANDEV=3840;\n\n Při nastavení D8 je třeba poslat ještě NKP příkaz: PUPD={0,1,0,1,1};")

# --- Třetí řádek (spínání od, roaming, GPS anténa, ostatní) ---
cols_down = st.columns([5, 5, 5, 5, 5])
labels_down = ["vstupy", "spínání od", "roaming", "GPS anténa", "ostatní"]

for i, label in enumerate(labels_down):
    with cols_down[i]:
        vybrano = st.selectbox(label, [""] + moznosti[label], key=label)
        if vybrano:
            vybrane_texty.append(texty.get(vybrano, ""))

# --- Výstupní textové pole ---
vystup = "".join(vybrane_texty)
st.text_area("NKP příkaz", value=vystup, height=200)

# --- Inverzní hledání (opačný směr) ---
input_text = st.text_area("Zadej NKP příkaz pro rozpoznání:", height=150)
if input_text:
    nalezene = [popis for kod, popis in inverse_texty.items() if input_text.strip() == kod.strip()]
    if nalezene:
        st.success("Vložený NKP příkaz odpovídá nastavením:")
        st.write(", ".join(nalezene))
    else:
        st.warning("Žádná shoda nenalezena.")
