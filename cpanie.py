import serial
from time import sleep
from tkinter import *
import config as cg
import functions as f
from pyfirmata import Arduino, util, INPUT, OUTPUT
import pyfirmata
import tkinter as tk
import threading


# direction_2.mode = pyfirmata.OUTPUT
# btn_przod.mode = pyfirmata.INPUT
run = True


def close_app(window):
    global run
    run = False
    window.quit()


def remote_control():
    while run:
        f.pilot_buttons(cg.MOTOR_VERTICAL, 1, "back")  # tył
        f.pilot_buttons(cg.MOTOR_VERTICAL, 0, "forward")  # przód
        f.pilot_buttons(cg.MOTOR_HORIZONTAL, 1, "right")  # prawo
        f.pilot_buttons(cg.MOTOR_HORIZONTAL, 0, "left")


def main():
    it = pyfirmata.util.Iterator(cg.BOARD)
    it.start()

    t1 = threading.Thread(target=remote_control)
    window = tk.Tk()
    t1.start()

    window.configure(background="gray")
    window.geometry("500x500")
    window.title("GUI")

    gui_przod = tk.Button(
        window, text="przod", command=lambda: f.movement(cg.MOTOR_VERTICAL, 0)
    )
    gui_przod.grid(row=0, column=0)

    gui_tyl = tk.Button(
        window, text="tyl", command=lambda: f.movement(cg.MOTOR_VERTICAL, 1)
    )
    gui_tyl.grid(row=1, column=0)

    gui_prawo = tk.Button(
        window, text="prawo", command=lambda: f.movement(cg.MOTOR_HORIZONTAL, 1)
    )
    gui_prawo.grid(row=2, column=0)

    gui_lewo = tk.Button(
        window, text="lewo", command=lambda: f.movement(cg.MOTOR_HORIZONTAL, 0)
    )
    gui_lewo.grid(row=3, column=0)

    quit_btn = tk.Button(window, text="quit", command=lambda: close_app(window))
    quit_btn.grid(row=4, column=0)

    window.mainloop()


if __name__ == "__main__":
    main()

# gui_kalibracja = tk.Button(window, text="kalibracja", command=kalibracja)
# gui_kalibracja.grid(row=4, column=0)
