import fitz


class pdf2img:
    
    def __init__(self):
        self.pdf_path = "/Users/dengdeshun/Desktop/Spider_testing/all.pdf"

    def conver_img(self):
        doc = fitz.open(self.pdf_path)
        
        for pg in range(doc.pageCount):
            page = doc[pg]
            rotate = int(0)
            # 每个尺寸的缩放系数为10，这将为我们生成分辨率提高100倍的图像。
            zoom_x, zoom_y = 2, 2
            trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
            pm = page.getPixmap(matrix=trans, alpha=False)
            pm.writePNG(f'images/{pg+1}.png')
            

if __name__ == '__main__':
    pdf_pro = pdf2img()
    pdf_pro.conver_img()
    print('done!')
