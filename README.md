Prototype 2x2 macro keypad.

- Hardware: Raspberry Pi Pico and a hand-wired 2x2 button matrix
- Software: [CircuitPython | https://circuitpython.org/] and [KMK firmware|https://github.com/KMKfw/kmk_firmware]

Config is trivial:
| Button | KeyCode |
|--------|---------|
| White  |  F21    |
| Red    | F22     |
| Blue   | F23     |
| Green  | F24     |

By default, Pico does not mount /Volumes/CIRCUITPY.  Press GP15 button (upper left  on Pico) while resetting to mount CIRCUITPY volume to change the program.

![PetePad01](https://github.com/user-attachments/assets/d70685b7-c837-4565-9097-773da3b17031)
