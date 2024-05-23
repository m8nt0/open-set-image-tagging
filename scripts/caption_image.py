# scripts/caption_image.py
import argparse
from ram.models import tag2text

def caption_image(image_path, model_path):
    # Load the model and image
    model = tag2text.load_pretrained(model_path)
    caption = model.caption(image_path)
    print(f"Image Caption: {caption}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Caption an image using Tag2Text")
    parser.add_argument('--image', type=str, required=True, help='Path to the image file')
    parser.add_argument('--model', type=str, default='models/tag2text_swin_base.pth', help='Path to the model checkpoint')
    args = parser.parse_args()
    caption_image(args.image, args.model)
