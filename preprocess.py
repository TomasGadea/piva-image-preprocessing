# -*- coding: utf-8 -*-

# system
import sys
import os
import argparse
# image processing
import matplotlib.pyplot as plt
from matplotlib import image
from PIL import Image


parser = argparse.ArgumentParser(description="image-convert")

parser.add_argument('--format', dest='fmt', type=str, metavar='format', required=True)  # BW, RGB, CMYK
parser.add_argument('--path', dest='p', type=str, metavar='path', required=True)
parser.add_argument('--filename', dest='fn', type=str, metavar='filename', required=False, default='output.jpg')
args = parser.parse_args()

path = args.p
filename = args.fn

if args.fmt == 'BW':
    format = 'L'
else:
    format = args.fmt

im = Image.open(path).convert(format)
im.save(filename)




