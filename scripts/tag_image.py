# scripts/tag_image.py
import argparse
from ram.models import ram_plus

def tag_image(image_path, model_path):
    # Load the model and image
    model = ram_plus.load_pretrained(model_path)
    tags = model.tag(image_path)
    print(f"Image Tags: {tags}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tag an image using RAM++")
    parser.add_argument('--image', type=str, required=True, help='Path to the image file')
    parser.add_argument('--model', type=str, default='models/ram_plus_swin_large_14m.pth', help='Path to the model checkpoint')
    args = parser.parse_args()
    tag_image(args.image, args.model)
