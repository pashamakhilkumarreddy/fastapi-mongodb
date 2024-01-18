import os
from base64 import b64encode
from uuid import uuid4

from PIL import Image
from pydantic import validate_arguments

static = 'static'


@validate_arguments
def save_picture(file, folder_name: str = '', file_name: str = None):
    random_uuid = str(uuid4())
    _, f_ext = os.path.splitext(file.filename)

    picture_name = (random_uuid if file_name == None else file_name.lower().replace(' ', '')) + f_ext
    path = os.path.join(static, folder_name)

    if not os.path.exists(path):
        os.makedirs(path)

    image_path = os.path.join(path, picture_name)

    output_size = (125, 125)
    img = Image.open(file.file)

    img.thumbnail(output_size)
    img.save(image_path)

    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
        base64_image = b64encode(image_data).decode('utf-8')

    return [image_data, f'{static}/{folder_name}/{picture_name}']
