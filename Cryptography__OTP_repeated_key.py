def string_fractionator(string, num):
    final_strings_list = []
    while len(string) > num:
        final_strings_list.append(string[:num])
        string = string[num::]
    final_strings_list.append(string)
  
    return final_strings_list

def translate_hexa(text):
   return(text.encode('latin1').hex())

def xor_hexa_letters(letter1, letter2):
    xorted_pairs = int(letter1, 16) ^ int(letter2, 16)
    formated_xor = str(hex(xorted_pairs))[2:].zfill(2)
    return bytes.fromhex(formated_xor).decode('latin1')
    

import re

def crib_column_atack(column_cipher, letter, regex = True):
    cripter_aplicate = []
    for letter_i in column_cipher:
        decodified_return = xor_hexa_letters(letter_i, translate_hexa(letter))
        if not re.search("^[a-zA-Z0-9_áéíóúÁÉÍÓÚüÜ«»,\.;\- \?¿!¡()'\"ñ]*$",decodified_return):
            return False
    return True

def fractionate_columns(string, key_len):
    final_key = ""
    string_fraction = string_fractionator(string, key_len)
    separated_columns = [ [ j[i:i+2] for j in string_fraction] for i in range(0, key_len, 2)]
    for column in separated_columns:
        for letter in "^[abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789áéíóúÁÉÍÓÚüÜ«»,\.;\- \?¿!¡()'\"ñ]*$":
            if crib_column_atack(column, letter):
                final_key += letter 
                break
            
    for sub in string_fraction:
        for i in range(16):
            print(xor_hexa_letters(sub[2*i:2*i+2], translate_hexa(final_key[i])), end = "")
        
    return f'\nKey = {final_key}'


# ----- START THE ATTACK -----

cipher_hexa_string = "0806170d1d1d4f029d0a1a440b081203309a074952081d0602110c440e014103201f1b1181004f0709450f111c040d12281a110b0601434309094907001f0e1d201f5424071c0a0f0504070b4f2f14162b17990452060e01810449000a4d1316261c0601131c4f021d100c08030c410724011000521c0a0e031108440a03410230165416074e1f0208170c440302411f29160296520f4f00030b06070a1f411629531c0c1702004d4c2808070003051c65160604520b0117030b0a011c4d141d24531509160b0e43080049120a040f0720531704010f1c43080049060e1f131c650a5406139f0e011e041f054f0e0e1d360706101b0a0e430d4505054f02131a291f1545160b4f1602451b89004d051665121310131d4f0705840f05010c125334061145010b4f131e000a0d1f04151227121a4502011d43190b49080a0e091c6517114502070a071e041a441f180d1a21120749520c0302020608174f1441162b1c0608171d4f0003080644071804052a005415000b070a1f119a16060e0e006b53310952031a0d080a49011d0c4107241d5417170d060602110c484f1c1416651e01061a0f1c430f0a1a051c4d02123716178813004f070945070b020f131669530d45020f1d024c080c0a0c040e1d24011804014e07020e8808441e180453361685041e0f1d0f0d164907000341162953100016014143260a1a8d4f2c131024171d0a522c1a0602018405434d100620531117134e0a0f4c0d06090d1f04532892074517031f11090b0d010b02135334061145010b4f15091784054f07001ea40054001c4e03024c0405000a0c4d532d121688134e0b0a1f151c011c190e532116541113024f0e03010644030c41032a001d061b9d0143080049080e1e4110240015165e4e1e1609450d011c090453311c1004014e1f0c088808440301041424010700520f03431e880644164d001124000000110b1d1009450d014f0c06062453170a1c4e0604190405440a1e070620010e0a5e4e16431817081e9c4d0d12365317041e020a104c06060a4f19001d651101001c4e1c0602110000004d100620531a0c1c091a0d0d450a051c0c410120101d079f0f4f0e8d164917000141023016540a061c0e430d4505054f050e01245310001e4e0c02000a1b4a4f280f53351c170a014e0e9203164544220c021c2b171b45141b0a43190b08440e01051624531984014e0011080007050b0c410a651f15071d1c060c1f0449151a0841103012181407070a110d450d014f01000065101b0b1d0d06070d16490c0e1e151265161a111d000c061f45190b1d4d120636530017171d0c0a090b1d0b1c4d0912271a00041c1a0a1042452c160e4d041d65051117160f0b43190b08440e010516245312001e07154f4c01060a0b08411d24171d00520b1d024c08081d001f411720530017170701170d450895001e410a65171b0b160b4f0d0d0100014f050011a8125408070b1d17034b0c26080e0909"
# Key len = 128 bits = 16 bytes = 32 hexadecimal digits = 16 pairs of hexadecimal digits (and each pair represent an latin1 symbol)
key_len = 32

print(fractionate_columns(cipher_hexa_string, key_len))
    
