import streamlit as st

# hodnoty vstupu
A1 = "digitální vstup"
A2 = "přepínač S/S"
A3 = "analogový vstup"
A4 = "5V zdroj (trvale)"
A5 = "5V zdroj (při +15)"
A6 = "in - OPER - nastavení pro APEX (generování poplachů dle SASS/GAS do OPERu na základě sepnutí IO1)"
A7 = "out - OPER - nastavení pro APEX (generování poplachů dle SASS/GAS do OPERu a sepnutí IO1)"
A8 = "výstup"
A9 = "AN - IBR"
B1 = "přepínač S/S"
B2 = "dig. vstup"
B3 = "analogový vstup"
B4 = "výstup"
B5 = "in - OPER -nastavení pro APEX (generování poplachů dle SASS/GAS do OPERu na základě sepnutí IO1)"
B6 = "AN - IBR"
C1 = "dig. vstup"
C2 = "přepínač S/S"
C3 = "váhy RVS"
C4 = "výstup"
C5 = "RFID"
D1 = "+15 drátová"
D2 = "dig. vstup"
D3 = "přepínač S/S"
E1 = "RFID"
E2 = "dig. vstup"
E3 = "přepínač S/S"
E4 = "výstup"
E5 = "Dallas - při použití teploměrů je nutné nastavit IO1 jako 5V zdroj pro jejich napájení"
F1 = "FMS rychlost 250"
F2 = "FMS rychlost 500"
F3 = "Full FMS rychlost 250"
F4 = "Full FMS rychlost 500"
F5 = "tachograf rychlost 250"
F6 = "tachograf rychlost 500"
F7 = "IBR, pouze čtení zprávy o celkovém stavu nádrže"
F8 = "zakázání CAN1"
G1 = "FMS rychlost 250"
G2 = "FMS rychlost 500"
G3 = "Full FMS rychlost 250"
G4 = "Full FMS rychlost 500"
G5 = "tachograf rychlost 250"
G6 = "tachograf rychlost 500"
G7 = "IBR, pouze čtení zprávy o celkovém stavu nádrže"
G8 = "zakázání CAN1"
H1 = "jizda dratova +15 + Acc + Nap"
H2 = "jizda dratova +15 + Acc"
H3 = "jizda dratova Acc + Nap"
H4 = "jízda ACC"
H5 = "jízda +15"
H6 = "jízda Nap"
I1 = "povolit"

# Možnosti pro jednotlivé vstupy
moznosti = {
    "IO1": [A1, A2, A3, A4, A5, A6, A7, A8, A9],
    "IO2": [B1, B2, B3, B4, B5, B6],
    "IO3": [C1, C2, C3, C4, C5],
    "IO4": [D1, D2, D3],
    "IO5": [E1, E2, E3, E4, E5],
    "CAN1": [F1, F2, F3, F4, F5, F6, F7, F8],
    "CAN2": [G1, G2, G3, G4, G5, G6, G7, G8],
    "Spínání od": [H1, H2, H3, H4, H5, H6],
    "Roaming": [I1]
}

# Texty
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
    B6: r"iop(d,{2,3},1);iop(a, 17,{3},1);anp(at,3,5000,5,60);IOR=10;IOF=21;SEB={'1991010','','','','',''};SASS={{0x20000,{0}},{0,{2,3}}};CANDEV=4;CANDEV;",
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
    H1: "DSM=15;",
    H2: "DSM=3;",
    H3: "DSM=13;",
    H4: "DSM=1;",
    H5: "DSM=2;",
    H6: "DSM=8;",
    I1: "GRM=2;"
}

st.title("Výběr možností")

vybrane_texty = []

# Pro každý vstup vytvoříme selectbox vedle názvu
for vstup, moznosti_list in moznosti.items():
    col1, col2 = st.columns([1, 2])  # první sloupec menší, druhý širší
    with col1:
        st.write(f"{vstup}:")
    with col2:
        vybrano = st.selectbox("", [""] + moznosti_list, key=vstup)
    if vybrano:
        vybrane_texty.append(texty[vybrano])

# Zobrazení výsledného textu
vystup = "".join(vybrane_texty)
st.text_area("Výstup (kopírovatelný)", value=vystup, height=250)