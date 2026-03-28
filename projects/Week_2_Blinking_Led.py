import time
import gpiod
from gpiod.line import Direction, Value

LINE = 17
CHIP = "/dev/gpiochip0"

request = gpiod.request_lines(
    CHIP,
    consumer="python-blink",
    config={
        LINE: gpiod.LineSettings(direction=Direction.OUTPUT)
    },
    output_values={
        LINE: Value.INACTIVE
    },
)

try:
    while True:
        request.set_value(LINE, Value.ACTIVE)
        time.sleep(0.5)
        request.set_value(LINE, Value.INACTIVE)
        time.sleep(0.5)
except KeyboardInterrupt:
    pass
finally:
    request.release()