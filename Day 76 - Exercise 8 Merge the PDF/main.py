from pypdf import PdfWriter
import os

path = r"C:\Users\ASUS\OneDrive\Desktop\Python\Day 76 - Exercise 8 Merge the PDF\pdf"

files = os.listdir(path)

merger = PdfWriter()

for pdf in files:
    merger.append(pdf)

merger.write("out-basic1.pdf")