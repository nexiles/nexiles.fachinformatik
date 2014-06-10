def hash_string(string):
    string_hex = string.encode('hex')
    nummber = int(string_hex, 16)
    modulo = [2,5,6,8,9,4,3,5,6,7,4,6,4,56,3,5,3,34]
    my_hash = 1
    m = 1
    for i in range(1,len(string_hex),1):
        try:
            mod = nummber % modulo[m]
            my_hash = my_hash + mod
            m = m + 1
        except:
            for u in range(1,my_hash,1):
                tok = my_hash % u
                my_hash = (tok * my_hash) % nummber
            m = 1
    return my_hash
