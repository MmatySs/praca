import config as cg


def step(motors):  # krok dla odpowiedniego state'a i silnika
    for i in reversed(range(2)):  # od 1 do 0
        motors["status"].write(i)
        cg.BOARD.pass_time(cg.T_SAMPL)


def movement(motors, pin):
    motors['direction'].write(pin)
    step(motors)


def pilot_buttons(motors, pin, dir):
    if cg.PILOT[dir].read() == 1:
        movement(motors, pin)


def remote_control():
    while run:
        pilot_buttons(cg.MOTOR_VERTICAL, 1, "back")  # tył
        pilot_buttons(cg.MOTOR_VERTICAL, 0, "forward")  # przód
        pilot_buttons(cg.MOTOR_HORIZONTAL, 1, "right")  # prawo
        pilot_buttons(cg.MOTOR_HORIZONTAL, 0, "left")

# def calibration():
#     while
# def kalibracja():
#     while wall_btn_przod.read() != 0:
#         przod_tył(0)
#     x_przod = 0
#     while wall_btn_tyl.read() != 0:
#         tyl()
#         x_tyl = x_przod + 1



