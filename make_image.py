from PIL import Image, ImageDraw, ImageFont
import math

W, H = 1600, 900
img = Image.new("RGB", (W, H))
pixels = img.load()
for y in range(H):
    for x in range(W):
        t = (x / W * 0.55 + y / H * 0.45)
        pixels[x, y] = (int(5 + 3 * t), int(12 + 9 * t), int(27 + 15 * t))

d = ImageDraw.Draw(img, "RGBA")
cyan = (45, 229, 255, 255)
lime = (190, 255, 78, 255)
white = (244, 248, 255, 255)
muted = (151, 174, 198, 255)

# Subtle grid dots and geometric framing.
for y in range(42, H, 44):
    for x in range(38, W, 44):
        d.ellipse((x, y, x + 2, y + 2), fill=(95, 150, 182, 48))
d.ellipse((1130, 95, 1550, 515), outline=(45, 229, 255, 38), width=2)
d.ellipse((1190, 155, 1490, 455), outline=(190, 255, 78, 30), width=2)
d.line([(0, 690), (1600, 690)], fill=(45, 229, 255, 35), width=2)

font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
def font(size):
    return ImageFont.truetype(font_path, size)

d.rounded_rectangle((84, 62, 430, 116), radius=8, fill=(45, 229, 255, 22), outline=(45, 229, 255, 140), width=2)
d.text((106, 72), "MUST-FOLLOW ON X", font=font(25), fill=cyan)

d.text((80, 146), "@crisxai5", font=font(112), fill=white, stroke_width=1, stroke_fill=(45, 229, 255, 80))
d.rounded_rectangle((85, 285, 735, 292), radius=3, fill=lime)
d.text((84, 316), "AI & CRYPTO, WITHOUT THE NOISE", font=font(35), fill=cyan)

# Rising signal chart on the right.
chart = [(930, 600), (1020, 540), (1100, 555), (1190, 435), (1270, 465), (1360, 330), (1450, 355), (1530, 215)]
d.line(chart, fill=(45, 229, 255, 200), width=5, joint="curve")
for i, (x, y) in enumerate(chart):
    r = 8 if i == len(chart) - 1 else 5
    d.ellipse((x-r, y-r, x+r, y+r), fill=lime if i == len(chart)-1 else cyan)

labels = ["AI AGENTS", "CRYPTO ALPHA", "WEB3 TOOLING", "ON-CHAIN AUTOMATION"]
positions = [(86, 430), (500, 430), (86, 535), (500, 535)]
for i, (label, (x, y)) in enumerate(zip(labels, positions)):
    accent = cyan if i % 2 == 0 else lime
    d.rounded_rectangle((x, y, x + 350, y + 76), radius=7, fill=(13, 29, 48, 230), outline=(*accent[:3], 190), width=2)
    d.rectangle((x, y, x + 7, y + 76), fill=accent)
    d.text((x + 25, y + 19), label, font=font(22), fill=white)

d.text((85, 748), "Sharp insight. Practical alpha. Follow @crisxai5", font=font(29), fill=white)
d.rounded_rectangle((85, 812, 1515, 816), radius=2, fill=(45, 229, 255, 120))
img.save("crisxai5-spotlight.png", "PNG", optimize=True)
