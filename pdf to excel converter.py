from tabula import read_pdf
from tabula import convert_into
import pandas as pd

pdf_file = "Some pdf file.pdf"
csv_file = "Some csv file.csv"
excel_file = "New excel file.xlsx"

convert_into(pdf_file, csv_file, output_format="csv", pages="all")

df = pd.read_csv(csv_file)
df.to_excel(excel_file, index=False)

print("complete!")