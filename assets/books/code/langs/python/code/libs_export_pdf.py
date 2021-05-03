# libs_export_pdf.py



Creating PDF documents
Inserting images
Inserting text and numbers
Visualizing data

pip install FPDF
import numpy as np
import pandas as pd
from fpdf import FPDF
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
pdf = FPDF(orientation = 'P', unit = 'mm', format = 'A4')
pdf.add_page()
pdf.set_font('helvetica', 'bold', 10)
pdf.set_text_color(255, 255, 255)

pdf.image('C:/Users/.../image.png', x = 0, y = 0, w = 210, h = 297)

pdf.text(x, y, txt)

pdf.set_xy(x, y)
pdf.cell(w, h, txt, border, align, fill) 

pdf.output('Automated PDF Report.pdf')

https://towardsdatascience.com/how-to-generate-automated-pdf-documents-with-python-4f3bcb6033e6