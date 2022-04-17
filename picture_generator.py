from PIL import Image, ImageDraw

import random, math, colorsys


def generate_art():
    print("Generate Art")
    image_size_px = 2000
    image_bg_color = (255, 255, 255, 255)
    image = Image.new("RGBA", size=(image_size_px, image_size_px), color=image_bg_color)
    draw = ImageDraw.Draw(image)
    points = []
    starting_pos = (0, image_size_px * 0.50), (image_size_px, image_size_px * 0.50)
    x = 200
    y = image_size_px * 0.50
    for _ in range(0, math.ceil(1120)):
        x += 70
        y += 100 - random.randint(0, image_size_px * 0.3)
        if y >= image_size_px * 0.4:
            y -= 300
        elif y <= image_size_px * 0.4:
            y += 300
        if x >= image_size_px:
            x -= 300
            break
        newpoints = (x, y)
        points.append(newpoints)
        y -= 100 - random.randint(0, image_size_px * 0.4)
        x += 70
        if x >= image_size_px:
            x -= 300
            break
        if y >= image_size_px * 0.4:
            y -= 300
        elif y <= image_size_px * 0.4:
            y += 300
        newpoints = (x, y)
        points.append(newpoints)
        line_xy = points
    smoothness_factor = 300

    for point1, point2 in zip(line_xy[:-1], line_xy[1:]):
        x_diff = point2[0] - point1[0]
        y_diff = point2[1] - point1[1]

        x_increment = x_diff / smoothness_factor
        y_increment = y_diff / smoothness_factor

        x_pos = point1[0]
        y_pos = point1[1]
        for _ in range(smoothness_factor):
            draw.ellipse(
                (x_pos, y_pos, x_pos + 80, y_pos + 80), fill=(255, 255, 255, 0)
            )
            x_pos += x_increment
            y_pos += y_increment

    image.save("front.png")

    return image


def create_grad(name: int):
    generate_art()
    filename = "front.png"
    filename1 = "back_smaller.jpg"
    frontImage = Image.open(filename)
    background = Image.open(filename1)
    frontImage = frontImage.convert("RGBA")
    background = background.convert("RGBA")
    width = (background.width - frontImage.width) // 2
    height = (background.height - frontImage.height) // 2
    background.paste(frontImage, (width, height), frontImage)
    background.save(f"pictures/{name}.png", format="png")


def make_multiples(amount: int):
    for k in range(0, amount):
        create_grad(k)


if __name__ == "__main__":
    make_multiples(int(input("How Many Copies Would You Like: ")))
