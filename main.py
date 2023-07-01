import tkinter as tk

class PixelArtPaint:
    def __init__(self, root, width, height, pixel_size, default_color):
        self.root = root
        self.root.title("Pixel Art Paint")

        self.canvas = tk.Canvas(self.root, width=width*pixel_size, height=height*pixel_size, bg="white")
        self.canvas.pack()

        self.pixel_size = pixel_size
        self.default_color = default_color

        self.canvas.bind("<Button-1>", self.on_pixel_click)

        self.create_pixels(width, height)

    def create_pixels(self, width, height):
        self.pixels = []
        for row in range(height):
            pixel_row = []
            for col in range(width):
                x0 = col * self.pixel_size
                y0 = row * self.pixel_size
                x1 = x0 + self.pixel_size
                y1 = y0 + self.pixel_size
                pixel = self.canvas.create_rectangle(x0, y0, x1, y1, fill=self.default_color, outline="")
                pixel_row.append(pixel)
            self.pixels.append(pixel_row)

    def on_pixel_click(self, event):
        x = event.x
        y = event.y
        col = x // self.pixel_size
        row = y // self.pixel_size
        pixel = self.pixels[row][col]
        self.canvas.itemconfigure(pixel, fill=self.default_color)

    def run(self):
        self.root.mainloop()

# Example usage:
if __name__ == '__main__':
    root = tk.Tk()
    pixel_art = PixelArtPaint(root, width=20, height=20, pixel_size=20, default_color="black")
    pixel_art.run()
