from PIL import Image

class List:
    """
    """
    def __init__(self, height, length):
        self.height = height
        self.length = length

        #Reads file
        fixed = []
        with open('elevation_small.txt', 'r') as elevations:
            for line in elevations:
                x = line.split()
                fixed.append(x)

        #Changes nested list into flat list
        heights_list = [[int(num) for num in row] for row in fixed]
        flattened_list = [num for item in heights_list for num in item]

        #Finds max and min elevations
        min_elevation = (max(flattened_list))
        max_elevation = (min(flattened_list))




        #Converts nested list into RGB values
        def elevations_to_colors(number):
            min_elevation = 3139
            max_elevation = 5648

            rgb_code = [[round(int(y) - min_elevation) / (max_elevation - min_elevation) * 255 for y in x] for x in number]
            return [[round(i) for i in rgb_code] for rgb_code in rgb_code]
        
        #print(elevations_to_colors(heights_list))
        
        
        
        def image(list):
        list = rgb_code
        plot = Image.new("RGB", (600, 600))
        for y, row in enumerate(rgb_code):
            for x, value, in enumerate(row):
                plot.putpixel((x, y), (value, value, value))
        plot.save('plotmap.png')
        plot.show('plotmap.png')

    