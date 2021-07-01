import PyPDF2  # pip install PyPDF2
book = open('pdf-extract-text-sample.pdf', 'rb')  # open read+binary
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

for num in range(0, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    print("----")
    print(text)
    print("----")