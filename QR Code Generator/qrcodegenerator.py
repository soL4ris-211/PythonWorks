import qrcode
import image
qr = qrcode.QRCode(
    version = 15, #15 means the version of the qr code, higher the number bigger the code image and complicated picture
    box_size = 10, #Size of the box where qr code will be displayed.
    border = 5 #It is the white part of the image -- border in all 4 sides with white color.
)

data = "https://github.com/soL4ris-211"
#As I have given the path of my GitHub profile like the same way you can give anything.

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black",back_color="white")
img.save("test.png")