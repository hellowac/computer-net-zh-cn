
import json

import pymupdf
import pprint

from operator import itemgetter
from itertools import groupby

from PIL import Image



print(f"使用pymupdf版本: {pymupdf.__version__}")

def get_images(doc: pymupdf.Document, pno: int):
    """ 提取第x页的图片 """

    # https://hellowac.github.io/PyMuPDF-zh-cn/document.html#Document.get_page_images
    images: list[tuple] = doc.get_page_images(pno, True)

    for index, image in enumerate(images):
        # print(image)
        (xref, smask, width, height, bpc, colorspace, alt_colorspace, name, filter, referencer) = image

        filename = f'docs/img/{pno+1}-{index}.png'

        print(f"保存图片到: {filename} - {name}")
        # pymupdf.Pixmap(doc, xref).save(filename)

        # 翻转图片（水平翻转）
        flipped_img = pymupdf.Pixmap(doc, xref).pil_image().convert('RGBA').transpose(Image.Transpose.FLIP_TOP_BOTTOM)

        # 获取像素数据
        datas = flipped_img.getdata()

        # 创建新数据列表
        new_data = []
        for item in datas:
            # item 是一个元组 (R, G, B, A)
            if item[:3] == (0, 0, 0):  # 如果 RGB 是 #000000（黑色）
                new_data.append((0, 0, 0, 0))  # 设置为透明
            else:
                new_data.append(item)

        # 更新图片数据
        flipped_img.putdata(new_data)

        # 保存图片
        flipped_img.save(filename, format="PNG")  # 必须保存为 PNG 才能保留透明度



def get_texts(doc: pymupdf.Document, pno: int):
    """ 提取第x页的文本 """

    # https://hellowac.github.io/PyMuPDF-zh-cn/document.html#Document.get_page_xobjects
    page: pymupdf.Page = doc[pno]

    # text_words = page.get_text('dict')

    text_words = page.get_text()

    print(f"第{pno+1}页: {text_words}")


    # Enjoy!

def main():

    filename = 'Computer+Networking+_+A+Top+Down+Approach,+7th,+converted.pdf'

    # 文档对象
    doc = pymupdf.open(filename)

    page_count = len(doc)

    # 提取图片
    pno = 0

    for pno in range(1, page_count):
        get_images(doc, pno=pno)

    # for pno in range(page_count):

    #     if pno < 4:
    #         get_texts(doc, pno)



if __name__ == "__main__":

    main()

  