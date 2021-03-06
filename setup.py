import os
from distutils.core import setup
import sys


setup(
    name = "plot_templates",
    version = "0.0.1",
    author = "Kilean Hwang",
    author_email = "kilean@lbl.gov",
    description = ("Templates for plot using seaborn, matplotlib and etc"),
    license = "Lawrence Berkeley National Laboratory",
    url = "",
    packages=['plot_templates'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Topic :: Utilities",
        "License :: Free for non-commercial use",
    ],
    zip_safe=False
)
