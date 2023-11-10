import qrcode
def generate_qrcode(text):
    qr=qrcode.QRcode(version=1,error_correction=qrcode.constants.ERROT_CORRECT_L,box_size=10,border=4)
    qr.add_data(text)
    qr.make(fit=True)
    img=qr.make_image(fill_color="black",back_color="white")
    img.save("qrcode.png")
    img.show()

url=input("Enter your url:")
generate_qrcode(url)
