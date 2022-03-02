from PIL import Image, ImageDraw

import random, math, colorsys

def random_color():

    # I want a bright, vivid color, so max V and S and only randomize HUE.
    h = random.random()
    s = 1
    v = 1
    float_rbg = colorsys.hsv_to_rgb(h, s, v)

    # Return as integer RGB.
    return (
        int(float_rbg[0] * 255),
        int(float_rbg[1] * 255),
        int(float_rbg[2] * 255),
    ) 

def generate_art():
    print('Generate Art')
    image_size_px = 2000
    image_bg_color = (255,255,255)
    image = Image.new(
        "RGB",
        size=(image_size_px, image_size_px),
        color = image_bg_color
    )

    draw = ImageDraw.Draw(image)
    points = []
    starting_pos = (0,image_size_px*.50),(image_size_px,image_size_px*.50)
    x = 0
    y = image_size_px*.50
    for _ in range(0, math.ceil(10)):
        x += 200
        y += (100-random.randint(0, image_size_px*0.4))
        if y >= image_size_px*0.4: 
            y -=300
        elif y <= image_size_px*0.4:
            y += 300
        newpoints = (x, y)
        points.append(newpoints)

        y -= (100-random.randint(0, image_size_px*0.4))
        x += 200
        newpoints = (x, y)
        points.append(newpoints)
        line_xy= (points)
        point_old = line_xy[0]
        for i in range(1, len(line_xy)):
            line_color = random_color()
            draw.line((line_xy[i], line_xy[i-1]), fill=random_color(), width= 100, joint='curve')

    image.save('test_image.png')

if __name__ == "__main__":
    generate_art()