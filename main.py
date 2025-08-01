from fpdf import FPDF
import pandas as pd

df=pd.read_csv("topics.csv")

pdf=FPDF(orientation="P",unit="mm",format="A4")
for i,j in df.iterrows():
    title=j["Topic"]

    pdf.add_page()
    pdf.set_font(family="Times",style="B",size=25)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0,h=25,txt=title,align="L",ln=1)
    pdf.line(10,30,200,30)
    for pages in range(j["Pages"]-1):
        pdf.add_page()

pdf.output("output.pdf")
