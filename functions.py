def venn_set(setlist): # receives number of sets and sets
    #check if "number of sets" and the number of "sets" given are the same
    from collections import Counter
    mysets=[]
    for item in setlist:
        mysets.append(item)
    
    numb = len(mysets)
    print(numb)
    sets = Counter() #set order: A, B, C, D, E, F
    if (numb == 6): ##for 6 different sets:
        A = mysets[0]
        B = mysets[1]
        C = mysets[2]
        D = mysets[3]
        E = mysets[4]
        F = mysets[5]
        #{a, b, c, d, e, f}
        sets['111111'] = len(A & B & C & D & E & F) #ABCDEF
        #{a, b, c, d, e}, {a, b, c, d, f}, {a, b, c, e, f}, {a, b, d, e, f}, {a, c, d, e, f}, {b, c, d, e, f},
        sets['111110'] = len((A & B & C & D & E) - F) #ABCDEf
        sets['111101'] = len((A & B & C & D & F) - E) #ABCDeF
        sets['111011'] = len((A & B & C & E & F) - D) #ABCdEF
        sets['110111'] = len((A & B & D & E & F) - C) #ABcDEF
        sets['101111'] = len((A & C & D & E & F) - B) #AbCDEF
        sets['011111'] = len((B & C & D & E & F) - A) #aBCDEF
        #{a, b, c, d}, {a, b, c, e}, {a, b, d, e}, {a, c, d, e}, {b, c, d, e}, {a, b, c, f}, {a, b, d, f}, {a, c, d, f}, {b, c, d, f}, {a, b, e, f}, {a, c, e, f}, {b, c, e, f}, {a, d, e, f}, {b, d, e, f}, {c, d, e, f},
        sets['111100'] = len((A & B & C & D) - E - F) #ABCDef
        sets['111010'] = len((A & B & C & E) - D - F) #ABCdEf
        sets['110110'] = len((A & B & D & E) - C - F) #ABcDEf
        sets['101110'] = len((A & C & D & E) - B - F) #AbCDEf
        sets['011110'] = len((B & C & D & E) - A - F) #aBCDEf
        sets['111001'] = len((A & B & C & F) - D - E) #ABCdeF
        sets['110101'] = len((A & B & D & F) - C - E) #ABcDeF
        sets['101101'] = len((A & C & D & F) - B - E) #AbCDeF
        sets['011101'] = len((B & C & D & F) - A - E) #aBCDeF
        sets['110011'] = len((A & B & E & F) - C - D) #ABcdEF
        sets['101011'] = len((A & C & E & F) - B - D) #AbCdEF
        sets['011011'] = len((B & C & E & F) - A - D) #aBCdEF
        sets['100111'] = len((A & D & E & F) - B - C) #AbcDEF
        sets['010111'] = len((B & D & E & F) - A - C) #aBcDEF
        sets['001111'] = len((C & D & E & F) - A - B) #abCDEF
        #{a, b, c}, {a, b, d}, {a, c, d}, {b, c, d}, {a, b, e}, {a, c, e}, {b, c, e}, {a, d, e}, {b, d, e}, {c, d, e}, {a, b, f}, {a, c, f}, {b, c, f}, {a, d, f}, {b, d, f}, {c, d, f}, {a, e, f}, {b, e, f}, {c, e, f}, {d, e, f},
        sets['111000'] = len((A & B & C) - D - E - F) #ABCdef
        sets['110100'] = len((A & B & D) - C - E - F) #ABcDef
        sets['101100'] = len((A & C & D) - B - E - F) #AbCDef
        sets['011100'] = len((B & C & D) - A - E - F) #aBCDef
        sets['110010'] = len((A & B & E) - C - D - F) #ABcdEf
        sets['101010'] = len((A & C & E) - B - D - F) #AbCdEf
        sets['011010'] = len((B & C & E) - A - D - F) #aBCdEf
        sets['100110'] = len((A & D & E) - B - C - F) #AbcDEf
        sets['010110'] = len((B & D & E) - A - C - F) #aBcDEf
        sets['001110'] = len((C & D & E) - A - B - F) #abCDEf
        sets['110001'] = len((A & B & F) - C - D - E) #ABcdeF
        sets['101001'] = len((A & C & F) - B - D - E) #AbCdeF
        sets['011001'] = len((B & C & F) - A - D - E) #aBCdeF
        sets['100101'] = len((A & D & F) - B - C - E) #AbcDeF
        sets['010101'] = len((B & D & F) - A - C - E) #aBcDeF
        sets['001101'] = len((C & D & F) - A - B - E) #abCDeF
        sets['100011'] = len((A & E & F) - B - C - D) #AbcdEF
        sets['010011'] = len((B & E & F) - A - C - D) #aBcdEF
        sets['001011'] = len((C & E & F) - A - B - D) #abCdEF
        sets['000111'] = len((D & E & F) - A - B - C) #abcDEF
        #{a, b}, {a, c}, {b, c}, {a, d}, {b, d}, {c, d}, {a, e}, {b, e}, {c, e}, {d, e}, {a, f}, {b, f}, {c, f}, {d, f}, {e, f},
        sets['110000'] = len((A & B) - C - D - E - F) #ABcdef
        sets['101000'] = len((A & C) - B - D - E - F) #AbCdef
        sets['011000'] = len((B & C) - A - D - E - F) #aBCdef
        sets['100100'] = len((A & D) - B - C - E - F) #AbcDef
        sets['010100'] = len((B & D) - A - C - E - F) #aBcDef
        sets['001100'] = len((C & D) - A - B - E - F) #abCDef
        sets['100010'] = len((A & E) - B - C - D - F) #AbcdEf
        sets['010010'] = len((B & E) - A - C - D - F) #aBcdEf
        sets['001010'] = len((C & E) - A - B - D - F) #abCdEf
        sets['000110'] = len((D & E) - A - B - C - F) #abcDEf
        sets['100001'] = len((A & F) - B - C - D - E) #AbcdeF
        sets['010001'] = len((B & F) - A - C - D - E) #aBcdeF
        sets['001001'] = len((C & F) - A - B - D - E) #abCdeF
        sets['000101'] = len((D & F) - A - B - C - E) #abcDeF
        sets['000011'] = len((E & F) - A - B - C - D) #abcdEF
        #{a}, {b}, {c}, {d}, {e}, {f},
        sets['100000'] = len(A - B - C - D - E - F) #Abcdef
        sets['010000'] = len(B - A - C - D - E - F) #aBcdef
        sets['001000'] = len(C - A - B - D - E - F) #abCdef
        sets['000100'] = len(D - A - B - C - E - F) #abcDef
        sets['000010'] = len(E - A - B - C - D - F) #abcdEf
        sets['000001'] = len(F - A - B - C - D - E) #abcdeF
    elif (numb == 5): # for 5 different sets:
        A = set(mysets[0])
        B = set(mysets[1])
        C = set(mysets[2])
        D = set(mysets[3])
        E = set(mysets[4])
        #{a}, {b}, {c}, {d}, {e},
        sets['10000'] = len(A - B - C - D - E) #Abcde
        sets['01000'] = len(B - A - C - D - E) #aBcde
        sets['00100'] = len(C - A - B - D - E) #abCde
        sets['00010'] = len(D - A - B - C - E) #abcDe
        sets['00001'] = len(E - A - B - C - D) #abcdE
        #{a, b}, {a, c}, {b, c}, {a, d}, {b, d}, {c, d}, {a, e}, {b, e}, {c, e}, {d, e}
        sets['11000'] = len((A & B) - C - D - E) #ABcde
        sets['10100'] = len((A & C) - B - D - E) #AbCde
        sets['01100'] = len((B & C) - A - D - E) #aBCde
        sets['10010'] = len((A & D) - B - C - E) #AbcDe
        sets['01010'] = len((B & D) - A - C - E) #aBcDe
        sets['00110'] = len((C & D) - A - B - E) #abCDe
        sets['10001'] = len((A & E) - B - C - D) #AbcdE
        sets['01001'] = len((B & E) - A - C - D) #aBcdE
        sets['00101'] = len((C & E) - A - B - D) #abCdE
        sets['00011'] = len((D & E) - A - B - C) #abcDE
        #{a, b, c}, {a, b, d}, {a, c, d}, {b, c, d}, {a, b, e}, {a, c, e}, {b, c, e}, {a, d, e}, {b, d, e}, {c, d, e},
        sets['11100'] = len((A & B & C) - D - E) #ABCde
        sets['11010'] = len((A & B & D) - C - E) #ABcDe
        sets['10110'] = len((A & C & D) - B - E) #AbCDe
        sets['01110'] = len((B & C & D) - A - E) #aBCDe
        sets['11001'] = len((A & B & E) - C - D) #ABcdE
        sets['10101'] = len((A & C & E) - B - D) #AbCdE
        sets['01101'] = len((B & C & E) - A - D) #aBCdE
        sets['10011'] = len((A & D & E) - B - C) #AbcDE
        sets['01011'] = len((B & D & E) - A - C) #aBcDE
        sets['00111'] = len((C & D & E) - A - B) #abCDE
        #{a, b, c, d}, {a, b, c, e}, {a, b, d, e}, {a, c, d, e}, {b, c, d, e},
        sets['11110'] = len((A & B & C & D) - E) #ABCDe
        sets['11101'] = len((A & B & C & E) - D) #ABCdE
        sets['11011'] = len((A & B & D & E) - C) #ABcDE
        sets['10111'] = len((A & C & D & E) - B) #AbCDE
        sets['01111'] = len((B & C & D & E) - A) #aBCDE
        #{a, b, c, d, e}
        sets['11111'] = len(A & B & C & D & E) #ABCDE
    elif (numb == 4): # for 4 different sets:
        A = set(mysets[0])
        B = set(mysets[1])
        C = set(mysets[2])
        D = set(mysets[3])
        #{a}, {b}, {c}, {d},
        sets['1000'] = len(A - B - C - D) #Abcd
        sets['0100'] = len(B - A - C - D) #aBcd
        sets['0010'] = len(C - A - B - D) #abCd
        sets['0001'] = len(D - A - B - C) #abcD
        #{a, b}, {a, c}, {b, c}, {a, d}, {b, d}, {c, d},
        sets['1100'] = len((A & B) - C - D) #ABcd
        sets['1010'] = len((A & C) - B - D) #AbCd
        sets['0110'] = len((B & C) - A - D) #aBCd
        sets['1001'] = len((A & D) - B - C) #AbcD
        sets['0101'] = len((B & D) - A - C) #aBcD
        sets['0011'] = len((C & D) - A - B) #abCD
        #{a, b, c}, {a, b, d}, {a, c, d}, {b, c, d},
        sets['1110'] = len((A & B & C) - D) #ABCd
        sets['1101'] = len((A & B & D) - C) #ABcD
        sets['1011'] = len((A & C & D) - B) #AbCD
        sets['0111'] = len((B & C & D) - A) #aBCD
        #{a, b, c, d}
        sets['1111'] = len(A & B & C & D) #ABCD
    elif (numb == 3): # for 3 different sets:
        A = set(mysets[0])
        B = set(mysets[1])
        C = set(mysets[2])
        #{a}, {b}, {c},
        sets['100'] = len(A - B - C) #Abc
        sets['010'] = len(B - A - C) #aBc
        sets['001'] = len(C - A - B) #abC
        #{a, b}, {a, c}, {b, c},
        sets['110'] = len((A & B) - C) #ABc
        sets['101'] = len((A & C) - B) #AbC
        sets['011'] = len((B & C) - A) #aBC
        #{a, b, c}
        sets['111'] = len(A & B & C) #ABC
    elif (numb == 2): # for 2 different sets:
        A = set(mysets[0])
        B = set(mysets[1])
        #{a}, {b},
        sets['10'] = len(A - B) #Ab
        sets['01'] = len(B - A) #aB
        #{a, b}
        sets['11'] = len(A & B) #ABc
    elif (numb == 7):
        A = set(mysets[0])
        B = set(mysets[1])
        C = set(mysets[2])
        D = set(mysets[3])
        E = set(mysets[4])
        F = set(mysets[5])
        G = set(mysets[6])
        # {a} {b} {c} {d} {e} {f} {g}
        sets['1000000'] = len(A - B - C - D - E - F - G) #Abcdefg
        sets['0100000'] = len(B - A - C - D - E - F - G) #aBcdefg
        sets['0010000'] = len(C - B - A - D - E - F - G) #abCdefg
        sets['0001000'] = len(D - B - C - A - E - F - G) #abcDefg
        sets['0000100'] = len(E - B - C - D - A - F - G) #abcdEfg
        sets['0000010'] = len(F - B - C - D - E - A - G) #abcdeFg
        sets['0000001'] = len(G - B - C - D - E - F - A) #abcdefG
        # {a,b} {a,c} {a,d} {a,e} {a,f} {a,g} {b,c} {b,d} {b,e} {b,f} {b,g}
        sets['1100000'] = len((A & B) - C - D - E - F - G) #ABcdefg
        sets['1010000'] = len((A & C) - B - D - E - F - G) #AbCdefg
        sets['1001000'] = len((A & D) - B - C - E - F - G) #AbcDefg
        sets['1000100'] = len((A & E) - B - C - D - F - G) #AbcdEfg
        sets['1000010'] = len((A & F) - B - C - D - E - G) #AbcdeFg
        sets['1000001'] = len((A & G) - B - C - D - E - F) #AbcdefG
        sets['0110000'] = len((B & C) - A - D - E - F - G) #aBCdefg
        sets['0101000'] = len((B & D) - A - C - E - F - G) #aBcDefg
        sets['0100100'] = len((B & E) - A - C - D - F - G) #aBcdEfg
        sets['0100010'] = len((B & F) - A - C - D - E - G) #aBcdeFg
        sets['0100001'] = len((B & G) - A - C - D - E - F) #aBcdefG
        # {c,d} {c,e} {c,f} {c,g} {d,e} {d,f} {d,g}
        sets['0011000'] = len((C & D) - A - B - E - F - G) #abCDefg
        sets['0010100'] = len((C & E) - A - B - D - F - G) #abCdEfg
        sets['0010010'] = len((C & F) - A - B - D - E - G) #abCdeFg
        sets['0010001'] = len((C & G) - A - B - D - E - F) #abCdefG
        sets['0001100'] = len((D & E) - A - B - C - F - G) #abcDEfg
        sets['0001010'] = len((D & F) - A - B - C - E - G) #abcDeFg
        sets['0001001'] = len((D & G) - A - B - C - E - F) #abcDefG
        # {e,f} {e,g} {f,g}
        sets['0000110'] = len((E & F) - A - B - C - D - G) #abcdEFg
        sets['0000101'] = len((E & G) - A - B - C - D - F) #abcdEfG
        sets['0000011'] = len((F & G) - A - B - C - D - E) #abcdeFG
        # {a,b,c} {a,b,d} {a,b,e} {a,b,f} {a,b,g} {a,c,d} {a,c,e} {a,c,f} {a,c,g}
        sets['1110000'] = len((A & B & C) - D - E - F - G) #ABCdefg
        sets['1101000'] = len((A & B & D) - C - E - F - G) #ABcDefg
        sets['1100100'] = len((A & B & E) - C - D - F - G) #ABcdEfg
        sets['1100010'] = len((A & B & F) - C - D - E - G) #ABcdeFg
        sets['1100001'] = len((A & B & G) - C - D - E - F) #ABcdefG
        sets['1011000'] = len((A & C & D) - B - E - F - G) #AbCDefg
        sets['1010100'] = len((A & C & E) - B - D - F - G) #AbCdEfg
        sets['1010010'] = len((A & C & F) - B - D - E - G) #AbCdeFg
        sets['1010001'] = len((A & C & G) - B - D - E - F) #AbCdefG
        # {a,d,e} {a,d,f} {a,d,g} {a,e,f} {a,e,g} {a,f,g}
        sets['1001100'] = len((A & D & E) - B - C - F - G) #AbcDEfg
        sets['1001010'] = len((A & D & F) - B - C - E - G) #AbcDeFg
        sets['1001001'] = len((A & D & G) - B - C - E - F) #AbcDefG
        sets['1000110'] = len((A & E & F) - B - C - D - G) #AbcdEFg
        sets['1000101'] = len((A & E & G) - B - C - D - F) #AbcdEfG
        sets['1000011'] = len((A & F & G) - B - C - D - E) #AbcdeFG
        # {b,c,d} {b,c,e} {b,c,f} {b,c,g} {b,d,e} {b,d,f}
        sets['0111000'] = len((B & C & D) - A - E - F - G) #aBCDefg
        sets['0110100'] = len((B & C & E) - A - D - F - G) #aBCdEfg
        sets['0110010'] = len((B & C & F) - A - D - E - G) #aBCdeFg
        sets['0110001'] = len((B & C & G) - A - D - E - F) #aBCdefG
        sets['0101100'] = len((B & D & E) - A - C - F - G) #aBcDEfg
        sets['0101010'] = len((B & D & F) - A - C - E - G) #aBcDeFg 
        # {b,d,g} {b,e,f} {b,e,g} {b,f,g}
        sets['0101001'] = len((B & D & G) - A - C - E - F) #aBcDefG
        sets['0100110'] = len((B & E & F) - A - C - D - G) #aBcdEFg
        sets['0100101'] = len((B & E & G) - A - C - D - F) #aBcdEFg
        sets['0100011'] = len((B & F & G) - A - C - D - E) #aBcdeFG
        # {c,d,e} {c,d,f} {c,d,g} {c,e,f} {c,e,g}
        sets['0011100'] = len((C & D & E) - A - B - F - G) #abCDEfg
        sets['0011010'] = len((C & D & F) - A - B - E - G) #abCDeFg
        sets['0011001'] = len((C & D & G) - A - B - E - F) #abCDefG
        sets['0010110'] = len((C & E & F) - A - B - D - G) #abCdEFg
        sets['0010101'] = len((C & E & G) - A - B - D - F) #abCdEfG
        # {c,f,g} {d,e,f} {d,e,g}
        sets['0010011'] = len((C & F & G) - A - B - D - E) #abCdeFG
        sets['0001110'] = len((D & E & F) - A - B - C - G) #abcDEFg
        sets['0001101'] = len((D & E & G) - A - B - C - F) #abcDEfG
        # {d,f,g} {e,f,g}
        sets['0001011'] = len((D & F & G) - A - B - C - E) #abcDeFG
        sets['0000111'] = len((E & F & G) - A - B - C - D) #abcdEFG
        # {a,b,c,d} {a,b,c,e} {a,b,c,f} {a,b,c,g} {a,b,d,e} {a,b,d,f} {a,b,d,g} {a,b,e,f} {a,b,e,g}
        sets['1111000'] = len((A & B & C & D) - E - F - G) #ABCDefg
        sets['1110100'] = len((A & B & C & E) - D - F - G) #ABCdEfg
        sets['1110010'] = len((A & B & C & F) - D - E - G) #ABCdeFg
        sets['1110001'] = len((A & B & C & G) - D - E - F) #ABCdefG
        sets['1101100'] = len((A & B & D & E) - C - F - G) #ABcDEfg
        sets['1101010'] = len((A & B & D & F) - C - E - G) #ABcDeFg
        sets['1101001'] = len((A & B & D & G) - C - E - F) #ABcDefG
        sets['1100110'] = len((A & B & E & F) - C - D - G) #ABcdEFg
        sets['1100101'] = len((A & B & E & G) - C - D - F) #ABcdEfG
        # {a,b,f,g} {a,c,d,e} {a,c,d,f}
        sets['1100011'] = len((A & B & F & G) - C - D - E) #ABcdeFG
        sets['1011100'] = len((A & C & D & E) - B - F - G) #AbCDEfg
        sets['1011010'] = len((A & C & D & F) - B - E - G) #AbCDeFg
        # {a,c,d,g} {a,c,e,f} {a,c,e,g} {a,c,f,g}
        sets['1011001'] = len((A & C & D & G) - B - E - F) #AbCDefG
        sets['1010110'] = len((A & C & E & F) - B - D - G) #AbCdEFg
        sets['1010101'] = len((A & C & E & G) - B - D - F) #AbCdEfG
        sets['1010011'] = len((A & C & F & G) - B - D - E) #AbCdeFG
        # {a,d,e,f} {a,d,e,g} {a,d,f,g}
        sets['1001110'] = len((A & D & E & F) - B - C - G) #AbcDEFg
        sets['1001101'] = len((A & D & E & G) - B - C - F) #AbcDEfG
        sets['1001011'] = len((A & D & F & G) - B - C - E) #AbcDeFG
        # {a,e,f,g}
        sets['1000111'] = len((A & E & F & G) - B - C - D) #AbcdEFG
        # {b,c,d,e} {b,c,d,f} {b,c,d,g}
        sets['0111100'] = len((B & C & D & E) - A - F - G) #aBCDEfg
        sets['0111010'] = len((B & C & D & F) - A - E - G) #aBCDeFg
        sets['0111001'] = len((B & C & D & G) - A - E - F) #aBCDefG
        # {b,c,e,f} {b,c,e,g} {b,c,f,g}
        sets['0110110'] = len((B & C & E & F) - A - D - G) #aBCdEFg
        sets['0110101'] = len((B & C & E & G) - A - D - F) #aBCdEfG
        sets['0110011'] = len((B & C & F & G) - A - D - E) #aBCdeFG
        # {b,d,e,f} {b,d,e,g} {b,d,f,g}
        sets['0101110'] = len((B & D & E & F) - A - C - G) #aBcDEFg
        sets['0101101'] = len((B & D & E & G) - A - C - F) #aBcDEfG
        sets['0101011'] = len((B & D & F & G) - A - C - E) #aBcDeFG
        # {b,e,f,g}
        sets['0100111'] = len((B & E & F & G) - A - C - D) #aBcdEFG
        # {c,d,e,f} {c,d,e,g} {c,d,f,g}
        sets['0011110'] = len((C & D & E & F) - A - B - G) #abCDEFg
        sets['0011101'] = len((C & D & E & G) - A - B - F) #abCDEfG
        sets['0011011'] = len((C & D & F & G) - A - B - E) #abCDeFG
        # {c,e,f,g}
        sets['0010111'] = len((C & E & F & G) - A - B - D) #abCdEFG
        # {d,e,f,g}
        sets['0001111'] = len((D & E & F & G) - A - B - C) #abcDEFG
        # {a,b,c,d,e} {a,b,c,d,f} {a,b,c,d,g}
        sets['1111100'] = len((A & B & C & D & E) - F - G) #ABCDEfg
        sets['1111010'] = len((A & B & C & D & F) - E - G) #ABCDeFg
        sets['1111001'] = len((A & B & C & D & G) - E - F) #ABCDefG
        # {a,b,c,e,f} {a,b,c,e,g} {a,b,c,f,g}
        sets['1110110'] = len((A & B & C & E & F) - D - G) #ABCdEFg
        sets['1110101'] = len((A & B & C & E & G) - D - F) #ABCdEfG
        sets['1110011'] = len((A & B & C & F & G) - D - E) #ABCdeFG
        # {a,b,d,e,f} {a,b,d,e,g}
        sets['1101110'] = len((A & B & D & E & F) - C - G) #ABcDEFg
        sets['1101101'] = len((A & B & D & E & G) - C - F) #ABcDEfG
        # {a,b,d,f,g}
        sets['1101011'] = len((A & B & D & F & G) - C - E) #ABcDeFG
        # {a,b,e,f,g}
        sets['1100111'] = len((A & B & E & F & G) - C - D) #ABcdEFG
        # {a,c,d,e,f} {a,c,d,e,g}
        sets['1011110'] = len((A & C & D & E & F) - B - G) #AbCDEFg
        sets['1011101'] = len((A & C & D & E & G) - B - F) #AbCDEfG
        # {a,c,d,f,g}
        sets['1011011'] = len((A & C & D & F & G) - B - E) #AbCDeFG
        # {a,c,e,f,g}
        sets['1010111'] = len((A & C & E & F & G) - B - D) #AbCdEFG
        # {a,d,e,f,g}
        sets['1001111'] = len((A & D & E & F & G) - B - C) #AbcDEFG
        # {b,c,d,e,f} {b,c,d,e,g}
        sets['0111110'] = len((B & C & D & E & F) - A - G) #aBCDEFg
        sets['0111101'] = len((B & C & D & E & G) - A - F) #aBCDEfG
        # {b,c,d,f,g}
        sets['0111011'] = len((B & C & D & F & G) - A - E) #aBCDeFG
        # {b,c,e,f,g}
        sets['0110111'] = len((B & C & E & F & G) - A - D) #aBCdEFG
        # {b,d,e,f,g}
        sets['0101111'] = len((B & D & E & F & G) - A - C) #aBcDEFG
        # {c,d,e,f,g}
        sets['0011111'] = len((C & D & E & F & G) - A - B) #abCDEFG
        # {a,b,c,d,e,f} {a,b,c,d,e,g} {a,b,c,d,f,g}
        sets['1111110'] = len((A & B & C & D & E & F) - G) #ABCDEFg
        sets['1111101'] = len((A & B & C & D & E & G) - F) #ABCDEfG
        sets['1111011'] = len((A & B & C & D & F & G) - E) #ABCDeFG
        # {a,b,c,e,f,g}
        sets['1110111'] = len((A & B & C & E & F & G) - D) #ABCdEFG
        # {a,b,d,e,f,g}
        sets['1101111'] = len((A & B & D & E & F & G) - C) #ABcDEFG
        # {a,c,d,e,f,g}
        sets['1011111'] = len((A & C & D & E & F & G) - B) #AbCDEFG
        # {b,c,d,e,f,g}
        sets['0111111'] = len((B & C & D & E & F & G) - A) #aBCDEFG
        # {a,b,c,d,e,f,g}
        sets['1111111'] = len(A & B & C & D & E & F & G) #ABCDEFG
    elif (numb == 8):
        A = set(mysets[0])
        B = set(mysets[1])
        C = set(mysets[2])
        D = set(mysets[3])
        E = set(mysets[4])
        F = set(mysets[5])
        G = set(mysets[6])
        H = set(mysets[7])
        # {a} {b} {c} {d} {e} {f} {g} {h}
        sets['10000000'] = len(A - B - C - D - E - F - G - H) #Abcdefgh
        sets['01000000'] = len(B - A - C - D - E - F - G - H) #aBcdefgh
        sets['00100000'] = len(C - B - A - D - E - F - G - H) #abCdefgh
        sets['00010000'] = len(D - B - C - A - E - F - G - H) #abcDefgh
        sets['00001000'] = len(E - B - C - D - A - F - G - H) #abcdEfgh
        sets['00000100'] = len(F - B - C - D - E - A - G - H) #abcdeFgh
        sets['00000010'] = len(G - B - C - D - E - F - A - H) #abcdefGh
        sets['00000001'] = len(H - B - C - D - E - F - G - A) #abcdefgH
        # {a,b} {a,c} {a,d} {a,e} {a,f} {a,g} {a,h} {b,c} {b,d} {b,e} {b,f} {b,g} {b,h}
        sets['11000000'] = len((A & B) - C - D - E - F - G - H) #ABcdefgh
        sets['10100000'] = len((A & C) - B - D - E - F - G - H) #AbCdefgh
        sets['10010000'] = len((A & D) - B - C - E - F - G - H) #AbcDefgh
        sets['10001000'] = len((A & E) - B - C - D - F - G - H) #AbcdEfgh
        sets['10000100'] = len((A & F) - B - C - D - E - G - H) #AbcdeFgh
        sets['10000010'] = len((A & G) - B - C - D - E - F - H) #AbcdefGh
        sets['10000001'] = len((A & H) - B - C - D - E - F - G) #AbcdefgH
        sets['01100000'] = len((B & C) - A - D - E - F - G - H) #aBCdefgh
        sets['01010000'] = len((B & D) - A - C - E - F - G - H) #aBcDefgh
        sets['01001000'] = len((B & E) - A - C - D - F - G - H) #aBcdEfgh
        sets['01000100'] = len((B & F) - A - C - D - E - G - H) #aBcdeFgh
        sets['01000010'] = len((B & G) - A - C - D - E - F - H) #aBcdefGh
        sets['01000001'] = len((B & H) - A - C - D - E - F - G) #aBcdefgH
        # {c,d} {c,e} {c,f} {c,g} {c,h} {d,e} {d,f} {d,g} {d,h}
        sets['00110000'] = len((C & D) - A - B - E - F - G - H) #abCDefgh
        sets['00101000'] = len((C & E) - A - B - D - F - G - H) #abCdEfgh
        sets['00100100'] = len((C & F) - A - B - D - E - G - H) #abCdeFgh
        sets['00100010'] = len((C & G) - A - B - D - E - F - H) #abCdefGh
        sets['00100001'] = len((C & H) - A - B - D - E - F - G) #abCdefgH
        sets['00011000'] = len((D & E) - A - B - C - F - G - H) #abcDEfgh
        sets['00010100'] = len((D & F) - A - B - C - E - G - H) #abcDeFgh
        sets['00010010'] = len((D & G) - A - B - C - E - F - H) #abcDefGh
        sets['00010001'] = len((D & H) - A - B - C - E - F - G) #abcDefgH
        # {e,f} {e,g} {e,h} {f,g} {f,h} {g,h}
        sets['00001100'] = len((E & F) - A - B - C - D - G - H) #abcdEFgh
        sets['00001010'] = len((E & G) - A - B - C - D - F - H) #abcdEfGh
        sets['00001001'] = len((E & H) - A - B - C - D - F - G) #abcdEfgH
        sets['00000110'] = len((F & G) - A - B - C - D - E - H) #abcdeFGh
        sets['00000101'] = len((F & H) - A - B - C - D - E - G) #abcdeFgH
        sets['00000011'] = len((G & H) - A - B - C - D - E - F) #abcdefGH
        # {a,b,c} {a,b,d} {a,b,e} {a,b,f} {a,b,g} {a,b,h} {a,c,d} {a,c,e} {a,c,f} {a,c,g} {a,c,h}
        sets['11100000'] = len((A & B & C) - D - E - F - G - H) #ABCdefgh
        sets['11010000'] = len((A & B & D) - C - E - F - G - H) #ABcDefgh
        sets['11001000'] = len((A & B & E) - C - D - F - G - H) #ABcdEfgh
        sets['11000100'] = len((A & B & F) - C - D - E - G - H) #ABcdeFgh
        sets['11000010'] = len((A & B & G) - C - D - E - F - H) #ABcdefGh
        sets['11000001'] = len((A & B & H) - C - D - E - F - G) #ABcdefgH
        sets['10110000'] = len((A & C & D) - B - E - F - G - H) #AbCDefgh
        sets['10101000'] = len((A & C & E) - B - D - F - G - H) #AbCdEfgh
        sets['10100100'] = len((A & C & F) - B - D - E - G - H) #AbCdeFgh
        sets['10100010'] = len((A & C & G) - B - D - E - F - H) #AbCdefGh
        sets['10100001'] = len((A & C & H) - B - D - E - F - G) #AbCdefgH
        # {a,d,e} {a,d,f} {a,d,g} {a,d,h} {a,e,f} {a,e,g} {a,e,h} {a,f,g} {a,f,h}
        sets['10011000'] = len((A & D & E) - B - C - F - G - H) #AbcDEfgh
        sets['10010100'] = len((A & D & F) - B - C - E - G - H) #AbcDeFgh
        sets['10010010'] = len((A & D & G) - B - C - E - F - H) #AbcDefGh
        sets['10010001'] = len((A & D & H) - B - C - E - F - G) #AbcDefgH
        sets['10001100'] = len((A & E & F) - B - C - D - G - H) #AbcdEFgh
        sets['10001010'] = len((A & E & G) - B - C - D - F - H) #AbcdEfGh
        sets['10001001'] = len((A & E & H) - B - C - D - F - G) #AbcdEfgH
        sets['10000110'] = len((A & F & G) - B - C - D - E - H) #AbcdeFGh
        sets['10000101'] = len((A & F & H) - B - C - D - E - G) #AbcdeFgH
        # {a,g,h} {b,c,d} {b,c,e} {b,c,f} {b,c,g} {b,c,h} {b,d,e} {b,d,f}
        sets['10000011'] = len((A & G & H) - B - C - D - E - F) #AbcdefGH
        sets['01110000'] = len((B & C & D) - A - E - F - G - H) #aBCDefgh
        sets['01101000'] = len((B & C & E) - A - D - F - G - H) #aBCdEfgh
        sets['01100100'] = len((B & C & F) - A - D - E - G - H) #aBCdeFgh
        sets['01100010'] = len((B & C & G) - A - D - E - F - H) #aBCdefGh
        sets['01100001'] = len((B & C & H) - A - D - E - F - G) #aBCdefgH
        sets['01011000'] = len((B & D & E) - A - C - F - G - H) #aBcDEfgh
        sets['01010100'] = len((B & D & F) - A - C - E - G - H) #aBcDeFgh 
        # {b,d,g} {b,d,h} {b,e,f} {b,e,g} {b,e,h} {b,f,g} {b,f,h} {b,g,h}
        sets['01010010'] = len((B & D & G) - A - C - E - F - H) #aBcDefGh
        sets['01010001'] = len((B & D & H) - A - C - E - F - G) #aBcDefgH
        sets['01001100'] = len((B & E & F) - A - C - D - G - H) #aBcdEFgh
        sets['01001010'] = len((B & E & G) - A - C - D - F - H) #aBcdEFgh
        sets['01001001'] = len((B & E & H) - A - C - D - F - G) #aBcdEfgH
        sets['01000110'] = len((B & F & G) - A - C - D - E - H) #aBcdeFGh
        sets['01000101'] = len((B & F & H) - A - C - D - E - G) #aBcdeFgH
        sets['01000011'] = len((B & G & H) - A - C - D - E - F) #aBcdefGH
        # {c,d,e} {c,d,f} {c,d,g} {c,d,h} {c,e,f} {c,e,g} {c,e,h}
        sets['00111000'] = len((C & D & E) - A - B - F - G - H) #abCDEfgh
        sets['00110100'] = len((C & D & F) - A - B - E - G - H) #abCDeFgh
        sets['00110010'] = len((C & D & G) - A - B - E - F - H) #abCDefGh
        sets['00110001'] = len((C & D & H) - A - B - E - F - G) #abCDefgH
        sets['00101100'] = len((C & E & F) - A - B - D - G - H) #abCdEFgh
        sets['00101010'] = len((C & E & G) - A - B - D - F - H) #abCdEfGh
        sets['00101001'] = len((C & E & H) - A - B - D - F - G) #abCdEfgH
        # {c,f,g} {c,f,h} {c,g,h} {d,e,f} {d,e,g} {d,e,h}
        sets['00100110'] = len((C & F & G) - A - B - D - E - H) #abCdeFGh
        sets['00100101'] = len((C & F & H) - A - B - D - E - G) #abCdeFgH
        sets['00100011'] = len((C & G & H) - A - B - D - E - F) #abCdefGH
        sets['00011100'] = len((D & E & F) - A - B - C - G - H) #abcDEFgh
        sets['00011010'] = len((D & E & G) - A - B - C - F - H) #abcDEfGh
        sets['00011001'] = len((D & E & H) - A - B - C - F - G) #abcDEfgH
        # {d,f,g} {d,f,h} {d,g,h} {e,f,g} {e,f,h} {e,g,h}
        sets['00010110'] = len((D & F & G) - A - B - C - E - H) #abcDeFGh
        sets['00010101'] = len((D & F & H) - A - B - C - E - G) #abcDeFgH
        sets['00010011'] = len((D & G & H) - A - B - C - E - F) #abcDefGH
        sets['00001110'] = len((E & F & G) - A - B - C - D - H) #abcdEFGh
        sets['00001101'] = len((E & F & H) - A - B - C - D - G) #abcdEFgH
        sets['00001011'] = len((E & G & H) - A - B - C - D - F) #abcdEfGH
        # {f,g,h}
        sets['00000111'] = len((F & G & H) - A - B - C - D - E) #abcdeFGH
        # {a,b,c,d} {a,b,c,e} {a,b,c,f} {a,b,c,g} {a,b,c,h} {a,b,d,e} {a,b,d,f} {a,b,d,g} {a,b,d,h} {a,b,e,f} {a,b,e,g}
        sets['11110000'] = len((A & B & C & D) - E - F - G - H) #ABCDefgh
        sets['11101000'] = len((A & B & C & E) - D - F - G - H) #ABCdEfgh
        sets['11100100'] = len((A & B & C & F) - D - E - G - H) #ABCdeFgh
        sets['11100010'] = len((A & B & C & G) - D - E - F - H) #ABCdefGh
        sets['11100001'] = len((A & B & C & H) - D - E - F - G) #ABCdefgH
        sets['11011000'] = len((A & B & D & E) - C - F - G - H) #ABcDEfgh
        sets['11010100'] = len((A & B & D & F) - C - E - G - H) #ABcDeFgh
        sets['11010010'] = len((A & B & D & G) - C - E - F - H) #ABcDefGh
        sets['11010001'] = len((A & B & D & H) - C - E - F - G) #ABcDefgH
        sets['11001100'] = len((A & B & E & F) - C - D - G - H) #ABcdEFgh
        sets['11001010'] = len((A & B & E & G) - C - D - F - H) #ABcdEfGh
        # {a,b,e,h} {a,b,f,g} {a,b,f,h} {a,b,g,h} {a,c,d,e} {a,c,d,f}
        sets['11001001'] = len((A & B & E & H) - C - D - F - G) #ABcdEfgH
        sets['11000110'] = len((A & B & F & G) - C - D - E - H) #ABcdeFGh
        sets['11000101'] = len((A & B & F & H) - C - D - E - G) #ABcdeFgH
        sets['11000011'] = len((A & B & G & H) - C - D - E - F) #ABcdefGH
        sets['10111000'] = len((A & C & D & E) - B - F - G - H) #AbCDEfgh
        sets['10110100'] = len((A & C & D & F) - B - E - G - H) #AbCDeFgh
        # {a,c,d,g} {a,c,d,h} {a,c,e,f} {a,c,e,g} {a,c,e,h} {a,c,f,g} {a,c,f,h} {a,c,g,h}
        sets['10110010'] = len((A & C & D & G) - B - E - F - H) #AbCDefGh
        sets['10110001'] = len((A & C & D & H) - B - E - F - G) #AbCDefgH
        sets['10101100'] = len((A & C & E & F) - B - D - G - H) #AbCdEFgh
        sets['10101010'] = len((A & C & E & G) - B - D - F - H) #AbCdEfGh
        sets['10101001'] = len((A & C & E & H) - B - D - F - G) #AbCdEfgH
        sets['10100110'] = len((A & C & F & G) - B - D - E - H) #AbCdeFGh
        sets['10100101'] = len((A & C & F & H) - B - D - E - G) #AbCdeFgH
        sets['10100011'] = len((A & C & G & H) - B - D - E - F) #AbCdefGH
        # {a,d,e,f} {a,d,e,g} {a,d,e,h} {a,d,f,g} {a,d,f,h} {a,d,g,h}
        sets['10011100'] = len((A & D & E & F) - B - C - G - H) #AbcDEFgh
        sets['10011010'] = len((A & D & E & G) - B - C - F - H) #AbcDEfGh
        sets['10011001'] = len((A & D & E & H) - B - C - F - G) #AbcDEfgH
        sets['10010110'] = len((A & D & F & G) - B - C - E - H) #AbcDeFGh
        sets['10010101'] = len((A & D & F & H) - B - C - E - G) #AbcDeFgH
        sets['10010011'] = len((A & D & G & H) - B - C - E - F) #AbcDefGH
        # {a,e,f,g} {a,e,f,h} {a,e,g,h} {a,f,g,h}
        sets['10001110'] = len((A & E & F & G) - B - C - D - H) #AbcdEFGh
        sets['10001101'] = len((A & E & F & H) - B - C - D - G) #AbcdEFgH
        sets['10001011'] = len((A & E & G & H) - B - C - D - F) #AbcdEfGH
        sets['10000111'] = len((A & F & G & H) - B - C - D - E) #AbcdeFGH
        # {b,c,d,e} {b,c,d,f} {b,c,d,g} {b,c,d,h}
        sets['01111000'] = len((B & C & D & E) - A - F - G - H) #aBCDEfgh
        sets['01110100'] = len((B & C & D & F) - A - E - G - H) #aBCDeFgh
        sets['01110010'] = len((B & C & D & G) - A - E - F - H) #aBCDefGh
        sets['01110001'] = len((B & C & D & H) - A - E - F - G) #aBCDefgH
        # {b,c,e,f} {b,c,e,g} {b,c,e,h} {b,c,f,g} {b,c,f,h} {b,c,g,h}
        sets['01101100'] = len((B & C & E & F) - A - D - G - H) #aBCdEFgh
        sets['01101010'] = len((B & C & E & G) - A - D - F - H) #aBCdEfGh
        sets['01101001'] = len((B & C & E & H) - A - D - F - G) #aBCdEfgH
        sets['01100110'] = len((B & C & F & G) - A - D - E - H) #aBCdeFGh
        sets['01100101'] = len((B & C & F & H) - A - D - E - G) #aBCdeFgH
        sets['01100011'] = len((B & C & G & H) - A - D - E - F) #aBCdefGH
        # {b,d,e,f} {b,d,e,g} {b,d,e,h} {b,d,f,g} {b,d,f,h} {b,d,g,h}
        sets['01011100'] = len((B & D & E & F) - A - C - G - H) #aBcDEFgh
        sets['01011010'] = len((B & D & E & G) - A - C - F - H) #aBcDEfGh
        sets['01011001'] = len((B & D & E & H) - A - C - F - G) #aBcDEfgH
        sets['01010110'] = len((B & D & F & G) - A - C - E - H) #aBcDeFGh
        sets['01010101'] = len((B & D & F & H) - A - C - E - G) #aBcDeFgH
        sets['01010011'] = len((B & D & G & H) - A - C - E - F) #aBcDefGH
        # {b,e,f,g} {b,e,f,h} {b,e,g,h} {b,f,g,h}
        sets['01001110'] = len((B & E & F & G) - A - C - D - H) #aBcdEFGh
        sets['01001101'] = len((B & E & F & H) - A - C - D - G) #aBcdEFgH
        sets['01001011'] = len((B & E & G & H) - A - C - D - F) #aBcdEfGH
        sets['01000111'] = len((B & F & G & H) - A - C - D - E) #aBcdeFGH
        # {c,d,e,f} {c,d,e,g} {c,d,e,h} {c,d,f,g} {c,d,f,h} {c,d,g,h}
        sets['00111100'] = len((C & D & E & F) - A - B - G - H) #abCDEFgh
        sets['00111010'] = len((C & D & E & G) - A - B - F - H) #abCDEfGh
        sets['00111001'] = len((C & D & E & H) - A - B - F - G) #abCDEfgH
        sets['00110110'] = len((C & D & F & G) - A - B - E - H) #abCDeFGh
        sets['00110101'] = len((C & D & F & H) - A - B - E - G) #abCDeFgH
        sets['00110011'] = len((C & D & G & H) - A - B - E - F) #abCDefGH
        # {c,e,f,g} {c,e,f,h} {c,e,g,h}
        sets['00101110'] = len((C & E & F & G) - A - B - D - H) #abCdEFGh
        sets['00101101'] = len((C & E & F & H) - A - B - D - G) #abCdEFgH
        sets['00101011'] = len((C & E & G & H) - A - B - D - F) #abCdEfGH
        # {c,f,g,h} {d,e,f,g} {d,e,f,h} {d,e,g,h}
        sets['00100111'] = len((C & F & G & H) - A - B - D - E) #abCdeFGH
        sets['00011110'] = len((D & E & F & G) - A - B - C - H) #abcDEFGh
        sets['00011101'] = len((D & E & F & H) - A - B - C - G) #abcDEFgH
        sets['00011011'] = len((D & E & G & H) - A - B - C - F) #abcDEfGH
        # {d,f,g,h}
        sets['000101110'] = len((D & F & G & H) - A - B - C - E) #abcDeFGH
        # {e,f,g,h}
        sets['00001111'] = len((E & F & G & H) - A - B - C - D) #abcdEFGH
        # {a,b,c,d,e} {a,b,c,d,f} {a,b,c,d,g} {a,b,c,d,h}
        sets['11111000'] = len((A & B & C & D & E) - F - G - H) #ABCDEfgh
        sets['11110100'] = len((A & B & C & D & F) - E - G - H) #ABCDeFgh
        sets['11110010'] = len((A & B & C & D & G) - E - F - H) #ABCDefGh
        sets['11110001'] = len((A & B & C & D & H) - E - F - G) #ABCDefgH
        # {a,b,c,e,f} {a,b,c,e,g} {a,b,c,e,h} {a,b,c,f,g} {a,b,c,f,h}
        sets['11101100'] = len((A & B & C & E & F) - D - G - H) #ABCdEFgh
        sets['11101010'] = len((A & B & C & E & G) - D - F - H) #ABCdEfGh
        sets['11101001'] = len((A & B & C & E & H) - D - F - G) #ABCdEfgH
        sets['11100110'] = len((A & B & C & F & G) - D - E - H) #ABCdeFGh
        sets['11100101'] = len((A & B & C & F & H) - D - E - G) #ABCdeFgH
        # {a,b,c,g,h}
        sets['11100011'] = len((A & B & C & G & H) - D - E - F) #ABCdefGH
        # {a,b,d,e,f} {a,b,d,e,g} {a,b,d,e,h}
        sets['11011100'] = len((A & B & D & E & F) - C - G - H) #ABcDEFgh
        sets['11011010'] = len((A & B & D & E & G) - C - F - H) #ABcDEfGh
        sets['11011001'] = len((A & B & D & E & H) - C - F - G) #ABcDEfgH
        # {a,b,d,f,g} {a,b,d,f,h} {a,b,d,g,h}
        sets['11010110'] = len((A & B & D & F & G) - C - E - H) #ABcDeFGh
        sets['11010101'] = len((A & B & D & F & H) - C - E - G) #ABcDeFgH
        sets['11010011'] = len((A & B & D & G & H) - C - E - F) #ABcDefGH
        # {a,b,e,f,g} {a,b,e,f,h}
        sets['11001110'] = len((A & B & E & F & G) - C - D - H) #ABcdEFGh
        sets['11001101'] = len((A & B & E & F & H) - C - D - G) #ABcdEFgH
        # {a,b,e,g,h}
        sets['11001011'] = len((A & B & E & G & H) - C - D - F) #ABcdEfGH
        # {a,b,f,g,h}
        sets['11000111'] = len((A & B & F & G & H) - C - D - E) #ABcdeFGH
        # {a,c,d,e,f} {a,c,d,e,g}
        sets['10111100'] = len((A & C & D & E & F) - B - G - H) #AbCDEFgh
        sets['10111010'] = len((A & C & D & E & G) - B - F - H) #AbCDEfGh
        # {a,c,d,e,h} {a,c,d,f,g} {a,c,d,f,h}
        sets['10111001'] = len((A & C & D & E & H) - B - F - G) #AbCDEfgH
        sets['10110110'] = len((A & C & D & F & G) - B - E - H) #AbCDeFGh
        sets['10110101'] = len((A & C & D & F & H) - B - E - G) #AbCDeFgH
        # {a,c,d,g,h} {a,c,e,f,g}
        sets['10110011'] = len((A & C & D & G & H) - B - E - F) #AbCDefGH
        sets['10101110'] = len((A & C & E & F & G) - B - D - H) #AbCdEFGh
        # {a,c,e,f,h} {a,c,e,g,h}
        sets['10101101'] = len((A & C & E & F & H) - B - D - G) #AbCdEFgH
        sets['10101011'] = len((A & C & E & G & H) - B - D - F) #AbCdEfGH
        # {a,c,f,g,h}
        sets['10100111'] = len((A & C & F & G & H) - B - D - E) #AbCdeFGH
        # {a,d,e,f,g} {a,d,e,f,h} {a,d,e,g,h}
        sets['10011110'] = len((A & D & E & F & G) - B - C - H) #AbcDEFGh
        sets['10011101'] = len((A & D & E & F & H) - B - C - G) #AbcDEFgH
        sets['10011011'] = len((A & D & E & G & H) - B - C - F) #AbcDEfGH
        # {a,d,f,g,h}
        sets['10010111'] = len((A & D & F & G & H) - B - C - E) #AbcDeFGH
        # {a,e,f,g,h}
        sets['10001111'] = len((A & E & F & G & H) - B - C - D) #AbcdEFGH
        # {b,c,d,e,f} {b,c,d,e,g} {b,c,d,e,h}
        sets['01111100'] = len((B & C & D & E & F) - A - G - H) #aBCDEFgh
        sets['01111010'] = len((B & C & D & E & G) - A - F - H) #aBCDEfGh
        sets['01111001'] = len((B & C & D & E & H) - A - F - G) #aBCDEfgH
        # {b,c,d,f,g} {b,c,d,f,h} {b,c,d,g,h}
        sets['01110110'] = len((B & C & D & F & G) - A - E - H) #aBCDeFGh
        sets['01110111'] = len((B & C & D & F & H) - A - E - G) #aBCDeFgH
        sets['01110011'] = len((B & C & D & G & H) - A - E - F) #aBCDefGH
        # {b,c,e,f,g} {b,c,e,f,h}
        sets['01101110'] = len((B & C & E & F & G) - A - D - H) #aBCdEFGh
        sets['01101101'] = len((B & C & E & F & H) - A - D - G) #aBCdEFgH
        # {b,c,e,g,h}
        sets['01101011'] = len((B & C & E & G & H) - A - D - F) #aBCdEfGH
        # {b,c,f,g,h}
        sets['01100111'] = len((B & C & F & G & H) - A - D - E) #aBCdeFGH
        # {b,d,e,f,g}
        sets['01011110'] = len((B & D & E & F & G) - A - C - H) #aBcDEFGh
        # {b,d,e,f,h} {b,d,e,g,h}
        sets['01011101'] = len((B & D & E & F & H) - A - C - G) #aBcDEFgH
        sets['01011011'] = len((B & D & E & G & H) - A - C - F) #aBcDEfGH
        # {b,d,f,g,h}
        sets['01010111'] = len((B & D & F & G & H) - A - C - E) #aBcDeFGH
        # {b,e,f,g,h}
        sets['01001111'] = len((B & E & F & G & H) - A - C - D) #aBcdEFGH
        # {c,d,e,f,g} {c,d,e,f,h} {c,d,e,g,h}
        sets['00111110'] = len((C & D & E & F & G) - A - B - H) #abCDEFGh
        sets['00111101'] = len((C & D & E & F & H) - A - B - G) #abCDEFgH
        sets['00111011'] = len((C & D & E & G & H) - A - B - F) #abCDEfGH
        # {c,d,f,g,h}
        sets['00110111'] = len((C & D & F & G & H) - A - B - E) #abCDeFGH
        # {c,e,f,g,h}
        sets['00101111'] = len((C & E & F & G & H) - A - B - D) #abCdEFGH
        # {d,e,f,g,h}
        sets['00011111'] = len((D & E & F & G & H) - A - B - C) #abcDEFGH
        # {a,b,c,d,e,f} {a,b,c,d,e,g} {a,b,c,d,e,h} {a,b,c,d,f,g} {a,b,c,d,f,h} {a,b,c,d,g,h}
        sets['11111100'] = len((A & B & C & D & E & F) - G - H) #ABCDEFgh
        sets['11111010'] = len((A & B & C & D & E & G) - F - H) #ABCDEfGh
        sets['11111001'] = len((A & B & C & D & E & H) - F - G) #ABCDEfgH
        sets['11110110'] = len((A & B & C & D & F & G) - E - H) #ABCDeFGh
        sets['11110101'] = len((A & B & C & D & F & H) - E - G) #ABCDeFgH
        sets['11110011'] = len((A & B & C & D & G & H) - E - F) #ABCDefGH
        # {a,b,c,e,f,g} {a,b,c,e,f,h} {a,b,c,e,g,h}
        sets['11101110'] = len((A & B & C & E & F & G) - D - H) #ABCdEFGh
        sets['11101101'] = len((A & B & C & E & F & H) - D - G) #ABCdEFgH
        sets['11101011'] = len((A & B & C & E & G & H) - D - F) #ABCdEfGH
        # {a,b,c,f,g,h}
        sets['11100111'] = len((A & B & C & F & G & H) - D - E) #ABCdeFGH
        # {a,b,d,e,f,g} {a,b,d,e,f,h} {a,b,d,e,g,h}
        sets['11011110'] = len((A & B & D & E & F & G) - C - H) #ABcDEFGh
        sets['11011101'] = len((A & B & D & E & F & H) - C - G) #ABcDEFgH
        sets['11011011'] = len((A & B & D & E & G & H) - C - F) #ABcDEfGH
        # {a,b,d,f,g,h}
        sets['11010111'] = len((A & B & D & F & G & H) - C - E) #ABcDeFGH
        # {a,b,e,f,g,h}
        sets['11001111'] = len((A & B & E & F & G & H) - C - D) #ABcdEFGH
        # {a,c,d,e,f,g} {a,c,d,e,f,h} {a,c,d,e,g,h}
        sets['10111110'] = len((A & C & D & E & F & G) - B - H) #AbCDEFGh
        sets['10111101'] = len((A & C & D & E & F & H) - B - G) #AbCDEFgH
        sets['10111011'] = len((A & C & D & E & G & H) - B - F) #AbCDEfGH
        # {a,c,d,f,g,h}
        sets['10110111'] = len((A & C & D & F & G & H) - B - E) #AbCDeFGH
        # {a,c,e,f,g,h}
        sets['10101111'] = len((A & C & E & F & G & H) - B - D) #AbCdEFGH
        # {a,d,e,f,g,h}
        sets['10011111'] = len((A & D & E & F & G & H) - B - C) #AbcDEFGH
        # {b,c,d,e,f,g} {b,c,d,e,f,h} {b,c,d,e,g,h}
        sets['01111110'] = len((B & C & D & E & F & G) - A - H) #aBCDEFGh
        sets['01111101'] = len((B & C & D & E & F & H) - A - G) #aBCDEFgH
        sets['01111011'] = len((B & C & D & E & G & H) - A - F) #aBCDEfGH
        # {b,c,d,f,g,h}
        sets['01110111'] = len((B & C & D & F & G & H) - A - E) #aBCDeFGH
        # {b,c,e,f,g,h}
        sets['01101111'] = len((B & C & E & F & G & H) - A - D) #aBCdEFGH
        # {b,d,e,f,g,h}
        sets['01011111'] = len((B & D & E & F & G & H) - A - C) #aBcDEFGH
        # {c,d,e,f,g,h}
        sets['00111111'] = len((C & D & E & F & G & H) - A - B) #abCDEFGH
        # {a,b,c,d,e,f,g} {a,b,c,d,e,f,h} {a,b,c,d,e,g,h}
        sets['11111110'] = len((A & B & C & D & E & F & G) - H) #ABCDEFGh
        sets['11111101'] = len((A & B & C & D & E & F & H) - G) #ABCDEFgH
        sets['11111011'] = len((A & B & C & D & E & G & H) - F) #ABCDEfGH
        # {a,b,c,d,f,g,h}
        sets['11110111'] = len((A & B & C & D & F & G & H) - E) #ABCDeFGH
        # {a,b,c,e,f,g,h}
        sets['11101111'] = len((A & B & C & E & F & G & H) - D) #ABCdEFGH
        # {a,b,d,e,f,g,h}
        sets['11011111'] = len((A & B & D & E & F & G & H) - C) #ABcDEFGH
        # {a,c,d,e,f,g,h}
        sets['10111111'] = len((A & C & D & E & F & G & H) - B) #AbCDEFGH
        # {b,c,d,e,f,g,h}
        sets['01111111'] = len((B & C & D & E & F & G & H) - A) #aBCDEFGH
        # {a,b,c,d,e,f,g,h}
        sets['11111111'] = len(A & B & C & D & E & F & G & H) #ABCDEFGH
    elif (numb == 9):
        A = set(mysets[0])
        B = set(mysets[1])
        C = set(mysets[2])
        D = set(mysets[3])
        E = set(mysets[4])
        F = set(mysets[5])
        G = set(mysets[6])
        H = set(mysets[7])
        I = set(mysets[8])
        # {a} {b} {c} {d} {e} {f} {g} {h} {i}
        sets['100000000'] = len(A - B - C - D - E - F - G - H - I) #Abcdefghi
        sets['010000000'] = len(B - A - C - D - E - F - G - H - I) #aBcdefghi
        sets['001000000'] = len(C - B - A - D - E - F - G - H - I) #abCdefghi
        sets['000100000'] = len(D - B - C - A - E - F - G - H - I) #abcDefghi
        sets['000010000'] = len(E - B - C - D - A - F - G - H - I) #abcdEfghi
        sets['000001000'] = len(F - B - C - D - E - A - G - H - I) #abcdeFghi
        sets['000000100'] = len(G - B - C - D - E - F - A - H - I) #abcdefGhi
        sets['000000010'] = len(H - B - C - D - E - F - G - A - I) #abcdefgHi
        sets['000000001'] = len(I - B - C - D - E - F - G - H - A) #abcdefghI
        # {a,b} {a,c} {a,d} {a,e} {a,f} {a,g} {a,h} {a,i} {b,c} {b,d} {b,e} {b,f} {b,g} {b,h}
        sets['110000000'] = len((A & B) - C - D - E - F - G - H - I) #ABcdefghi
        sets['101000000'] = len((A & C) - B - D - E - F - G - H - I) #AbCdefghi
        sets['100100000'] = len((A & D) - B - C - E - F - G - H - I) #AbcDefghi
        sets['100010000'] = len((A & E) - B - C - D - F - G - H - I) #AbcdEfghi
        sets['100001000'] = len((A & F) - B - C - D - E - G - H - I) #AbcdeFghi
        sets['100000100'] = len((A & G) - B - C - D - E - F - H - I) #AbcdefGhi
        sets['100000010'] = len((A & H) - B - C - D - E - F - G - I) #AbcdefgHi
        sets['100000001'] = len((A & I) - B - C - D - E - F - G - H) #AbcdefghI
        sets['011000000'] = len((B & C) - A - D - E - F - G - H - I) #aBCdefghi
        sets['010100000'] = len((B & D) - A - C - E - F - G - H - I) #aBcDefghi
        sets['010010000'] = len((B & E) - A - C - D - F - G - H - I) #aBcdEfghi
        sets['010001000'] = len((B & F) - A - C - D - E - G - H - I) #aBcdeFghi
        sets['010000100'] = len((B & G) - A - C - D - E - F - H - I) #aBcdefGhi
        sets['010000010'] = len((B & H) - A - C - D - E - F - G - I) #aBcdefgHi
        # {b,i} {c,d} {c,e} {c,f} {c,g} {c,h} {c,i} {d,e} {d,f} {d,g} {d,h} {d,i}
        sets['010000001'] = len((B & I) - A - C - D - E - F - G - H) #aBcdefghI
        sets['001100000'] = len((C & D) - A - B - E - F - G - H - I) #abCDefghi
        sets['001010000'] = len((C & E) - A - B - D - F - G - H - I) #abCdEfghi
        sets['001001000'] = len((C & F) - A - B - D - E - G - H - I) #abCdeFghi
        sets['001000100'] = len((C & G) - A - B - D - E - F - H - I) #abCdefGhi
        sets['001000010'] = len((C & H) - A - B - D - E - F - G - I) #abCdefgHi
        sets['001000001'] = len((C & I) - A - B - D - E - F - G - H) #abCdefghI
        sets['000110000'] = len((D & E) - A - B - C - F - G - H - I) #abcDEfghi
        sets['000101000'] = len((D & F) - A - B - C - E - G - H - I) #abcDeFghi
        sets['000100100'] = len((D & G) - A - B - C - E - F - H - I) #abcDefGhi
        sets['000100010'] = len((D & H) - A - B - C - E - F - G - I) #abcDefgHi
        sets['000100001'] = len((D & I) - A - B - C - E - F - G - H) #abcDefghI
        # {e,f} {e,g} {e,h} {e,i} {f,g} {f,h} {f,i} {g,h} {g,i} {h,i}
        sets['000011000'] = len((E & F) - A - B - C - D - G - H - I) #abcdEFghi
        sets['000010100'] = len((E & G) - A - B - C - D - F - H - I) #abcdEfGhi
        sets['000010010'] = len((E & H) - A - B - C - D - F - G - I) #abcdEfgHi
        sets['000010001'] = len((E & I) - A - B - C - D - F - G - H) #abcdEfghI
        sets['000001100'] = len((F & G) - A - B - C - D - E - H - I) #abcdeFGhi
        sets['000001010'] = len((F & H) - A - B - C - D - E - G - I) #abcdeFgHi
        sets['000001001'] = len((F & I) - A - B - C - D - E - G - H) #abcdeFghI
        sets['000000110'] = len((G & H) - A - B - C - D - E - F - I) #abcdefGHi
        sets['000000101'] = len((G & I) - A - B - C - D - E - F - H) #abcdefGhI
        sets['000000011'] = len((H & I) - A - B - C - D - E - F - G) #abcdefgHI
        # {a,b,c} {a,b,d} {a,b,e} {a,b,f} {a,b,g} {a,b,h} {a,b,i} {a,c,d} {a,c,e} {a,c,f} {a,c,g} {a,c,h} {a,c,i}
        sets['111000000'] = len((A & B & C) - D - E - F - G - H - I) #ABCdefghi
        sets['110100000'] = len((A & B & D) - C - E - F - G - H - I) #ABcDefghi
        sets['110010000'] = len((A & B & E) - C - D - F - G - H - I) #ABcdEfghi
        sets['110001000'] = len((A & B & F) - C - D - E - G - H - I) #ABcdeFghi
        sets['110000100'] = len((A & B & G) - C - D - E - F - H - I) #ABcdefGhi
        sets['110000010'] = len((A & B & H) - C - D - E - F - G - I) #ABcdefgHi
        sets['110000001'] = len((A & B & I) - C - D - E - F - G - H) #ABcdefghI
        sets['101100000'] = len((A & C & D) - B - E - F - G - H - I) #AbCDefghi
        sets['101010000'] = len((A & C & E) - B - D - F - G - H - I) #AbCdEfghi
        sets['101001000'] = len((A & C & F) - B - D - E - G - H - I) #AbCdeFghi
        sets['101000100'] = len((A & C & G) - B - D - E - F - H - I) #AbCdefGhi
        sets['101000010'] = len((A & C & H) - B - D - E - F - G - I) #AbCdefgHi
        sets['101000001'] = len((A & C & I) - B - D - E - F - G - H) #AbCdefghI
        # {a,d,e} {a,d,f} {a,d,g} {a,d,h} {a,d,i} {a,e,f} {a,e,g} {a,e,h} {a,e,i} {a,f,g} {a,f,h} {a,f,i}
        sets['100110000'] = len((A & D & E) - B - C - F - G - H - I) #AbcDEfghi
        sets['100101000'] = len((A & D & F) - B - C - E - G - H - I) #AbcDeFghi
        sets['100100100'] = len((A & D & G) - B - C - E - F - H - I) #AbcDefGhi
        sets['100100010'] = len((A & D & H) - B - C - E - F - G - I) #AbcDefgHi
        sets['100100001'] = len((A & D & I) - B - C - E - F - G - H) #AbcDefghI
        sets['100011000'] = len((A & E & F) - B - C - D - G - H - I) #AbcdEFghi
        sets['100010100'] = len((A & E & G) - B - C - D - F - H - I) #AbcdEfGhi
        sets['100010010'] = len((A & E & H) - B - C - D - F - G - I) #AbcdEfgHi
        sets['100010001'] = len((A & E & I) - B - C - D - F - G - H) #AbcdEfghI
        sets['100001100'] = len((A & F & G) - B - C - D - E - H - I) #AbcdeFGhi
        sets['100001010'] = len((A & F & H) - B - C - D - E - G - I) #AbcdeFgHi
        sets['100001001'] = len((A & F & I) - B - C - D - E - G - H) #AbcdeFghI
        # {a,g,h} {a,g,i} {a,h,i} {b,c,d} {b,c,e} {b,c,f} {b,c,g} {b,c,h} {b,c,i} {b,d,e} {b,d,f}
        sets['100000110'] = len((A & G & H) - B - C - D - E - F - I) #AbcdefGHi
        sets['100000101'] = len((A & G & I) - B - C - D - E - F - H) #AbcdefGhI
        sets['100000011'] = len((A & H & I) - B - C - D - E - F - G) #AbcdefgHI
        sets['011100000'] = len((B & C & D) - A - E - F - G - H - I) #aBCDefghi
        sets['011010000'] = len((B & C & E) - A - D - F - G - H - I) #aBCdEfghi
        sets['011001000'] = len((B & C & F) - A - D - E - G - H - I) #aBCdeFghi
        sets['011000100'] = len((B & C & G) - A - D - E - F - H - I) #aBCdefGhi
        sets['011000010'] = len((B & C & H) - A - D - E - F - G - I) #aBCdefgHi
        sets['011000001'] = len((B & C & I) - A - D - E - F - G - H) #aBCdefghI
        sets['010110000'] = len((B & D & E) - A - C - F - G - H - I) #aBcDEfghi
        sets['010101000'] = len((B & D & F) - A - C - E - G - H - I) #aBcDeFghi 
        # {b,d,g} {b,d,h} {b,d,i} {b,e,f} {b,e,g} {b,e,h} {b,e,i} {b,f,g} {b,f,h} {b,f,i} {b,g,h} {b,g,i}
        sets['010100100'] = len((B & D & G) - A - C - E - F - H - I) #aBcDefGhi
        sets['010100010'] = len((B & D & H) - A - C - E - F - G - I) #aBcDefgHi
        sets['010100001'] = len((B & D & I) - A - C - E - F - G - H) #aBcDefghI
        sets['010011000'] = len((B & E & F) - A - C - D - G - H - I) #aBcdEFghI
        sets['010010100'] = len((B & E & G) - A - C - D - F - H - I) #aBcdEFghI
        sets['010010010'] = len((B & E & H) - A - C - D - F - G - I) #aBcdEfgHi
        sets['010010001'] = len((B & E & I) - A - C - D - F - G - H) #aBcdEfghI
        sets['010001100'] = len((B & F & G) - A - C - D - E - H - I) #aBcdeFGhi
        sets['010001010'] = len((B & F & H) - A - C - D - E - G - I) #aBcdeFgHi
        sets['010001001'] = len((B & F & I) - A - C - D - E - G - H) #aBcdeFghI
        sets['010000110'] = len((B & G & H) - A - C - D - E - F - I) #aBcdefGHi
        sets['010000101'] = len((B & G & I) - A - C - D - E - F - H) #aBcdefGhI
        # {b,h,i} {c,d,e} {c,d,f} {c,d,g} {c,d,h} {c,d,i} {c,e,f} {c,e,g} {c,e,h} {c,e,i}
        sets['010000011'] = len((B & H & I) - A - C - D - E - F - G) #aBcdefgHI
        sets['001110000'] = len((C & D & E) - A - B - F - G - H - I) #abCDEfghi
        sets['001101000'] = len((C & D & F) - A - B - E - G - H - I) #abCDeFghi
        sets['001100100'] = len((C & D & G) - A - B - E - F - H - I) #abCDefGhi
        sets['001100010'] = len((C & D & H) - A - B - E - F - G - I) #abCDefgHi
        sets['001100001'] = len((C & D & I) - A - B - E - F - G - H) #abCDefghI
        sets['001011000'] = len((C & E & F) - A - B - D - G - H - I) #abCdEFghi
        sets['001010100'] = len((C & E & G) - A - B - D - F - H - I) #abCdEfGhi
        sets['001010010'] = len((C & E & H) - A - B - D - F - G - I) #abCdEfgHi
        sets['001010001'] = len((C & E & I) - A - B - D - F - G - H) #abCdEfghI
        # {c,f,g} {c,f,h} {c,f,i} {c,g,h} {c,g,i} {c,h,i} {d,e,f} {d,e,g} {d,e,h} {d,e,i}
        sets['001001100'] = len((C & F & G) - A - B - D - E - H - I) #abCdeFGhi
        sets['001001010'] = len((C & F & H) - A - B - D - E - G - I) #abCdeFgHi
        sets['001001001'] = len((C & F & I) - A - B - D - E - G - H) #abCdeFghI
        sets['001000110'] = len((C & G & H) - A - B - D - E - F - I) #abCdefGHi
        sets['001000101'] = len((C & G & I) - A - B - D - E - F - H) #abCdefGhI
        sets['001000011'] = len((C & H & I) - A - B - D - E - F - G) #abCdefgHI
        sets['000111000'] = len((D & E & F) - A - B - C - G - H - I) #abcDEFghi
        sets['000110100'] = len((D & E & G) - A - B - C - F - H - I) #abcDEfGhi
        sets['000110010'] = len((D & E & H) - A - B - C - F - G - I) #abcDEfgHi
        sets['000110001'] = len((D & E & I) - A - B - C - F - G - H) #abcDEfghI
        # {d,f,g} {d,f,h} {d,f,i} {d,g,h} {d,g,i} {d,h,i} {e,f,g} {e,f,h} {e,f,i} {e,g,h}
        sets['000101100'] = len((D & F & G) - A - B - C - E - H - I) #abcDeFGhi
        sets['000101010'] = len((D & F & H) - A - B - C - E - G - I) #abcDeFgHi
        sets['000101001'] = len((D & F & I) - A - B - C - E - G - H) #abcDeFghI
        sets['000100110'] = len((D & G & H) - A - B - C - E - F - I) #abcDefGHi
        sets['000100101'] = len((D & G & I) - A - B - C - E - F - H) #abcDefGhI
        sets['000100011'] = len((D & H & I) - A - B - C - E - F - G) #abcDefgHI
        sets['000011100'] = len((E & F & G) - A - B - C - D - H - I) #abcdEFGhi
        sets['000011010'] = len((E & F & H) - A - B - C - D - G - I) #abcdEFgHi
        sets['000011001'] = len((E & F & I) - A - B - C - D - G - H) #abcdEFghI
        sets['000010110'] = len((E & G & H) - A - B - C - D - F - I) #abcdEfGHi
        # {e,g,i} {e,h,i} {f,g,h} {f,g,i} {f,h,i} {g,h,i}
        sets['000010101'] = len((E & G & I) - A - B - C - D - F - H) #abcdEfGhI
        sets['000010011'] = len((E & H & I) - A - B - C - D - F - G) #abcdEfgHI
        sets['000001110'] = len((F & G & H) - A - B - C - D - E - I) #abcdeFGHi
        sets['000001101'] = len((F & G & I) - A - B - C - D - E - H) #abcdeFGhI
        sets['000001011'] = len((F & H & I) - A - B - C - D - E - G) #abcdeFgHI
        sets['000000111'] = len((G & H & I) - A - B - C - D - E - F) #abcdefGHI
        # {a,b,c,d} {a,b,c,e} {a,b,c,f} {a,b,c,g} {a,b,c,h} {a,b,c,i} {a,b,d,e} {a,b,d,f} {a,b,d,g} {a,b,d,h} {a,b,d,i} {a,b,e,f} {a,b,e,g}
        sets['111100000'] = len((A & B & C & D) - E - F - G - H - I) #ABCDefghi
        sets['111010000'] = len((A & B & C & E) - D - F - G - H - I) #ABCdEfghi
        sets['111001000'] = len((A & B & C & F) - D - E - G - H - I) #ABCdeFghi
        sets['111000100'] = len((A & B & C & G) - D - E - F - H - I) #ABCdefGhi
        sets['111000010'] = len((A & B & C & H) - D - E - F - G - I) #ABCdefgHi
        sets['111000001'] = len((A & B & C & I) - D - E - F - G - H) #ABCdefghI
        sets['110110000'] = len((A & B & D & E) - C - F - G - H - I) #ABcDEfghi
        sets['110101000'] = len((A & B & D & F) - C - E - G - H - I) #ABcDeFghi
        sets['110100100'] = len((A & B & D & G) - C - E - F - H - I) #ABcDefGhi
        sets['110100010'] = len((A & B & D & H) - C - E - F - G - I) #ABcDefgHi
        sets['110100001'] = len((A & B & D & I) - C - E - F - G - H) #ABcDefghI
        sets['110011000'] = len((A & B & E & F) - C - D - G - H - I) #ABcdEFghi
        sets['110010100'] = len((A & B & E & G) - C - D - F - H - I) #ABcdEfGhi
        # {a,b,e,h} {a,b,e,i} {a,b,f,g} {a,b,f,h} {a,b,f,i} {a,b,g,h} {a,b,g,i} {a,b,h,i} {a,c,d,e} {a,c,d,f}
        sets['110010010'] = len((A & B & E & H) - C - D - F - G - I) #ABcdEfgHi
        sets['110010001'] = len((A & B & E & I) - C - D - F - G - H) #ABcdEfghI
        sets['110001100'] = len((A & B & F & G) - C - D - E - H - I) #ABcdeFGhi
        sets['110001010'] = len((A & B & F & H) - C - D - E - G - I) #ABcdeFgHi
        sets['110001001'] = len((A & B & F & I) - C - D - E - G - H) #ABcdeFghI
        sets['110000110'] = len((A & B & G & H) - C - D - E - F - I) #ABcdefGHi
        sets['110000101'] = len((A & B & G & I) - C - D - E - F - H) #ABcdefGhI
        sets['110000011'] = len((A & B & H & I) - C - D - E - F - G) #ABcdefgHI
        sets['101110000'] = len((A & C & D & E) - B - F - G - H - I) #AbCDEfghi
        sets['101101000'] = len((A & C & D & F) - B - E - G - H - I) #AbCDeFghi
        # {a,c,d,g} {a,c,d,h} {a,c,d,i} {a,c,e,f} {a,c,e,g} {a,c,e,h} {a,c,e,i} {a,c,f,g} {a,c,f,h} {a,c,f,i} {a,c,g,h} {a,c,g,i}
        sets['101100100'] = len((A & C & D & G) - B - E - F - H - I) #AbCDefGhi
        sets['101100010'] = len((A & C & D & H) - B - E - F - G - I) #AbCDefgHi
        sets['101100001'] = len((A & C & D & I) - B - E - F - G - H) #AbCDefghI
        sets['101011000'] = len((A & C & E & F) - B - D - G - H - I) #AbCdEFghi
        sets['101010100'] = len((A & C & E & G) - B - D - F - H - I) #AbCdEfGhi
        sets['101010010'] = len((A & C & E & H) - B - D - F - G - I) #AbCdEfgHi
        sets['101010001'] = len((A & C & E & I) - B - D - F - G - H) #AbCdEfghI
        sets['101001100'] = len((A & C & F & G) - B - D - E - H - I) #AbCdeFGhi
        sets['101001010'] = len((A & C & F & H) - B - D - E - G - I) #AbCdeFgHi
        sets['101001001'] = len((A & C & F & I) - B - D - E - G - H) #AbCdeFghI
        sets['101000110'] = len((A & C & G & H) - B - D - E - F - I) #AbCdefGHi
        sets['101000101'] = len((A & C & G & I) - B - D - E - F - H) #AbCdefGhI
        # {a,c,h,i} {a,d,e,f} {a,d,e,g} {a,d,e,h} {a,d,e,i} {a,d,f,g} {a,d,f,h} {a,d,f,i} {a,d,g,h} {a,d,g,i}
        sets['101000011'] = len((A & C & H & I) - B - D - E - F - G) #AbCdefgHI
        sets['100111000'] = len((A & D & E & F) - B - C - G - H - I) #AbcDEFghi
        sets['100110100'] = len((A & D & E & G) - B - C - F - H - I) #AbcDEfGhi
        sets['100110010'] = len((A & D & E & H) - B - C - F - G - I) #AbcDEfgHi
        sets['100110001'] = len((A & D & E & I) - B - C - F - G - H) #AbcDEfghI
        sets['100101100'] = len((A & D & F & G) - B - C - E - H - I) #AbcDeFGhi
        sets['100101010'] = len((A & D & F & H) - B - C - E - G - I) #AbcDeFgHi
        sets['100101001'] = len((A & D & F & I) - B - C - E - G - H) #AbcDeFghI
        sets['100100110'] = len((A & D & G & H) - B - C - E - F - I) #AbcDefGHi
        sets['100100101'] = len((A & D & G & I) - B - C - E - F - H) #AbcDefGhI
        # {a,d,h,i} {a,e,f,g} {a,e,f,h} {a,e,f,i} {a,e,g,h} {a,e,g,i} {a,e,h,i} {a,f,g,h}
        sets['100100011'] = len((A & D & H & I) - B - C - E - F - G) #AbcDefgHI
        sets['100011100'] = len((A & E & F & G) - B - C - D - H - I) #AbcdEFGhi
        sets['100011010'] = len((A & E & F & H) - B - C - D - G - I) #AbcdEFgHi
        sets['100011001'] = len((A & E & F & I) - B - C - D - G - H) #AbcdEFghI
        sets['100010110'] = len((A & E & G & H) - B - C - D - F - I) #AbcdEfGHi
        sets['100010101'] = len((A & E & G & I) - B - C - D - F - H) #AbcdEfGhI
        sets['100010011'] = len((A & E & H & I) - B - C - D - F - G) #AbcdEfgHI
        sets['100001110'] = len((A & F & G & H) - B - C - D - E - I) #AbcdeFGHi
        # {a,f,g,i} {a,f,h,i} {a,g,h,i} {b,c,d,e} {b,c,d,f} {b,c,d,g} {b,c,d,h} {b,c,d,i}
        sets['100001101'] = len((A & F & G & I) - B - C - D - E - H) #AbcdeFGhI
        sets['100001011'] = len((A & F & H & I) - B - C - D - E - G) #AbcdeFgHI
        sets['100000111'] = len((A & G & H & I) - B - C - D - E - F) #AbcdefGHI
        sets['011110000'] = len((B & C & D & E) - A - F - G - H - I) #aBCDEfghi
        sets['011101000'] = len((B & C & D & F) - A - E - G - H - I) #aBCDeFghi
        sets['011100100'] = len((B & C & D & G) - A - E - F - H - I) #aBCDefGhi
        sets['011100010'] = len((B & C & D & H) - A - E - F - G - I) #aBCDefgHi
        sets['011100001'] = len((B & C & D & I) - A - E - F - G - H) #aBCDefghI
        # {b,c,e,f} {b,c,e,g} {b,c,e,h} {b,c,e,i} {b,c,f,g} {b,c,f,h} {b,c,f,i} {b,c,g,h} {b,c,g,i} {b,c,h,i}
        sets['011011000'] = len((B & C & E & F) - A - D - G - H - I) #aBCdEFghi
        sets['011010100'] = len((B & C & E & G) - A - D - F - H - I) #aBCdEfGhi
        sets['011010010'] = len((B & C & E & H) - A - D - F - G - I) #aBCdEfgHi
        sets['011010001'] = len((B & C & E & I) - A - D - F - G - H) #aBCdEfghI
        sets['011001100'] = len((B & C & F & G) - A - D - E - H - I) #aBCdeFGhi
        sets['011001010'] = len((B & C & F & H) - A - D - E - G - I) #aBCdeFgHi
        sets['011001001'] = len((B & C & F & I) - A - D - E - G - H) #aBCdeFghI
        sets['011000110'] = len((B & C & G & H) - A - D - E - F - I) #aBCdefGHi
        sets['011000101'] = len((B & C & G & I) - A - D - E - F - H) #aBCdefGhI
        sets['011000011'] = len((B & C & H & I) - A - D - E - F - G) #aBCdefgHI
        # {b,d,e,f} {b,d,e,g} {b,d,e,h} {b,d,e,i} {b,d,f,g} {b,d,f,h} {b,d,f,i} {b,d,g,h} {b,d,g,i} {b,d,h,i}
        sets['010111000'] = len((B & D & E & F) - A - C - G - H - I) #aBcDEFghi
        sets['010110100'] = len((B & D & E & G) - A - C - F - H - I) #aBcDEfGhi
        sets['010110010'] = len((B & D & E & H) - A - C - F - G - I) #aBcDEfgHi
        sets['010110001'] = len((B & D & E & I) - A - C - F - G - H) #aBcDEfghI
        sets['010101100'] = len((B & D & F & G) - A - C - E - H - I) #aBcDeFGhi
        sets['010101010'] = len((B & D & F & H) - A - C - E - G - I) #aBcDeFgHi
        sets['010101001'] = len((B & D & F & I) - A - C - E - G - H) #aBcDeFghI
        sets['010100110'] = len((B & D & G & H) - A - C - E - F - I) #aBcDefGHi
        sets['010100101'] = len((B & D & G & I) - A - C - E - F - H) #aBcDefGhI
        sets['010100011'] = len((B & D & H & I) - A - C - E - F - G) #aBcDefgHI
        # {b,e,f,g} {b,e,f,h} {b,e,f,i} {b,e,g,h} {b,e,g,i} {b,e,h,i} {b,f,g,h} {b,f,g,i} {b,f,h,i}
        sets['010011100'] = len((B & E & F & G) - A - C - D - H - I) #aBcdEFGhi
        sets['010011010'] = len((B & E & F & H) - A - C - D - G - I) #aBcdEFgHi
        sets['010011001'] = len((B & E & F & I) - A - C - D - G - H) #aBcdEFghI
        sets['010010110'] = len((B & E & G & H) - A - C - D - F - I) #aBcdEfGHi
        sets['010010101'] = len((B & E & G & I) - A - C - D - F - H) #aBcdEfGhI
        sets['010010011'] = len((B & E & H & I) - A - C - D - F - G) #aBcdEfgHI
        sets['010001110'] = len((B & F & G & H) - A - C - D - E - I) #aBcdeFGHi
        sets['010001101'] = len((B & F & G & I) - A - C - D - E - H) #aBcdeFGhI
        sets['010001011'] = len((B & F & H & I) - A - C - D - E - G) #aBcdeFgHI
        # {b,g,h,i} {c,d,e,f} {c,d,e,g} {c,d,e,h} {c,d,e,i} {c,d,f,g} {c,d,f,h} {c,d,f,i} {c,d,g,h}
        sets['010000111'] = len((B & G & H & I) - A - C - D - E - F) #aBcdefGHI
        sets['001111000'] = len((C & D & E & F) - A - B - G - H - I) #abCDEFghi
        sets['001110100'] = len((C & D & E & G) - A - B - F - H - I) #abCDEfGhi
        sets['001110010'] = len((C & D & E & H) - A - B - F - G - I) #abCDEfgHi
        sets['001110001'] = len((C & D & E & I) - A - B - F - G - H) #abCDEfghI
        sets['001101100'] = len((C & D & F & G) - A - B - E - H - I) #abCDeFGhi
        sets['001101010'] = len((C & D & F & H) - A - B - E - G - I) #abCDeFgHi
        sets['001101001'] = len((C & D & F & I) - A - B - E - G - H) #abCDeFghI
        sets['001100110'] = len((C & D & G & H) - A - B - E - F - I) #abCDefGHi
        # {c,d,g,i} {c,d,h,i} {c,e,f,g} {c,e,f,h} {c,e,f,i} {c,e,g,h} {c,e,g,i} {c,e,h,i}
        sets['001100101'] = len((C & D & G & I) - A - B - E - F - H) #abCDefGhI
        sets['001100011'] = len((C & D & H & I) - A - B - E - F - G) #abCDefgHI
        sets['001011100'] = len((C & E & F & G) - A - B - D - H - I) #abCdEFGhi
        sets['001011010'] = len((C & E & F & H) - A - B - D - G - I) #abCdEFgHi
        sets['001011001'] = len((C & E & F & I) - A - B - D - G - H) #abCdEFghI
        sets['001010110'] = len((C & E & G & H) - A - B - D - F - I) #abCdEfGHi
        sets['001010101'] = len((C & E & G & I) - A - B - D - F - H) #abCdEfGhI
        sets['001010011'] = len((C & E & H & I) - A - B - D - F - G) #abCdEfgHI
        # {c,f,g,h} {c,f,g,i} {c,f,h,i} {c,g,h,i} {d,e,f,g} {d,e,f,h} {d,e,f,i} {d,e,g,h}
        sets['001001110'] = len((C & F & G & H) - A - B - D - E - I) #abCdeFGHi
        sets['001001101'] = len((C & F & G & I) - A - B - D - E - H) #abCdeFGhI
        sets['001001011'] = len((C & F & H & I) - A - B - D - E - G) #abCdeFgHI
        sets['001000111'] = len((C & G & H & I) - A - B - D - E - F) #abCdefGHI
        sets['000111100'] = len((D & E & F & G) - A - B - C - H - I) #abcDEFGhi
        sets['000111010'] = len((D & E & F & H) - A - B - C - G - I) #abcDEFgHi
        sets['000111001'] = len((D & E & F & I) - A - B - C - G - H) #abcDEFghI
        sets['000110110'] = len((D & E & G & H) - A - B - C - F - I) #abcDEfGHi
        # {d,e,g,i} {d,e,h,i} {d,f,g,h} {d,f,g,i} {d,f,h,i} {d,g,h,i}
        sets['000110101'] = len((D & E & G & I) - A - B - C - F - H) #abcDEfGhI
        sets['000110011'] = len((D & E & H & I) - A - B - C - F - G) #abcDEfgHI
        sets['000101110'] = len((D & F & G & H) - A - B - C - E - I) #abcDeFGHi
        sets['000101101'] = len((D & F & G & I) - A - B - C - E - H) #abcDeFGhI
        sets['000101011'] = len((D & F & H & I) - A - B - C - E - G) #abcDeFgHI
        sets['000100111'] = len((D & G & H & I) - A - B - C - E - F) #abcDefGHI
        # {e,f,g,h} {e,f,g,i} {e,f,h,i} {e,g,h,i} {f,g,h,i}
        sets['000011110'] = len((E & F & G & H) - A - B - C - D - I) #abcdEFGHi
        sets['000011101'] = len((E & F & G & I) - A - B - C - D - H) #abcdEFGhI
        sets['000011011'] = len((E & F & H & I) - A - B - C - D - G) #abcdEFgHI
        sets['000010111'] = len((E & G & H & I) - A - B - C - D - F) #abcdEfGHI
        sets['000001111'] = len((F & G & H & I) - A - B - C - D - E) #abcdeFGHI
        # {a,b,c,d,e} {a,b,c,d,f} {a,b,c,d,g} {a,b,c,d,h} {a,b,c,d,i}
        sets['111110000'] = len((A & B & C & D & E) - F - G - H - I) #ABCDEfghi
        sets['111101000'] = len((A & B & C & D & F) - E - G - H - I) #ABCDeFghi
        sets['111100100'] = len((A & B & C & D & G) - E - F - H - I) #ABCDefGhi
        sets['111100010'] = len((A & B & C & D & H) - E - F - G - I) #ABCDefgHi
        sets['111100001'] = len((A & B & C & D & I) - E - F - G - H) #ABCDefghI
        # {a,b,c,e,f} {a,b,c,e,g} {a,b,c,e,h} {a,b,c,e,i} {a,b,c,f,g} {a,b,c,f,h}
        sets['111011000'] = len((A & B & C & E & F) - D - G - H - I) #ABCdEFghi
        sets['111010100'] = len((A & B & C & E & G) - D - F - H - I) #ABCdEfGhi
        sets['111010010'] = len((A & B & C & E & H) - D - F - G - I) #ABCdEfgHi
        sets['111010001'] = len((A & B & C & E & I) - D - F - G - H) #ABCdEfghI
        sets['111001100'] = len((A & B & C & F & G) - D - E - H - I) #ABCdeFGhi
        sets['111001010'] = len((A & B & C & F & H) - D - E - G - I) #ABCdeFgHi
        # {a,b,c,f,i} {a,b,c,g,h} {a,b,c,g,i} {a,b,c,h,i}
        sets['111001001'] = len((A & B & C & F & I) - D - E - G - H) #ABCdeFghI
        sets['111000110'] = len((A & B & C & G & H) - D - E - F - I) #ABCdefGHi
        sets['111000101'] = len((A & B & C & G & I) - D - E - F - H) #ABCdefGhI
        sets['111000011'] = len((A & B & C & H & I) - D - E - F - G) #ABCdefgHI
        # {a,b,d,e,f} {a,b,d,e,g} {a,b,d,e,h} {a,b,d,e,i}
        sets['110111000'] = len((A & B & D & E & F) - C - G - H - I) #ABcDEFghi
        sets['110110100'] = len((A & B & D & E & G) - C - F - H - I) #ABcDEfGhi
        sets['110110010'] = len((A & B & D & E & H) - C - F - G - I) #ABcDEfgHi
        sets['110110001'] = len((A & B & D & E & I) - C - F - G - H) #ABcDEfghI
        # {a,b,d,f,g} {a,b,d,f,h} {a,b,d,f,i} {a,b,d,g,h} {a,b,d,g,i}
        sets['110101100'] = len((A & B & D & F & G) - C - E - H - I) #ABcDeFGhi
        sets['110101010'] = len((A & B & D & F & H) - C - E - G - I) #ABcDeFgHi
        sets['110101001'] = len((A & B & D & F & I) - C - E - G - H) #ABcDeFghI
        sets['110100110'] = len((A & B & D & G & H) - C - E - F - I) #ABcDefGHi
        sets['110100101'] = len((A & B & D & G & I) - C - E - F - H) #ABcDefGhI
        # {a,b,d,h,i} {a,b,e,f,g} {a,b,e,f,h} {a,b,e,f,i}
        sets['110100011'] = len((A & B & D & H & I) - C - E - F - G) #ABcDefgHI
        sets['110011100'] = len((A & B & E & F & G) - C - D - H - I) #ABcdEFGhi
        sets['110011010'] = len((A & B & E & F & H) - C - D - G - I) #ABcdEFgHi
        sets['110011001'] = len((A & B & E & F & I) - C - D - G - H) #ABcdEFghI
        # {a,b,e,g,h} {a,b,e,g,i} {a,b,e,h,i}
        sets['110010110'] = len((A & B & E & G & H) - C - D - F - I) #ABcdEfGHi
        sets['110010101'] = len((A & B & E & G & I) - C - D - F - H) #ABcdEfGhI
        sets['110010011'] = len((A & B & E & H & I) - C - D - F - G) #ABcdEfgHI
        # {a,b,f,g,h} {a,b,f,g,i} {a,b,f,h,i}
        sets['110001110'] = len((A & B & F & G & H) - C - D - E - I) #ABcdeFGHi
        sets['110001101'] = len((A & B & F & G & I) - C - D - E - H) #ABcdeFGhI
        sets['110001011'] = len((A & B & F & H & I) - C - D - E - G) #ABcdeFgHI
        # {a,b,g,h,i} {a,c,d,e,f} {a,c,d,e,g}
        sets['110000111'] = len((A & B & G & H & I) - C - D - E - F) #ABcdefGHI
        sets['101111000'] = len((A & C & D & E & F) - B - G - H - I) #AbCDEFghi
        sets['101110100'] = len((A & C & D & E & G) - B - F - H - I) #AbCDEfGhi
        # {a,c,d,e,h} {a,c,d,e,i} {a,c,d,f,g} {a,c,d,f,h} {a,c,d,f,i}
        sets['101110010'] = len((A & C & D & E & H) - B - F - G - I) #AbCDEfgHi
        sets['101110001'] = len((A & C & D & E & I) - B - F - G - H) #AbCDEfghI
        sets['101101100'] = len((A & C & D & F & G) - B - E - H - I) #AbCDeFGhi
        sets['101101010'] = len((A & C & D & F & H) - B - E - G - I) #AbCDeFgHi
        sets['101101001'] = len((A & C & D & F & I) - B - E - G - H) #AbCDeFghI
        # {a,c,d,g,h} {a,c,d,g,i} {a,c,d,h,i} {a,c,e,f,g}
        sets['101100110'] = len((A & C & D & G & H) - B - E - F - I) #AbCDefGHi
        sets['101100101'] = len((A & C & D & G & I) - B - E - F - H) #AbCDefGhI
        sets['101100011'] = len((A & C & D & H & I) - B - E - F - G) #AbCDefgHI
        sets['101011100'] = len((A & C & E & F & G) - B - D - H - I) #AbCdEFGhi
        # {a,c,e,f,h} {a,c,e,f,i} {a,c,e,g,h} {a,c,e,g,i}
        sets['101011010'] = len((A & C & E & F & H) - B - D - G - I) #AbCdEFgHi
        sets['101011001'] = len((A & C & E & F & I) - B - D - G - H) #AbCdEFghI
        sets['101010110'] = len((A & C & E & G & H) - B - D - F - I) #AbCdEfGHi
        sets['101010101'] = len((A & C & E & G & I) - B - D - F - H) #AbCdEfGhI
        # {a,c,e,h,i} {a,c,f,g,h} {a,c,f,g,i}
        sets['101010011'] = len((A & C & E & H & I) - B - D - F - G) #AbCdEfgHI
        sets['101001110'] = len((A & C & F & G & H) - B - D - E - I) #AbCdeFGHi
        sets['101001101'] = len((A & C & F & G & I) - B - D - E - H) #AbCdeFGhI
        # {a,c,f,h,i} {a,c,g,h,i}
        sets['101001011'] = len((A & C & F & H & I) - B - D - E - G) #AbCdeFgHI
        sets['101000111'] = len((A & C & G & H & I) - B - D - E - F) #AbCdefGHI
        # {a,d,e,f,g} {a,d,e,f,h} {a,d,e,f,i} {a,d,e,g,h} {a,d,e,g,i}
        sets['100111100'] = len((A & D & E & F & G) - B - C - H - I) #AbcDEFGhi
        sets['100111010'] = len((A & D & E & F & H) - B - C - G - I) #AbcDEFgHi
        sets['100111001'] = len((A & D & E & F & I) - B - C - G - H) #AbcDEFghI
        sets['100110110'] = len((A & D & E & G & H) - B - C - F - I) #AbcDEfGHi
        sets['100110101'] = len((A & D & E & G & I) - B - C - F - H) #AbcDEfGhI
        # {a,d,e,h,i} {a,d,f,g,h} {a,d,f,g,i}
        sets['100110011'] = len((A & D & E & H & I) - B - C - F - G) #AbcDEfgHI
        sets['100101110'] = len((A & D & F & G & H) - B - C - E - I) #AbcDeFGHi
        sets['100101101'] = len((A & D & F & G & I) - B - C - E - H) #AbcDeFGhI
        # {a,d,f,h,i} {a,d,g,h,i}
        sets['100101011'] = len((A & D & F & H & I) - B - C - E - G) #AbcDeFgHI
        sets['100100111'] = len((A & D & G & H & I) - B - C - E - F) #AbcDefGHI
        # {a,e,f,g,h} {a,e,f,g,i} {a,e,f,h,i}
        sets['100011110'] = len((A & E & F & G & H) - B - C - D - I) #AbcdEFGHi
        sets['100011101'] = len((A & E & F & G & I) - B - C - D - H) #AbcdEFGhI
        sets['100011011'] = len((A & E & F & H & I) - B - C - D - G) #AbcdEFgHI
        # {a,e,g,h,i} {a,f,g,h,i}
        sets['100010111'] = len((A & E & G & H & I) - B - C - D - F) #AbcdEfGHI
        sets['100001111'] = len((A & F & G & H & I) - B - C - D - E) #AbcdeFGHI
        # {b,c,d,e,f} {b,c,d,e,g} {b,c,d,e,h} {b,c,d,e,i}
        sets['011111000'] = len((B & C & D & E & F) - A - G - H - I) #aBCDEFghi
        sets['011110100'] = len((B & C & D & E & G) - A - F - H - I) #aBCDEfGhi
        sets['011110010'] = len((B & C & D & E & H) - A - F - G - I) #aBCDEfgHi
        sets['011110001'] = len((B & C & D & E & I) - A - F - G - H) #aBCDEfghI
        # {b,c,d,f,g} {b,c,d,f,h} {b,c,d,f,i} {b,c,d,g,h}
        sets['011101100'] = len((B & C & D & F & G) - A - E - H - I) #aBCDeFGhi
        sets['011101110'] = len((B & C & D & F & H) - A - E - G - I) #aBCDeFgHi
        sets['011101101'] = len((B & C & D & F & I) - A - E - G - H) #aBCDeFghI
        sets['011100110'] = len((B & C & D & G & H) - A - E - F - I) #aBCDefGHi
        # {b,c,d,g,i} {b,c,d,h,i} {b,c,e,f,g} {b,c,e,f,h}
        sets['011100101'] = len((B & C & D & G & I) - A - E - F - H) #aBCDefGhI
        sets['011100011'] = len((B & C & D & H & I) - A - E - F - G) #aBCDefgHI
        sets['011011100'] = len((B & C & E & F & G) - A - D - H - I) #aBCdEFGhi
        sets['011011010'] = len((B & C & E & F & H) - A - D - G - I) #aBCdEFgHi
        # {b,c,e,f,i} {b,c,e,g,h} {b,c,e,g,i} {b,c,e,h,i}
        sets['011011001'] = len((B & C & E & F & I) - A - D - G - H) #aBCdEFghI
        sets['011010110'] = len((B & C & E & G & H) - A - D - F - I) #aBCdEfGHi
        sets['011010101'] = len((B & C & E & G & I) - A - D - F - H) #aBCdEfGhI
        sets['011010011'] = len((B & C & E & H & I) - A - D - F - G) #aBCdEfgHI
        # {b,c,f,g,h} {b,c,f,g,i} {b,c,f,h,i}
        sets['011001110'] = len((B & C & F & G & H) - A - D - E - I) #aBCdeFGHi
        sets['011001101'] = len((B & C & F & G & I) - A - D - E - H) #aBCdeFGhI
        sets['011001011'] = len((B & C & F & H & I) - A - D - E - G) #aBCdeFgHI
        # {b,c,g,h,i} {b,d,e,f,g}
        sets['011000111'] = len((B & C & G & H & I) - A - D - E - F) #aBCdefGHI
        sets['010111100'] = len((B & D & E & F & G) - A - C - H - I) #aBcDEFGhi
        # {b,d,e,f,h} {b,d,e,f,i} {b,d,e,g,h} {b,d,e,g,i} {b,d,e,h,i}
        sets['010111010'] = len((B & D & E & F & H) - A - C - G - I) #aBcDEFgHi
        sets['010111001'] = len((B & D & E & F & I) - A - C - G - H) #aBcDEFghI
        sets['010110110'] = len((B & D & E & G & H) - A - C - F - I) #aBcDEfGHi
        sets['010110101'] = len((B & D & E & G & I) - A - C - F - H) #aBcDEfGhI
        sets['010110011'] = len((B & D & E & H & I) - A - C - F - G) #aBcDEfgHI
        # {b,d,f,g,h} {b,d,f,g,i} {b,d,f,h,i}
        sets['010101110'] = len((B & D & F & G & H) - A - C - E - I) #aBcDeFGHi
        sets['010101101'] = len((B & D & F & G & I) - A - C - E - H) #aBcDeFGhI
        sets['010101011'] = len((B & D & F & H & I) - A - C - E - G) #aBcDeFgHI
        # {b,d,g,h,i} {b,e,f,g,h}
        sets['010100111'] = len((B & D & G & H & I) - A - C - E - F) #aBcDefGHI
        sets['010011110'] = len((B & E & F & G & H) - A - C - D - I) #aBcdEFGHi
        # {b,e,f,g,i} {b,e,f,h,i} {b,e,g,h,i}
        sets['010011101'] = len((B & E & F & G & I) - A - C - D - H) #aBcdEFGhI
        sets['010011011'] = len((B & E & F & H & I) - A - C - D - G) #aBcdEFgHI
        sets['010010111'] = len((B & E & G & H & I) - A - C - D - F) #aBcdEfGHI
        # {b,f,g,h,i}
        sets['010001111'] = len((B & F & G & H & I) - A - C - D - E) #aBcdeFGHI
        # {c,d,e,f,g} {c,d,e,f,h} {c,d,e,f,i} {c,d,e,g,h} {c,d,e,g,i}
        sets['001111100'] = len((C & D & E & F & G) - A - B - H - I) #abCDEFGhi
        sets['001111010'] = len((C & D & E & F & H) - A - B - G - I) #abCDEFgHi
        sets['001111001'] = len((C & D & E & F & I) - A - B - G - H) #abCDEFghI
        sets['001110110'] = len((C & D & E & G & H) - A - B - F - I) #abCDEfGHi
        sets['001110101'] = len((C & D & E & G & I) - A - B - F - H) #abCDEfGhI
        # {c,d,e,h,i} {c,d,f,g,h} {c,d,f,g,i}
        sets['001110011'] = len((C & D & E & H & I) - A - B - F - G) #abCDEfgHI
        sets['001101110'] = len((C & D & F & G & H) - A - B - E - I) #abCDeFGHi
        sets['001101101'] = len((C & D & F & G & I) - A - B - E - H) #abCDeFGhI
        # {c,d,f,h,i} {c,d,g,h,i}
        sets['001101011'] = len((C & D & F & H & I) - A - B - E - G) #abCDeFgHI
        sets['001100111'] = len((C & D & G & H & I) - A - B - E - F) #abCDefGHI
        # {c,e,f,g,h} {c,e,f,g,i} {c,e,f,h,i}
        sets['001011110'] = len((C & E & F & G & H) - A - B - D - I) #abCdEFGHi
        sets['001011101'] = len((C & E & F & G & I) - A - B - D - H) #abCdEFGhI
        sets['001011011'] = len((C & E & F & H & I) - A - B - D - G) #abCdEFgHI
        # {c,e,g,h,i} {c,f,g,h,i}
        sets['001010111'] = len((C & E & G & H & I) - A - B - D - F) #abCdEfGHI
        sets['001001111'] = len((C & F & G & H & I) - A - B - D - E) #abCdeFGHI
        # {d,e,f,g,h} {d,e,f,g,i}
        sets['000111110'] = len((D & E & F & G & H) - A - B - C - I) #abcDEFGHi
        sets['000111101'] = len((D & E & F & G & I) - A - B - C - H) #abcDEFGhI
        # {d,e,f,h,i} {d,e,g,h,i}
        sets['000111011'] = len((D & E & F & H & I) - A - B - C - G) #abcDEFgHI
        sets['000110111'] = len((D & E & G & H & I) - A - B - C - F) #abcDEfGHI
        # {d,f,g,h,i} {e,f,g,h,i}
        sets['000101111'] = len((D & F & G & H & I) - A - B - C - E) #abcDeFGHI
        sets['000011111'] = len((E & F & G & H & I) - A - B - C - D) #abcdEFGHI
        # {a,b,c,d,e,f} {a,b,c,d,e,g} {a,b,c,d,e,h} {a,b,c,d,e,i} {a,b,c,d,f,g} {a,b,c,d,f,h} {a,b,c,d,f,i} {a,b,c,d,g,h} {a,b,c,d,g,i}
        sets['111111000'] = len((A & B & C & D & E & F) - G - H - I) #ABCDEFghi
        sets['111110100'] = len((A & B & C & D & E & G) - F - H - I) #ABCDEfGhi
        sets['111110010'] = len((A & B & C & D & E & H) - F - G - I) #ABCDEfgHi
        sets['111110001'] = len((A & B & C & D & E & I) - F - G - H) #ABCDEfghI
        sets['111101100'] = len((A & B & C & D & F & G) - E - H - I) #ABCDeFGhi
        sets['111101010'] = len((A & B & C & D & F & H) - E - G - I) #ABCDeFgHi
        sets['111101001'] = len((A & B & C & D & F & I) - E - G - H) #ABCDeFghI
        sets['111100110'] = len((A & B & C & D & G & H) - E - F - I) #ABCDefGHi
        sets['111100101'] = len((A & B & C & D & G & I) - E - F - H) #ABCDefGhI
        # {a,b,c,d,h,i} {a,b,c,e,f,g} {a,b,c,e,f,h} {a,b,c,e,f,i} {a,b,c,e,g,h} {a,b,c,e,g,i}
        sets['111100011'] = len((A & B & C & D & H & I) - E - F - G) #ABCDefgHI
        sets['111011100'] = len((A & B & C & E & F & G) - D - H - I) #ABCdEFGhi
        sets['111011010'] = len((A & B & C & E & F & H) - D - G - I) #ABCdEFgHi
        sets['111011001'] = len((A & B & C & E & F & I) - D - G - H) #ABCdEFghI
        sets['111010110'] = len((A & B & C & E & G & H) - D - F - I) #ABCdEfGHi
        sets['111010101'] = len((A & B & C & E & G & I) - D - F - H) #ABCdEfGhI
        # {a,b,c,e,h,i} {a,b,c,f,g,h} {a,b,c,f,g,i} {a,b,c,f,h,i} {a,b,c,g,h,i}
        sets['111010011'] = len((A & B & C & E & H & I) - D - F - G) #ABCdEfgHI
        sets['111001110'] = len((A & B & C & F & G & H) - D - E - I) #ABCdeFGHi
        sets['111001101'] = len((A & B & C & F & G & I) - D - E - H) #ABCdeFGhI
        sets['111001011'] = len((A & B & C & F & H & I) - D - E - G) #ABCdeFgHI
        sets['111000111'] = len((A & B & C & G & H & I) - D - E - F) #ABCdefGHI
        # {a,b,d,e,f,g} {a,b,d,e,f,h} {a,b,d,e,f,i} {a,b,d,e,g,h} {a,b,d,e,g,i} {a,b,d,e,h,i}
        sets['110111100'] = len((A & B & D & E & F & G) - C - H - I) #ABcDEFGhi
        sets['110111010'] = len((A & B & D & E & F & H) - C - G - I) #ABcDEFgHi
        sets['110111001'] = len((A & B & D & E & F & I) - C - G - H) #ABcDEFghI
        sets['110110110'] = len((A & B & D & E & G & H) - C - F - I) #ABcDEfGHi
        sets['110110101'] = len((A & B & D & E & G & I) - C - F - H) #ABcDEfGhI
        sets['110110011'] = len((A & B & D & E & H & I) - C - F - G) #ABcDEfgHI
        # {a,b,d,f,g,h} {a,b,d,f,g,i} {a,b,d,f,h,i} {a,b,d,g,h,i}
        sets['110101110'] = len((A & B & D & F & G & H) - C - E - I) #ABcDeFGHi
        sets['110101101'] = len((A & B & D & F & G & I) - C - E - H) #ABcDeFGhI
        sets['110101011'] = len((A & B & D & F & H & I) - C - E - G) #ABcDeFgHI
        sets['110100111'] = len((A & B & D & G & H & I) - C - E - F) #ABcDefGHI
        # {a,b,e,f,g,h} {a,b,e,f,g,i} {a,b,e,f,h,i} {a,b,e,g,h,i} {a,b,f,g,h,i}
        sets['110011110'] = len((A & B & E & F & G & H) - C - D - I) #ABcdEFGHi
        sets['110011101'] = len((A & B & E & F & G & I) - C - D - H) #ABcdEFGhI
        sets['110011011'] = len((A & B & E & F & H & I) - C - D - G) #ABcdEFgHI
        sets['110010111'] = len((A & B & E & G & H & I) - C - D - F) #ABcdEfGHI
        sets['110001111'] = len((A & B & F & G & H & I) - C - D - E) #ABcdeFGHI
        # {a,c,d,e,f,g} {a,c,d,e,f,h} {a,c,d,e,f,i} {a,c,d,e,g,h} {a,c,d,e,g,i}
        sets['101111100'] = len((A & C & D & E & F & G) - B - H - I) #AbCDEFGhi
        sets['101111010'] = len((A & C & D & E & F & H) - B - G - I) #AbCDEFgHi
        sets['101111001'] = len((A & C & D & E & F & I) - B - G - H) #AbCDEFghI
        sets['101110110'] = len((A & C & D & E & G & H) - B - F - I) #AbCDEfGHi
        sets['101110101'] = len((A & C & D & E & G & I) - B - F - H) #AbCDEfGhI
        # {a,c,d,e,h,i} {a,c,d,f,g,h} {a,c,d,f,g,i} {a,c,d,f,h,i} {a,c,d,g,h,i}
        sets['101110011'] = len((A & C & D & E & H & I) - B - F - G) #AbCDEfgHI
        sets['101101110'] = len((A & C & D & F & G & H) - B - E - I) #AbCDeFGHi
        sets['101101101'] = len((A & C & D & F & G & I) - B - E - H) #AbCDeFGhI
        sets['101101011'] = len((A & C & D & F & H & I) - B - E - G) #AbCDeFgHI
        sets['101100111'] = len((A & C & D & G & H & I) - B - E - F) #AbCDefGHI
        # {a,c,e,f,g,h} {a,c,e,f,g,i} {a,c,e,f,h,i} {a,c,e,g,h,i}
        sets['101011110'] = len((A & C & E & F & G & H) - B - D - I) #AbCdEFGHi
        sets['101011101'] = len((A & C & E & F & G & I) - B - D - H) #AbCdEFGhI
        sets['101011011'] = len((A & C & E & F & H & I) - B - D - G) #AbCdEFgHI
        sets['101010111'] = len((A & C & E & F & H & I) - B - D - G) #AbCdEFgHI
        # {a,c,f,g,h,i} {a,d,e,f,g,h} {a,d,e,f,g,i} {a,d,e,f,h,i}
        sets['101001111'] = len((A & C & F & G & H & I) - B - D - E) #AbCdeFGHI
        sets['100111110'] = len((A & D & E & F & G & H) - B - C - I) #AbcDEFGHi
        sets['100111101'] = len((A & D & E & F & G & I) - B - C - H) #AbcDEFGhI
        sets['100111011'] = len((A & D & E & F & H & I) - B - C - G) #AbcDEFgHI
        # {a,d,e,g,h,i} {a,d,f,g,h,i} {a,e,f,g,h,i}
        sets['100110111'] = len((A & D & E & G & H & I) - B - C - F) #AbcDEfGHI
        sets['100101111'] = len((A & D & F & G & H & I) - B - C - E) #AbcDeFGHI
        sets['100011111'] = len((A & E & F & G & H & I) - B - C - D) #AbcdEFGHI
        # {b,c,d,e,f,g} {b,c,d,e,f,h} {b,c,d,e,f,i} {b,c,d,e,g,h} {b,c,d,e,g,i}
        sets['011111100'] = len((B & C & D & E & F & G) - A - H - I) #aBCDEFGhi
        sets['011111010'] = len((B & C & D & E & F & H) - A - G - I) #aBCDEFgHi
        sets['011111001'] = len((B & C & D & E & F & I) - A - G - H) #aBCDEFghI
        sets['011110110'] = len((B & C & D & E & G & H) - A - F - I) #aBCDEfGHi
        sets['011110101'] = len((B & C & D & E & G & I) - A - F - H) #aBCDEfGhI
        # {b,c,d,e,h,i} {b,c,d,f,g,h} {b,c,d,f,g,i} {b,c,d,f,h,i} {b,c,d,g,h,i}
        sets['011110011'] = len((B & C & D & E & H & I) - A - F - G) #aBCDEfgHI
        sets['011101110'] = len((B & C & D & F & G & H) - A - E - I) #aBCDeFGHi
        sets['011101101'] = len((B & C & D & F & G & I) - A - E - H) #aBCDeFGhI
        sets['011101011'] = len((B & C & D & F & H & I) - A - E - G) #aBCDeFgHI
        sets['011100111'] = len((B & C & D & G & H & I) - A - E - F) #aBCDefGHI
        # {b,c,e,f,g,h} {b,c,e,f,g,i} {b,c,e,f,h,i} {b,c,e,g,h,i}
        sets['011011110'] = len((B & C & E & F & G & H) - A - D - I) #aBCdEFGHi
        sets['011011101'] = len((B & C & E & F & G & I) - A - D - H) #aBCdEFGhI
        sets['011011011'] = len((B & C & E & F & H & I) - A - D - G) #aBCdEFgHI
        sets['011010111'] = len((B & C & E & G & H & I) - A - D - F) #aBCdEfGHI
        # {b,c,f,g,h,i} {b,d,e,f,g,h} {b,d,e,f,g,i} {b,d,e,f,h,i}
        sets['011001111'] = len((B & C & F & G & H & I) - A - D - E) #aBCdeFGHI
        sets['010111110'] = len((B & D & E & F & G & H) - A - C - I) #aBcDEFGHi
        sets['010111101'] = len((B & D & E & F & G & I) - A - C - H) #aBcDEFGhI
        sets['010111011'] = len((B & D & E & F & H & I) - A - C - G) #aBcDEFgHI
        # {b,d,e,g,h,i} {b,d,f,g,h,i}
        sets['010110111'] = len((B & D & E & G & H & I) - A - C - F) #aBcDEfGHI
        sets['010101111'] = len((B & D & F & G & H & I) - A - C - E) #aBcDeFGHI
        # {b,e,f,g,h,i} {c,d,e,f,g,h} {c,d,e,f,g,i} {c,d,e,f,h,i}
        sets['010011111'] = len((B & E & F & G & H & I) - A - C - D) #aBcdEFGHI
        sets['001111110'] = len((C & D & E & F & G & H) - A - B - I) #abCDEFGHi
        sets['001111101'] = len((C & D & E & F & G & I) - A - B - H) #abCDEFGhI
        sets['001111011'] = len((C & D & E & F & H & I) - A - B - G) #abCDEFgHI
        # {c,d,e,g,h,i} {c,d,f,g,h,i} {c,e,f,g,h,i}
        sets['001110111'] = len((C & D & E & G & H & I) - A - B - F) #abCDEfGHI
        sets['001101111'] = len((C & D & F & G & H & I) - A - B - E) #abCDeFGHI
        sets['001011111'] = len((C & E & F & G & H & I) - A - B - D) #abCdEFGHI
        # {d,e,f,g,h,i}
        sets['000111111'] = len((D & E & F & G & H & I) - A - B - C) #abcDEFGHI
        # {a,b,c,d,e,f,g} {a,b,c,d,e,f,h} {a,b,c,d,e,f,i} {a,b,c,d,e,g,h} {a,b,c,d,e,g,i} {a,b,c,d,e,h,i}
        sets['111111100'] = len((A & B & C & D & E & F & G) - H - I) #ABCDEFGhi
        sets['111111010'] = len((A & B & C & D & E & F & H) - G - I) #ABCDEFgHi
        sets['111111001'] = len((A & B & C & D & E & F & I) - G - H) #ABCDEFghI
        sets['111110110'] = len((A & B & C & D & E & G & H) - F - I) #ABCDEfGHi
        sets['111110101'] = len((A & B & C & D & E & G & I) - F - H) #ABCDEfGhI
        sets['111110011'] = len((A & B & C & D & E & H & I) - F - G) #ABCDEfgHI
        # {a,b,c,d,f,g,h} {a,b,c,d,f,g,i} {a,b,c,d,f,h,i} {a,b,c,d,g,h,i}
        sets['111101110'] = len((A & B & C & D & F & G & H) - E - I) #ABCDeFGHi
        sets['111101101'] = len((A & B & C & D & F & G & I) - E - H) #ABCDeFGhI
        sets['111101011'] = len((A & B & C & D & F & H & I) - E - G) #ABCDeFgHI
        sets['111100111'] = len((A & B & C & D & G & H & I) - E - F) #ABCDefGHI
        # {a,b,c,e,f,g,h} {a,b,c,e,f,g,i} {a,b,c,e,f,h,i} {a,b,c,e,g,h,i}
        sets['111011110'] = len((A & B & C & E & F & G & H) - D - I) #ABCdEFGHi
        sets['111011101'] = len((A & B & C & E & F & G & I) - D - H) #ABCdEFGhI
        sets['111011011'] = len((A & B & C & E & F & H & I) - D - G) #ABCdEFgHI
        sets['111010111'] = len((A & B & C & E & G & H & I) - D - F) #ABCdEfGHI
        # {a,b,c,f,g,h,i} {a,b,d,e,f,g,h}
        sets['111001111'] = len((A & B & C & F & G & H & I) - D - E) #ABCdeFGHI
        sets['110111110'] = len((A & B & D & E & F & G & H) - C - I) #ABcDEFGHi
        # {a,b,d,e,f,g,i} {a,b,d,e,f,h,i} {a,b,d,e,g,h,i}
        sets['110111101'] = len((A & B & D & E & F & G & I) - C - H) #ABcDEFGhI
        sets['110111011'] = len((A & B & D & E & F & H & I) - C - G) #ABcDEFgHI
        sets['110110111'] = len((A & B & D & E & G & H & I) - C - F) #ABcDEfGHI
        # {a,b,d,f,g,h,i} {a,b,e,f,g,h,i}
        sets['110101111'] = len((A & B & D & F & G & H & I) - C - E) #ABcDeFGHI
        sets['110011111'] = len((A & B & E & F & G & H & I) - C - D) #ABcdEFGHI
        # {a,c,d,e,f,g,h} {a,c,d,e,f,g,i} {a,c,d,e,f,h,i} {a,c,d,e,g,h,i}
        sets['101111110'] = len((A & C & D & E & F & G & H) - B - I) #AbCDEFGHi
        sets['101111101'] = len((A & C & D & E & F & G & I) - B - H) #AbCDEFGhI
        sets['101111011'] = len((A & C & D & E & F & H & I) - B - G) #AbCDEFgHI
        sets['101110111'] = len((A & C & D & E & G & H & I) - B - F) #AbCDEfGHI
        # {a,c,d,f,g,h,i} {a,c,e,f,g,h,i}
        sets['101101111'] = len((A & C & D & F & G & H & I) - B - E) #AbCDeFGHI
        sets['101011111'] = len((A & C & E & F & G & H & I) - B - D) #AbCdEFGHI
        # {a,d,e,f,g,h,i}
        sets['100111111'] = len((A & D & E & F & G & H & I) - B - C) #AbcDEFGHI
        # {b,c,d,e,f,g,h} {b,c,d,e,f,g,i} {b,c,d,e,f,h,i}
        sets['011111110'] = len((B & C & D & E & F & G & H) - A - I) #aBCDEFGHi
        sets['011111101'] = len((B & C & D & E & F & G & I) - A - H) #aBCDEFGhI
        sets['011111011'] = len((B & C & D & E & F & H & I) - A - G) #aBCDEFgHI
        # {b,c,d,e,g,h,i} {b,c,d,f,g,h,i}
        sets['011110111'] = len((B & C & D & E & G & H & I) - A - F) #aBCDEfGHI
        sets['011101111'] = len((B & C & D & F & G & H & I) - A - E) #aBCDeFGHI
        # {b,c,e,f,g,h,i} {b,d,e,f,g,h,i}
        sets['011011111'] = len((B & C & E & F & G & H & I) - A - D) #aBCdEFGHI
        sets['010111111'] = len((B & D & E & F & G & H & I) - A - C) #aBcDEFGHI
        # {c,d,e,f,g,h,i}
        sets['001111111'] = len((C & D & E & F & G & H & I) - A - B) #abCDEFGHI
        # {a,b,c,d,e,f,g,h} {a,b,c,d,e,f,g,i} {a,b,c,d,e,f,h,i} {a,b,c,d,e,g,h,i}
        sets['111111110'] = len((A & B & C & D & E & F & G & H) - I) #ABCDEFGHi
        sets['111111101'] = len((A & B & C & D & E & F & G & I) - H) #ABCDEFGhI
        sets['111111011'] = len((A & B & C & D & E & F & H & I) - G) #ABCDEFgHI
        sets['111110111'] = len((A & B & C & D & E & G & H & I) - F) #ABCDEfGHI
        # {a,b,c,d,f,g,h,i} {a,b,c,e,f,g,h,i}
        sets['111101111'] = len((A & B & C & D & F & G & H & I) - E) #ABCDeFGHI
        sets['111011111'] = len((A & B & C & E & F & G & H & I) - D) #ABCdEFGHI
        # {a,b,d,e,f,g,h,i}
        sets['110111111'] = len((A & B & D & E & F & G & H & I) - C) #ABcDEFGHI
        # {a,c,d,e,f,g,h,i}
        sets['101111111'] = len((A & C & D & E & F & G & H & I) - B) #AbCDEFGHI
        # {b,c,d,e,f,g,h,i}
        sets['011111111'] = len((B & C & D & E & F & G & H & I) - A) #aBCDEFGHI
        # {a,b,c,d,e,f,g,h,i}
        sets['111111111'] = len(A & B & C & D & E & F & G & H & I) #ABCDEFGHI
    elif (numb == 10):
        A = set(mysets[0])
        B = set(mysets[1])
        C = set(mysets[2])
        D = set(mysets[3])
        E = set(mysets[4])
        F = set(mysets[5])
        G = set(mysets[6])
        H = set(mysets[7])
        I = set(mysets[8])
        J = set(mysets[9])
        # {a} {b} {c} {d} {e} {f} {g} {h} {i} {j}
        sets['1000000000'] = len(A - B - C - D - E - F - G - H - I - J) #Abcdefghij
        sets['0100000000'] = len(B - A - C - D - E - F - G - H - I - J) #aBcdefghij
        sets['0010000000'] = len(C - B - A - D - E - F - G - H - I - J) #abCdefghij
        sets['0001000000'] = len(D - B - C - A - E - F - G - H - I - J) #abcDefghij
        sets['0000100000'] = len(E - B - C - D - A - F - G - H - I - J) #abcdEfghij
        sets['0000010000'] = len(F - B - C - D - E - A - G - H - I - J) #abcdeFghij
        sets['0000001000'] = len(G - B - C - D - E - F - A - H - I - J) #abcdefGhij
        sets['0000000100'] = len(H - B - C - D - E - F - G - A - I - J) #abcdefgHij
        sets['0000000010'] = len(I - B - C - D - E - F - G - H - A - J) #abcdefghIj
        sets['0000000001'] = len(J - B - C - D - E - F - G - H - I - A) #abcdefghiJ
        # {a,b} {a,c} {a,d} {a,e} {a,f} {a,g} {a,h} {a,i} {a,j} {b,c} {b,d} {b,e} {b,f} {b,g} {b,h}
        sets['1100000000'] = len((A & B) - C - D - E - F - G - H - I - J) #ABcdefghij
        sets['1010000000'] = len((A & C) - B - D - E - F - G - H - I - J) #AbCdefghij
        sets['1001000000'] = len((A & D) - B - C - E - F - G - H - I - J) #AbcDefghij
        sets['1000100000'] = len((A & E) - B - C - D - F - G - H - I - J) #AbcdEfghij
        sets['1000010000'] = len((A & F) - B - C - D - E - G - H - I - J) #AbcdeFghij
        sets['1000001000'] = len((A & G) - B - C - D - E - F - H - I - J) #AbcdefGhij
        sets['1000000100'] = len((A & H) - B - C - D - E - F - G - I - J) #AbcdefgHij
        sets['1000000010'] = len((A & I) - B - C - D - E - F - G - H - J) #AbcdefghIj
        sets['1000000001'] = len((A & J) - B - C - D - E - F - G - H - I) #AbcdefghiJ
        sets['0110000000'] = len((B & C) - A - D - E - F - G - H - I - J) #aBCdefghij
        sets['0101000000'] = len((B & D) - A - C - E - F - G - H - I - J) #aBcDefghij
        sets['0100100000'] = len((B & E) - A - C - D - F - G - H - I - J) #aBcdEfghij
        sets['0100010000'] = len((B & F) - A - C - D - E - G - H - I - J) #aBcdeFghij
        sets['0100001000'] = len((B & G) - A - C - D - E - F - H - I - J) #aBcdefGhij
        sets['0100000100'] = len((B & H) - A - C - D - E - F - G - I - J) #aBcdefgHij
        # {b,i} {b,j} {c,d} {c,e} {c,f} {c,g} {c,h} {c,i} {c,j} {d,e} {d,f} {d,g} {d,h} {d,i} {d,j}
        sets['0100000010'] = len((B & I) - A - C - D - E - F - G - H - J) #aBcdefghIj
        sets['0100000001'] = len((B & J) - A - C - D - E - F - G - H - I) #aBcdefghiJ
        sets['0011000000'] = len((C & D) - A - B - E - F - G - H - I - J) #abCDefghij
        sets['0010100000'] = len((C & E) - A - B - D - F - G - H - I - J) #abCdEfghij
        sets['0010010000'] = len((C & F) - A - B - D - E - G - H - I - J) #abCdeFghij
        sets['0010001000'] = len((C & G) - A - B - D - E - F - H - I - J) #abCdefGhij
        sets['0010000100'] = len((C & H) - A - B - D - E - F - G - I - J) #abCdefgHij
        sets['0010000010'] = len((C & I) - A - B - D - E - F - G - H - J) #abCdefghIj
        sets['0010000001'] = len((C & J) - A - B - D - E - F - G - H - I) #abCdefghiJ
        sets['0001100000'] = len((D & E) - A - B - C - F - G - H - I - J) #abcDEfghij
        sets['0001010000'] = len((D & F) - A - B - C - E - G - H - I - J) #abcDeFghij
        sets['0001001000'] = len((D & G) - A - B - C - E - F - H - I - J) #abcDefGhij
        sets['0001000100'] = len((D & H) - A - B - C - E - F - G - I - J) #abcDefgHij
        sets['0001000010'] = len((D & I) - A - B - C - E - F - G - H - J) #abcDefghIj
        sets['0001000001'] = len((D & J) - A - B - C - E - F - G - H - I) #abcDefghiJ
        # {e,f} {e,g} {e,h} {e,i} {e,j} {f,g} {f,h} {f,i} {f,j} {g,h} {g,i} {g,j} {h,i} {h,j} {i,j}
        sets['0000110000'] = len((E & F) - A - B - C - D - G - H - I - J) #abcdEFghij
        sets['0000101000'] = len((E & G) - A - B - C - D - F - H - I - J) #abcdEfGhij
        sets['0000100100'] = len((E & H) - A - B - C - D - F - G - I - J) #abcdEfgHij
        sets['0000100010'] = len((E & I) - A - B - C - D - F - G - H - J) #abcdEfghIj
        sets['0000100001'] = len((E & J) - A - B - C - D - F - G - H - I) #abcdEfghiJ
        sets['0000011000'] = len((F & G) - A - B - C - D - E - H - I - J) #abcdeFGhij
        sets['0000010100'] = len((F & H) - A - B - C - D - E - G - I - J) #abcdeFgHij
        sets['0000010010'] = len((F & I) - A - B - C - D - E - G - H - J) #abcdeFghIj
        sets['0000010001'] = len((F & J) - A - B - C - D - E - G - H - I) #abcdeFghiJ
        sets['0000001100'] = len((G & H) - A - B - C - D - E - F - I - J) #abcdefGHij
        sets['0000001010'] = len((G & I) - A - B - C - D - E - F - H - J) #abcdefGhIj
        sets['0000001001'] = len((G & J) - A - B - C - D - E - F - H - I) #abcdefGhiJ
        sets['0000000110'] = len((H & I) - A - B - C - D - E - F - G - J) #abcdefgHIj
        sets['0000000101'] = len((H & J) - A - B - C - D - E - F - G - I) #abcdefgHiJ
        sets['0000000011'] = len((I & J) - A - B - C - D - E - F - G - H) #abcdefghIJ
        # {a,b,c} {a,b,d} {a,b,e} {a,b,f} {a,b,g} {a,b,h} {a,b,i} {a,b,j} {a,c,d} {a,c,e} {a,c,f} {a,c,g} {a,c,h} {a,c,i} {a,c,j}
        sets['1110000000'] = len((A & B & C) - D - E - F - G - H - I - J) #ABCdefghij
        sets['1101000000'] = len((A & B & D) - C - E - F - G - H - I - J) #ABcDefghij
        sets['1100100000'] = len((A & B & E) - C - D - F - G - H - I - J) #ABcdEfghij
        sets['1100010000'] = len((A & B & F) - C - D - E - G - H - I - J) #ABcdeFghij
        sets['1100001000'] = len((A & B & G) - C - D - E - F - H - I - J) #ABcdefGhij
        sets['1100000100'] = len((A & B & H) - C - D - E - F - G - I - J) #ABcdefgHij
        sets['1100000010'] = len((A & B & I) - C - D - E - F - G - H - J) #ABcdefghIj
        sets['1100000001'] = len((A & B & J) - C - D - E - F - G - H - I) #ABcdefghiJ
        sets['1011000000'] = len((A & C & D) - B - E - F - G - H - I - J) #AbCDefghij
        sets['1010100000'] = len((A & C & E) - B - D - F - G - H - I - J) #AbCdEfghij
        sets['1010010000'] = len((A & C & F) - B - D - E - G - H - I - J) #AbCdeFghij
        sets['1010001000'] = len((A & C & G) - B - D - E - F - H - I - J) #AbCdefGhij
        sets['1010000100'] = len((A & C & H) - B - D - E - F - G - I - J) #AbCdefgHij
        sets['1010000010'] = len((A & C & I) - B - D - E - F - G - H - J) #AbCdefghIj
        sets['1010000001'] = len((A & C & J) - B - D - E - F - G - H - I) #AbCdefghiJ
        # {a,d,e} {a,d,f} {a,d,g} {a,d,h} {a,d,i} {a,d,j} {a,e,f} {a,e,g} {a,e,h} {a,e,i} {a,e,j} {a,f,g} {a,f,h} {a,f,i} {a,f,j}
        sets['1001100000'] = len((A & D & E) - B - C - F - G - H - I - J) #AbcDEfghij
        sets['1001010000'] = len((A & D & F) - B - C - E - G - H - I - J) #AbcDeFghij
        sets['1001001000'] = len((A & D & G) - B - C - E - F - H - I - J) #AbcDefGhij
        sets['1001000100'] = len((A & D & H) - B - C - E - F - G - I - J) #AbcDefgHij
        sets['1001000010'] = len((A & D & I) - B - C - E - F - G - H - J) #AbcDefghIj
        sets['1001000001'] = len((A & D & J) - B - C - E - F - G - H - I) #AbcDefghiJ
        sets['1000110000'] = len((A & E & F) - B - C - D - G - H - I - J) #AbcdEFghij
        sets['1000101000'] = len((A & E & G) - B - C - D - F - H - I - J) #AbcdEfGhij
        sets['1000100100'] = len((A & E & H) - B - C - D - F - G - I - J) #AbcdEfgHij
        sets['1000100010'] = len((A & E & I) - B - C - D - F - G - H - J) #AbcdEfghIj
        sets['1000100001'] = len((A & E & J) - B - C - D - F - G - H - I) #AbcdEfghiJ
        sets['1000011000'] = len((A & F & G) - B - C - D - E - H - I - J) #AbcdeFGhij
        sets['1000010100'] = len((A & F & H) - B - C - D - E - G - I - J) #AbcdeFgHij
        sets['1000010010'] = len((A & F & I) - B - C - D - E - G - H - J) #AbcdeFghIj
        sets['1000010001'] = len((A & F & J) - B - C - D - E - G - H - I) #AbcdeFghiJ
        # {a,g,h} {a,g,i} {a,g,j} {a,h,i} {a,h,j} {a,i,j} {b,c,d} {b,c,e} {b,c,f} {b,c,g} {b,c,h} {b,c,i} {b,c,j} {b,d,e} {b,d,f}
        sets['1000001100'] = len((A & G & H) - B - C - D - E - F - I - J) #AbcdefGHij
        sets['1000001010'] = len((A & G & I) - B - C - D - E - F - H - J) #AbcdefGhIj
        sets['1000001001'] = len((A & G & J) - B - C - D - E - F - H - I) #AbcdefGHiJ
        sets['1000000110'] = len((A & H & I) - B - C - D - E - F - G - J) #AbcdefgHIj
        sets['1000000101'] = len((A & H & J) - B - C - D - E - F - G - I) #AbcdefgHiJ
        sets['1000000011'] = len((A & I & J) - B - C - D - E - F - G - H) #AbcdefghIJ
        sets['0111000000'] = len((B & C & D) - A - E - F - G - H - I - J) #aBCDefghij
        sets['0110100000'] = len((B & C & E) - A - D - F - G - H - I - J) #aBCdEfghij
        sets['0110010000'] = len((B & C & F) - A - D - E - G - H - I - J) #aBCdeFghij
        sets['0110001000'] = len((B & C & G) - A - D - E - F - H - I - J) #aBCdefGhij
        sets['0110000100'] = len((B & C & H) - A - D - E - F - G - I - J) #aBCdefgHij
        sets['0110000010'] = len((B & C & I) - A - D - E - F - G - H - J) #aBCdefghIj
        sets['0110000001'] = len((B & C & J) - A - D - E - F - G - H - I) #aBCdefghiJ
        sets['0101100000'] = len((B & D & E) - A - C - F - G - H - I - J) #aBcDEfghij
        sets['0101010000'] = len((B & D & F) - A - C - E - G - H - I - J) #aBcDeFghij 
        # {b,d,g} {b,d,h} {b,d,i} {b,d,j} {b,e,f} {b,e,g} {b,e,h} {b,e,i} {b,e,j} {b,f,g} {b,f,h} {b,f,i} {b,f,j} {b,g,h} {b,g,i}
        sets['0101001000'] = len((B & D & G) - A - C - E - F - H - I - J) #aBcDefGhij
        sets['0101000100'] = len((B & D & H) - A - C - E - F - G - I - J) #aBcDefgHij
        sets['0101000010'] = len((B & D & I) - A - C - E - F - G - H - J) #aBcDefghIj
        sets['0101000001'] = len((B & D & J) - A - C - E - F - G - H - I) #aBcDefgHiJ
        sets['0100110000'] = len((B & E & F) - A - C - D - G - H - I - J) #aBcdEFghIj
        sets['0100101000'] = len((B & E & G) - A - C - D - F - H - I - J) #aBcdEfGhiJ
        sets['0100100100'] = len((B & E & H) - A - C - D - F - G - I - J) #aBcdEfgHij
        sets['0100100010'] = len((B & E & I) - A - C - D - F - G - H - J) #aBcdEfghIj
        sets['0100100001'] = len((B & E & J) - A - C - D - F - G - H - I) #aBcdEfghiJ
        sets['0100011000'] = len((B & F & G) - A - C - D - E - H - I - J) #aBcdeFGhij
        sets['0100010100'] = len((B & F & H) - A - C - D - E - G - I - J) #aBcdeFgHij
        sets['0100010010'] = len((B & F & I) - A - C - D - E - G - H - J) #aBcdeFghIj
        sets['0100010001'] = len((B & F & J) - A - C - D - E - G - H - I) #aBcdeFghiJ
        sets['0100001100'] = len((B & G & H) - A - C - D - E - F - I - J) #aBcdefGHij
        sets['0100001010'] = len((B & G & I) - A - C - D - E - F - H - J) #aBcdefGhIj
        # {b,g,j} {b,h,i} {b,h,j} {b,i,j} {c,d,e} {c,d,f} {c,d,g} {c,d,h} {c,d,i} {c,d,j} {c,e,f} {c,e,g} {c,e,h} {c,e,i} {c,e,j}
        sets['0100001001'] = len((B & G & J) - A - C - D - E - F - H - I) #aBcdefGhiJ
        sets['0100000110'] = len((B & H & I) - A - C - D - E - F - G - J) #aBcdefgHIj
        sets['0100000101'] = len((B & H & J) - A - C - D - E - F - G - I) #aBcdefgHiJ
        sets['0100000011'] = len((B & I & J) - A - C - D - E - F - G - H) #aBcdefghIJ
        sets['0011100000'] = len((C & D & E) - A - B - F - G - H - I - J) #abCDEfghij
        sets['0011010000'] = len((C & D & F) - A - B - E - G - H - I - J) #abCDeFghij
        sets['0011001000'] = len((C & D & G) - A - B - E - F - H - I - J) #abCDefGhij
        sets['0011000100'] = len((C & D & H) - A - B - E - F - G - I - J) #abCDefgHij
        sets['0011000010'] = len((C & D & I) - A - B - E - F - G - H - J) #abCDefghIj
        sets['0011000001'] = len((C & D & J) - A - B - E - F - G - H - I) #abCDefghiJ
        sets['0010110000'] = len((C & E & F) - A - B - D - G - H - I - J) #abCdEFghij
        sets['0010101000'] = len((C & E & G) - A - B - D - F - H - I - J) #abCdEfGhij
        sets['0010100100'] = len((C & E & H) - A - B - D - F - G - I - J) #abCdEfgHij
        sets['0010100010'] = len((C & E & I) - A - B - D - F - G - H - J) #abCdEfghIj
        sets['0010100001'] = len((C & E & J) - A - B - D - F - G - H - I) #abCdEfghiJ
        # {c,f,g} {c,f,h} {c,f,i} {c,f,j} {c,g,h} {c,g,i} {c,g,j} {c,h,i} {c,h,j} {c,i,j} {d,e,f} {d,e,g} {d,e,h} {d,e,i} {d,e,j}
        sets['0010011000'] = len((C & F & G) - A - B - D - E - H - I - J) #abCdeFGhij
        sets['0010010100'] = len((C & F & H) - A - B - D - E - G - I - J) #abCdeFgHij
        sets['0010010010'] = len((C & F & I) - A - B - D - E - G - H - J) #abCdeFghIj
        sets['0010010001'] = len((C & F & J) - A - B - D - E - G - H - I) #abCdeFghiJ
        sets['0010001100'] = len((C & G & H) - A - B - D - E - F - I - J) #abCdefGHij
        sets['0010001010'] = len((C & G & I) - A - B - D - E - F - H - J) #abCdefGhIj
        sets['0010001001'] = len((C & G & J) - A - B - D - E - F - H - I) #abCdefGhiJ
        sets['0010000110'] = len((C & H & I) - A - B - D - E - F - G - J) #abCdefgHIj
        sets['0010000101'] = len((C & H & J) - A - B - D - E - F - G - I) #abCdefgHiJ
        sets['0010000011'] = len((C & I & J) - A - B - D - E - F - G - H) #abCdefghIJ
        sets['0001110000'] = len((D & E & F) - A - B - C - G - H - I - J) #abcDEFghij
        sets['0001101000'] = len((D & E & G) - A - B - C - F - H - I - J) #abcDEfGhij
        sets['0001100100'] = len((D & E & H) - A - B - C - F - G - I - J) #abcDEfgHij
        sets['0001100010'] = len((D & E & I) - A - B - C - F - G - H - J) #abcDEfghIj
        sets['0001100001'] = len((D & E & J) - A - B - C - F - G - H - I) #abcDEfghiJ
        # {d,f,g} {d,f,h} {d,f,i} {d,f,j} {d,g,h} {d,g,i} {d,g,j} {d,h,i} {d,h,j} {d,i,j} {e,f,g} {e,f,h} {e,f,i} {e,f,j} {e,g,h}
        sets['0001011000'] = len((D & F & G) - A - B - C - E - H - I - J) #abcDeFGhij
        sets['0001010100'] = len((D & F & H) - A - B - C - E - G - I - J) #abcDeFgHij
        sets['0001010010'] = len((D & F & I) - A - B - C - E - G - H - J) #abcDeFghIj
        sets['0001010001'] = len((D & F & J) - A - B - C - E - G - H - I) #abcDeFghiJ
        sets['0001001100'] = len((D & G & H) - A - B - C - E - F - I - J) #abcDefGHij
        sets['0001001010'] = len((D & G & I) - A - B - C - E - F - H - J) #abcDefGhIj
        sets['0001001001'] = len((D & G & J) - A - B - C - E - F - H - I) #abcDefGhiJ
        sets['0001000110'] = len((D & H & I) - A - B - C - E - F - G - J) #abcDefgHIj
        sets['0001000101'] = len((D & H & J) - A - B - C - E - F - G - I) #abcDefgHiJ
        sets['0001000011'] = len((D & I & J) - A - B - C - E - F - G - H) #abcDefghIJ
        sets['0000111000'] = len((E & F & G) - A - B - C - D - H - I - J) #abcdEFGhij
        sets['0000110100'] = len((E & F & H) - A - B - C - D - G - I - J) #abcdEFgHij
        sets['0000110010'] = len((E & F & I) - A - B - C - D - G - H - J) #abcdEFghIj
        sets['0000110001'] = len((E & F & J) - A - B - C - D - G - H - I) #abcdEFghiJ
        sets['0000101100'] = len((E & G & H) - A - B - C - D - F - I - J) #abcdEfGHij
        # {e,g,i} {e,g,j} {e,h,i} {e,h,j} {e,i,j} {f,g,h} {f,g,i} {f,g,j} {f,h,i} {f,h,j} {f,i,j} {g,h,i} {g,h,j} {g,i,j} {h,i,j}
        sets['0000101010'] = len((E & G & I) - A - B - C - D - F - H - J) #abcdEfGhIj
        sets['0000101001'] = len((E & G & J) - A - B - C - D - F - H - I) #abcdEfGhiJ
        sets['0000100110'] = len((E & H & I) - A - B - C - D - F - G - J) #abcdEfgHIj
        sets['0000100101'] = len((E & H & J) - A - B - C - D - F - G - I) #abcdEfgHiJ
        sets['0000100011'] = len((E & I & J) - A - B - C - D - F - G - H) #abcdEfghIJ
        sets['0000011100'] = len((F & G & H) - A - B - C - D - E - I - J) #abcdeFGHij
        sets['0000011010'] = len((F & G & I) - A - B - C - D - E - H - J) #abcdeFGhIj
        sets['0000011001'] = len((F & G & J) - A - B - C - D - E - H - I) #abcdeFGhiJ
        sets['0000010110'] = len((F & H & I) - A - B - C - D - E - G - J) #abcdeFgHIj
        sets['0000010101'] = len((F & H & J) - A - B - C - D - E - G - I) #abcdeFgHiJ
        sets['0000010011'] = len((F & I & J) - A - B - C - D - E - G - H) #abcdeFghIJ
        sets['0000001110'] = len((G & H & I) - A - B - C - D - E - F - J) #abcdefGHIj
        sets['0000001101'] = len((G & H & J) - A - B - C - D - E - F - I) #abcdefGHiJ
        sets['0000001011'] = len((G & I & J) - A - B - C - D - E - F - H) #abcdefGhIJ
        sets['0000000111'] = len((H & I & J) - A - B - C - D - E - F - G) #abcdefgHIJ
        # {a,b,c,d} {a,b,c,e} {a,b,c,f} {a,b,c,g} {a,b,c,h} {a,b,c,i} {a,b,c,j} {a,b,d,e} {a,b,d,f} {a,b,d,g} {a,b,d,h} {a,b,d,i} {a,b,d,j} {a,b,e,f} {a,b,e,g}
        sets['1111000000'] = len((A & B & C & D) - E - F - G - H - I - J) #ABCDefghij
        sets['1110100000'] = len((A & B & C & E) - D - F - G - H - I - J) #ABCdEfghij
        sets['1110010000'] = len((A & B & C & F) - D - E - G - H - I - J) #ABCdeFghij
        sets['1110001000'] = len((A & B & C & G) - D - E - F - H - I - J) #ABCdefGhij
        sets['1110000100'] = len((A & B & C & H) - D - E - F - G - I - J) #ABCdefgHij
        sets['1110000010'] = len((A & B & C & I) - D - E - F - G - H - J) #ABCdefghIj
        sets['1110000001'] = len((A & B & C & J) - D - E - F - G - H - I) #ABCdefghiJ
        sets['1101100000'] = len((A & B & D & E) - C - F - G - H - I - J) #ABcDEfghij
        sets['1101010000'] = len((A & B & D & F) - C - E - G - H - I - J) #ABcDeFghij
        sets['1101001000'] = len((A & B & D & G) - C - E - F - H - I - J) #ABcDefGhij
        sets['1101000100'] = len((A & B & D & H) - C - E - F - G - I - J) #ABcDefgHij
        sets['1101000010'] = len((A & B & D & I) - C - E - F - G - H - J) #ABcDefghIj
        sets['1101000001'] = len((A & B & D & J) - C - E - F - G - H - I) #ABcDefghiJ
        sets['1100110000'] = len((A & B & E & F) - C - D - G - H - I - J) #ABcdEFghij
        sets['1100101000'] = len((A & B & E & G) - C - D - F - H - I - J) #ABcdEfGhij
        # {a,b,e,h} {a,b,e,i} {a,b,e,j} {a,b,f,g} {a,b,f,h} {a,b,f,i} {a,b,f,j} {a,b,g,h} {a,b,g,i} {a,b,g,j} {a,b,h,i} {a,b,h,j} {a,b,i,j} {a,c,d,e} {a,c,d,f}
        sets['1100100100'] = len((A & B & E & H) - C - D - F - G - I - J) #ABcdEfgHij
        sets['1100100010'] = len((A & B & E & I) - C - D - F - G - H - J) #ABcdEfghIj
        sets['1100100001'] = len((A & B & E & J) - C - D - F - G - H - I) #ABcdEfghiJ
        sets['1100011000'] = len((A & B & F & G) - C - D - E - H - I - J) #ABcdeFGhij
        sets['1100010100'] = len((A & B & F & H) - C - D - E - G - I - J) #ABcdeFgHij
        sets['1100010010'] = len((A & B & F & I) - C - D - E - G - H - J) #ABcdeFghIj
        sets['1100010001'] = len((A & B & F & J) - C - D - E - G - H - I) #ABcdeFghiJ
        sets['1100001100'] = len((A & B & G & H) - C - D - E - F - I - J) #ABcdefGHij
        sets['1100001010'] = len((A & B & G & I) - C - D - E - F - H - J) #ABcdefGhIj
        sets['1100001001'] = len((A & B & G & J) - C - D - E - F - H - I) #ABcdefGhiJ
        sets['1100000110'] = len((A & B & H & I) - C - D - E - F - G - J) #ABcdefgHIj
        sets['1100000101'] = len((A & B & H & J) - C - D - E - F - G - I) #ABcdefgHiJ
        sets['1100000011'] = len((A & B & I & J) - C - D - E - F - G - H) #ABcdefghIJ
        sets['1011100000'] = len((A & C & D & E) - B - F - G - H - I - J) #AbCDEfghij
        sets['1011010000'] = len((A & C & D & F) - B - E - G - H - I - J) #AbCDeFghij
        # {a,c,d,g} {a,c,d,h} {a,c,d,i} {a,c,d,j} {a,c,e,f} {a,c,e,g} {a,c,e,h} {a,c,e,i} {a,c,e,j} {a,c,f,g} {a,c,f,h} {a,c,f,i} {a,c,f,j} {a,c,g,h} {a,c,g,i}
        sets['1011001000'] = len((A & C & D & G) - B - E - F - H - I - J) #AbCDefGhij
        sets['1011000100'] = len((A & C & D & H) - B - E - F - G - I - J) #AbCDefgHij
        sets['1011000010'] = len((A & C & D & I) - B - E - F - G - H - J) #AbCDefghIj
        sets['1011000001'] = len((A & C & D & J) - B - E - F - G - H - I) #AbCDefghiJ
        sets['1010110000'] = len((A & C & E & F) - B - D - G - H - I - J) #AbCdEFghij
        sets['1010101000'] = len((A & C & E & G) - B - D - F - H - I - J) #AbCdEfGhij
        sets['1010100100'] = len((A & C & E & H) - B - D - F - G - I - J) #AbCdEfgHij
        sets['1010100010'] = len((A & C & E & I) - B - D - F - G - H - J) #AbCdEfghIj
        sets['1010100001'] = len((A & C & E & J) - B - D - F - G - H - I) #AbCdEfghiJ
        sets['1010011000'] = len((A & C & F & G) - B - D - E - H - I - J) #AbCdeFGhij
        sets['1010010100'] = len((A & C & F & H) - B - D - E - G - I - J) #AbCdeFgHij
        sets['1010010010'] = len((A & C & F & I) - B - D - E - G - H - J) #AbCdeFghIj
        sets['1010010001'] = len((A & C & F & J) - B - D - E - G - H - I) #AbCdeFghiJ
        sets['1010001100'] = len((A & C & G & H) - B - D - E - F - I - J) #AbCdefGHij
        sets['1010001010'] = len((A & C & G & I) - B - D - E - F - H - J) #AbCdefGhIj
        # {a,c,g,j} {a,c,h,i} {a,c,h,j} {a,c,i,j} {a,d,e,f} {a,d,e,g} {a,d,e,h} {a,d,e,i} {a,d,e,j} {a,d,f,g} {a,d,f,h} {a,d,f,i} {a,d,f,j} {a,d,g,h} {a,d,g,i}
        sets['1010001001'] = len((A & C & G & J) - B - D - E - F - H - I) #AbCdefGhiJ
        sets['1010000110'] = len((A & C & H & I) - B - D - E - F - G - J) #AbCdefgHIj
        sets['1010000101'] = len((A & C & H & J) - B - D - E - F - G - I) #AbCdefgHiJ
        sets['1010000011'] = len((A & C & I & J) - B - D - E - F - G - H) #AbCdefghIJ
        sets['1001110000'] = len((A & D & E & F) - B - C - G - H - I - J) #AbcDEFghij
        sets['1001101000'] = len((A & D & E & G) - B - C - F - H - I - J) #AbcDEfGhij
        sets['1001100100'] = len((A & D & E & H) - B - C - F - G - I - J) #AbcDEfgHij
        sets['1001100010'] = len((A & D & E & I) - B - C - F - G - H - J) #AbcDEfghIj
        sets['1001100001'] = len((A & D & E & J) - B - C - F - G - H - I) #AbcDEfghiJ
        sets['1001011000'] = len((A & D & F & G) - B - C - E - H - I - J) #AbcDeFGhij
        sets['1001010100'] = len((A & D & F & H) - B - C - E - G - I - J) #AbcDeFgHij
        sets['1001010010'] = len((A & D & F & I) - B - C - E - G - H - J) #AbcDeFghIj
        sets['1001010001'] = len((A & D & F & J) - B - C - E - G - H - I) #AbcDeFghiJ
        sets['1001001100'] = len((A & D & G & H) - B - C - E - F - I - J) #AbcDefGHij
        sets['1001001010'] = len((A & D & G & I) - B - C - E - F - H - J) #AbcDefGhIj
        # {a,d,g,j} {a,d,h,i} {a,d,h,j} {a,d,i,j} {a,e,f,g} {a,e,f,h} {a,e,f,i} {a,e,f,j} {a,e,g,h} {a,e,g,i} {a,e,g,j} {a,e,h,i} {a,e,h,j} {a,e,i,j} {a,f,g,h}
        sets['1001001001'] = len((A & D & G & J) - B - C - E - F - H - I) #AbcDefGhiJ
        sets['1001000110'] = len((A & D & H & I) - B - C - E - F - G - J) #AbcDefgHIj
        sets['1001000101'] = len((A & D & H & J) - B - C - E - F - G - I) #AbcDefgHiJ
        sets['1001000011'] = len((A & D & I & J) - B - C - E - F - G - H) #AbcDefghIJ
        sets['1000111000'] = len((A & E & F & G) - B - C - D - H - I - J) #AbcdEFGhij
        sets['1000110100'] = len((A & E & F & H) - B - C - D - G - I - J) #AbcdEFgHij
        sets['1000110010'] = len((A & E & F & I) - B - C - D - G - H - J) #AbcdEFghIj
        sets['1000110001'] = len((A & E & F & J) - B - C - D - G - H - I) #AbcdEFghiJ
        sets['1000101100'] = len((A & E & G & H) - B - C - D - F - I - J) #AbcdEfGHij
        sets['1000101010'] = len((A & E & G & I) - B - C - D - F - H - J) #AbcdEfGhIj
        sets['1000101001'] = len((A & E & G & J) - B - C - D - F - H - I) #AbcdEfGhiJ
        sets['1000100110'] = len((A & E & H & I) - B - C - D - F - G - J) #AbcdEfgHIj
        sets['1000100101'] = len((A & E & H & J) - B - C - D - F - G - I) #AbcdEfgHiJ
        sets['1000100011'] = len((A & E & I & J) - B - C - D - F - G - H) #AbcdEfghIJ
        sets['1000011100'] = len((A & F & G & H) - B - C - D - E - I - J) #AbcdeFGHij
        # {a,f,g,i} {a,f,g,j} {a,f,h,i} {a,f,h,j} {a,f,i,j} {a,g,h,i} {a,g,h,j} {a,g,i,j} {a,h,i,j} {b,c,d,e} {b,c,d,f} {b,c,d,g} {b,c,d,h} {b,c,d,i} {b,c,d,j}
        sets['1000011010'] = len((A & F & G & I) - B - C - D - E - H - J) #AbcdeFGhIj
        sets['1000011001'] = len((A & F & G & J) - B - C - D - E - H - I) #AbcdeFGhiJ
        sets['1000010110'] = len((A & F & H & I) - B - C - D - E - G - J) #AbcdeFgHIj
        sets['1000010101'] = len((A & F & H & J) - B - C - D - E - G - I) #AbcdeFgHiJ
        sets['1000010011'] = len((A & F & I & J) - B - C - D - E - G - H) #AbcdeFghIJ
        sets['1000001110'] = len((A & G & H & I) - B - C - D - E - F - J) #AbcdefGHIj
        sets['1000001101'] = len((A & G & H & J) - B - C - D - E - F - I) #AbcdefGHiJ
        sets['1000001011'] = len((A & G & I & J) - B - C - D - E - F - H) #AbcdefGhIJ
        sets['1000000111'] = len((A & H & I & J) - B - C - D - E - F - G) #AbcdefgHIJ
        sets['0111100000'] = len((B & C & D & E) - A - F - G - H - I - J) #aBCDEfghij
        sets['0111010000'] = len((B & C & D & F) - A - E - G - H - I - J) #aBCDeFghij
        sets['0111001000'] = len((B & C & D & G) - A - E - F - H - I - J) #aBCDefGhij
        sets['0111000100'] = len((B & C & D & H) - A - E - F - G - I - J) #aBCDefgHij
        sets['0111000010'] = len((B & C & D & I) - A - E - F - G - H - J) #aBCDefghIj
        sets['0111000001'] = len((B & C & D & J) - A - E - F - G - H - I) #aBCDefghiJ
        # {b,c,e,f} {b,c,e,g} {b,c,e,h} {b,c,e,i} {b,c,e,j} {b,c,f,g} {b,c,f,h} {b,c,f,i} {b,c,f,j} {b,c,g,h} {b,c,g,i} {b,c,g,j} {b,c,h,i} {b,c,h,j} {b,c,i,j}
        sets['0110110000'] = len((B & C & E & F) - A - D - G - H - I - J) #aBCdEFghij
        sets['0110101000'] = len((B & C & E & G) - A - D - F - H - I - J) #aBCdEfGhij
        sets['0110100100'] = len((B & C & E & H) - A - D - F - G - I - J) #aBCdEfgHij
        sets['0110100010'] = len((B & C & E & I) - A - D - F - G - H - J) #aBCdEfghIj
        sets['0110100001'] = len((B & C & E & J) - A - D - F - G - H - I) #aBCdEfghiJ
        sets['0110011000'] = len((B & C & F & G) - A - D - E - H - I - J) #aBCdeFGhij
        sets['0110010100'] = len((B & C & F & H) - A - D - E - G - I - J) #aBCdeFgHij
        sets['0110010010'] = len((B & C & F & I) - A - D - E - G - H - J) #aBCdeFghIj
        sets['0110010001'] = len((B & C & F & J) - A - D - E - F - H - I) #aBCdeFghiJ
        sets['0110001100'] = len((B & C & G & H) - A - D - E - F - I - J) #aBCdefGHij
        sets['0110001010'] = len((B & C & G & I) - A - D - E - F - H - J) #aBCdefGhIj
        sets['0110001001'] = len((B & C & G & J) - A - D - E - F - H - I) #aBCdefGhiJ
        sets['0110000110'] = len((B & C & H & I) - A - D - E - F - G - J) #aBCdefgHIj
        sets['0110000101'] = len((B & C & H & J) - A - D - E - F - G - I) #aBCdefgHiJ
        sets['0110000011'] = len((B & C & I & J) - A - D - E - F - G - H) #aBCdefghIJ
        # {b,d,e,f} {b,d,e,g} {b,d,e,h} {b,d,e,i} {b,d,e,j} {b,d,f,g} {b,d,f,h} {b,d,f,i} {b,d,f,j} {b,d,g,h} {b,d,g,i} {b,d,g,j} {b,d,h,i} {b,d,h,j} {b,d,i,j}
        sets['0101110000'] = len((B & D & E & F) - A - C - G - H - I - J) #aBcDEFghij
        sets['0101101000'] = len((B & D & E & G) - A - C - F - H - I - J) #aBcDEfGhij
        sets['0101100100'] = len((B & D & E & H) - A - C - F - G - I - J) #aBcDEfgHij
        sets['0101100010'] = len((B & D & E & I) - A - C - F - G - H - J) #aBcDEfghIj
        sets['0101100001'] = len((B & D & E & J) - A - C - F - G - H - I) #aBcDEfghiJ
        sets['0101011000'] = len((B & D & F & G) - A - C - E - H - I - J) #aBcDeFGhij
        sets['0101010100'] = len((B & D & F & H) - A - C - E - G - I - J) #aBcDeFgHij
        sets['0101010010'] = len((B & D & F & I) - A - C - E - G - H - J) #aBcDeFghIj
        sets['0101010001'] = len((B & D & F & J) - A - C - E - G - H - I) #aBcDeFghiJ
        sets['0101001100'] = len((B & D & G & H) - A - C - E - F - I - J) #aBcDefGHij
        sets['0101001010'] = len((B & D & G & I) - A - C - E - F - H - J) #aBcDefGhIj
        sets['0101001001'] = len((B & D & G & J) - A - C - E - F - H - I) #aBcDefGhiJ
        sets['0101000110'] = len((B & D & H & I) - A - C - E - F - G - J) #aBcDefgHIj
        sets['0101000101'] = len((B & D & H & J) - A - C - E - F - G - I) #aBcDefgHiJ
        sets['0101000011'] = len((B & D & I & J) - A - C - E - F - G - H) #aBcDefghIJ
        # {b,e,f,g} {b,e,f,h} {b,e,f,i} {b,e,f,j} {b,e,g,h} {b,e,g,i} {b,e,g,j} {b,e,h,i} {b,e,h,j} {b,e,i,j} {b,f,g,h} {b,f,g,i} {b,f,g,j} {b,f,h,i} {b,f,h,j}
        sets['0100111000'] = len((B & E & F & G) - A - C - D - H - I - J) #aBcdEFGhij
        sets['0100110100'] = len((B & E & F & H) - A - C - D - G - I - J) #aBcdEFgHij
        sets['0100110010'] = len((B & E & F & I) - A - C - D - G - H - J) #aBcdEFghIj
        sets['0100110001'] = len((B & E & F & J) - A - C - D - G - H - I) #aBcdEFghiJ
        sets['0100101100'] = len((B & E & G & H) - A - C - D - F - I - J) #aBcdEfGHij
        sets['0100101010'] = len((B & E & G & I) - A - C - D - F - H - J) #aBcdEfGhIj
        sets['0100101001'] = len((B & E & G & J) - A - C - D - F - H - I) #aBcdEfGhiJ
        sets['0100100110'] = len((B & E & H & I) - A - C - D - F - G - J) #aBcdEfgHIj
        sets['0100100101'] = len((B & E & H & J) - A - C - D - F - G - I) #aBcdEfgHiJ
        sets['0100100011'] = len((B & E & I & J) - A - C - D - F - G - H) #aBcdEfghIJ
        sets['0100011100'] = len((B & F & G & H) - A - C - D - E - I - J) #aBcdeFGHij
        sets['0100011010'] = len((B & F & G & I) - A - C - D - E - H - J) #aBcdeFGhIj
        sets['0100011001'] = len((B & F & G & J) - A - C - D - E - H - I) #aBcdeFGhiJ
        sets['0100010110'] = len((B & F & H & I) - A - C - D - E - G - J) #aBcdeFgHIj
        sets['0100010101'] = len((B & F & H & J) - A - C - D - E - G - I) #aBcdeFgHiJ
        # {b,f,i,j} {b,g,h,i} {b,g,h,j} {b,g,i,j} {b,h,i,j} {c,d,e,f} {c,d,e,g} {c,d,e,h} {c,d,e,i} {c,d,e,j} {c,d,f,g} {c,d,f,h} {c,d,f,i} {c,d,f,j} {c,d,g,h}
        sets['0100010011'] = len((B & F & I & J) - A - C - D - E - G - H) #aBcdeFghIJ
        sets['0100001110'] = len((B & G & H & I) - A - C - D - E - F - J) #aBcdefGHIj
        sets['0100001101'] = len((B & G & H & J) - A - C - D - E - F - I) #aBcdefGHiJ
        sets['0100001011'] = len((B & G & I & J) - A - C - D - E - F - H) #aBcdefGhIJ
        sets['0100000111'] = len((B & H & I & J) - A - C - D - E - F - G) #aBcdefgHIJ
        sets['0011110000'] = len((C & D & E & F) - A - B - G - H - I - J) #abCDEFghij
        sets['0011101000'] = len((C & D & E & G) - A - B - F - H - I - J) #abCDEfGhij
        sets['0011100100'] = len((C & D & E & H) - A - B - F - G - I - J) #abCDEfgHij
        sets['0011100010'] = len((C & D & E & I) - A - B - F - G - H - J) #abCDEfghIj
        sets['0011100001'] = len((C & D & E & J) - A - B - F - G - H - I) #abCDEfghiJ
        sets['0011011000'] = len((C & D & F & G) - A - B - E - H - I - J) #abCDeFGhij
        sets['0011010100'] = len((C & D & F & H) - A - B - E - G - I - J) #abCDeFgHij
        sets['0011010010'] = len((C & D & F & I) - A - B - E - G - H - J) #abCDeFghIj
        sets['0011010001'] = len((C & D & F & J) - A - B - E - G - H - I) #abCDeFghiJ
        sets['0011001100'] = len((C & D & G & H) - A - B - E - F - I - J) #abCDefGHij
        # {c,d,g,i} {c,d,g,j} {c,d,h,i} {c,d,h,j} {c,d,i,j} {c,e,f,g} {c,e,f,h} {c,e,f,i} {c,e,f,j} {c,e,g,h} {c,e,g,i} {c,e,g,j} {c,e,h,i} {c,e,h,j} {c,e,i,j}
        sets['0011001010'] = len((C & D & G & I) - A - B - E - F - H - J) #abCDefGhIj
        sets['0011001001'] = len((C & D & G & J) - A - B - E - F - H - I) #abCDefGhiJ
        sets['0011000110'] = len((C & D & H & I) - A - B - E - F - G - J) #abCDefgHIj
        sets['0011000101'] = len((C & D & H & J) - A - B - E - F - G - I) #abCDefgHiJ
        sets['0011000011'] = len((C & D & I & J) - A - B - E - F - G - H) #abCDefghIJ
        sets['0010111000'] = len((C & E & F & G) - A - B - D - H - I - J) #abCdEFGhij
        sets['0010110100'] = len((C & E & F & H) - A - B - D - G - I - J) #abCdEFgHij
        sets['0010110010'] = len((C & E & F & I) - A - B - D - G - H - J) #abCdEFghIj
        sets['0010110001'] = len((C & E & F & J) - A - B - D - G - H - I) #abCdEFghiJ
        sets['0010101100'] = len((C & E & G & H) - A - B - D - F - I - J) #abCdEfGHij
        sets['0010101010'] = len((C & E & G & I) - A - B - D - F - H - J) #abCdEfGhIj
        sets['0010101001'] = len((C & E & G & J) - A - B - D - F - H - I) #abCdEfGhiJ
        sets['0010100110'] = len((C & E & H & I) - A - B - D - F - G - J) #abCdEfgHIj
        sets['0010100101'] = len((C & E & H & J) - A - B - D - F - G - I) #abCdEfgHiJ
        sets['0010100011'] = len((C & E & I & J) - A - B - D - F - G - H) #abCdEfghIJ
        # {c,f,g,h} {c,f,g,i} {c,f,g,j} {c,f,h,i} {c,f,h,j} {c,f,i,j} {c,g,h,i} {c,g,h,j} {c,g,i,j} {c,h,i,j} {d,e,f,g} {d,e,f,h} {d,e,f,i} {d,e,f,j} {d,e,g,h}
        sets['0010011100'] = len((C & F & G & H) - A - B - D - E - I - J) #abCdeFGHij
        sets['0010011010'] = len((C & F & G & I) - A - B - D - E - H - J) #abCdeFGhIj
        sets['0010011001'] = len((C & F & G & J) - A - B - D - E - H - I) #abCdeFGhiJ
        sets['0010010110'] = len((C & F & H & I) - A - B - D - E - G - J) #abCdeFgHIj
        sets['0010010101'] = len((C & F & H & J) - A - B - D - E - G - I) #abCdeFgHiJ
        sets['0010010011'] = len((C & F & I & J) - A - B - D - E - G - H) #abCdeFghIJ
        sets['0010001110'] = len((C & G & H & I) - A - B - D - E - F - J) #abCdefGHIj
        sets['0010001101'] = len((C & G & H & J) - A - B - D - E - F - I) #abCdefGHiJ
        sets['0010001011'] = len((C & G & I & J) - A - B - D - E - F - H) #abCdefGhIJ
        sets['0010000111'] = len((C & H & I & J) - A - B - D - E - F - G) #abCdefgHIJ
        sets['0001111000'] = len((D & E & F & G) - A - B - C - H - I - J) #abcDEFGhij
        sets['0001110100'] = len((D & E & F & H) - A - B - C - G - I - J) #abcDEFgHij
        sets['0001110010'] = len((D & E & F & I) - A - B - C - G - H - J) #abcDEFghIj
        sets['0001110001'] = len((D & E & F & J) - A - B - C - G - H - I) #abcDEFghiJ
        sets['0001101100'] = len((D & E & G & H) - A - B - C - F - I - J) #abcDEfGHij
        # {d,e,g,i} {d,e,g,j} {d,e,h,i} {d,e,h,j} {d,e,i,j} {d,f,g,h} {d,f,g,i} {d,f,g,j} {d,f,h,i} {d,f,h,j} {d,f,i,j} {d,g,h,i} {d,g,h,j} {d,g,i,j} {d,h,i,j}
        sets['0001101010'] = len((D & E & G & I) - A - B - C - F - H - J) #abcDEfGhIj
        sets['0001101001'] = len((D & E & G & J) - A - B - C - F - H - I) #abcDEfGhiJ
        sets['0001100110'] = len((D & E & H & I) - A - B - C - F - G - J) #abcDEfgHIj
        sets['0001100101'] = len((D & E & H & J) - A - B - C - F - G - I) #abcDEfgHiJ
        sets['0001100011'] = len((D & E & I & J) - A - B - C - F - G - H) #abcDEfghIJ
        sets['0001011100'] = len((D & F & G & H) - A - B - C - E - I - J) #abcDeFGHij
        sets['0001011010'] = len((D & F & G & I) - A - B - C - E - H - J) #abcDeFGhIj
        sets['0001011001'] = len((D & F & G & J) - A - B - C - E - H - I) #abcDeFGhiJ
        sets['0001010110'] = len((D & F & H & I) - A - B - C - E - G - J) #abcDeFgHIj
        sets['0001010101'] = len((D & F & H & J) - A - B - C - E - G - I) #abcDeFgHiJ
        sets['0001010011'] = len((D & F & I & J) - A - B - C - E - G - H) #abcDeFghIJ
        sets['0001001110'] = len((D & G & H & I) - A - B - C - E - F - J) #abcDefGHIj
        sets['0001001101'] = len((D & G & H & J) - A - B - C - E - F - I) #abcDefGHiJ
        sets['0001001011'] = len((D & G & I & J) - A - B - C - E - F - H) #abcDefGhIJ
        sets['0001000111'] = len((D & H & I & J) - A - B - C - E - F - G) #abcDefgHIJ
        # {e,f,g,h} {e,f,g,i} {e,f,g,j} {e,f,h,i} {e,f,h,j} {e,f,i,j} {e,g,h,i} {e,g,h,j} {e,g,i,j} {e,h,i,j} {f,g,h,i} {f,g,h,j} {f,g,i,j} {f,h,i,j} {g,h,i,j}
        sets['0000111100'] = len((E & F & G & H) - A - B - C - D - I - J) #abcdEFGHij
        sets['0000111010'] = len((E & F & G & I) - A - B - C - D - H - J) #abcdEFGhIj
        sets['0000111001'] = len((E & F & G & J) - A - B - C - D - H - I) #abcdEFGhiJ
        sets['0000110110'] = len((E & F & H & I) - A - B - C - D - G - J) #abcdEFgHIj
        sets['0000110101'] = len((E & F & H & J) - A - B - C - D - G - I) #abcdEFgHiJ
        sets['0000110011'] = len((E & F & I & J) - A - B - C - D - G - H) #abcdEFghIJ
        sets['0000101110'] = len((E & G & H & I) - A - B - C - D - F - J) #abcdEfGHIj
        sets['0000101101'] = len((E & G & H & J) - A - B - C - D - F - I) #abcdEfGHiJ
        sets['0000101011'] = len((E & G & I & J) - A - B - C - D - F - H) #abcdEfGhIJ
        sets['0000100111'] = len((E & H & I & J) - A - B - C - D - F - G) #abcdEfgHIJ
        sets['0000011110'] = len((F & G & H & I) - A - B - C - D - E - J) #abcdeFGHIj
        sets['0000011101'] = len((F & G & H & J) - A - B - C - D - E - I) #abcdeFGHiJ
        sets['0000011011'] = len((F & G & I & J) - A - B - C - D - E - H) #abcdeFGhIJ
        sets['0000010111'] = len((F & H & I & J) - A - B - C - D - E - G) #abcdeFgHIJ
        sets['0000001111'] = len((G & H & I & J) - A - B - C - D - E - F) #abcdefGHIJ
        # {a,b,c,d,e} {a,b,c,d,f} {a,b,c,d,g} {a,b,c,d,h} {a,b,c,d,i} {a,b,c,d,j}
        sets['1111100000'] = len((A & B & C & D & E) - F - G - H - I - J) #ABCDEfghij
        sets['1111010000'] = len((A & B & C & D & F) - E - G - H - I - J) #ABCDeFghij
        sets['1111001000'] = len((A & B & C & D & G) - E - F - H - I - J) #ABCDefGhij
        sets['1111000100'] = len((A & B & C & D & H) - E - F - G - I - J) #ABCDefgHij
        sets['1111000010'] = len((A & B & C & D & I) - E - F - G - H - J) #ABCDefghIj
        sets['1111000001'] = len((A & B & C & D & J) - E - F - G - H - I) #ABCDefghiJ
        # {a,b,c,e,f} {a,b,c,e,g} {a,b,c,e,h} {a,b,c,e,i} {a,b,c,e,j} {a,b,c,f,g} {a,b,c,f,h}
        sets['1110110000'] = len((A & B & C & E & F) - D - G - H - I - J) #ABCdEFghij
        sets['1110101000'] = len((A & B & C & E & G) - D - F - H - I - J) #ABCdEfGhij
        sets['1110100100'] = len((A & B & C & E & H) - D - F - G - I - J) #ABCdEfgHij
        sets['1110100010'] = len((A & B & C & E & I) - D - F - G - H - J) #ABCdEfghIj
        sets['1110100001'] = len((A & B & C & E & J) - D - F - G - H - I) #ABCdEfghiJ
        sets['1110011000'] = len((A & B & C & F & G) - D - E - H - I - J) #ABCdeFGhij
        sets['1110010100'] = len((A & B & C & F & H) - D - E - G - I - J) #ABCdeFgHij
        # {a,b,c,f,i} {a,b,c,f,j} {a,b,c,g,h} {a,b,c,g,i} {a,b,c,g,j} {a,b,c,h,i} {a,b,c,h,j}
        sets['1110010010'] = len((A & B & C & F & I) - D - E - G - H - J) #ABCdeFghIj
        sets['1110010001'] = len((A & B & C & F & J) - D - E - G - H - I) #ABCdeFghiJ
        sets['1110001100'] = len((A & B & C & G & H) - D - E - F - I - J) #ABCdefGHij
        sets['1110001010'] = len((A & B & C & G & I) - D - E - F - H - J) #ABCdefGhIj
        sets['1110001001'] = len((A & B & C & G & J) - D - E - F - H - I) #ABCdefGhiJ
        sets['1110000110'] = len((A & B & C & H & I) - D - E - F - G - J) #ABCdefgHIj
        sets['1110000101'] = len((A & B & C & H & J) - D - E - F - G - I) #ABCdefgHiJ
        # {a,b,c,i,j} {a,b,d,e,f} {a,b,d,e,g} {a,b,d,e,h} {a,b,d,e,i} {a,b,d,e,j}
        sets['1110000011'] = len((A & B & C & I & J) - D - E - F - G - H) #ABCdefghIJ
        sets['1101110000'] = len((A & B & D & E & F) - C - G - H - I - J) #ABcDEFghij
        sets['1101101000'] = len((A & B & D & E & G) - C - F - H - I - J) #ABcDEfGhij
        sets['1101100100'] = len((A & B & D & E & H) - C - F - G - I - J) #ABcDEfgHij
        sets['1101100010'] = len((A & B & D & E & I) - C - F - G - H - J) #ABcDEfghIj
        sets['1101100001'] = len((A & B & D & E & J) - C - F - G - H - I) #ABcDEfghiJ
        # {a,b,d,f,g} {a,b,d,f,h} {a,b,d,f,i} {a,b,d,f,j} {a,b,d,g,h} {a,b,d,g,i}
        sets['1101011000'] = len((A & B & D & F & G) - C - E - H - I - J) #ABcDeFGhij
        sets['1101010100'] = len((A & B & D & F & H) - C - E - G - I - J) #ABcDeFgHij
        sets['1101010010'] = len((A & B & D & F & I) - C - E - G - H - J) #ABcDeFghIj
        sets['1101010001'] = len((A & B & D & F & J) - C - E - G - H - I) #ABcDeFghiJ
        sets['1101001100'] = len((A & B & D & G & H) - C - E - F - I - J) #ABcDefGHij
        sets['1101001010'] = len((A & B & D & G & I) - C - E - F - H - J) #ABcDefGhIj
        # {a,b,d,g,j} {a,b,d,h,i} {a,b,d,h,j} {a,b,d,i,j} {a,b,e,f,g} {a,b,e,f,h} {a,b,e,f,i}
        sets['1101001001'] = len((A & B & D & G & J) - C - E - F - H - I) #ABcDefGhiJ
        sets['1101000110'] = len((A & B & D & H & I) - C - E - F - G - J) #ABcDefgHIj
        sets['1101000101'] = len((A & B & D & H & J) - C - E - F - G - I) #ABcDefgHiJ
        sets['1101000011'] = len((A & B & D & I & J) - C - E - F - G - H) #ABcDefghIJ
        sets['1100111000'] = len((A & B & E & F & G) - C - D - H - I - J) #ABcdEFGhij
        sets['1100110100'] = len((A & B & E & F & H) - C - D - G - I - J) #ABcdEFgHij
        sets['1100110010'] = len((A & B & E & F & I) - C - D - G - H - J) #ABcdEFghIj
        # {a,b,e,f,j} {a,b,e,g,h} {a,b,e,g,i} {a,b,e,g,j} {a,b,e,h,i} {a,b,e,h,j} {a,b,e,i,j}
        sets['1100110001'] = len((A & B & E & F & J) - C - D - G - H - I) #ABcdEFghiJ
        sets['1100101100'] = len((A & B & E & G & H) - C - D - F - I - J) #ABcdEfGHij
        sets['1100101010'] = len((A & B & E & G & I) - C - D - F - H - J) #ABcdEfGhIj
        sets['1100101001'] = len((A & B & E & G & J) - C - D - F - H - I) #ABcdEfGhiJ
        sets['1100100110'] = len((A & B & E & H & I) - C - D - F - G - J) #ABcdEfgHIj
        sets['1100100101'] = len((A & B & E & H & J) - C - D - F - G - I) #ABcdEfgHiJ
        sets['1100100011'] = len((A & B & E & I & J) - C - D - F - G - H) #ABcdEfghIJ
        # {a,b,f,g,h} {a,b,f,g,i} {a,b,f,g,j} {a,b,f,h,i} {a,b,f,h,j} {a,b,f,i,j}
        sets['1100011100'] = len((A & B & F & G & H) - C - D - E - I - J) #ABcdeFGHij
        sets['1100011010'] = len((A & B & F & G & I) - C - D - E - H - J) #ABcdeFGhIj
        sets['1100011001'] = len((A & B & F & G & J) - C - D - E - H - I) #ABcdeFGhiJ
        sets['1100010110'] = len((A & B & F & H & I) - C - D - E - G - J) #ABcdeFgHIj
        sets['1100010101'] = len((A & B & F & H & J) - C - D - E - G - I) #ABcdeFgHiJ
        sets['1100010011'] = len((A & B & F & I & J) - C - D - E - G - H) #ABcdeFghIJ
        # {a,b,g,h,i} {a,b,g,h,j} {a,b,g,i,j} {a,b,h,i,j} {a,c,d,e,f} {a,c,d,e,g}
        sets['1100001110'] = len((A & B & G & H & I) - C - D - E - F - J) #ABcdefGHIj
        sets['1100001101'] = len((A & B & G & H & J) - C - D - E - F - I) #ABcdefGHiJ
        sets['1100001011'] = len((A & B & G & I & J) - C - D - E - F - H) #ABcdefGhIJ
        sets['1100000111'] = len((A & B & H & I & J) - C - D - E - F - G) #ABcdefgHIJ
        sets['1011110000'] = len((A & C & D & E & F) - B - G - H - I - J) #AbCDEFghij
        sets['1011101000'] = len((A & C & D & E & G) - B - F - H - I - J) #AbCDEfGhij
        # {a,c,d,e,h} {a,c,d,e,i} {a,c,d,e,j} {a,c,d,f,g} {a,c,d,f,h} {a,c,d,f,i} {a,c,d,f,j}
        sets['1011100100'] = len((A & C & D & E & H) - B - F - G - I - J) #AbCDEfgHij
        sets['1011100010'] = len((A & C & D & E & I) - B - F - G - H - J) #AbCDEfghIj
        sets['1011100001'] = len((A & C & D & E & J) - B - F - G - H - I) #AbCDEfghiJ
        sets['1011011000'] = len((A & C & D & F & G) - B - E - H - I - J) #AbCDeFGhij
        sets['1011010100'] = len((A & C & D & F & H) - B - E - G - I - J) #AbCDeFgHij
        sets['1011010010'] = len((A & C & D & F & I) - B - E - G - H - J) #AbCDeFghIj
        sets['1011010001'] = len((A & C & D & F & J) - B - E - G - H - I) #AbCDeFghiJ
        # {a,c,d,g,h} {a,c,d,g,i} {a,c,d,g,j} {a,c,d,h,i} {a,c,d,h,j} {a,c,d,i,j} {a,c,e,f,g}
        sets['1011001100'] = len((A & C & D & G & H) - B - E - F - I - J) #AbCDefGHij
        sets['1011001010'] = len((A & C & D & G & I) - B - E - F - H - J) #AbCDefGhIj
        sets['1011001001'] = len((A & C & D & G & J) - B - E - F - H - I) #AbCDefGhiJ
        sets['1011000110'] = len((A & C & D & H & I) - B - E - F - G - J) #AbCDefgHIj
        sets['1011000101'] = len((A & C & D & H & J) - B - E - F - G - I) #AbCDefgHiJ
        sets['1011000011'] = len((A & C & D & I & J) - B - E - F - G - H) #AbCDefghIJ
        sets['1010111000'] = len((A & C & E & F & G) - B - D - H - I - J) #AbCdEFGhij
        # {a,c,e,f,h} {a,c,e,f,i} {a,c,e,f,j} {a,c,e,g,h} {a,c,e,g,i} {a,c,e,g,j}
        sets['1010110100'] = len((A & C & E & F & H) - B - D - G - I - J) #AbCdEFgHij
        sets['1010110010'] = len((A & C & E & F & I) - B - D - G - H - J) #AbCdEFghIj
        sets['1010110001'] = len((A & C & E & F & J) - B - D - G - H - I) #AbCdEFghiJ
        sets['1010101100'] = len((A & C & E & G & H) - B - D - F - I - J) #AbCdEfGHij
        sets['1010101010'] = len((A & C & E & G & I) - B - D - F - H - J) #AbCdEfGhIj
        sets['1010101001'] = len((A & C & E & G & J) - B - D - F - H - I) #AbCdEfGhiJ
        # {a,c,e,h,i} {a,c,e,h,j} {a,c,e,i,j} {a,c,f,g,h} {a,c,f,g,i} {a,c,f,g,j}
        sets['1010100110'] = len((A & C & E & H & I) - B - D - F - G - J) #AbCdEfgHIj
        sets['1010100101'] = len((A & C & E & H & J) - B - D - F - G - I) #AbCdEfgHiJ
        sets['1010100011'] = len((A & C & E & I & J) - B - D - F - G - H) #AbCdEfghIJ
        sets['1010011100'] = len((A & C & F & G & H) - B - D - E - I - J) #AbCdeFGHij
        sets['1010011010'] = len((A & C & F & G & I) - B - D - E - H - J) #AbCdeFGhIj
        sets['1010011001'] = len((A & C & F & G & J) - B - D - E - H - I) #AbCdeFGhiJ
        # {a,c,f,h,i} {a,c,f,h,j} {a,c,f,i,j} {a,c,g,h,i} {a,c,g,h,j} {a,c,g,i,j} {a,c,h,i,j}
        sets['1010010110'] = len((A & C & F & H & I) - B - D - E - G - J) #AbCdeFgHIj
        sets['1010010101'] = len((A & C & F & H & J) - B - D - E - G - I) #AbCdeFgHiJ
        sets['1010010011'] = len((A & C & F & I & J) - B - D - E - G - H) #AbCdeFghIJ
        sets['1010001110'] = len((A & C & G & H & I) - B - D - E - F - J) #AbCdefGHIj
        sets['1010001101'] = len((A & C & G & H & J) - B - D - E - F - I) #AbCdefGHiJ
        sets['1010001011'] = len((A & C & G & I & J) - B - D - E - F - H) #AbCdefGhIJ
        sets['1010000111'] = len((A & C & H & I & J) - B - D - E - F - G) #AbCdefgHIJ
        # {a,d,e,f,g} {a,d,e,f,h} {a,d,e,f,i} {a,d,e,f,j} {a,d,e,g,h} {a,d,e,g,i} {a,d,e,g,j}
        sets['1001111000'] = len((A & D & E & F & G) - B - C - H - I - J) #AbcDEFGhij
        sets['1001110100'] = len((A & D & E & F & H) - B - C - G - I - J) #AbcDEFgHij
        sets['1001110010'] = len((A & D & E & F & I) - B - C - G - H - J) #AbcDEFghIj
        sets['1001110001'] = len((A & D & E & F & J) - B - C - G - H - I) #AbcDEFghiJ
        sets['1001101100'] = len((A & D & E & G & H) - B - C - F - I - J) #AbcDEfGHij
        sets['1001101010'] = len((A & D & E & G & I) - B - C - F - H - J) #AbcDEfGhIj
        sets['1001101001'] = len((A & D & E & G & J) - B - C - F - H - I) #AbcDEfGhiJ
        # {a,d,e,h,i} {a,d,e,h,j} {a,d,e,i,j} {a,d,f,g,h} {a,d,f,g,i} {a,d,f,g,j}
        sets['1001100110'] = len((A & D & E & H & I) - B - C - F - G - J) #AbcDEfgHIj
        sets['1001100101'] = len((A & D & E & H & J) - B - C - F - G - I) #AbcDEfgHiJ
        sets['1001100011'] = len((A & D & E & I & J) - B - C - F - G - H) #AbcDEfghIJ
        sets['1001011100'] = len((A & D & F & G & H) - B - C - E - I - J) #AbcDeFGHij
        sets['1001011010'] = len((A & D & F & G & I) - B - C - E - H - J) #AbcDeFGhIj
        sets['1001011001'] = len((A & D & F & G & J) - B - C - E - H - I) #AbcDeFGhiJ
        # {a,d,f,h,i} {a,d,f,h,j} {a,d,f,i,j} {a,d,g,h,i} {a,d,g,h,j} {a,d,g,i,j}
        sets['1001010110'] = len((A & D & F & H & I) - B - C - E - G - J) #AbcDeFgHIj
        sets['1001010101'] = len((A & D & F & H & J) - B - C - E - G - I) #AbcDeFgHiJ
        sets['1001010011'] = len((A & D & F & I & J) - B - C - E - G - H) #AbcDeFghIJ
        sets['1001001110'] = len((A & D & G & H & I) - B - C - E - F - J) #AbcDefGHIj
        sets['1001001101'] = len((A & D & G & H & J) - B - C - E - F - I) #AbcDefGHiJ
        sets['1001001011'] = len((A & D & G & I & J) - B - C - E - F - H) #AbcDefGhIJ
        # {a,d,h,i,j} {a,e,f,g,h} {a,e,f,g,i} {a,e,f,g,j} {a,e,f,h,i} {a,e,f,h,j} {a,e,f,i,j}
        sets['1001000111'] = len((A & D & H & I & J) - B - C - E - F - G) #AbcDefgHIJ
        sets['1000111100'] = len((A & E & F & G & H) - B - C - D - I - J) #AbcdEFGHij
        sets['1000111010'] = len((A & E & F & G & I) - B - C - D - H - J) #AbcdEFGhIj
        sets['1000111001'] = len((A & E & F & G & J) - B - C - D - H - I) #AbcdEFGhiJ
        sets['1000110110'] = len((A & E & F & H & I) - B - C - D - G - J) #AbcdEFgHIj
        sets['1000110101'] = len((A & E & F & H & J) - B - C - D - G - I) #AbcdEFgHiJ
        sets['1000110011'] = len((A & E & F & I & J) - B - C - D - G - H) #AbcdEFghIJ
        # {a,e,g,h,i} {a,e,g,h,j} {a,e,g,i,j} {a,e,h,i,j} {a,f,g,h,i} {a,f,g,h,j} {a,f,g,i,j}
        sets['1000101110'] = len((A & E & G & H & I) - B - C - D - F - J) #AbcdEfGHIj
        sets['1000101101'] = len((A & E & G & H & J) - B - C - D - F - I) #AbcdEfGHiJ
        sets['1000101011'] = len((A & E & G & I & J) - B - C - D - F - H) #AbcdEfGhIJ
        sets['1000100111'] = len((A & E & H & I & J) - B - C - D - F - G) #AbcdEfgHIJ
        sets['1000011110'] = len((A & F & G & H & I) - B - C - D - E - J) #AbcdeFGHIj
        sets['1000011101'] = len((A & F & G & H & J) - B - C - D - E - I) #AbcdeFGHiJ
        sets['1000011011'] = len((A & F & G & I & J) - B - C - D - E - H) #AbcdeFGhIJ
        # {a,f,h,i,j} {a,g,h,i,j} {b,c,d,e,f} {b,c,d,e,g} {b,c,d,e,h} {b,c,d,e,i}
        sets['1000010111'] = len((A & F & H & I & J) - B - C - D - E - G) #AbcdeFgHIJ
        sets['1000001111'] = len((A & G & H & I & J) - B - C - D - E - F) #AbcdefGHIJ
        sets['0111110000'] = len((B & C & D & E & F) - A - G - H - I - J) #aBCDEFghij
        sets['0111101000'] = len((B & C & D & E & G) - A - F - H - I - J) #aBCDEfGhij
        sets['0111100100'] = len((B & C & D & E & H) - A - F - G - I - J) #aBCDEfgHij
        sets['0111100010'] = len((B & C & D & E & I) - A - F - G - H - J) #aBCDEfghIj
        # {b,c,d,e,j} {b,c,d,f,g} {b,c,d,f,h} {b,c,d,f,i} {b,c,d,f,j} {b,c,d,g,h}
        sets['0111100001'] = len((B & C & D & E & J) - A - F - G - H - I) #aBCDEfghiJ
        sets['0111011000'] = len((B & C & D & F & G) - A - E - H - I - J) #aBCDeFGhij
        sets['0111011100'] = len((B & C & D & F & H) - A - E - G - I - J) #aBCDeFgHij
        sets['0111011010'] = len((B & C & D & F & I) - A - E - G - H - J) #aBCDeFghIj
        sets['0111011001'] = len((B & C & D & F & J) - A - E - G - H - I) #aBCDeFghiJ
        sets['0111001100'] = len((B & C & D & G & H) - A - E - F - I - J) #aBCDefGHij
        # {b,c,d,g,i} {b,c,d,g,j} {b,c,d,h,i} {b,c,d,h,j} {b,c,d,i,j} {b,c,e,f,g} {b,c,e,f,h}
        sets['0111001010'] = len((B & C & D & G & I) - A - E - F - H - J) #aBCDefGhIj
        sets['0111001001'] = len((B & C & D & G & J) - A - E - F - H - I) #aBCDefGhiJ
        sets['0111000110'] = len((B & C & D & H & I) - A - E - F - G - J) #aBCDefgHIj
        sets['0111000101'] = len((B & C & D & H & J) - A - E - F - G - I) #aBCDefgHiJ
        sets['0111000011'] = len((B & C & D & I & J) - A - E - F - G - H) #aBCDefghIJ
        sets['0110111000'] = len((B & C & E & F & G) - A - D - H - I - J) #aBCdEFGhij
        sets['0110110100'] = len((B & C & E & F & H) - A - D - G - I - J) #aBCdEFgHij
        # {b,c,e,f,i} {b,c,e,f,j} {b,c,e,g,h} {b,c,e,g,i} {b,c,e,g,j} {b,c,e,h,i} {b,c,e,h,j}
        sets['0110110010'] = len((B & C & E & F & I) - A - D - G - H - J) #aBCdEFghIj
        sets['0110110001'] = len((B & C & E & F & J) - A - D - G - H - I) #aBCdEFghiJ
        sets['0110101100'] = len((B & C & E & G & H) - A - D - F - I - J) #aBCdEfGHij
        sets['0110101010'] = len((B & C & E & G & I) - A - D - F - H - J) #aBCdEfGhIj
        sets['0110101001'] = len((B & C & E & G & J) - A - D - F - H - I) #aBCdEfGhiJ
        sets['0110100110'] = len((B & C & E & H & I) - A - D - F - G - J) #aBCdEfgHIj
        sets['0110100101'] = len((B & C & E & H & J) - A - D - F - G - I) #aBCdEfgHiJ
        # {b,c,e,i,j} {b,c,f,g,h} {b,c,f,g,i} {b,c,f,g,j} {b,c,f,h,i} {b,c,f,h,j}
        sets['0110100011'] = len((B & C & E & I & J) - A - D - F - G - H) #aBCdEfghIJ
        sets['0110011100'] = len((B & C & F & G & H) - A - D - E - I - J) #aBCdeFGHij
        sets['0110011010'] = len((B & C & F & G & I) - A - D - E - H - J) #aBCdeFGhIj
        sets['0110011001'] = len((B & C & F & G & J) - A - D - E - H - I) #aBCdeFGhiJ
        sets['0110010110'] = len((B & C & F & H & I) - A - D - E - G - J) #aBCdeFgHIj
        sets['0110010101'] = len((B & C & F & H & J) - A - D - E - G - I) #aBCdeFgHiJ
        # {b,c,f,i,j} {b,c,g,h,i} {b,c,g,h,j} {b,c,g,i,j} {b,c,h,i,j} {b,d,e,f,g}
        sets['0110010011'] = len((B & C & F & I & J) - A - D - E - G - H) #aBCdeFghIJ
        sets['0110001110'] = len((B & C & G & H & I) - A - D - E - F - J) #aBCdefGHIj
        sets['0110001101'] = len((B & C & G & H & J) - A - D - E - F - I) #aBCdefGHiJ
        sets['0110001011'] = len((B & C & G & I & J) - A - D - E - F - H) #aBCdefGhIJ
        sets['0110000111'] = len((B & C & H & I & J) - A - D - E - F - G) #aBCdefgHIJ
        sets['0101111000'] = len((B & D & E & F & G) - A - C - H - I - J) #aBcDEFGhij
        # {b,d,e,f,h} {b,d,e,f,i} {b,d,e,f,j} {b,d,e,g,h} {b,d,e,g,i} {b,d,e,g,j} {b,d,e,h,i}
        sets['0101110100'] = len((B & D & E & F & H) - A - C - G - I - J) #aBcDEFgHij
        sets['0101110010'] = len((B & D & E & F & I) - A - C - G - H - J) #aBcDEFghIj
        sets['0101110001'] = len((B & D & E & F & J) - A - C - G - H - I) #aBcDEFghiJ
        sets['0101101100'] = len((B & D & E & G & H) - A - C - F - I - J) #aBcDEfGHij
        sets['0101101010'] = len((B & D & E & G & I) - A - C - F - H - J) #aBcDEfGhIj
        sets['0101101001'] = len((B & D & E & G & J) - A - C - F - H - I) #aBcDEfGhiJ
        sets['0101100110'] = len((B & D & E & H & I) - A - C - F - G - J) #aBcDEfgHIj
        # {b,d,e,h,j} {b,d,e,i,j} {b,d,f,g,h} {b,d,f,g,i} {b,d,f,g,j} {b,d,f,h,i} {b,d,f,h,j}
        sets['0101100101'] = len((B & D & E & H & J) - A - C - F - G - I) #aBcDEfgHiJ
        sets['0101100011'] = len((B & D & E & I & J) - A - C - F - G - H) #aBcDEfghIJ
        sets['0101011100'] = len((B & D & F & G & H) - A - C - E - I - J) #aBcDeFGHij
        sets['0101011010'] = len((B & D & F & G & I) - A - C - E - H - J) #aBcDeFGhIj
        sets['0101011001'] = len((B & D & F & G & J) - A - C - E - H - I) #aBcDeFGhiJ
        sets['0101010110'] = len((B & D & F & H & I) - A - C - E - G - J) #aBcDeFgHIj
        sets['0101010101'] = len((B & D & F & H & J) - A - C - E - G - I) #aBcDeFgHiJ
        # {b,d,f,i,j} {b,d,g,h,i} {b,d,g,h,j} {b,d,g,i,j} {b,d,h,i,j} {b,e,f,g,h}
        sets['0101010011'] = len((B & D & F & I & J) - A - C - E - G - H) #aBcDeFghIJ
        sets['0101001110'] = len((B & D & G & H & I) - A - C - E - F - J) #aBcDefGHIj
        sets['0101001101'] = len((B & D & G & H & J) - A - C - E - F - I) #aBcDefGHiJ
        sets['0101001011'] = len((B & D & G & I & J) - A - C - E - F - H) #aBcDefGhIJ
        sets['0101000111'] = len((B & D & H & I & J) - A - C - E - F - G) #aBcDefgHIJ
        sets['0100111100'] = len((B & E & F & G & H) - A - C - D - I - J) #aBcdEFGHij
        # {b,e,f,g,i} {b,e,f,g,j} {b,e,f,h,i} {b,e,f,h,j} {b,e,f,i,j} {b,e,g,h,i}
        sets['0100111010'] = len((B & E & F & G & I) - A - C - D - H - J) #aBcdEFGhIj
        sets['0100111001'] = len((B & E & F & G & J) - A - C - D - H - I) #aBcdEFGhiJ
        sets['0100110110'] = len((B & E & F & H & I) - A - C - D - G - J) #aBcdEFgHIj
        sets['0100110101'] = len((B & E & F & H & J) - A - C - D - G - I) #aBcdEFgHiJ
        sets['0100110011'] = len((B & E & F & I & J) - A - C - D - G - H) #aBcdEFghIJ
        sets['0100101110'] = len((B & E & G & H & I) - A - C - D - F - J) #aBcdEfGHIj
        # {b,e,g,h,j} {b,e,g,i,j} {b,e,h,i,j} {b,f,g,h,i} {b,f,g,h,j} {b,f,g,i,j} {b,f,h,i,j}
        sets['0100101101'] = len((B & E & G & H & J) - A - C - D - F - I) #aBcdEfGHiJ
        sets['0100101011'] = len((B & E & G & I & J) - A - C - D - F - H) #aBcdEfGhIJ
        sets['0100100111'] = len((B & E & H & I & J) - A - C - D - F - G) #aBcdEfgHIJ
        sets['0100011110'] = len((B & F & G & H & I) - A - C - D - E - J) #aBcdeFGHIj
        sets['0100011101'] = len((B & F & G & H & J) - A - C - D - E - I) #aBcdeFGHiJ
        sets['0100011011'] = len((B & F & G & I & J) - A - C - D - E - H) #aBcdeFGhIJ
        sets['0100010111'] = len((B & F & H & I & J) - A - C - D - E - G) #aBcdeFgHIJ
        # {b,g,h,i,j} {c,d,e,f,g} {c,d,e,f,h} {c,d,e,f,i} {c,d,e,f,j} {c,d,e,g,h} {c,d,e,g,i}
        sets['0100001111'] = len((B & G & H & I & J) - A - C - D - E - F) #aBcdefGHIJ
        sets['0011111000'] = len((C & D & E & F & G) - A - B - H - I - J) #abCDEFGhij
        sets['0011110100'] = len((C & D & E & F & H) - A - B - G - I - J) #abCDEFgHij
        sets['0011110010'] = len((C & D & E & F & I) - A - B - G - H - J) #abCDEFghIj
        sets['0011110001'] = len((C & D & E & F & J) - A - B - G - H - I) #abCDEFghiJ
        sets['0011101100'] = len((C & D & E & G & H) - A - B - F - I - J) #abCDEfGHij
        sets['0011101010'] = len((C & D & E & G & I) - A - B - F - H - J) #abCDEfGhIj
        # {c,d,e,g,j} {c,d,e,h,i} {c,d,e,h,j} {c,d,e,i,j} {c,d,f,g,h} {c,d,f,g,i}
        sets['0011101001'] = len((C & D & E & G & J) - A - B - F - H - I) #abCDEfGhiJ
        sets['0011100110'] = len((C & D & E & H & I) - A - B - F - G - J) #abCDEfgHIj
        sets['0011100101'] = len((C & D & E & H & J) - A - B - F - G - I) #abCDEfgHiJ
        sets['0011100011'] = len((C & D & E & I & J) - A - B - F - G - H) #abCDEfghIJ
        sets['0011011100'] = len((C & D & F & G & H) - A - B - E - I - J) #abCDeFGHij
        sets['0011011010'] = len((C & D & F & G & I) - A - B - E - H - J) #abCDeFGhIj
        # {c,d,f,g,j} {c,d,f,h,i} {c,d,f,h,j} {c,d,f,i,j} {c,d,g,h,i} {c,d,g,h,j}
        sets['0011011001'] = len((C & D & F & G & J) - A - B - E - H - I) #abCDeFGhiJ
        sets['0011010110'] = len((C & D & F & H & I) - A - B - E - G - J) #abCDeFgHIj
        sets['0011010101'] = len((C & D & F & H & J) - A - B - E - G - I) #abCDeFgHiJ
        sets['0011010011'] = len((C & D & F & I & J) - A - B - E - G - H) #abCDeFghIJ
        sets['0011001110'] = len((C & D & G & H & I) - A - B - E - F - J) #abCDefGHIj
        sets['0011001101'] = len((C & D & G & H & J) - A - B - E - F - I) #abCDefGHiJ
        # {c,d,g,i,j} {c,d,h,i,j} {c,e,f,g,h} {c,e,f,g,i} {c,e,f,g,j} {c,e,f,h,i} {c,e,f,h,j}
        sets['0011001011'] = len((C & D & G & I & J) - A - B - E - F - H) #abCDefGhIJ
        sets['0011000111'] = len((C & D & H & I & J) - A - B - E - F - G) #abCDefgHIJ
        sets['0010111100'] = len((C & E & F & G & H) - A - B - D - I - J) #abCdEFGHij
        sets['0010111010'] = len((C & E & F & G & I) - A - B - D - H - J) #abCdEFGhIj
        sets['0010111001'] = len((C & E & F & G & J) - A - B - D - H - I) #abCdEFGhiJ
        sets['0010110110'] = len((C & E & F & H & I) - A - B - D - G - J) #abCdEFgHIj
        sets['0010110101'] = len((C & E & F & H & J) - A - B - D - G - I) #abCdEFgHiJ
        # {c,e,f,i,j} {c,e,g,h,i} {c,e,g,h,j} {c,e,g,i,j} {c,e,h,i,j} {c,f,g,h,i} {c,f,g,h,j}
        sets['0010110011'] = len((C & E & F & I & J) - A - B - D - G - H) #abCdEFghIJ
        sets['0010101110'] = len((C & E & G & H & I) - A - B - D - F - J) #abCdEfGHIj
        sets['0010101101'] = len((C & E & G & H & J) - A - B - D - F - I) #abCdEfGHiJ
        sets['0010101011'] = len((C & E & G & I & J) - A - B - D - F - H) #abCdEfGhIJ
        sets['0010100111'] = len((C & E & H & I & J) - A - B - D - F - G) #abCdEfgHIJ
        sets['0010011110'] = len((C & F & G & H & I) - A - B - D - E - J) #abCdeFGHIj
        sets['0010011101'] = len((C & F & G & H & J) - A - B - D - E - I) #abCdeFGHiJ
        # {c,f,g,i,j} {c,f,h,i,j} {c,g,h,i,j} {d,e,f,g,h} {d,e,f,g,i} {d,e,f,g,j}
        sets['0010011011'] = len((C & F & G & I & J) - A - B - D - E - H) #abCdeFGhIJ
        sets['0010010111'] = len((C & F & H & I & J) - A - B - D - E - G) #abCdeFgHIJ
        sets['0010001111'] = len((C & G & H & I & J) - A - B - D - E - F) #abCdefGHIJ
        sets['0001111100'] = len((D & E & F & G & H) - A - B - C - I - J) #abcDEFGHij
        sets['0001111010'] = len((D & E & F & G & I) - A - B - C - H - J) #abcDEFGhIj
        sets['0001111001'] = len((D & E & F & G & J) - A - B - C - H - I) #abcDEFGhiJ
        # {d,e,f,h,i} {d,e,f,h,j} {d,e,f,i,j} {d,e,g,h,i} {d,e,g,h,j} {d,e,g,i,j}
        sets['0001110110'] = len((D & E & F & H & I) - A - B - C - G - J) #abcDEFgHIj
        sets['0001110101'] = len((D & E & F & H & J) - A - B - C - G - I) #abcDEFgHiJ
        sets['0001110011'] = len((D & E & F & I & J) - A - B - C - G - H) #abcDEFghIJ
        sets['0001101110'] = len((D & E & G & H & I) - A - B - C - F - J) #abcDEfGHIj
        sets['0001101101'] = len((D & E & G & H & J) - A - B - C - F - I) #abcDEfGHiJ
        sets['0001101011'] = len((D & E & G & I & J) - A - B - C - F - H) #abcDEfGhIJ
        # {d,e,h,i,j} {d,f,g,h,i} {d,f,g,h,j} {d,f,g,i,j} {d,f,h,i,j} {d,g,h,i,j} {e,f,g,h,i}
        sets['0001100111'] = len((D & E & H & I & J) - A - B - C - F - G) #abcDEfgHIJ
        sets['0001011110'] = len((D & F & G & H & I) - A - B - C - E - J) #abcDeFGHIj
        sets['0001011101'] = len((D & F & G & H & J) - A - B - C - E - I) #abcDeFGHiJ
        sets['0001011011'] = len((D & F & G & I & J) - A - B - C - E - H) #abcDeFGhIJ
        sets['0001010111'] = len((D & F & H & I & J) - A - B - C - E - G) #abcDeFgHIJ
        sets['0001001111'] = len((D & G & H & I & J) - A - B - C - E - F) #abcDefGHIJ
        sets['0000111110'] = len((E & F & G & H & I) - A - B - C - D - J) #abcdEFGHIj
        # {e,f,g,h,j} {e,f,g,i,j} {e,f,h,i,j} {e,g,h,i,j} {f,g,h,i,j}
        sets['0000111101'] = len((E & F & G & H & J) - A - B - C - D - I) #abcdEFGHiJ
        sets['0000111011'] = len((E & F & G & I & J) - A - B - C - D - H) #abcdEFGhIJ
        sets['0000110111'] = len((E & F & H & I & J) - A - B - C - D - G) #abcdEFgHIJ
        sets['0000101111'] = len((E & G & H & I & J) - A - B - C - D - F) #abcdEfGHIJ
        sets['0000011111'] = len((F & G & H & I & J) - A - B - C - D - E) #abcdeFGHIJ
        # {a,b,c,d,e,f} {a,b,c,d,e,g} {a,b,c,d,e,h} {a,b,c,d,e,i} {a,b,c,d,e,j} {a,b,c,d,f,g} {a,b,c,d,f,h} {a,b,c,d,f,i} {a,b,c,d,f,j} {a,b,c,d,g,h} {a,b,c,d,g,i}
        sets['1111110000'] = len((A & B & C & D & E & F) - G - H - I - J) #ABCDEFghij
        sets['1111101000'] = len((A & B & C & D & E & G) - F - H - I - J) #ABCDEfGhij
        sets['1111100100'] = len((A & B & C & D & E & H) - F - G - I - J) #ABCDEfgHij
        sets['1111100010'] = len((A & B & C & D & E & I) - F - G - H - J) #ABCDEfghIj
        sets['1111100001'] = len((A & B & C & D & E & J) - F - G - H - I) #ABCDEfghiJ
        sets['1111011000'] = len((A & B & C & D & F & G) - E - H - I - J) #ABCDeFGhij
        sets['1111010100'] = len((A & B & C & D & F & H) - E - G - I - J) #ABCDeFgHij
        sets['1111010010'] = len((A & B & C & D & F & I) - E - G - H - J) #ABCDeFghIj
        sets['1111010001'] = len((A & B & C & D & F & J) - E - G - H - I) #ABCDeFghiJ
        sets['1111001100'] = len((A & B & C & D & G & H) - E - F - I - J) #ABCDefGHij
        sets['1111001010'] = len((A & B & C & D & G & I) - E - F - H - J) #ABCDefGhIj
        # {a,b,c,d,g,j} {a,b,c,d,h,i} {a,b,c,d,h,j} {a,b,c,d,i,j} {a,b,c,e,f,g} {a,b,c,e,f,h} {a,b,c,e,f,i} {a,b,c,e,f,j} {a,b,c,e,g,h} {a,b,c,e,g,i} {a,b,c,e,g,j}
        sets['1111001001'] = len((A & B & C & D & G & J) - E - F - H - I) #ABCDefGhiJ
        sets['1111000110'] = len((A & B & C & D & H & I) - E - F - G - J) #ABCDefgHIj
        sets['1111000101'] = len((A & B & C & D & H & J) - E - F - G - I) #ABCDefgHiJ
        sets['1111000011'] = len((A & B & C & D & I & J) - E - F - G - H) #ABCDefghIJ
        sets['1110111000'] = len((A & B & C & E & F & G) - D - H - I - J) #ABCdEFGhij
        sets['1110110100'] = len((A & B & C & E & F & H) - D - G - I - J) #ABCdEFgHij
        sets['1110110010'] = len((A & B & C & E & F & I) - D - G - H - J) #ABCdEFghIj
        sets['1110110001'] = len((A & B & C & E & F & J) - D - G - H - I) #ABCdEFghiJ
        sets['1110101100'] = len((A & B & C & E & G & H) - D - F - I - J) #ABCdEfGHij
        sets['1110101010'] = len((A & B & C & E & G & I) - D - F - H - J) #ABCdEfGhIj
        sets['1110101001'] = len((A & B & C & E & G & J) - D - F - H - I) #ABCdEfGhiJ
        # {a,b,c,e,h,i} {a,b,c,e,h,j} {a,b,c,e,i,j} {a,b,c,f,g,h} {a,b,c,f,g,i} {a,b,c,f,g,j} {a,b,c,f,h,i} {a,b,c,f,h,j} {a,b,c,f,i,j} {a,b,c,g,h,i} {a,b,c,g,h,j}
        sets['1110100110'] = len((A & B & C & E & H & I) - D - F - G - J) #ABCdEfgHIj
        sets['1110100101'] = len((A & B & C & E & H & J) - D - F - G - I) #ABCdEfgHiJ
        sets['1110100011'] = len((A & B & C & E & I & J) - D - F - G - H) #ABCdEfghIJ
        sets['1110011100'] = len((A & B & C & F & G & H) - D - E - I - J) #ABCdeFGHij
        sets['1110011010'] = len((A & B & C & F & G & J) - D - E - H - J) #ABCdeFGhIj
        sets['1110011001'] = len((A & B & C & F & G & J) - D - E - H - I) #ABCdeFGhiJ
        sets['1110010110'] = len((A & B & C & F & H & I) - D - E - G - J) #ABCdeFgHIj
        sets['1110010101'] = len((A & B & C & F & H & J) - D - E - G - I) #ABCdeFgHiJ
        sets['1110010011'] = len((A & B & C & F & I & J) - D - E - G - H) #ABCdeFghIJ
        sets['1110001110'] = len((A & B & C & G & H & I) - D - E - F - J) #ABCdefGHIj
        sets['1110001101'] = len((A & B & C & G & H & J) - D - E - F - I) #ABCdefGHiJ
        # {a,b,c,g,i,j} {a,b,c,h,i,j} {a,b,d,e,f,g} {a,b,d,e,f,h} {a,b,d,e,f,i} {a,b,d,e,f,j} {a,b,d,e,g,h} {a,b,d,e,g,i} {a,b,d,e,g,j} {a,b,d,e,h,i} {a,b,d,e,h,j}
        sets['1110001011'] = len((A & B & C & G & I & J) - D - E - F - H) #ABCdefGhIJ
        sets['1110000111'] = len((A & B & C & H & I & J) - D - E - F - G) #ABCdefgHIJ
        sets['1101111000'] = len((A & B & D & E & F & G) - C - H - I - J) #ABcDEFGhij
        sets['1101110100'] = len((A & B & D & E & F & H) - C - G - I - J) #ABcDEFgHij
        sets['1101110010'] = len((A & B & D & E & F & I) - C - G - H - J) #ABcDEFghIj
        sets['1101110001'] = len((A & B & D & E & F & J) - C - G - H - I) #ABcDEFghiJ
        sets['1101101100'] = len((A & B & D & E & G & H) - C - F - I - J) #ABcDEfGHij
        sets['1101101010'] = len((A & B & D & E & G & I) - C - F - H - J) #ABcDEfGhIj
        sets['1101101001'] = len((A & B & D & E & G & J) - C - F - H - I) #ABcDEfGhiJ
        sets['1101100110'] = len((A & B & D & E & H & I) - C - F - G - J) #ABcDEfgHIj
        sets['1101100101'] = len((A & B & D & E & H & J) - C - F - G - I) #ABcDEfgHiJ
        # {a,b,d,e,i,j} {a,b,d,f,g,h} {a,b,d,f,g,i} {a,b,d,f,g,j} {a,b,d,f,h,i} {a,b,d,f,h,j} {a,b,d,f,i,j} {a,b,d,g,h,i} {a,b,d,g,h,j} {a,b,d,g,i,j} {a,b,d,h,i,j}
        sets['1101100011'] = len((A & B & D & E & I & J) - C - F - G - H) #ABcDEfghIJ
        sets['1101011100'] = len((A & B & D & F & G & H) - C - E - I - J) #ABcDeFGHij
        sets['1101011010'] = len((A & B & D & F & G & I) - C - E - H - J) #ABcDeFGhIj
        sets['1101011001'] = len((A & B & D & F & G & J) - C - E - H - I) #ABcDeFGhiJ 
        sets['1101010110'] = len((A & B & D & F & H & I) - C - E - G - J) #ABcDeFgHIj
        sets['1101010101'] = len((A & B & D & F & H & J) - C - E - G - I) #ABcDeFgHiJ 
        sets['1101010011'] = len((A & B & D & F & I & J) - C - E - G - H) #ABcDeFghIJ
        sets['1101001110'] = len((A & B & D & G & H & I) - C - E - F - J) #ABcDefGHIj
        sets['1101001101'] = len((A & B & D & G & H & J) - C - E - F - I) #ABcDefGHiJ
        sets['1101001011'] = len((A & B & D & G & I & J) - C - E - F - H) #ABcDefGhIJ
        sets['1101000111'] = len((A & B & D & H & I & J) - C - E - F - G) #ABcDefgHIJ
        # {a,b,e,f,g,h} {a,b,e,f,g,i} {a,b,e,f,g,j} {a,b,e,f,h,i} {a,b,e,f,h,j} {a,b,e,f,i,j} {a,b,e,g,h,i} {a,b,e,g,h,j} {a,b,e,g,i,j} {a,b,e,h,i,j} {a,b,f,g,h,i}
        sets['1100111100'] = len((A & B & E & F & G & H) - C - D - I - J) #ABcdEFGHij
        sets['1100111010'] = len((A & B & E & F & G & I) - C - D - H - J) #ABcdEFGhIj
        sets['1100111001'] = len((A & B & E & F & G & J) - C - D - H - I) #ABcdEFGhiJ
        sets['1100110110'] = len((A & B & E & F & H & I) - C - D - G - J) #ABcdEFgHIj
        sets['1100110101'] = len((A & B & E & F & H & J) - C - D - G - I) #ABcdEFgHiJ
        sets['1100110011'] = len((A & B & E & F & I & J) - C - D - G - H) #ABcdEFghIJ
        sets['1100101110'] = len((A & B & E & G & I & J) - C - D - F - H) #ABcdEfGHIj
        sets['1100101101'] = len((A & B & E & G & H & J) - C - D - F - I) #ABcdEfGHiJ
        sets['1100101011'] = len((A & B & E & G & I & J) - C - D - F - H) #ABcdEfGhIJ
        sets['1100100111'] = len((A & B & E & H & I & J) - C - D - F - G) #ABcdEfgHIJ
        sets['1100011110'] = len((A & B & F & G & H & I) - C - D - E - J) #ABcdeFGHIj
        # {a,b,f,g,h,j} {a,b,f,g,i,j} {a,b,f,h,i,j} {a,b,g,h,i,j} {a,c,d,e,f,g} {a,c,d,e,f,h} {a,c,d,e,f,i} {a,c,d,e,f,j} {a,c,d,e,g,h} {a,c,d,e,g,i} {a,c,d,e,g,j}
        sets['1100011101'] = len((A & B & F & G & H & J) - C - D - E - I) #ABcdeFGHiJ
        sets['1100011011'] = len((A & B & F & G & I & J) - C - D - E - H) #ABcdeFGhIJ
        sets['1100010111'] = len((A & B & F & H & I & J) - C - D - E - G) #ABcdeFgHIJ
        sets['1100001111'] = len((A & B & G & H & I & J) - C - D - E - F) #ABcdefGHIJ
        sets['1011111000'] = len((A & C & D & E & F & G) - B - H - I - J) #AbCDEFGhij
        sets['1011110100'] = len((A & C & D & E & F & H) - B - G - I - J) #AbCDEFgHij
        sets['1011110010'] = len((A & C & D & E & F & I) - B - G - H - J) #AbCDEFghIj
        sets['1011110001'] = len((A & C & D & E & F & J) - B - G - H - I) #AbCDEFghiJ
        sets['1011101100'] = len((A & C & D & E & G & H) - B - F - I - J) #AbCDEfGHij
        sets['1011101010'] = len((A & C & D & E & G & I) - B - F - H - J) #AbCDEfGhIj
        sets['1011101001'] = len((A & C & D & E & G & J) - B - F - H - I) #AbCDEfGhiJ
        # {a,c,d,e,h,i} {a,c,d,e,h,j} {a,c,d,e,i,j} {a,c,d,f,g,h} {a,c,d,f,g,i} {a,c,d,f,g,j} {a,c,d,f,h,i} {a,c,d,f,h,j} {a,c,d,f,i,j} {a,c,d,g,h,i} {a,c,d,g,h,j}
        sets['1011100110'] = len((A & C & D & E & H & I) - B - F - G - J) #AbCDEfgHIj
        sets['1011100101'] = len((A & C & D & E & H & J) - B - F - G - I) #AbCDEfgHiJ
        sets['1011100011'] = len((A & C & D & E & I & J) - B - F - G - H) #AbCDEfghIJ
        sets['1011011100'] = len((A & C & D & F & G & H) - B - E - I - J) #AbCDeFGHij
        sets['1011011010'] = len((A & C & D & F & G & I) - B - E - H - J) #AbCDeFGhIj
        sets['1011011001'] = len((A & C & D & F & G & J) - B - E - H - I) #AbCDeFGhiJ
        sets['1011010110'] = len((A & C & D & F & H & I) - B - E - G - J) #AbCDeFgHIj
        sets['1011010101'] = len((A & C & D & F & H & J) - B - E - G - I) #AbCDeFgHiJ
        sets['1011010011'] = len((A & C & D & F & I & J) - B - E - G - H) #AbCDeFghIJ
        sets['1011001110'] = len((A & C & D & G & H & I) - B - E - F - J) #AbCDefGHIj
        sets['1011001101'] = len((A & C & D & G & H & J) - B - E - F - I) #AbCDefGHiJ
        # {a,c,d,g,i,j} {a,c,d,h,i,J} {a,c,e,f,g,h} {a,c,e,f,g,i} {a,c,e,f,g,j} {a,c,e,f,h,i} {a,c,e,f,h,j} {a,c,e,f,i,j} {a,c,e,g,h,i} {a,c,e,g,h,j} {a,c,e,g,i,j}
        sets['1011001011'] = len((A & C & D & G & I & J) - B - E - F - H) #AbCDefGhIJ
        sets['1011000111'] = len((A & C & D & H & I & J) - B - E - F - G) #AbCDefgHIJ
        sets['1010111100'] = len((A & C & E & F & G & H) - B - D - I - J) #AbCdEFGHij
        sets['1010111010'] = len((A & C & E & F & G & I) - B - D - H - J) #AbCdEFGhIj
        sets['1010111001'] = len((A & C & E & F & G & J) - B - D - H - I) #AbCdEFGhiJ
        sets['1010110110'] = len((A & C & E & F & H & I) - B - D - G - J) #AbCdEFgHIj
        sets['1010110101'] = len((A & C & E & F & H & J) - B - D - G - I) #AbCdEFgHiJ
        sets['1010110011'] = len((A & C & E & F & I & J) - B - D - G - H) #AbCdEFghIJ
        sets['1010101110'] = len((A & C & E & G & H & I) - B - D - F - J) #AbCdEfGHIj
        sets['1010101101'] = len((A & C & E & G & H & J) - B - D - F - I) #AbCdEfGHiJ
        sets['1010101011'] = len((A & C & E & G & I & J) - B - D - F - H) #AbCdEfGhIJ
        # {a,c e,h,i,j} {a,c,f,g,h,I} {a,c,f,g,h,j} {a,c,f,g,i,j} {a,c,f,h,i,j} {a,c,g,h,i,j} {a,d,e,f,g,h} {a,d,e,f,g,i} {a,d,e,f,g,j} {a,d,e,f,h,i} {a,d,e,f,h,j}
        sets['1010100111'] = len((A & C & E & H & I & J) - B - D - F - G) #AbCdEfgHIJ
        sets['1010011110'] = len((A & C & F & G & H & I) - B - D - E - J) #AbCdeFGHIj
        sets['1010011101'] = len((A & C & F & G & H & J) - B - D - E - I) #AbCdeFGHiJ
        sets['1010011011'] = len((A & C & F & G & I & J) - B - D - E - H) #AbCdeFGhIJ
        sets['1010010111'] = len((A & C & F & H & I & J) - B - D - E - G) #AbCdeFgHIJ
        sets['1010001111'] = len((A & C & G & H & I & J) - B - D - E - F) #AbCdefGHIJ
        sets['1001111100'] = len((A & D & E & F & G & H) - B - C - I - J) #AbcDEFGHij
        sets['1001111010'] = len((A & D & E & F & G & I) - B - C - H - J) #AbcDEFGhIj
        sets['1001111001'] = len((A & D & E & F & G & J) - B - C - H - I) #AbcDEFGhiJ
        sets['1001110110'] = len((A & D & E & F & H & I) - B - C - G - J) #AbcDEFgHIj
        sets['1001110101'] = len((A & D & E & F & H & J) - B - C - G - I) #AbcDEFgHiJ
        # {a,d,e,f,i,j} {a,d,e,g,h,i} {a,d,e,g,h,j} {a,d,e,g,i,j} {a,d,e,h,i,j} {a,d,f,g,h,i} {a,d,f,g,h,j} {a,d,f,g,i,j} {a,d,f,h,i,j} {a,d,g,h,i,j} {a,e,f,g,h,i}
        sets['1001110011'] = len((A & D & E & F & I & J) - B - C - G - H) #AbcDEFghIJ
        sets['1001101110'] = len((A & D & E & G & H & I) - B - C - F - J) #AbcDEfGHIj
        sets['1001101101'] = len((A & D & E & G & H & J) - B - C - F - I) #AbcDEfGHiJ
        sets['1001101011'] = len((A & D & E & G & I & J) - B - C - F - H) #AbcDEfGhIJ
        sets['1001100111'] = len((A & D & E & H & I & J) - B - C - F - G) #AbcDEfgHIJ
        sets['1001011110'] = len((A & D & F & G & H & I) - B - C - E - J) #AbcDeFGHIj
        sets['1001011101'] = len((A & D & F & G & H & J) - B - C - E - I) #AbcDeFGHiJ
        sets['1001011011'] = len((A & D & F & G & I & J) - B - C - E - H) #AbcDeFGhIJ
        sets['1001010111'] = len((A & D & F & H & I & J) - B - C - E - G) #AbcDeFgHIJ
        sets['1001001111'] = len((A & D & G & H & I & J) - B - C - E - F) #AbcDefGHIJ
        sets['1000111110'] = len((A & E & F & G & H & I) - B - C - D - J) #AbcdEFGHIj
        # {a,e,f,g,h,j} {a,e,f,g,i,j} {a,e,f,h,i,j} {a,e,g,h,i,j} {a,f,g,h,i,j} {b,c,d,e,f,g} {b,c,d,e,f,h} {b,c,d,e,f,i} {b,c,d,e,f,j} {b,c,d,e,g,h} {b,c,d,e,g,i}
        sets['1000111101'] = len((A & E & F & G & H & J) - B - C - D - I) #AbcdEFGHiJ
        sets['1000111011'] = len((A & E & F & G & I & J) - B - C - D - H) #AbcdEFGhIJ
        sets['1000110111'] = len((A & E & F & H & I & J) - B - C - D - G) #AbcdEFgHIJ
        sets['1000101111'] = len((A & E & G & H & I & J) - B - C - D - F) #AbcdEfGHIJ
        sets['1000011111'] = len((A & F & G & H & I & J) - B - C - D - E) #AbcdeFGHIJ
        sets['0111111000'] = len((B & C & D & E & F & G) - A - H - I - J) #aBCDEFGhij
        sets['0111110100'] = len((B & C & D & E & F & H) - A - G - I - J) #aBCDEFgHij
        sets['0111110010'] = len((B & C & D & E & F & I) - A - G - H - J) #aBCDEFghIj
        sets['0111110001'] = len((B & C & D & E & F & J) - A - G - H - I) #aBCDEFghiJ
        sets['0111101100'] = len((B & C & D & E & G & H) - A - F - I - J) #aBCDEfGHij
        sets['0111101010'] = len((B & C & D & E & G & I) - A - F - H - J) #aBCDEfGhIj
        # {b,c,d,e,g,j} {b,c,d,e,h,i} {b,c,d,e,h,j} {b,c,d,e,i,j} {b,c,d,f,g,h} {b,c,d,f,g,i} {b,c,d,f,g,j} {b,c,d,f,h,i} {b,c,d,f,h,j} {b,c,d,f,i,j} {b,c,d,g,h,i}
        sets['0111101001'] = len((B & C & D & E & G & J) - A - F - H - I) #aBCDEfGhiJ
        sets['0111100110'] = len((B & C & D & E & H & I) - A - F - G - J) #aBCDEfgHIj
        sets['0111100101'] = len((B & C & D & E & H & J) - A - F - G - I) #aBCDEfgHiJ
        sets['0111100011'] = len((B & C & D & E & I & J) - A - F - G - H) #aBCDEfghIJ
        sets['0111011100'] = len((B & C & D & F & G & H) - A - E - I - J) #aBCDeFGHij
        sets['0111011010'] = len((B & C & D & F & G & I) - A - E - H - J) #aBCDeFGhIj
        sets['0111011001'] = len((B & C & D & F & G & J) - A - E - H - I) #aBCDeFGhiJ
        sets['0111010110'] = len((B & C & D & F & H & I) - A - E - G - J) #aBCDeFgHIj
        sets['0111010101'] = len((B & C & D & F & H & J) - A - E - G - I) #aBCDeFgHiJ
        sets['0111010011'] = len((B & C & D & F & I & J) - A - E - G - H) #aBCDeFghIJ
        sets['0111001110'] = len((B & C & D & G & H & I) - A - E - F - J) #aBCDefGHIj
        # {b,c,d,g,h,j} {b,c,d,g,i,j} {b,c,d,h,i,j} {b,c,e,f,g,h} {b,c,e,f,g,i} {b,c,e,f,g,j} {b,c,e,f,h,i} {b,c,e,f,h,j} {b,c,e,f,i,j} {b,c,e,g,h,i} {b,c,e,g,h,j}
        sets['0111001101'] = len((B & C & D & G & H & J) - A - E - F - I) #aBCDefGHiJ
        sets['0111001011'] = len((B & C & D & G & I & J) - A - E - F - H) #aBCDefGhIJ
        sets['0111000111'] = len((B & C & D & H & I & J) - A - E - F - G) #aBCDefgHIJ
        sets['0110111100'] = len((B & C & E & F & G & H) - A - D - I - J) #aBCdEFGHij
        sets['0110111010'] = len((B & C & E & F & G & I) - A - D - H - J) #aBCdEFGhIj
        sets['0110111001'] = len((B & C & E & F & G & J) - A - D - H - I) #aBCdEFGhiJ
        sets['0110110110'] = len((B & C & E & F & H & I) - A - D - G - J) #aBCdEFgHIj
        sets['0110110101'] = len((B & C & E & F & H & J) - A - D - G - I) #aBCdEFgHiJ
        sets['0110110011'] = len((B & C & E & F & I & J) - A - D - G - H) #aBCdEFghIJ
        sets['0110101110'] = len((B & C & E & G & H & I) - A - D - F - J) #aBCdEfGHIj
        sets['0110101101'] = len((B & C & E & G & H & J) - A - D - F - I) #aBCdEfGHiJ
        # {b,c,e,g,i,j} {b,c,e,h,i,j} {b,c,f,g,h,i} {b,c,f,g,h,j} {b,c,f,g,i,j} {b,c,f,h,i,j} {b,c,g,h,i,j} {b,d,e,f,g,h} {b,d,e,f,g,i} {b,d,e,f,g,j} {b,d,e,f,h,i}
        sets['0110101011'] = len((B & C & E & G & I & J) - A - D - F - H) #aBCdEfGhIJ
        sets['0110100111'] = len((B & C & E & H & I & J) - A - D - F - G) #aBCdEfgHIJ
        sets['0110011110'] = len((B & C & F & G & H & I) - A - D - E - J) #aBCdeFGHIj
        sets['0110011101'] = len((B & C & F & G & H & J) - A - D - E - I) #aBCdeFGHiJ
        sets['0110011011'] = len((B & C & F & G & I & J) - A - D - E - H) #aBCdeFGhIJ
        sets['0110010111'] = len((B & C & F & H & I & J) - A - D - E - G) #aBCdeFgHIJ
        sets['0110001111'] = len((B & C & G & H & I & J) - A - D - E - F) #aBCdefGHIJ
        sets['0101111100'] = len((B & D & E & F & G & H) - A - C - I - J) #aBcDEFGHij
        sets['0101111010'] = len((B & D & E & F & G & I) - A - C - H - J) #aBcDEFGhIj
        sets['0101111001'] = len((B & D & E & F & G & J) - A - C - H - I) #aBcDEFGhiJ
        sets['0101110110'] = len((B & D & E & F & H & I) - A - C - G - J) #aBcDEFgHIj
        # {b,d,e,f,h,j} {b,d,e,f,i,j} {b,d,e,g,h,i} {b,d,e,g,h,j} {b,d,e,g,i,j} {b,d,e,h,i,j} {b,d,f,g,h,i} {b,d,f,g,h,j} {b,d,f,g,i,j} {b,d,f,h,i,j} {b,d,g,h,i,j}
        sets['0101110101'] = len((B & D & E & F & H & J) - A - C - G - I) #aBcDEFgHiJ
        sets['0101110011'] = len((B & D & E & F & I & J) - A - C - G - H) #aBcDEFghIJ
        sets['0101101110'] = len((B & D & E & G & H & I) - A - C - F - J) #aBcDEfGHIj
        sets['0101101101'] = len((B & D & E & G & H & J) - A - C - F - I) #aBcDEfGHiJ
        sets['0101101011'] = len((B & D & E & G & I & J) - A - C - F - H) #aBcDEfGhIJ
        sets['0101100111'] = len((B & D & E & H & I & J) - A - C - F - G) #aBcDEfgHIJ
        sets['0101011110'] = len((B & D & F & G & H & I) - A - C - E - J) #aBcDeFGHIj
        sets['0101011101'] = len((B & D & F & G & H & J) - A - C - E - I) #aBcDeFGHiJ
        sets['0101011011'] = len((B & D & F & G & I & J) - A - C - E - H) #aBcDeFGhIJ
        sets['0101010111'] = len((B & D & F & H & I & J) - A - C - E - G) #aBcDeFgHIJ
        sets['0101001111'] = len((B & D & G & H & I & J) - A - C - E - F) #aBcDefGHIJ
        # {b,e,f,g,h,i} {b,e,f,g,h,j} {b,e,f,g,i,j} {b,e,f,h,i,j} {b,e,g,h,i,j} {b,f,g,h,i,j} {c,d,e,f,g,h} {c,d,e,f,g,i} {c,d,e,f,g,j} {c,d,e,f,h,i} {c,d,e,f,h,j}
        sets['0100111110'] = len((B & E & F & G & H & I) - A - C - D - J) #aBcdEFGHIj
        sets['0100111101'] = len((B & E & F & G & H & J) - A - C - D - I) #aBcdEFGHiJ
        sets['0100111011'] = len((B & E & F & G & I & J) - A - C - D - H) #aBcdEFGhIJ
        sets['0100110111'] = len((B & E & F & H & I & J) - A - C - D - G) #aBcdEFgHIJ
        sets['0100101111'] = len((B & E & G & H & I & J) - A - C - D - F) #aBcdEfGHIJ
        sets['0100011111'] = len((B & F & G & H & I & J) - A - C - D - E) #aBcdeFGHIJ
        sets['0011111100'] = len((C & D & E & F & G & H) - A - B - I - J) #abCDEFGHij
        sets['0011111010'] = len((C & D & E & F & G & I) - A - B - H - J) #abCDEFGhIj
        sets['0011111001'] = len((C & D & E & F & G & J) - A - B - H - I) #abCDEFGhiJ
        sets['0011110110'] = len((C & D & E & F & H & I) - A - B - G - J) #abCDEFgHIj
        sets['0011110101'] = len((C & D & E & F & H & J) - A - B - G - I) #abCDEFgHiJ
        # {c,d,e,f,i,j} {c,d,e,g,h,i} {c,d,e,g,h,j} {c,d,e,g,i,j} {c,d,e,h,i,j} {c,d,f,g,h,i} {c,d,f,g,h,j} {c,d,f,g,i,j} {c,d,f,h,i,j} {c,d,g,h,i,j} {c,e,f,g,h,i}
        sets['0011110011'] = len((C & D & E & F & I & J) - A - B - G - H) #abCDEFghIJ
        sets['0011101110'] = len((C & D & E & G & H & I) - A - B - F - J) #abCDEfGHIj
        sets['0011101101'] = len((C & D & E & G & H & J) - A - B - F - I) #abCDEfGHiJ
        sets['0011101011'] = len((C & D & E & G & I & J) - A - B - F - H) #abCDEfGhIJ
        sets['0011100111'] = len((C & D & E & H & I & J) - A - B - F - G) #abCDEfgHIJ
        sets['0011011110'] = len((C & D & F & G & H & I) - A - B - E - J) #abCDeFGHIj
        sets['0011011101'] = len((C & D & F & G & H & J) - A - B - E - I) #abCDeFGHiJ
        sets['0011011011'] = len((C & D & F & G & I & J) - A - B - E - H) #abCDeFGhIJ
        sets['0011010111'] = len((C & D & F & H & I & J) - A - B - E - G) #abCDeFgHIJ
        sets['0011001111'] = len((C & D & G & H & I & J) - A - B - E - F) #abCDefGHIJ
        sets['0010111110'] = len((C & E & F & G & H & I) - A - B - D - J) #abCdEFGHIj
        # {c,e,f,g,h,j} {c,e,f,g,i,j} {c,e,f,h,i,j} {c,e,g,h,i,j} {c,f,g,h,i,j} {d,e,f,g,h,i} {d,e,f,g,h,j} {d,e,f,g,i,j} {d,e,f,h,i,j} {d,e,g,h,i,j} {d,f,g,h,i,j}
        sets['0010111101'] = len((C & E & F & G & H & J) - A - B - D - I) #abCdEFGHiJ
        sets['0010111011'] = len((C & E & F & G & I & J) - A - B - D - H) #abCdEFGhIJ
        sets['0010110111'] = len((C & E & F & H & I & J) - A - B - D - G) #abCdEFgHIJ
        sets['0010101111'] = len((C & E & G & H & I & J) - A - B - D - F) #abCdEfGHIJ
        sets['0010011111'] = len((C & F & G & H & I & J) - A - B - D - E) #abCdeFGHIJ
        sets['0001111110'] = len((D & E & F & G & H & I) - A - B - C - J) #abcDEFGHIj
        sets['0001111101'] = len((D & E & F & G & H & J) - A - B - C - I) #abcDEFGHiJ
        sets['0001111011'] = len((D & E & F & G & I & J) - A - B - C - H) #abcDEFGhIJ
        sets['0001110111'] = len((D & E & F & H & I & J) - A - B - C - G) #abcDEFgHIJ
        sets['0001101111'] = len((D & E & G & H & I & J) - A - B - C - F) #abcDEfGHIJ
        sets['0001011111'] = len((D & F & G & H & I & J) - A - B - C - E) #abcDeFGHIJ
        # {e,f,g,h,i,j}
        sets['0000111111'] = len((E & F & G & H & I & J) - A - B - C - D) #abcdEFGHIJ
        # {a,b,c,d,e,f,g} {a,b,c,d,e,f,h} {a,b,c,d,e,f,i} {a,b,c,d,e,f,j} {a,b,c,d,e,g,h} {a,b,c,d,e,g,i} {a,b,c,d,e,g,j} {a,b,c,d,e,h,i} {a,b,c,d,e,h,j}
        sets['1111111000'] = len((A & B & C & D & E & F & G) - H - I - J) #ABCDEFGhij
        sets['1111110100'] = len((A & B & C & D & E & F & H) - G - I - J) #ABCDEFgHij
        sets['1111110010'] = len((A & B & C & D & E & F & I) - G - H - J) #ABCDEFghIj
        sets['1111110001'] = len((A & B & C & D & E & F & J) - G - H - I) #ABCDEFghiJ
        sets['1111101100'] = len((A & B & C & D & E & G & H) - F - I - J) #ABCDEfGHij
        sets['1111101010'] = len((A & B & C & D & E & G & I) - F - H - J) #ABCDEfGhIj
        sets['1111101001'] = len((A & B & C & D & E & G & J) - F - H - I) #ABCDEfGhiJ
        sets['1111100110'] = len((A & B & C & D & E & H & I) - F - G - J) #ABCDEfgHIj
        sets['1111100101'] = len((A & B & C & D & E & H & J) - F - G - I) #ABCDEfgHiJ
        # {a,b,c,d,e,i,j} {a,b,c,d,f,g,h} {a,b,c,d,f,g,i} {a,b,c,d,f,g,j} {a,b,c,d,f,h,i} {a,b,c,d,f,h,j} {a,b,c,d,f,i,j} {a,b,c,d,g,h,i} {a,b,c,d,g,h,j}
        sets['1111100011'] = len((A & B & C & D & E & I & J) - F - G - H) #ABCDEfghIJ
        sets['1111011100'] = len((A & B & C & D & F & G & H) - E - I - J) #ABCDeFGHij
        sets['1111011010'] = len((A & B & C & D & F & G & I) - E - H - J) #ABCDeFGhIj
        sets['1111011001'] = len((A & B & C & D & F & G & J) - E - H - I) #ABCDeFGhiJ
        sets['1111010110'] = len((A & B & C & D & F & H & I) - E - G - J) #ABCDeFgHIj
        sets['1111010101'] = len((A & B & C & D & F & H & J) - E - G - I) #ABCDeFgHiJ
        sets['1111010011'] = len((A & B & C & D & F & I & J) - E - G - H) #ABCDeFghIJ
        sets['1111001110'] = len((A & B & C & D & G & H & I) - E - F - J) #ABCDefGHIj
        sets['1111001101'] = len((A & B & C & D & G & H & J) - E - F - I) #ABCDefGHiJ
        # {a,b,c,d,g,i,j} {a,b,c,d,h,i,j} {a,b,c,e,f,g,h} {a,b,c,e,f,g,i} {a,b,c,e,f,g,j} {a,b,c,e,f,h,i} {a,b,c,e,f,h,j} {a,b,c,e,f,i,j} {a,b,c,e,g,h,i}
        sets['1111001011'] = len((A & B & C & D & G & I & J) - E - F - H) #ABCDefGhIJ
        sets['1111000111'] = len((A & B & C & D & H & I & J) - E - F - G) #ABCDefgHIJ
        sets['1110111100'] = len((A & B & C & E & F & G & H) - D - I - J) #ABCdEFGHij
        sets['1110111010'] = len((A & B & C & E & F & G & I) - D - H - J) #ABCdEFGhIj
        sets['1110111001'] = len((A & B & C & E & F & G & J) - D - H - I) #ABCdEFGhiJ
        sets['1110110110'] = len((A & B & C & E & F & H & I) - D - G - J) #ABCdEFgHIj
        sets['1110110101'] = len((A & B & C & E & F & H & J) - D - G - I) #ABCdEFgHiJ
        sets['1110110011'] = len((A & B & C & E & F & I & J) - D - G - H) #ABCdEFghIJ
        sets['1110101110'] = len((A & B & C & E & G & H & I) - D - F - J) #ABCdEfGHIj
        # {a,b,c,e,g,h,j} {a,b,c,e,g,i,j} {a,b,c,e,h,i,j} {a,b,c,f,g,h,i} {a,b,c,f,g,h,j} {a,b,c,f,g,i,j} {a,b,c,f,h,i,j} {a,b,c,g,h,i,j} {a,b,d,e,f,g,h}
        sets['1110101101'] = len((A & B & C & E & G & H & J) - D - F - I) #ABCdEfGHiJ
        sets['1110101011'] = len((A & B & C & E & G & I & J) - D - F - H) #ABCdEfGhIJ
        sets['1110100111'] = len((A & B & C & E & H & I & J) - D - F - G) #ABCdEfgHIJ
        sets['1110011110'] = len((A & B & C & F & G & H & I) - D - E - J) #ABCdeFGHIj
        sets['1110011101'] = len((A & B & C & F & G & H & J) - D - E - I) #ABCdeFGHiJ
        sets['1110011011'] = len((A & B & C & F & G & I & J) - D - E - H) #ABCdeFGhIJ
        sets['1110010111'] = len((A & B & C & F & H & I & J) - D - E - G) #ABCdeFgHIJ
        sets['1110001111'] = len((A & B & C & G & H & I & J) - D - E - F) #ABCdefGHIJ
        sets['1101111100'] = len((A & B & D & E & F & G & H) - C - I - J) #ABcDEFGHij
        # {a,b,d,e,f,g,i} {a,b,d,e,f,g,j} {a,b,d,e,f,h,i} {a,b,d,e,f,h,j} {a,b,d,e,f,i,j} {a,b,d,e,g,h,i} {a,b,d,e,g,h,j} {a,b,d,e,g,i,j} {a,b,d,e,h,i,j}
        sets['1101111010'] = len((A & B & D & E & F & G & I) - C - H - J) #ABcDEFGhIj
        sets['1101111001'] = len((A & B & D & E & F & G & J) - C - H - I) #ABcDEFGhiJ
        sets['1101110110'] = len((A & B & D & E & F & H & I) - C - G - J) #ABcDEFgHIj
        sets['1101110101'] = len((A & B & D & E & F & H & J) - C - G - I) #ABcDEFgHiJ
        sets['1101110011'] = len((A & B & D & E & F & I & J) - C - G - H) #ABcDEFghIJ
        sets['1101101110'] = len((A & B & D & E & G & H & I) - C - F - J) #ABcDEfGHIj
        sets['1101101101'] = len((A & B & D & E & G & H & J) - C - F - I) #ABcDEfGHiJ
        sets['1101101011'] = len((A & B & D & E & G & I & J) - C - F - H) #ABcDEfGhIJ
        sets['1101100111'] = len((A & B & D & E & H & I & J) - C - F - G) #ABcDEfgHIJ
        # {a,b,d,f,g,h,i} {a,b,d,f,g,h,j} {a,b,d,f,g,i,j} {a,b,d,f,h,i,j} {a,b,d,g,h,i,j} {a,b,e,f,g,h,i} {a,b,e,f,g,h,j} {a,b,e,f,g,i,j} {a,b,e,f,h,i,j}
        sets['1101011110'] = len((A & B & D & F & G & H & I) - C - E - J) #ABcDeFGHIj
        sets['1101011101'] = len((A & B & D & F & G & H & J) - C - E - I) #ABcDeFGHiJ
        sets['1101011011'] = len((A & B & D & F & G & I & J) - C - E - H) #ABcDeFGhIJ
        sets['1101010111'] = len((A & B & D & F & H & I & J) - C - E - G) #ABcDeFgHIJ
        sets['1101001111'] = len((A & B & D & G & H & I & J) - C - E - F) #ABcDefGHIJ
        sets['1100111110'] = len((A & B & E & F & G & H & I) - C - D - J) #ABcdEFGHIj
        sets['1100111101'] = len((A & B & E & F & G & H & J) - C - D - I) #ABcdEFGHiJ
        sets['1100111011'] = len((A & B & E & F & G & I & J) - C - D - H) #ABcdEFGhIJ
        sets['1100110111'] = len((A & B & E & F & H & I & J) - C - D - G) #ABcdEFgHIJ
        # {a,b,e,g,h,i,j} {a,b,f,g,h,i,j} {a,c,d,e,f,g,h} {a,c,d,e,f,g,i} {a,c,d,e,f,g,j} {a,c,d,e,f,h,i} {a,c,d,e,f,h,j} {a,c,d,e,f,i,j} {a,c,d,e,g,h,i}
        sets['1100101111'] = len((A & B & E & G & H & I & J) - C - D - F) #ABcdEfGHIJ
        sets['1100011111'] = len((A & B & F & G & H & I & J) - C - D - E) #ABcdeFGHIJ
        sets['1011111100'] = len((A & C & D & E & F & G & H) - B - I - J) #AbCDEFGHij
        sets['1011111010'] = len((A & C & D & E & F & G & I) - B - H - J) #AbCDEFGhIj
        sets['1011111001'] = len((A & C & D & E & F & G & J) - B - H - I) #AbCDEFGhiJ
        sets['1011110110'] = len((A & C & D & E & F & H & I) - B - G - J) #AbCDEFgHIj
        sets['1011110101'] = len((A & C & D & E & F & H & J) - B - G - I) #AbCDEFgHiJ
        sets['1011110011'] = len((A & C & D & E & F & I & J) - B - G - H) #AbCDEFghIJ
        sets['1011101110'] = len((A & C & D & E & G & H & I) - B - F - J) #AbCDEfGHIj
        # {a,c,d,e,g,h,j} {a,c,d,e,g,i,j} {a,c,d,e,h,i,j} {a,c,d,f,g,h,i} {a,c,d,f,g,h,j} {a,c,d,f,g,i,j} {a,c,d,f,h,i,j} {a,c,d,g,h,i,j} {a,c,e,f,g,h,i}
        sets['1011101101'] = len((A & C & D & E & G & H & J) - B - F - I) #AbCDEfGHiJ
        sets['1011101011'] = len((A & C & D & E & G & I & J) - B - F - H) #AbCDEfGhIJ
        sets['1011100111'] = len((A & C & D & E & H & I & J) - B - F - G) #AbCDEfgHIJ
        sets['1011011110'] = len((A & C & D & F & G & H & I) - B - E - J) #AbCDeFGHIj
        sets['1011011101'] = len((A & C & D & F & G & H & J) - B - E - I) #AbCDeFGHiJ
        sets['1011011011'] = len((A & C & D & F & G & I & J) - B - E - H) #AbCDeFGhIJ
        sets['1011010111'] = len((A & C & D & F & H & I & J) - B - E - G) #AbCDeFgHIJ
        sets['1011001111'] = len((A & C & D & G & H & I & J) - B - E - F) #AbCDefGHIJ
        sets['1010111110'] = len((A & C & E & F & G & H & I) - B - D - J) #AbCdEFGHIj
        # {a,c,e,f,g,h,j} {a,c,e,f,g,i,j} {a,c,e,f,h,i,j} {a,c,e,g,h,i,j} {a,c,f,g,h,i,j} {a,d,e,f,g,h,i} {a,d,e,f,g,h,j} {a,d,e,f,g,i,j} {a,d,e,f,h,i,j}
        sets['1010111101'] = len((A & C & E & F & G & H & J) - B - D - I) #AbCdEFGHiJ
        sets['1010111011'] = len((A & C & E & F & G & I & J) - B - D - H) #AbCdEFGhIJ
        sets['1010110111'] = len((A & C & E & F & H & I & J) - B - D - G) #AbCdEFgHIJ
        sets['1010101111'] = len((A & C & E & G & H & I & J) - B - D - F) #AbCdEfGHIJ
        sets['1010011111'] = len((A & C & F & G & H & I & J) - B - D - E) #AbCdeFGHIJ
        sets['1001111110'] = len((A & D & E & F & G & H & I) - B - C - J) #AbcDEFGHIj
        sets['1001111101'] = len((A & D & E & F & G & H & J) - B - C - I) #AbcDEFGHiJ
        sets['1001111011'] = len((A & D & E & F & G & I & J) - B - C - H) #AbcDEFGhIJ
        sets['1001110111'] = len((A & D & E & F & H & I & J) - B - C - G) #AbcDEFgHIJ
        # {a,d,e,g,h,i,j} {a,d,f,g,h,i,j} {a,e,f,g,h,i,j} {b,c,d,e,f,g,h} {b,c,d,e,f,g,i} {b,c,d,e,f,g,j} {b,c,d,e,f,h,i} {b,c,d,e,f,h,j} {b,c,d,e,f,i,j}
        sets['1001101111'] = len((A & D & E & G & H & I & J) - B - C - F) #AbcDEfGHIJ
        sets['1001011111'] = len((A & D & F & G & H & I & J) - B - C - E) #AbcDeFGHIJ
        sets['1000111111'] = len((A & E & F & G & H & I & J) - B - C - D) #AbcdEFGHIJ
        sets['0111111100'] = len((B & C & D & E & F & G & H) - A - I - J) #aBCDEFGHij
        sets['0111111010'] = len((B & C & D & E & F & G & I) - A - H - J) #aBCDEFGhIj
        sets['0111111001'] = len((B & C & D & E & F & G & J) - A - H - I) #aBCDEFGhiJ
        sets['0111110110'] = len((B & C & D & E & F & H & I) - A - G - J) #aBCDEFgHIj
        sets['0111110101'] = len((B & C & D & E & F & H & J) - A - G - I) #aBCDEFgHiJ
        sets['0111110011'] = len((B & C & D & E & F & I & J) - A - G - H) #aBCDEFghIJ
        # {b,c,d,e,g,h,i} {b,c,d,e,g,h,j} {b,c,d,e,g,i,j} {b,c,d,e,h,i,j} {b,c,d,f,g,h,i} {b,c,d,f,g,h,j} {b,c,d,f,g,i,j} {b,c,d,f,h,i,j} {b,c,d,g,h,i,j}
        sets['0111101110'] = len((B & C & D & E & G & H & I) - A - F - J) #aBCDEfGHIj
        sets['0111101101'] = len((B & C & D & E & G & H & J) - A - F - I) #aBCDEfGHiJ
        sets['0111101011'] = len((B & C & D & E & G & I & J) - A - F - H) #aBCDEfGhIJ
        sets['0111100111'] = len((B & C & D & E & H & I & J) - A - F - G) #aBCDEfgHIJ
        sets['0111011110'] = len((B & C & D & F & G & H & I) - A - E - J) #aBCDeFGHIj
        sets['0111011101'] = len((B & C & D & F & G & H & J) - A - E - I) #aBCDeFGHiJ
        sets['0111011011'] = len((B & C & D & F & G & I & J) - A - E - H) #aBCDeFGhIJ
        sets['0111010111'] = len((B & C & D & F & H & I & J) - A - E - G) #aBCDeFgHIJ
        sets['0111001111'] = len((B & C & D & G & H & I & J) - A - E - F) #aBCDefGHIJ
        # {b,c,e,f,g,h,i} {b,c,e,f,g,h,j} {b,c,e,f,g,i,j} {b,c,e,f,h,i,j} {b,c,e,g,h,i,j} {b,c,f,g,h,i,j} {b,d,e,f,g,h,i} {b,d,e,f,g,h,j} {b,d,e,f,g,i,j}
        sets['0110111110'] = len((B & C & E & F & G & H & I) - A - D - J) #aBCdEFGHIj
        sets['0110111101'] = len((B & C & E & F & G & H & J) - A - D - I) #aBCdEFGHiJ
        sets['0110111011'] = len((B & C & E & F & G & I & J) - A - D - H) #aBCdEFGhIJ
        sets['0110110111'] = len((B & C & E & F & H & I & J) - A - D - G) #aBCdEFgHIJ
        sets['0110101111'] = len((B & C & E & G & H & I & J) - A - D - F) #aBCdEfGHIJ
        sets['0110011111'] = len((B & C & F & G & H & I & J) - A - D - E) #aBCdeFGHIJ
        sets['0101111110'] = len((B & D & E & F & G & H & I) - A - C - J) #aBcDEFGHIj
        sets['0101111101'] = len((B & D & E & F & G & H & J) - A - C - I) #aBcDEFGHiJ
        sets['0101111011'] = len((B & D & E & F & G & I & J) - A - C - H) #aBcDEFGhIJ
        # {b,d,e,f,h,i,j} {b,d,e,g,h,i,j} {b,d,f,g,h,i,j} {b,e,f,g,h,i,j} {c,d,e,f,g,h,i} {c,d,e,f,g,h,j} {c,d,e,f,g,i,j} {c,d,e,f,h,i,j} {c,d,e,g,h,i,j}
        sets['0101110111'] = len((B & D & E & F & H & I & J) - A - C - G) #aBcDEFgHIJ
        sets['0101101111'] = len((B & D & E & G & H & I & J) - A - C - F) #aBcDEfGHIJ
        sets['0101011111'] = len((B & D & F & G & H & I & J) - A - C - E) #aBcDeFGHIJ
        sets['0100111111'] = len((B & E & F & G & H & I & J) - A - C - D) #aBcdEFGHIJ
        sets['0011111110'] = len((C & D & E & F & G & H & I) - A - B - J) #abCDEFGHIj
        sets['0011111101'] = len((C & D & E & F & G & H & J) - A - B - I) #abCDEFGHiJ
        sets['0011111011'] = len((C & D & E & F & G & I & J) - A - B - H) #abCDEFGhIJ
        sets['0011110111'] = len((C & D & E & F & H & I & J) - A - B - G) #abCDEFgHIJ
        sets['0011101111'] = len((C & D & E & G & H & I & J) - A - B - F) #abCDEfGHIJ
        # {c,d,f,g,h,i,j} {c,e,f,g,h,i,j} {d,e,f,g,h,i,j}
        sets['0011011111'] = len((C & D & F & G & H & I & J) - A - B - E) #abCDeFGHIJ
        sets['0010111111'] = len((C & E & F & G & H & I & J) - A - B - D) #abCdEFGHIJ
        sets['0001111111'] = len((D & E & F & G & H & I & J) - A - B - C) #abcDEFGHIJ
        # {a,b,c,d,e,f,g,h} {a,b,c,d,e,f,g,i} {a,b,c,d,e,f,g,j} {a,b,c,d,e,f,h,i} {a,b,c,d,e,f,h,j} {a,b,c,d,e,f,i,j} {a,b,c,d,e,g,h,i} {a,b,c,d,e,g,h,j}
        sets['1111111100'] = len((A & B & C & D & E & F & G & H) - I - J) #ABCDEFGHij
        sets['1111111010'] = len((A & B & C & D & E & F & G & I) - H - J) #ABCDEFGhIj
        sets['1111111001'] = len((A & B & C & D & E & F & G & J) - H - I) #ABCDEFGhiJ
        sets['1111110110'] = len((A & B & C & D & E & F & H & I) - G - J) #ABCDEFgHIj
        sets['1111110101'] = len((A & B & C & D & E & F & H & J) - G - I) #ABCDEFgHiJ
        sets['1111110011'] = len((A & B & C & D & E & F & I & J) - G - H) #ABCDEFghIJ
        sets['1111101110'] = len((A & B & C & D & E & G & H & I) - F - J) #ABCDEfGHIj
        sets['1111101101'] = len((A & B & C & D & E & G & H & J) - F - I) #ABCDEfGHiJ
        # {a,b,c,d,e,g,i,j} {a,b,c,d,e,h,i,j} {a,b,c,d,f,g,h,i} {a,b,c,d,f,g,h,j} {a,b,c,d,f,g,i,j} {a,b,c,d,f,h,i,j} {a,b,c,d,g,h,i,j} {a,b,c,e,f,g,h,i}
        sets['1111101011'] = len((A & B & C & D & E & G & I & J) - F - H) #ABCDEfGhIJ
        sets['1111100111'] = len((A & B & C & D & E & H & I & J) - F - G) #ABCDEfgHIJ
        sets['1111011110'] = len((A & B & C & D & F & G & H & I) - E - J) #ABCDeFGHIj
        sets['1111011101'] = len((A & B & C & D & F & G & H & J) - E - I) #ABCDeFGHiJ
        sets['1111011011'] = len((A & B & C & D & F & G & I & J) - E - H) #ABCDeFGhIJ
        sets['1111010111'] = len((A & B & C & D & F & H & I & J) - E - G) #ABCDeFgHIJ
        sets['1111001111'] = len((A & B & C & D & G & H & I & J) - E - F) #ABCDefGHIJ
        sets['1110111110'] = len((A & B & C & E & F & G & H & I) - D - J) #ABCdEFGHIj
        # {a,b,c,e,f,g,h,j} {a,b,c,e,f,g,i,j} {a,b,c,e,f,h,i,j} {a,b,c,e,g,h,i,j} {a,b,c,f,g,h,i,j} {a,b,d,e,f,g,h,i} {a,b,d,e,f,g,h,j} {a,b,d,e,f,g,i,j}
        sets['1110111101'] = len((A & B & C & E & F & G & H & J) - D - I) #ABCdEFGHiJ
        sets['1110111011'] = len((A & B & C & E & F & G & I & J) - D - H) #ABCdEFGhIJ
        sets['1110110111'] = len((A & B & C & E & F & H & I & J) - D - G) #ABCdEFgHIJ
        sets['1110101111'] = len((A & B & C & E & G & H & I & J) - D - F) #ABCdEfGHIJ
        sets['1110011111'] = len((A & B & C & F & G & H & I & J) - D - E) #ABCdeFGHIJ
        sets['1101111110'] = len((A & B & D & E & F & G & H & I) - C - J) #ABcDEFGHIj
        sets['1101111101'] = len((A & B & D & E & F & G & H & J) - C - I) #ABcDEFGHiJ
        sets['1101111011'] = len((A & B & D & E & F & G & I & J) - C - H) #ABcDEFGhIJ
        # {a,b,d,e,f,h,i,j} {a,b,d,e,g,h,i,j} {a,b,d,f,g,h,i,j} {a,b,e,f,g,h,i,j} {a,c,d,e,f,g,h,i} {a,c,d,e,f,g,h,j} {a,c,d,e,f,g,i,j} {a,c,d,e,f,h,i,j}
        sets['1101110111'] = len((A & B & D & E & F & H & I & J) - C - G) #ABcDEFgHIJ
        sets['1101101111'] = len((A & B & D & E & G & H & I & J) - C - F) #ABcDEfGHIJ
        sets['1101011111'] = len((A & B & D & F & G & H & I & J) - C - E) #ABcDeFGHIJ
        sets['1100111111'] = len((A & B & E & F & G & H & I & J) - C - D) #ABcdEFGHIJ
        sets['1011111110'] = len((A & C & D & E & F & G & H & I) - B - J) #AbCDEFGHIj
        sets['1011111101'] = len((A & C & D & E & F & G & H & J) - B - I) #AbCDEFGHiJ
        sets['1011111011'] = len((A & C & D & E & F & G & I & J) - B - H) #AbCDEFGhIJ
        sets['1011110111'] = len((A & C & D & E & F & H & I & J) - B - G) #AbCDEFgHIJ
        # {a,c,d,e,g,h,i,j} {a,c,d,f,g,h,i,j} {a,c,e,f,g,h,i,j} {a,d,e,f,g,h,i,j} {b,c,d,e,f,g,h,i} {b,c,d,e,f,g,h,j} {b,c,d,e,f,g,i,j} {b,c,d,e,f,h,i,j}
        sets['1011101111'] = len((A & C & D & E & G & H & I & J) - B - F) #AbCDEfGHIJ
        sets['1011011111'] = len((A & C & D & F & G & H & I & J) - B - E) #AbCDeFGHIJ
        sets['1010111111'] = len((A & C & E & F & G & H & I & J) - B - D) #AbCdEFGHIJ
        sets['1001111111'] = len((A & D & E & F & G & H & I & J) - B - C) #AbcDEFGHIJ
        sets['0111111110'] = len((B & C & D & E & F & G & H & I) - A - J) #aBCDEFGHIj
        sets['0111111101'] = len((B & C & D & E & F & G & H & J) - A - I) #aBCDEFGHiJ
        sets['0111111011'] = len((B & C & D & E & F & G & I & J) - A - H) #aBCDEFGhIJ
        sets['0111110111'] = len((B & C & D & E & F & H & I & J) - A - G) #aBCDEFgHIJ
        # {b,c,d,e,g,h,i,j} {b,c,d,f,g,h,i,j} {b,c,e,f,g,h,i,j} {b,d,e,f,g,h,i,j} {c,d,e,f,g,h,i,j}
        sets['0111101111'] = len((B & C & D & E & G & H & I & J) - A - F) #aBCDEfGHIJ
        sets['0111011111'] = len((B & C & D & F & G & H & I & J) - A - E) #aBCDeFGHIJ
        sets['0110111111'] = len((B & C & E & F & G & H & I & J) - A - D) #aBCdEFGHIJ
        sets['0101111111'] = len((B & D & E & F & G & H & I & J) - A - C) #aBcDEFGHIJ
        sets['0011111111'] = len((C & D & E & F & G & H & I & J) - A - B) #abCDEFGHIJ
        # {a,b,c,d,e,f,g,h,i} {a,b,c,d,e,f,g,h,j} {a,b,c,d,e,f,g,i,j} {a,b,c,d,e,f,h,i,j} {a,b,c,d,e,g,h,i,j} {a,b,c,d,f,g,h,i,j} {a,b,c,e,f,g,h,i,j} {a,b,d,e,f,g,h,i,j} {a,c,d,e,f,g,h,i,j} {b,c,d,e,f,g,h,i,j} 
        sets['1111111110'] = len((A & B & C & D & E & F & G & H & I) - J) #ABCDEFGHIj
        sets['1111111101'] = len((A & B & C & D & E & F & G & H & J) - I) #ABCDEFGHiJ
        sets['1111111011'] = len((A & B & C & D & E & F & G & I & J) - H) #ABCDEFGhIJ
        sets['1111110111'] = len((A & B & C & D & E & F & H & I & J) - G) #ABCDEFgHIJ
        sets['1111101111'] = len((A & B & C & D & E & G & H & I & J) - F) #ABCDEfGHIJ
        sets['1111011111'] = len((A & B & C & D & F & G & H & I & J) - E) #ABCDeFGHIJ
        sets['1110111111'] = len((A & B & C & E & F & G & H & I & J) - D) #ABCdEFGHIJ
        sets['1101111111'] = len((A & B & D & E & F & G & H & I & J) - C) #ABcDEFGHIJ
        sets['1011111111'] = len((A & C & D & E & F & G & H & I & J) - B) #AbCDEFGHIJ
        sets['0111111111'] = len((B & C & D & E & F & G & H & I & J) - A) #aBCDEFGHIJ
        # {a,b,c,d,e,f,g,h,i,j}
        sets['1111111111'] = len(A & B & C & D & E & F & G & H & I & J) #ABCDEFGHIJ
    else:
        print("You need to have between 2 and 10 sets.")
        return 0

    return sets

