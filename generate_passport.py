def main(infofile, photofile):
    from eth_account import Account, messages
    import getpass
    import json
    import base64
    import time
    import hashlib
    info = {}
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞß "
    alt = {
        " ": "<",
        "À": "A1",
        "Á": "A2",
        "Â": "A3",
        "Ã": "A4",
        "Ä": "A5",
        "Å": "A6",
        "Æ": "A7",
        "Ç": "C1",
        "È": "E1",
        "É": "E2",
        "Ê": "E3",
        "Ë": "E4",
        "Ì": "I1",
        "Í": "I2",
        "Î": "I3",
        "Ï": "I4",
        "Ð": "D1",
        "Ñ": "N1",
        "Ò": "O1",
        "Ó": "O2",
        "Ô": "O3",
        "Õ": "O4",
        "Ö": "O5",
        "Ø": "O7",
        "Ù": "U1",
        "Ú": "U2",
        "Û": "U3",
        "Ü": "U4",
        "Ý": "Y1",
        "Þ": "Y2",
        "ß": "S1"
    }
    with open(infofile, "r", encoding="utf-8") as f:
        info = json.loads(f.read())
    info["name"] = info["name"].upper()
    for x in info["name"]:
        if x not in chars:
            print(x + "is not allowed")
            exit()
    name_readable = "".join([alt[x] if x in alt else x for x in info["name"]])
    if len(name_readable) > 38:
        print("Name too long")
        exit()
    info["place"] = info["place"].upper()
    for x in info["place"]:
        if x not in chars:
            print(x + "is not allowed")
            exit()
    hash = info["hash"][2:].upper()
    info["issue"] = int(time.time())
    mrz_area1 = "P<TGD" + name_readable + "<"*(39-len(name_readable))
    mrz_area2 = ("0x" + hash + "<<")
    id = hash[:4]+hash[-4:]
    birth = str(info["birth"])
    print("    Name: " + info["name"])
    print("Pronouns: " + info["pronouns"])
    print("   Place: "+info["place"])
    print("   Birth: "+birth[0:4]+"/"+birth[4:6]+"/"+birth[6:8])
    print(" MR Area: " + mrz_area1)
    print("          " + mrz_area2)
    print("      ID: " + id)
    head = b"TGDPASSPORT\x00"
    hash_b = int(info["hash"], 16).to_bytes(20, "big")
    del info["hash"]
    info = json.dumps(info, ensure_ascii=False).encode(encoding="latin-1")
    photo = b''
    with open(photofile, "rb") as f:
        photo = f.read()
    info_short = info
    info = info+b'\x00'+photo
    prvkey = getpass.getpass("Your private key: ")
    msg_hash_hex = hashlib.sha512(info).hexdigest()
    message = messages.encode_defunct(hexstr=msg_hash_hex)
    signed_message = Account.sign_message(message, private_key=prvkey)
    msg_hash_hex = hashlib.sha512(info_short).hexdigest()
    message = messages.encode_defunct(hexstr=msg_hash_hex)
    signed_shortmessage = Account.sign_message(message, private_key=prvkey)
    with open(id+".tgdpassport", "wb") as f:
        f.write(head+hash_b+signed_message.signature+info)
    bc = b'TGD\x00'+hash_b+signed_shortmessage.signature+info_short
    return id, bc


if __name__ == "__main__":
    import sys
    main(sys.argv[1], sys.argv[2])
