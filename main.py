from fpdf import FPDF
import pandas as pd

df=pd.read_csv("topics.csv")

pdf=FPDF(orientation="P",unit="mm",format="A4")
pdf.set_auto_page_break(auto=False,margin=0)
for i,j in df.iterrows():
    diff=20
    title=j["Topic"]

    pdf.add_page()
    pdf.set_font(family="Times",style="B",size=25)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0,h=25,txt=title,align="L",ln=1)
    pdf.line(10,30,200,30)
    pdf.ln(250)
    pdf.set_font(family="Times", style="B", size=10)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0,h=10,txt=title,align="R")

    for lines in range(30):
        diff+=10
        pdf.line(10,y1=diff,x2=200,y2=diff)

    for pages in range(j["Pages"]-1):
        diff=0
        pdf.add_page()
        pdf.ln(274)
        pdf.set_font(family="Times", style="B", size=10)
        pdf.set_text_color(180,180,180)
        pdf.cell(w=0,h=10,txt=title,align="R")
        for lines in range(30):
            diff += 10
            pdf.line(10, y1=diff, x2=200, y2=diff)


pdf.output("output.pdf")
