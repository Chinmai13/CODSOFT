from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
from PIL import Image
import torch

model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
processor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

image = Image.open("image.jpg").convert("RGB")
pixel_values = processor(images=image, return_tensors="pt").pixel_values

output_ids = model.generate(pixel_values, max_length=16)
caption = tokenizer.decode(output_ids[0], skip_special_tokens=True)
print(caption)
