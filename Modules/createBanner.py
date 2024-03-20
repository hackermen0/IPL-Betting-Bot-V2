from PIL import Image, ImageFont, ImageDraw

img1 = Image.open("./Static/Logo/Delhi Capitals.jpg")
img2 = Image.open("./Static/Logo/Chennai Super Kings.jpg")


banner = Image.new("RGB", (1024, 512), "black")

banner.paste(img1, (0,0))
banner.paste(img2, (512, 0))

font = ImageFont.truetype("./Static/Fonts/Roboto-Bold.ttf", 36)

draw = ImageDraw.Draw(banner)

draw.text((480, 250), "V", fill = (255, 255, 255), font = font, anchor = "mm")
draw.text((540, 250), "S", fill = (255, 255, 255), font = font, anchor = "mm")

banner.save("Banner.png")