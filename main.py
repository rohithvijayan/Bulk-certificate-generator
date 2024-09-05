import cv2
from PIL import ImageFont,ImageDraw,Image
list_names=[]
def data_clean():
    with open('names.txt','r') as file:
        for name in file.readlines():
            #print(name.strip())
            list_names.append(name.strip())

def gen_certificate():
    for name in list_names:
        #template=cv2.imread('arts certificate.png')
        #cv2.putText(template,name,(196,218),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.5,color=(0,0,0),thickness=1,lineType=cv2.LINE_AA)
        #cv2.putText(template,'rohith',(111,308),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.3,color=(0,0,0),thickness=1,lineType=cv2.LINE_AA)
        template=Image.open('arts certificate.png')
        draw=ImageDraw.Draw(template)
        font=ImageFont.truetype('JosefinSans-SemiBoldItalic.ttf',size=15)
        text_width = draw.textlength(name, font=font)
        x_coordinate = (template.width - text_width) // 2
        draw.text((x_coordinate,208),text=name,font=font,fill=(0,0,0),)
        template.save(f'generated _certifcates/{name}.jpg')
        #cv2.imwrite(f'generated _certifcates/{name}.jpg',template)

data_clean()
print(list_names)
gen_certificate()
