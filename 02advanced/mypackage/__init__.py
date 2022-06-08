from pyfiglet import FigletFont
from pyfiglet import Figlet
from rich import print


def Print():
    print(FigletFont().getFonts()) # 获取到所有的字体
    f = Figlet(font="slant", width=300)  # 字体和宽度，可以为空即默认
    print(f.renderText("TEST"))
"""
  _______________________
 /_  __/ ____/ ___/_  __/
  / / / __/  \__ \ / /
 / / / /___ ___/ // /
/_/ /_____//____//_/
 
"""

def Print2():
    test=r'''
 ▄▀▀▀█▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▀▀▄  ▄▀▀▀█▀▀▄ 
█    █  ▐ ▐  ▄▀   ▐ █ █   ▐ █    █  ▐ 
▐   █       █▄▄▄▄▄     ▀▄   ▐   █     
   █        █    ▌  ▀▄   █     █      
 ▄▀        ▄▀▄▄▄▄    █▀▀▀    ▄▀       
█          █    ▐    ▐      █         
▐          ▐                ▐         
'''
    print(f'[green]{test}[green/]')



if __name__ == '__main__':
    Print()
    Print2()

