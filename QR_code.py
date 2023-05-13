
import qrcode

qr = qrcode.QRCode(version = 1,
				box_size = 10,
				border = 5)


qr.add_data("https://rpatel9675.github.io/rocky.github.io/")

qr.make(fit = True)
img = qr.make_image(fill_color = 'black',
					back_color = 'white')

img.save("Rocky's_cv.png")
