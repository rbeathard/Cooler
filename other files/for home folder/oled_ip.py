# For use with I2C OLED screens. 
# This requires the Adafruit Circuit Python OLED library, which superceeds earlier Adafruit OLED libraries
# Install it with `pip install adafruit-circuitpython-ssd1306`

import time
from subprocess import check_output

from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

def get_ip():
    cmd = "hostname -I | cut -d\' \' -f1"
    return check_output(cmd, shell=True).decode("utf-8").strip()


# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# Clear display.
disp.fill(0)
disp.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new("1", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Load default font.
font = ImageFont.load_default()

no_IP = True

draw.text((x, top + 0), "Initializing WiFi", font=font, fill=255)
disp.image(image)
disp.show()
time.sleep(5)
while no_IP:
    # Clear display.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    disp.fill(0)
    disp.show()
    ip_addr = get_ip()
    if ip_addr:
        draw.text((x, top + 0), "IP: " + ip_addr, font=font, fill=255)
        draw.text((x, 12), "    /earthrover", font=font, fill=255)

        no_IP = False
    else:
        draw.text((x, top + 0), "Searching for WiFi", font=font, fill=255)
    disp.image(image)
    disp.show()
    time.sleep(5)
