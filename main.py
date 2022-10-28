from PrinterClass import Printer
from time import sleep

def charbychar(txt):
    for a in txt:
        print(a, end="", flush=True)
        sleep(0.05)


charbychar("WELCOME TO BOOKLET CONVERTER")
sleep(0.5)
print()
charbychar("Created by Ameer Navas")
print()
sleep(0.5)
inp_file_name = input("Enter the input file name: ")
sleep(1)
out_file_name = input("Enter name for the booklet: ")

print("please wait", end="" ,flush=True)
for i in range(7):
    print('.', end="",flush=True)
    sleep(0.5)
print("\nYour Booklet is ready")
sleep(1)
charbychar("Thank You :)")
print()

myprinter = Printer(inp_file_name)
out_pdf = myprinter.final_booklet()  # this is final pdf (object/instance of PdfFileWriter)

with open(out_file_name, 'wb') as file:
    out_pdf.write(file)




# BUGS
# 1) odd page, last index blank page (-1) is not added
# 2) only pdf with pages multiples of 4  will work perfectly 
            # (add pages to make multiples of 4, using modulus operator)


