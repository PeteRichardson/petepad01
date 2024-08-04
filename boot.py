import board
import digitalio

#import supervisor
#supervisor.set_usb_device_descriptor("peterichardson.com","PetePad01")

# If not pressed, the key will be at +V (due to the pull-up).
# https://learn.adafruit.com/customizing-usb-devices-in-circuitpython/circuitpy-midi-serial#circuitpy-mass-storage-device-3096583-4
button = digitalio.DigitalInOut(board.GP12)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# Disable devices only if button is not pressed.
if button.value:
    import storage
    storage.disable_usb_drive()
