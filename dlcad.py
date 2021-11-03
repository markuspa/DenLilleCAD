import tkinter as tk
import lib.dlcadcore

APP_NAME = "DenLilleCAD"
APP_VERSION = "0.1"

try:
    app = tk.Tk()
except:
    import os
    os.system('xrdb -load /dev/null')
    os.system('xrdb -query')
    app = tk.Tk()

app.title(APP_NAME + ' ' + APP_VERSION) # - filename.dlc
app.minsize(400,300)

app.columnconfigure(0, weight=1)
app.rowconfigure(0, weight=1)

statusbar = tk.Frame(app)
statusbar.grid(column=0, row=1, sticky='we')
stat_coords_text = tk.StringVar()
stat_coords = tk.Label(statusbar, textvariable=stat_coords_text, \
        bd=1, relief=tk.SUNKEN, anchor='sw', width=20)
stat_snap = tk.Label(statusbar, \
        text="SNAP", bd=1, relief=tk.RAISED, anchor='sw')
stat_ortho = tk.Label(statusbar, \
        text="ORTHO", bd=1, relief=tk.RAISED, anchor='sw')

stat_coords.grid(column=0, row=0, sticky='w')
stat_snap.grid(column=1, row=0, sticky='w')
stat_ortho.grid(column=2, row=0, sticky='w')

canvas = tk.Canvas(app, background='gray98', cursor='tcross')
canvas.grid(column=0, row=0, sticky='nwes')




cad = lib.dlcadcore.Dlcadcore(canvas)


cad.test()
cad.line(0,0,10,0)





app.mainloop()

