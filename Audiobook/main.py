import pyttsx3
import PyPDF2
book = open('sop.pdf', 'rb')  # Paste the PDF file in the first set of single quotes
# The 2nd set of quotes stating 'rb', indicates Read in Binary call of the imported package - Python to Text Speech (pyttsx3)    
pdf_Reader = PyPDF2.PdfFileReader(book)
pages = pdf_Reader.numPages
print("Number of pages:", pages)
speaker = pyttsx3.init()
for reading in range(0, pages):   # This is the range defined to the Audiobook.
    page = pdf_Reader.getPage(0)  # Here 0 is the indexed page number from the audiobook will start reading.
    text_extract = page.extractText()
    speaker.say(text_extract)
    speaker.runAndWait()