from PIL import Image, ImageDraw, ImageFont

# 创建一个白色背景的A4图片
width, height = 2480, 3508  # A4纸的宽度和高度，单位是像素
background_color = (31, 41, 55)  # 白色
image = Image.new("RGB", (width, height), background_color)
draw = ImageDraw.Draw(image)

# 在图片内创建一个竖条的矩形框
rectangle_width = 300  # 矩形框的宽度
rectangle_height = height - 200  # 矩形框的高度，稍微小于A4高度，留出一些边距
rectangle_x = 90  # 距离左侧3cm
rectangle_y = 100  # 上下边距为100像素
rectangle_color = (255, 255, 255)  # 彩色边框的颜色
border_width = 5  # 矩形边框的宽度
corner_radius = 20  # 圆角的半径

draw.rectangle(
    [
        (rectangle_x, rectangle_y),
        (rectangle_x + rectangle_width, rectangle_y + rectangle_height),
    ],
    outline=rectangle_color,
    width=border_width,
)

# 在矩形框内绘制文字
font_size = 60
font = ImageFont.truetype("arial.ttf", font_size)

# 定义文字内容
text_content = """
1=A
2=B
3=C
4=D
5=E
6=F
7=G
8=H
9=I
10=J
11=K
12=L
13=M
14=N
15=O
16=P
17=Q
18=R
19=S
20=T
21=U
22=V
23=W
24=X
25=Y
26=Z
"""

# 将文字按行分割
lines = text_content.strip().split("\n")

# 设置行高
line_height = 1.5

# 计算每行文字的左上角位置
start_x = rectangle_x + (rectangle_width - draw.textbbox((0, 0), lines[0], font=font)[2]) // 2  # 左右居中

# 计算总文字高度，考虑行间距
total_text_height = sum(draw.textbbox((0, 0), line, font=font)[3] * line_height for line in lines)

# 计算 start_y，考虑矩形高度
start_y = rectangle_y + (rectangle_height - total_text_height) // 2  # 上下居中

# 逐行绘制文字
for line in lines:
    text_width, text_height = draw.textbbox((0, 0), line, font=font)[2], draw.textbbox((0, 0), line, font=font)[3]
    draw.text((start_x, start_y), line, font=font, fill=(0, 0, 0))
    start_y += text_height * line_height  # 使用text_height和line_height确保文字行间距正确

# 保存图片
image.save("output_image.png")

# 显示图片
image.show()
