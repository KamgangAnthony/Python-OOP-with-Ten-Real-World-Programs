from canvas import Canvas
from shape import Shape


def input_int(msg):
    while True:
        try:
            our_int_input = int(input(msg))
        except:
            # print("Invalid value!")
            continue
        if our_int_input < 0:
            # print("Negative value!")
            continue
        else:
            return our_int_input


def input_canvas_color(msg):
    while True:
        try:
            our_input = input(msg)
        except:
            continue

        while our_input.lower() != "black" and our_input.lower() != "white":
            print("Invalid canvas color. Please enter \"white\" or \"black\"")
            our_input = input("Enter canvas color (white or black): ")
        return our_input


user_width = input_int("Enter canvas width: ")
user_height = input_int("Enter canvas height: ")
canvas_color = input_canvas_color("Enter canvas color (white or black): ")

our_canvas = Canvas(user_width, user_height, canvas_color)


while True:
    shape = input("What do you like to draw (rectangle or square) ? Enter quit to quit. ")
    shape = shape.lower()

    if shape == "quit":
        break

    if shape != "rectangle" and shape != "square":
        # print("Invalid shape.")
        continue

    x_of_shape = input_int(f"Enter x of the {shape}: ")
    y_of_shape = input_int(f"Enter y of the {shape}: ")
    width_of_shape = input_int(f"Enter the width of the {shape}: ")
    height_of_shape = input_int(f"Enter the height of the {shape}: ")
    red_in_shape = input_int(f"How much red should the {shape} have? ")
    green_in_shape = input_int(f"How much green should the {shape} have? ")
    blue_in_shape = input_int(f"How much blue should the {shape} have? ")

    our_starting_coordinates = (x_of_shape, y_of_shape)
    our_colors = (red_in_shape, green_in_shape, blue_in_shape)
    our_shape = Shape(shape, our_starting_coordinates, width_of_shape, height_of_shape, our_colors)
    canvas_data = our_shape.add_shape_info_to_data(our_canvas.data)

our_canvas.export_the_image(our_canvas.data)

# image_exporter = ImageDrawer(canvas_data)
# image_exporter.export_the_image()

# our_canvas = Canvas(123, 250, "white")
# canvas_data = our_canvas.send_data()
#
# our_starting_coordinates = StartingCoordinates(40, 20)
# our_colors = ColorRGB(100, 220, 50)
# our_shape = Shape("square", our_starting_coordinates, 50, 50, our_colors)
# canvas_data = our_shape.add_shape_info_to_data(canvas_data)
#
# our_starting_coordinates = StartingCoordinates(20, 40)
# our_colors = ColorRGB(0, 220, 0)
# our_shape = Shape("rectangle", our_starting_coordinates, 80, 95, our_colors)
# canvas_data = our_shape.add_shape_info_to_data(canvas_data)

# while True:
#     try:
#         user_width = int(input("Enter canvas width: "))
#         user_height = int(input("Enter canvas height: "))
#     except:
#         print("Enter valid values < 0: ")
#         continue
#     if user_width < 0 or user_height < 0:
#         print("Enter valid values < 0: ")
#         continue
#     else:
#         break
