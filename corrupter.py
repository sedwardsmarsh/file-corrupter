# script for corrupting a file

import fpdf


def create_test_pdf(path: str = 'corrupt me.pdf') -> str:
    # save FPDF() class into a
    # variable pdf
    pdf = fpdf.FPDF()
    # Add a page
    pdf.add_page()
    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", size = 15)
    # create a cell
    pdf.cell(200, 10, txt = "GeeksforGeeks",
            ln = 1, align = 'C')
    # add another cell
    pdf.cell(200, 10, txt = "A Computer Science portal for geeks.",
            ln = 2, align = 'C')
    # save the pdf with name .pdf
    pdf.output(path)
    return path


def create_test_txt(path: str = 'corrupt me.txt') -> str:
    f = open(path, 'w') # if the file it doesn't exist create it and open in write 'w' mode
    f.write('Can you read this?') # write to the file
    f.close() # close the file pointer
    return path


def corrupt_file(path: str) -> None:
    f = open(path, 'wb') # open the file in binary mode for writing
    for offset in range(1, 3):
        f.seek(offset)
        f.write(bytes('garbage', 'utf-8')) # write anything into the file
    f.close()


# testing
pdf_file_path = create_test_pdf()
txt_file_path = create_test_txt()
corrupt_file(pdf_file_path)
corrupt_file(txt_file_path)