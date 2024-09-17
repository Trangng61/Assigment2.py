import sys
from CustomCanvas import CustomCanvas
from Rectangle import Rectangle
import Pack


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file>")
        return
    input_file = sys.argv[1]

    # Read input file
    with open(input_file, 'r') as f:
        lines = f.readlines()

    canvas_height, canvas_width = map(int, lines[0].split(','))
    canvas = CustomCanvas(canvas_height, canvas_width)
    # Read rectangles
    rectangles = []

    for line in lines[1:]:
        height, width = map(int, line.split(','))
        rectangles.append(Rectangle(height, width))

    packed_rectangles = Pack.pack(rectangles, (canvas_height, canvas_width))
    for rect in packed_rectangles:
        canvas.draw_rectangle(rect)

    canvas.display()


if __name__ == '__main__':
    main()
