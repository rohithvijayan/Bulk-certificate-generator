import cv2
from PIL import ImageFont, ImageDraw, Image
import pandas as pd
import random
# Load the Excel file
file_path = 'individual_results(1).xlsx'
data = pd.read_excel(file_path)

# Extract the necessary columns
list_names = data[['Name', 'Program Name', 'Winner Type']].values.tolist()

def gen_certificate():
    for name, program_name, winner_type in list_names:
        template = Image.open('arts certificate.png')
        draw = ImageDraw.Draw(template)
        
        # Load the font
        font = ImageFont.truetype('JosefinSans-SemiBoldItalic.ttf', size=85)

        # Position the name
        text_width = draw.textlength(name, font=font)
        x_coordinate = (template.width - text_width) // 2
        draw.text((824,940), text=name, font=font, fill=(0, 0, 0))
        
        # Position the Program Name
        program_text_width = draw.textlength(program_name, font=font)
        program_x_coordinate = (template.width - program_text_width) // 2
        draw.text((628,1204), text=program_name, font=font, fill=(0, 0, 0))

        # Position the Winner Type
        winner_text_width = draw.textlength(winner_type, font=font)
        winner_x_coordinate = (template.width - winner_text_width) // 2
        draw.text((2228,1092), text=winner_type, font=font, fill=(0, 0, 0))
        
        # Save the certificate
        template.save(f'generated _certifcates/{name}_{random.randint(0,100)}.png')

# Generate the certificates
gen_certificate()
