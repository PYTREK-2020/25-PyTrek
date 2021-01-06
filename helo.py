import pyttsx3 as py
import PyPDF2
book=open('sample.pdf','rb')
pdf=PyPDF2.PdfFileReader(book)
pages=pdf.numPages
print(pages)
sp=py.init()
page=pdf.getPage(2)
text= page.extractText()
sp.say(text)
sp.runAndWait()