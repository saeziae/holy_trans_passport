def main(file):
    from PIL import Image, ImageDraw, ImageFont
    import qrcode
    from eth_account import Account, messages
    import json
    import time
    import hashlib
    import io
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
    with open(file, "rb") as f:
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
    photo = info[1]
    info = json.loads(info[0].decode(encoding="latin-1"))
    id = id.hex().upper()
    id_short = id[:4]+id[-4:]
    birth = str(info["birth"])
    name_readable = "".join([alt[x] if x in alt else x for x in info["name"]])
    mrz_area1 = "P<TGD" + name_readable + "<"*(39-len(name_readable))
    mrz_area2 = ("0x" + id + "<<")

    birth = time.strftime(
        "%Y / %m %b / %d", time.strptime(birth, "%Y%m%d")).upper()
    issue = time.strftime(
        "%Y / %m %b / %d", time.localtime(info["issue"])).upper()

    qr = qrcode.QRCode(version=1,
                       box_size=4,
                       border=0)
    qr.add_data("ethereum:0x"+id)
    qr_img = qr.make_image(fill_color=(0, 0, 0),
                           back_color="transparent")
    qr.make(fit=True)

    f_number = ImageFont.truetype("no-font.ttf", size=60)
    f_text = ImageFont.truetype("text-font.ttf", size=35)
    f_id = ImageFont.truetype("mrz-font.ttf", size=50,
                              layout_engine=ImageFont.Layout.BASIC)
    im = Image.open("background.png")
    mask = Image.open("mask.png")
    photo = Image.open(io.BytesIO(photo)).convert("RGBA")
    photo = photo.resize((320, 480))
    imd = ImageDraw.ImageDraw(im)
    imd.text((1147, 175), id_short, font=f_number, fill=(244, 62, 66))
    imd.text((500, 292), info["name"], font=f_text, fill=(0, 0, 0))
    imd.text((1004, 292), info["pronouns"], font=f_text, fill=(0, 0, 0))
    imd.text((500, 510), birth, font=f_text, fill=(0, 0, 0))
    imd.text((1004, 510), info["place"], font=f_text, fill=(0, 0, 0))
    imd.text((500, 615), issue, font=f_text, fill=(0, 0, 0))
    imd.text((88, 794), mrz_area1, font=f_id, fill=(0, 0, 0))
    imd.text((88, 874), mrz_area2, font=f_id, fill=(0, 0, 0))
    im.paste(qr_img, (1270, 20), mask=qr_img)
    im.paste(photo, (120, 240), photo)
    im.alpha_composite(mask)
    im.save(id_short+".png")


if __name__ == "__main__":
    import sys
    main(sys.argv[1])
