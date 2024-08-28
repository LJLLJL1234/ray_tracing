from src.ray_color import RayColor

class Canvas:
    def __init__(self, width, height, ppm_split=70):
        self.width = width
        self.height = height
        self.default_color = RayColor(0,0,0)
        self.grid = [[self.default_color for _ in range(width)] for _ in range(height)]
        self.ppm_split = ppm_split

    def write_pixel(self, x, y, color):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = color
        else: 
            raise IndexError("Canvas coordinates out of range")
        
    def get_pixel(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]
        else:
            raise IndexError("Canvas coordinates out of range")
        
    def canvas_to_ppm(self):
        header = f"P3\n{self.width} {self.height}\n255"
        body = self._get_ppm_body()
        return "\n".join([header, body])
    
    def _get_ppm_body(self):
        ppm_array = []
        for y in range(self.height):
            for x in range(self.width):
                pixel_scaled_colors = self.grid[y][x].get_scaled_colors()
                ppm_array.extend(str(c) for c in pixel_scaled_colors)
        ppm_rows = []
        temp_row = ""
        for i in range(len(ppm_array)):
            color_to_be_added = str(ppm_array[i])
            if len(temp_row) + len(color_to_be_added + " ") <= self.ppm_split:
                # add the next color string to the current row if the result is shorter or equal to the ppm split
                temp_row = temp_row + color_to_be_added + " "
            else:
                # the row is ready, add it to the ppm_rows array and start a new temp row
                ppm_rows.append(temp_row.rstrip())
                temp_row = color_to_be_added + " "
        ppm_rows.append(temp_row.rstrip()) 
        
        return "\n".join(ppm_rows)
    
    def save_ppm_file(self):
        ppm_string = self.canvas_to_ppm()
        output_path = "/Users/Lauri.Lehtola/private_projects/ray_tracing/output/test_file.ppm"

        with open(output_path, 'w') as file:
            file.write(ppm_string)



