import PyPDF2 as pdf

# To open a PDF file we use the PsdFileReader methon
# This method takes a file stream as it's first argument.
# So we'll use the open function to create the streams
# We need to open the file in binary mode. So we'll use the rb (read binary) argument
with open("first.pdf", "rb") as file:
    reader = pdf.PdfFileReader(file)

    # number of pages
    print(reader.numPages)

    # Get page
    page = reader.getPage(0)
    print(page)

    # rotate the page object in memory
    page.rotateClockwise(90)

    # write rotated page
    writer = pdf.PdfFileWriter()
    writer.addPage(page)

    # write on disk (wb = write binary)
    with open("rotated.pdf", "wb") as output:
        writer.write(output)
