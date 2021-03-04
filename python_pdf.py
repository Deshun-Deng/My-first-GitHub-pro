from PyPDF2 import PdfFileReader, PdfFileWriter
import pdfplumber
import random
class pdf_joy:
    def __init__(self):
        self.pdf_reader = PdfFileReader(r"/Users/dengdeshun/Downloads/华西-智付通授信尽调报告.pdf")
        self.pdf_writer = PdfFileWriter()

    def extract_page(self):
        #提取页面
        for page_idx in range(self.pdf_reader.numPages):
            page = self.pdf_reader.getPage(page_idx)
            print('-'*100)
            print(page.extractText())

    def extract_text(self):
        #提取pdf文字
        pdf_reader = pdfplumber.open(r"/Users/dengdeshun/Downloads/华西-智付通授信尽调报告.pdf")
        page = pdf_reader.pages[0]
        print(page.extract_text())
        print(page.extract_table())

    def pdf_split(self):
        #拆分pdf
        for page in range(self.pdf_reader.numPages):
            pdf_writer = PdfFileWriter()
            single_page = self.pdf_reader.getPage(page)
            pdf_writer.addPage(single_page)
            with open(f'{page}.pdf', 'wb') as pdf:
                pdf_writer.write(pdf)

    def merge_pdf(self):
        #合并pdf
        pdf_writer = PdfFileWriter()
        pdf_names = [f'{i}.pdf' for i in range(4)]+['all.pdf']
        for pdf_name in pdf_names:
            pf = PdfFileReader(pdf_name)
            for page_idx in range(pf.numPages):
                page = pf.getPage(page_idx)
                pdf_writer.addPage(page)
        with open('all2.pdf', 'wb') as pf2:
            pdf_writer.write(pf2)
        pass

    def rotate_pdf(self):
        #旋转pdf
        pdf_writer = self.pdf_writer
        for idx in range(self.pdf_reader.numPages):
            page = self.pdf_reader.getPage(idx)
            if idx % 2 == 0:
                page = page.rotateClockwise(90)
            else:
                page = page.rotateCounterClockwise(90)
            pdf_writer.addPage(page)
        with open('rotatePdf.pdf', 'wb') as pdf:
            pdf_writer.write(pdf)
        # rotateClockwise(90) 顺时针旋转90度
        # rotateCounterClockwise(90) 逆时针旋转90度
        pass

    def pdf_split2(self):
        page_count = list(map(lambda x: int(x), input("Split Pages Nums:").split()))
        # print(page_count)
        self.pdf_reader = PdfFileReader("/Users/dengdeshun/Desktop/Spider_testing/all2.pdf")
        if len(page_count) == 1:
            num = self.pdf_reader.numPages
            ele = page_count[0]
            page_count = [ele]*(num//ele)
            if num%ele != 0:
                page_count += [num-ele*(num//ele)]
        page_idx = []
        for i in range(1, len(page_count)+1):
            page_idx.append(self.page_index(page_count[:i]))
        print(page_idx)
        for idx in page_idx:
            self.save_pdf_idx(idx)

    def page_index(self, page_cnt):
        if len(page_cnt) == 1:
            return [0, page_cnt[-1]-1]
        return [self.page_index(page_cnt[:-1])[1]+1, self.page_index(page_cnt[:-1])[1]+page_cnt[-1]]

    def save_pdf_idx(self, idx):
        pdf_writer = PdfFileWriter()
        for page in range(idx[0], idx[1]+1):
            single_page = self.pdf_reader.getPage(page)
            pdf_writer.addPage(single_page)
        with open(f'pdfs/{int(random.randrange(1234,4321))}.pdf', 'wb') as pdf:
            pdf_writer.write(pdf)

if __name__ == '__main__':
    solution = pdf_joy()
    # solution.pdf_split()
    # solution.merge_pdf()
    # solution.rotate_pdf()
    solution.pdf_split2()