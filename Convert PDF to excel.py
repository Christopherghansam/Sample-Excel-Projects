import pandas as pd
import PyPDF2
import openpyxl

# open the PDF file
with open('x.pdf', 'rb') as pdf_file:
    # create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    # create an empty list to store the data
    data = []
    # iterate over every page in the PDF
    for page in range(len(pdf_reader.pages)):
        # extract the text from the page
        text = pdf_reader.pages[page].extract_text()
        # split the text into lines
        lines = text.split('\n')
        # append the lines to the data list
        data.extend(lines)
    # convert the data list to a Pandas DataFrame
    df = pd.DataFrame(data)
    # write the DataFrame to an Excel spreadsheet
    df.to_excel('excel.xlsx', index=False, header=False)
