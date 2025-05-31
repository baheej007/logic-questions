import qrcode

data = "https://github.com/Baheej-Portfolio"
qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill="black", back_color="white")
img.save("my_qr.png")
