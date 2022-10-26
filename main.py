# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
# SPDX-License-Identifier: MIT
"""CircuitPython I2C Device Address Scan"""
import time
import board

# To use default I2C bus (most boards)
i2c = board.I2C()

# To use the STEMMA QT connector (most boards)
# i2c = board.STEMMA_I2C()

# To create I2C bus on specific pins
# import busio
i2c = busio.I2C(board.GP1, board.GP0);

while not i2c.try_lock():
    pass

try:
    while True:
        print(
            "I2C addresses found:",
            [hex(device_address) for device_address in i2c.scan()],
        )
        time.sleep(2)

finally:  # unlock the i2c bus when ctrl-c'ing out of the loop
    i2c.unlock()
