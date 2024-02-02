import os
import platform
from .sources import *

if platform.system() == "Windows":
    os.system("color FF")

def __movie_cat_providers__():
    print(vidsrcto.__metadata__)
    
    vidsrcto.__metadata__["_class"](
        arg_1 = "Argument #1",
        arg_2 = "Argument #2",
        arg_3 = "Argument #3",
    )

if __name__ == "__main__":
    __movie_cat_providers__()