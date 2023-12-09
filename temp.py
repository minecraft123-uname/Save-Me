from PIL import Image


# img = Image.open("src/arrow_raw.png")
# n = 0.05
# size = (int(img.size[0] * n), int(img.size[1] * n))
# img.resize(size).save("src/arrow.png")

# buoy = Image.open('buoy1.png')
# new = Image.new(size=buoy.size, mode="RGBA")
# for i in range(buoy.size[0]):
# 	for j in range(buoy.size[1]):
# 		if sum(buoy.getpixel((i, j))[:2]) < 440:
# 			new.putpixel((i, j), buoy.getpixel((i, j)))
# 		else:
# 			new.putpixel((i, j), (255, 255, 255, 0))
# new.save("new.png")

Image.open("src/arrow2.png").resize((135, 30)).save("src/arrow.png")