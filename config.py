from pyfirmata import Arduino

BOARD = Arduino("com3")
T_SAMPL = 0.005

MOTOR_VERTICAL = {
    "status": BOARD.digital[2],
    "direction": BOARD.digital[3],
    "front_sensor": BOARD.get_pin("d:4:i"),
    "back_sensor": BOARD.get_pin("d:11:i"),
}
MOTOR_HORIZONTAL = {
    "status": BOARD.digital[5],
    "direction": BOARD.digital[10],
    "left_sensor": BOARD.get_pin("d:12:i"),
    "right_sensor": BOARD.get_pin("d:13:i"),
}
PILOT = {
    "forward": BOARD.get_pin("d:6:i"),
    "back": BOARD.get_pin("d:7:i"),
    "right": BOARD.get_pin("d:8:i"),
    "left": BOARD.get_pin("d:9:i"),
}
