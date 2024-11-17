from screeninfo import get_monitors

# Get the primary monitor
monitor = get_monitors()[0]

# Get the width and height
width = monitor.width
height = monitor.height

# Calculate the total number of pixels (width * height)
total_pixels = width * height

# Print the results
print(f"Screen resolution: {width}x{height}")
print(f"Total number of pixels: {total_pixels}")
