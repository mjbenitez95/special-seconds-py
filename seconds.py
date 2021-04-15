#!/usr/bin/env python
#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
from decimal import *
import time

SPECIAL_TIME = 1579136400

class Seconds(SampleBase):
    def __init__(self, *args, **kwargs):
        super(Seconds, self).__init__(*args, **kwargs)

    def run(self):
        canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../../../fonts/6x12.bdf")
        textColor = graphics.Color(0, 89, 100)
        pos = 2

        while True:
            canvas.Clear()
            seconds_diff = int(time.time()) - int(SPECIAL_TIME)
            days_diff = (Decimal(seconds_diff)/Decimal(86400))
            years_diff = (Decimal(seconds_diff)/Decimal(31536000))

            seconds_text = str(seconds_diff) + " s"
            days_text = str(days_diff.quantize(Decimal('0.1'), rounding=ROUND_DOWN)) + " days"
            years_text = str(years_diff.quantize(Decimal('.0001'), rounding=ROUND_DOWN)) + " yrs"
            
            seconds_line = graphics.DrawText(canvas, font, pos, 10, textColor, seconds_text)
            days_line = graphics.DrawText(canvas, font, pos, 19, textColor, days_text)
            years_line = graphics.DrawText(canvas, font, pos, 28, textColor, years_text)

            time.sleep(0.1)
            canvas = self.matrix.SwapOnVSync(canvas)


# Main function
if __name__ == "__main__":
    run_text = Seconds()
    if (not run_text.process()):
        run_text.print_help()
