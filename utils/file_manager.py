from tkinter import filedialog


class FileManager:
    @staticmethod
    def open_file():
        return filedialog.askopenfilename(
            title="Open Image",
            filetypes=[
                ("Image Files", "*.png *.jpg *.jpeg *.bmp"),
                ("All Files", "*.*")
            ]
        )

    @staticmethod
    def save_file():
        return filedialog.asksaveasfilename(
            title="Save Image As",
            defaultextension=".png",
            filetypes=[
                ("PNG Image", "*.png"),
                ("JPEG Image", "*.jpg"),
                ("Bitmap Image", "*.bmp")
            ]
        )
