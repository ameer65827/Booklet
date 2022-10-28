from PyPDF2 import PdfFileReader, PdfFileWriter

class Printer:

    def __init__(self,inp_file):
        self.inp_pdf = PdfFileReader(inp_file)          # getting the input pdf and making object
        self.out_pdf = PdfFileWriter()                  # creating PdfFileWriter object

        self.pg_num = self.inp_pdf.getNumPages()        # get page numbers
        self.pdf_pages = self.inp_pdf.pages                 # making iterable "all pages" object

        # calling booklet_order function
        self.booklet_order()

    def booklet_order(self):
        self.order = list()  
        N = self.pg_num

        #even
        if N%2==0:
            self.order.append(N-1)
            n = N-2
            b = N-2
        else:  # odd
            self.order.append(-1)
            n = N-1
            b = N-1
        
        a = 0
        flag = 0
        for i in range(int(n/2)):

            if (flag == 0):
                self.order.append(a)
                a+=1
                self.order.append(a)
                a+=1
                flag = 1
            else:
                self.order.append(b)
                b-=1
                self.order.append(b)
                b-=1
                flag = 0

        self.order.append(a)                # middle landscape view, first page.

    def crop(self, pdf_page):
        firstPage = pdf_page
        rect = firstPage.mediaBox

        rect.upper_left = (558.104, 755)
        rect.lower_left = (53.896, 42.05)

    def final_booklet(self):
        for a in self.order:
            self.crop(self.pdf_pages[a])
            self.out_pdf.addPage(self.pdf_pages[a])
        return self.out_pdf





