from PIL import Image

def convert_to_pdf(image_path, output_path):
    try:
        image = Image.open(image_path)
        img_converted = image.convert('RGB')
        img_converted.save(output_path)
        print(f"Successfully converted to {output_path}")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    img_path = input("Enter image path (e.g., photo.jpg): ")
    convert_to_pdf(img_path, "output.pdf")
