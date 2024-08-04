from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
import board
print("Starting")


keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP18, board.GP19)
keyboard.row_pins = (board.GP16, board.GP17)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.F21, KC.F22, KC.F23, KC.F24]
]

if __name__ == '__main__':
    keyboard.go()