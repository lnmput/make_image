from PIL import ImageDraw, ImageFont


def create_left_area(image, a4_width, a4_height):
    draw = ImageDraw.Draw(image)

    # 在图片内创建一个竖条的矩形框
    rectangle_width = 300  # 矩形框的宽度
    rectangle_height = a4_height - 200  # 矩形框的高度，稍微小于A4高度，留出一些边距
    rectangle_x = 90  # 距离左侧3cm
    rectangle_y = 100  # 上下边距为100像素
    rectangle_color = (0, 0, 0)  # 黑色边框的颜色
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
    font_size = 58
    font = ImageFont.truetype("./fonts/arial.ttf", font_size)

    # 定义文字内容
    text_content = ("1=A,2=B,3=C,4=D,5=E,6=F,7=G,8=H,9=I,10=J,11=K,12=L,13=M,14=N,15=O,16=P,17=Q,18=R,19=S,20=T,21=U,"
                    "22=V,23=W,24=X,25=Y,26=Z")

    # text_content = ("1=a,2=b,3=c,4=d,5=e,6=f,7=g,8=h,9=i,10=j,11=k,12=l,13=m,14=n,15=o,16=p,17=q,18=r,19=s,20=t,21=u,"
    #                 "22=v,23=w,24=x,25=y,26=z")

    # 将文字按行分割
    lines = text_content.strip().split(",")

    # 设置行高
    line_height = 1.5

    # 计算每行文字的左上角位置
    start_x = rectangle_x + (rectangle_width - draw.textbbox((0, 0), lines[0], font=font)[2]) // 2  # 左右居中

    # 计算总文字高度，考虑行间距
    total_text_height = sum(draw.textbbox((0, 0), line, font=font)[3] * line_height for line in lines)

    # 计算 start_y，考虑矩形高度
    start_y = rectangle_y + (rectangle_height - total_text_height) // 2  # 上下居中

    # 修改文字颜色为黑色
    text_color = (0, 0, 0)

    # 逐行绘制文字
    for line in lines:
        text_width, text_height = draw.textbbox((0, 0), line, font=font)[2], draw.textbbox((0, 0), line, font=font)[3]
        draw.text((start_x, start_y), line, font=font, fill=text_color)
        start_y += text_height * line_height  # 使用text_height和line_height确保文字行间距正确

    # 保存图片
    # image.save("output_image.png")

    # 显示图片
    # image.show()

    return image
