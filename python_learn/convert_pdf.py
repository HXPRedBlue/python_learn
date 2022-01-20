
from pdf2image import convert_from_path

images = convert_from_path("./python_learn/AVA.pdf")

for i in range(len(images)):
    images[i].save('./python_learn/pdf_img/page' + str(i) + '.jpg', 'JPEG')