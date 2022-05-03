from rembg.bg import remove
import numpy as np
import io
from PIL import Image
input_path = 'lambo.jpg'
output_path = 'out.png'
f = np.fromfile(input_path)
result = remove(f,model_name="carros")
img = Image.open(io.BytesIO(result)).convert("RGBA")
img.save(output_path)