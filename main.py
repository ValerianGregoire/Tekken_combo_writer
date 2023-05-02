import tkinter as tk
from app import render

win = tk.Tk()
win.title("Tekken 7 - Combo Writer")
win.iconbitmap('./assets/icon.ico')
win.resizable(True,False)
win.geometry('444x169+250+130')

tk.Label(win, text = "Type a combo to render").pack(fill = 'x')


# Combo input
combo = tk.StringVar()
comboEntry = tk.Entry(win, textvariable = combo)
comboEntry.pack(fill = 'x', pady = 10)


# Render and save options
checkbox_frame = tk.Frame(win)
checkbox_frame.pack(pady = 10)

render_checkvar = tk.BooleanVar(value = True)
checkbox_render = tk.Checkbutton(checkbox_frame,
                                 text = 'Render',
                                 onvalue = True,
                                 offvalue = False,
                                 variable = render_checkvar)
checkbox_render.pack(side = 'left')

save_checkvar = tk.BooleanVar(value = True)
checkbox_save = tk.Checkbutton(checkbox_frame,
                              text = 'Save Render',
                              onvalue = True,
                              offvalue = False,
                              variable = save_checkvar)
checkbox_save.pack(side = 'left')

text_checkvar = tk.BooleanVar(value = True)
checkbox_text = tk.Checkbutton(checkbox_frame,
                                 text = 'Display Text',
                                 onvalue = True,
                                 offvalue = False,
                                 variable = text_checkvar)
checkbox_text.pack(side = 'left')

bottom_frame = tk.Frame(win)
bottom_frame.pack(fill = 'x', pady = 20)



def run():
    render(combo.get(),
           display = render_checkvar.get(),
           save = save_checkvar.get(),
           text = text_checkvar.get())

download_button = tk.Button(bottom_frame, text = 'Print', command = run)
download_button.pack(side = 'right', padx = 30)

tk.Label(bottom_frame,
         text = 'Example: df2 df2 u333+4 fF33 124').pack(side = 'right',
                                                          padx = 30,
                                                          anchor = 'w')

win.mainloop()
