#!/usr/bin/env python3
from PIL import Image

gambar = Image.open("1.webp").convert("RGB")
gambar.save("1.png", "png")