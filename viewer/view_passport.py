from eth_account import Account, messages
import getpass
import json
import base64
import time
import hashlib
import sys
import cv2
import numpy as np
info = {}
bin = b''
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
with open(sys.argv[1], "rb") as f:
    bin = f.read()
head = bin[:12]
if head != b'TGDPASSPORT\x00':
    exit()
id = bin[12:32]
sign = bin[32:97]
info = bin[97:]
msg_hash_hex = hashlib.sha512(info).hexdigest()
message = messages.encode_defunct(hexstr=msg_hash_hex)
address = Account.recover_message(message, signature=sign)
if address[2:].lower() == id.hex():
    print("==THIS PASSPORT IS VALID==")
else:
    print("==THIS PASSPORT IS INVALID==")
    exit()
info = info.split(b"\x00", 1)
nparr = np.frombuffer(info[1], np.uint8)
info = json.loads(info[0].decode(encoding="latin-1"))
id = id.hex().upper()
birth = str(info["birth"])
name_readable = "".join([alt[x] if x in alt else x for x in info["name"]])
mrz_area1 = "P<TGD" + name_readable + "<"*(39-len(name_readable))
mrz_area2 = ("0x" + id + "<<")
print("      ID: "+(id[:4]+id[-4:]))
print("    Name: "+info["name"])
print("Pronouns: "+info["pronouns"])
print("   Place: "+info["place"])
print("   Birth: "+birth[0:4]+"/"+birth[4:6]+"/"+birth[6:8])
print("   Issue: "+time.strftime("%Y/%m/%d %H:%M:%S",
      time.localtime(info["issue"]))+" Timezone:"+str(time.timezone))
print(mrz_area1)
print(mrz_area2)
img = cv2.imdecode(nparr, cv2.IMREAD_ANYCOLOR)
cv2.namedWindow("IMG")
cv2.imshow("IMG", img)
cv2.waitKey()
cv2.destroyAllWindows()
