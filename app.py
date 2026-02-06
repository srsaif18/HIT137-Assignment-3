import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
from image_processing.processor import ImageProcessor
from utils.file_manager import FileManager
from gui.widgets import StatusBar


class ImageEditorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        #  Set window properties
        self.title("Group-Assignment-03 - Image Editor")
        self.geometry("1200x800")
        
        # Initialize image processor and file path
        self.processor = ImageProcessor()
        self.file_path = None
        
        # Undo/Redo stacks
        self.undo_stack = []
        self.redo_stack = []
        self.current_file = None

        self.create_menu()
        self.create_widgets()

    # Menu and widget creation methods
    def create_menu(self):
        menu = tk.Menu(self)
        file_menu = tk.Menu(menu, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_image)
        file_menu.add_command(label="Save", command=self.save_image)
        file_menu.add_command(label="Save As", command=self.save_as_image)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        edit_menu = tk.Menu(menu, tearoff=0)
        edit_menu.add_command(label="Undo", command=self.undo)
        edit_menu.add_command(label="Redo", command=self.redo)

        menu.add_cascade(label="Edit", menu=edit_menu)
        menu.add_cascade(label="File", menu=file_menu)
        self.config(menu=menu)

    def create_widgets(self):
        main = tk.Frame(self)
        main.pack(fill=tk.BOTH, expand=True)

        # SCROLLABLE CONTROL PANEL 
        container = tk.Frame(main)
        container.pack(side=tk.LEFT, fill=tk.Y)
        canvas = tk.Canvas(container, width=280, highlightthickness=0)
        canvas.pack(side=tk.LEFT, fill=tk.Y, expand=False)
        scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)

        # INNER FRAME
        panel = tk.Frame(
            canvas,
            padx=20,
            pady=20
        )

        # Add inner frame to canvas
        canvas.create_window((0, 0), window=panel, anchor="nw")

        # Auto-resize scroll region
        panel.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        # CONTROL PANEL CONTENT
        tk.Label(panel, text="Basic Image Effects", font=("Arial", 14, "bold")).pack(pady=20)
        tk.Button(panel, text="Open Image", command=self.open_image, height=2,font=("Arial", 12)).pack(fill=tk.X, pady=4)
        tk.Button(panel, text="Original Image", command=self.reset_image, height=2,font=("Arial", 12)).pack(fill=tk.X, pady=4)

        tk.Button(panel, text="Grayscale", command=self.apply_grayscale, height=2,font=("Arial", 12)).pack(fill=tk.X, pady=4)
        tk.Button(panel, text="Edge Detection", command=self.apply_edges, height=2,font=("Arial", 12)).pack(fill=tk.X, pady=4)

        tk.Button(panel, text="Rotate 90°", command=lambda: self.apply_rotate(90), height=2,font=("Arial", 12)).pack(fill=tk.X, pady=2)
        tk.Button(panel, text="Rotate 180°", command=lambda: self.apply_rotate(180), height=2,font=("Arial", 12)).pack(fill=tk.X, pady=2)
        tk.Button(panel, text="Rotate 270°", command=lambda: self.apply_rotate(270), height=2,font=("Arial", 12)).pack(fill=tk.X, pady=2)

        tk.Button(panel, text="Flip Horizontal", command=lambda: self.apply_flip(1), height=2,font=("Arial", 12)).pack(fill=tk.X, pady=2)
        tk.Button(panel, text="Flip Vertical", command=lambda: self.apply_flip(0), height=2,font=("Arial", 12)).pack(fill=tk.X, pady=2)

        # Blur Slider
        tk.Label(panel, text="Blur Intensity").pack(pady=(10, 0))
        self.blur_slider = tk.Scale(panel, from_=0, to=10, orient=tk.HORIZONTAL,command=self.apply_blur)
        self.blur_slider.pack(fill=tk.X)

        # Brightness Slider
        tk.Label(panel, text="Brightness").pack(pady=(10, 0))
        self.brightness_slider = tk.Scale(panel, from_=-100, to=100,
                                        orient=tk.HORIZONTAL,
                                        command=self.apply_brightness)
        self.brightness_slider.pack(fill=tk.X)

        # Contrast Slider
        tk.Label(panel, text="Contrast").pack(pady=(10, 0))
        self.contrast_slider = tk.Scale(panel, from_=1, to=3, resolution=0.1,orient=tk.HORIZONTAL,command=self.apply_contrast)
        self.contrast_slider.pack(fill=tk.X)

        # Resize Slider
        tk.Label(panel, text="Resize / Scale").pack(pady=(10, 0))
        self.resize_slider = tk.Scale(panel, from_=0.2, to=2.0,
                                    resolution=0.1,
                                    orient=tk.HORIZONTAL,
                                    command=self.apply_resize)
        self.resize_slider.set(1.0)
        self.resize_slider.pack(fill=tk.X)

        image_frame = tk.Frame(main, bg="#ddd")
        image_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.canvas = tk.Label(image_frame, bg="#ddd", text="Open an image and start with editing!", font=("Arial", 16), fg="#555")
        self.canvas.pack(expand=True)
        self.status = StatusBar(self)

    # Undo/Redo functionality
    def undo(self):
        if not self.undo_stack:
            return
        self.redo_stack.append(self.processor.image.copy())
        self.processor.image = self.undo_stack.pop()
        self.display_image(self.processor.image)
        self.status.update_status("Undo applied")

    def redo(self):
        if not self.redo_stack:
            return
        self.undo_stack.append(self.processor.image.copy())
        self.processor.image = self.redo_stack.pop()
        self.display_image(self.processor.image)
        self.status.update_status("Redo applied")

    # save current state before applying new effect
    def save_state(self):
        if self.processor.image is not None:
            self.undo_stack.append(self.processor.image.copy())
            self.redo_stack.clear()


    def save_image(self):
        path = FileManager.save_file()
        if path:
            cv2.imwrite(path, self.processor.image)
            messagebox.showinfo("Saved", "Image saved successfully")

    def display_image(self, image):
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(rgb)
        img = ImageTk.PhotoImage(img)
        self.canvas.configure(image=img)
        self.canvas.image = img


  # Check if an image is loaded before applying any processing
    def image_loaded(self):
     return self.processor.image is not None
    
  # applying effects with error handling
    def apply_grayscale(self):
        if not self.image_loaded():
            messagebox.showwarning("No Image", "No image loaded to apply grayscale.")
            return
        self.save_state()
        self.display_image(self.processor.grayscale())

    def apply_edges(self):
        if not self.image_loaded():
            messagebox.showwarning("No Image", "No image loaded to apply edge detection.")
            return  
        self.save_state()   
        self.display_image(self.processor.edge_detection())

    def apply_rotate(self, angle):
        if not self.image_loaded():
            messagebox.showwarning("No Image", "No image loaded to rotate.")
            return  
        self.save_state()
        self.display_image(self.processor.rotate(angle))

    def apply_flip(self, mode):
        if not self.image_loaded():
            messagebox.showwarning("No Image", "No image loaded to flip.")
            return
        self.save_state()   
        self.display_image(self.processor.flip(mode))

    
        if not self.image_loaded():
            messagebox.showwarning("No Image", "No image loaded to apply grayscale.")
            return
        self.save_state()   
        self.display_image(self.processor.grayscale())

   
        if not self.image_loaded():
            messagebox.showwarning("No Image", "No image loaded to apply edge detection.")
            return
        self.save_state()
        self.display_image(self.processor.edge_detection())

    def apply_blur(self, value):
        if not self.image_loaded():
            messagebox.showwarning("No Image", "No image loaded to apply blur.")
            return
        self.save_state()
        self.display_image(self.processor.blur(int(value)))

    def apply_brightness(self, value):
        if not self.image_loaded():
            messagebox.showwarning("No Image", "No image loaded to adjust brightness.")
            return
        self.save_state()
        self.display_image(self.processor.adjust_brightness(int(value)))

    def apply_contrast(self, value):
        if not self.image_loaded():
            messagebox.showwarning("No Image", "No image loaded to adjust contrast.")
            return
        self.save_state()            
        self.display_image(self.processor.adjust_contrast(float(value)))

    def apply_flip(self, mode):
        if not self.image_loaded():
            messagebox.showwarning("No Image", "No image loaded to flip.")
            return
        self.save_state()
        self.display_image(self.processor.flip(mode))


    def apply_resize(self, value):
        if not self.image_loaded():
            messagebox.showwarning("No Image", "No image loaded to resize.")
            return
        self.save_state()
        self.display_image(self.processor.resize(float(value)))
   
    # Helper methods   
    def open_image(self):
        path = FileManager.open_file()
        if path:
            image = self.processor.load_image(path)
            self.file_path = path
            self.display_image(image)
            self.status.update_status(f"Loaded: {path}")
    # Reset image method with error handling
    def reset_image(self):
        if not self.image_loaded():
            messagebox.showwarning("No Image", "No image loaded to reset.")
            return
        if self.processor.original is not None:
            self.display_image(self.processor.reset())
            
  
    def save_image(self):
        if self.processor.image is None:
            messagebox.showwarning("No Image", "No image to save.")
            return

        if self.current_file:
            cv2.imwrite(self.current_file, self.processor.image)
            messagebox.showinfo("Saved", "Image saved successfully.")
        else:
            self.save_as_image()


    def save_as_image(self):
        if self.processor.image is None:
            messagebox.showwarning("No Image", "No image to save.")
            return

        path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG", "*.png"), ("JPG", "*.jpg"), ("BMP", "*.bmp")]
        )

        if path:
            cv2.imwrite(path, self.processor.image)
            self.current_file = path
            messagebox.showinfo("Saved", "Image saved successfully.")
