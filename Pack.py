from rectpack import newPacker
from Rectangle import Rectangle


def pack(allRect, canvasSize):
    packer = newPacker()

    for rect in allRect:
        packer.add_rect(rect.width, rect.height)

    packer.add_bin(canvasSize[1], canvasSize[0])

    packer.pack()

    packed_rectangles = []
    for abin in packer:
        for rect in abin:
            x, y, w, h = rect.x, rect.y, rect.width, rect.height
            packed_rectangles.append(Rectangle(h, w, x, y))

    return packed_rectangles
