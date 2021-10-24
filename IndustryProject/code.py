
from pdf2image import convert_from_path
import pytesseract
import cv2
import re

paths = []
for i in range(10):
    st = 'C:\\Users\\Manas\\PycharmProjects\\week1project1\\invoice_pdf\\invoice_' + str(i) + '-converted.pdf'
    paths.append(st)
    img = convert_from_path(paths[i], 400,
                            poppler_path="C:\\Users\\Manas\\PycharmProjects\\week1project1\\poppler-0.68.0_x86\\poppler-0.68.0\\bin" )
    for p in img:
        st = 'im'+str(i)+'.jpg'
        p.save(st,'JPEG')
        i = i+1


total = 0
for j in range(10):
    img = cv2.imread("C:\\Users\\Manas\\PycharmProjects\\week1project1\\im" + str(j) + ".jpg")
    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract"

    image = cv2.imread("page0.jpg")
    text = pytesseract.image_to_string(img)
    float_list = []
    text_to_search = text
    pattern=re.compile(r'[+-]?[0-9]+\.[0-9]+')
    matches=pattern.finditer(text_to_search)
    for match in matches:
        float_list.append(float(text[match.span()[0]:match.span()[1]]))
# print(text[match.span()[0]:match.span()[1]]) #for getting the grand total
        (max(float_list))
        for ele in range(0, len(float_list)):
            total = total + float_list[ele]

print(total)




