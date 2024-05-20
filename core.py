from sessions.silueta import SiluetaSession
from PIL import Image
from PIL.Image import Image as PILImage
from pathlib import Path


def generate_mask(image_path: str) -> list[PILImage]:
    img = Image.open(image_path)
    predictor = SiluetaSession('silueta', None)
    masks = predictor.predict(img)
    return masks

def rmbg(image:str):
    image_file = Image.open(image)
    mask = generate_mask(image)[0]

    mask = mask.convert('L')

    image_file.putalpha(mask)
    image_file.save('bgless_' + Path(image).stem + '.png')
