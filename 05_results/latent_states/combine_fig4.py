"""Usage: python combine_fig4.py Figures_and_scripts.zip (requires pypdf)."""
from pathlib import Path
import io, sys, zipfile
from pypdf import PdfReader, PdfWriter, Transformation

out=Path(__file__).resolve().parent
with zipfile.ZipFile(sys.argv[1]) as src:
    original=PdfReader(io.BytesIO(src.read('fig/Fig4_identifiability.pdf'))).pages[0]
panel=PdfReader(str(out/'Fig4c-Synthetic-recovery.pdf')).pages[0]
width=190*72/25.4
def dims(pg):
    b=pg.cropbox
    return width/float(b.width), float(b.height)*width/float(b.width)
sa,ha=dims(original); sc,hc=dims(panel)
w=PdfWriter(); full=w.add_blank_page(width, ha+hc+4)
for pg,scale,dy in [(original,sa,hc+4),(panel,sc,0)]:
    b=pg.cropbox
    full.merge_transformed_page(pg,Transformation().translate(-float(b.left),-float(b.bottom)).scale(scale).translate(0,dy))
with (out/'Fig4-Complete.pdf').open('wb') as f: w.write(f)
