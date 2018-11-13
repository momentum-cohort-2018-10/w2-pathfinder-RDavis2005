from PIL import Image

#Reads file
fixed = []
with open('elevation_small.txt', 'r') as elevations:
    for line in elevations:
        x = line.split()
        fixed.append(x)

#Changes list of strings into list of integers
heights_list = [[int(num) for num in row] for row in fixed]

#Changes nested list of integers into flat list of integers
flattened_list = [num for item in heights_list for num in item]

#Finds min elevation
def find_min(flattened_list):
    """
    """
    min_elevation = (max(flattened_list))
    return min_elevation

#Finds max elevation 
def find_max(flattened_list):
    """
    """
    max_elevation = (min(flattened_list))
    return max_elevation

#Converts nested list into RGB values
def elevations_to_colors(number):
    """
    """
    min_elevation = 3139
    max_elevation = 5648

    rgb_code = [[round(int(y) - min_elevation) / (max_elevation - min_elevation) * 255 for y in x] for x in number]
    return [[round(i) for i in rgb_code] for rgb_code in rgb_code]

#print(elevations_to_colors(heights_list)) #Test print RGB converted elevations
value = elevations_to_colors(heights_list)

plot = Image.new("RGB", (600, 600))
for y, row in enumerate(value):
    for x, value, in enumerate(row):
        plot.putpixel((x, y), (value, value, value))
        plot.putpixel((x, 340), (value, 255, value)) #Tests plotting straight line from 0,340 coordinate
plot.save('plotmap.png')
plot.show('plotmap.png')

def plot_path(number):
    pass

#if value to right is equal to current_value, putpixel
#if value to right (+1 y or -1 y) is closest to current_value, putpixel