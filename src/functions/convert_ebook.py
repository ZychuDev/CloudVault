import subprocess

def epub_to_mobi(input_epub_path, output_mobi_path):
    # Use ebook-convert to convert EPUB to MOBI
    ebook_convert_cmd = ["ebook-convert", input_epub_path, output_mobi_path]
    subprocess.run(ebook_convert_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

if __name__ == "__main__":
    input_epub_file = "../../assets/Romeo_and_Juliet.epub"
    output_mobi_file = "../../assets/Romeo_and_Juliet.mobi"

    epub_to_mobi(input_epub_file, output_mobi_file)