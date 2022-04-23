from tkinter import Tk, Button, Label, Text
import qrcode
from PIL import ImageTk, Image
import base64
from io import BytesIO


class QRGenerator(Tk):
    def __init__(self):
        super().__init__()
        self.configure(background='#1f1f1f')
        self.title('QR code generator')
        self.initialize()
        self.generate_qr('https://github.com/SaraFarron/qr-codes')

    def generate_qr(self, data: str):
        img = qrcode.make(data)
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue())
        qr_code = Image.open(BytesIO(base64.b64decode(img_str)))
        qr_code = ImageTk.PhotoImage(qr_code)
        label = Label(image=qr_code, bg='#1f1f1f')
        label.grid(column=1, row=0, padx=10, pady=10, sticky='NESW')

    def initialize(self):
        self.grid()
        text_box = Text(height=12, width=12, bg='#3d3d3d', fg='#c9c9c9', font=("Helvetica", 14))
        text_box.grid(column=0, row=0, padx=10, pady=10, sticky='NESW')

        # Use CTkButton instead of tkinter Button
        button = Button(text="Generate QR code",
                        command=lambda: self.generate_qr(text_box.get(1.0, 'end')),
                        fg='#cccccc', bg='#3d3d3d')
        button.grid(column=0, row=1, padx=10, pady=10)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=2)


if __name__ == '__main__':
    app = QRGenerator()
    app.mainloop()
