import sys
from pyfiglet import Figlet
import random

fonts = Figlet().getFonts() #获取字体列表
if len(sys.argv) == 1:
    ft = random.choice(fonts)
elif len(sys.argv) == 3:
    if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
        ft = sys.argv[2]
else:
    sys.exit("Invalid usage")

text = input("Input: ")
print("Output:\n", Figlet(font = ft).renderText(text))