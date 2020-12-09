## PDF file to Audio mp3 file
#
 
## Import stuff
#
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from gtts import gTTS
import pdfplumber

## Create window
#
root = tk.Tk()
root.minsize(width = 300, height = 420)
root.maxsize(width = 300, height = 420)

canvas1 = tk.Canvas(root, width = 300, height = 420, bg = 'azure3', relief = 'raised')
canvas1.pack()

## Create heading or title
#

label1 = tk.Label(root, text = "PDF Audio Store", bg = 'azure3')
label1.config(font = ('helvetica', 16))
canvas1.create_window(150, 20, window = label1)

final = ""

## Get PDF file
# 
def get_pdf():
    global final
    global pdf_checker

    try:
        import_file_path = filedialog.askopenfilename()

        if(str(import_file_path).endswith(".pdf")):
            pdf = pdfplumber.open(import_file_path)
            pdf_checker = pdf

            n = len(pdf.pages)

            for page in range(n):
                data = pdf.pages[page].extract_text()
                final = final + "\n" + data
            
            messagebox.showinfo("Information", "PDF is imported")
        else:
            raise Exception("Provide .pdf file only")
    
    except Exception as e:
        messagebox.showerror("Error", "{}".format(e))
    
    else:
        print("Continue to conversion")

brows_pdf = tk.Button(text = "PDF entry", command = get_pdf, bg = 'royalblue', fg = "white", font = ('helvetica', 12, 'bold'),
                      border = 0,
                      activebackground = "green")

canvas1.create_window(150, 60, window = brows_pdf)


## Conversion store
#

def convert_audio():
    global final
    global pdf_checker

    try:
        print("File Information")
        print(pdf_checker)
        export_file_path = filedialog.asksaveasfilename(defaultextension = ".mp3")
        final_file = gTTS(text = final, lang = "en")
        final_file.save(export_file_path)
    
        messagebox.showinfo("Information", "Audio file generated")
    except NameError:
        messagebox.showwarning("Warning", "Import PDF first")
    

audio_button = tk.Button(text = "Convert to Audio", command = convert_audio, bg = 'royalblue', fg = "white", font = ('helvetica', 12, 'bold'),
                      border = 0,
                      activebackground = "green")
canvas1.create_window(150, 100, window = audio_button)

root.mainloop()


## End






