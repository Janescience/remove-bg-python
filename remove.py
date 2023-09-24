from rembg import remove

from PIL import Image

input_path = 'test.jpeg'

output_path = 'test.png'

inp = Image.open(input_path)

outp = remove(inp)

outp.save(output_path)

Image.open('test.png')