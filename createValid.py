from PIL import Image, ImageDraw

# Create a 512x512 transparent image
img = Image.new("RGBA", (512, 512), (0, 0, 0, 0))

# Draw a solid circle in the center
draw = ImageDraw.Draw(img)
circle_center = (256, 256)
circle_radius = 10
draw.ellipse(
   (0, 0, 512, 512),
    fill = (230, 216, 230, 255)
)


# Draw a slightly non-transparent pixel outside the circle


# Save the image to a file
img.save("violation4.png")

# Display the image
img.show()
