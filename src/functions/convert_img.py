from PIL import Image

def convert_img(input_tiff_path, output_jpg_path):
        tiff_image = Image.open(input_tiff_path)

        # Convert TIFF to JPEG
        tiff_image.convert("RGB").save(output_jpg_path, "JPEG")

if __name__ == "__main__":
    input_tiff_file = "../../assets/file_example_TIFF_1MB.tiff"
    output_jpg_file = "../../assets/file_example_TIFF_1MB.jpg"

    convert_img(input_tiff_file, output_jpg_file)