import ebooklib

def epub_epub_to_mobi(input_epub_path, output_mobi_path):
    book = ebooklib.epub.read_epub(input_epub_file)
    mobi_path = output_mobi_file
    ebook
if __name__ == "__main__":
    input_epub_file = "../../assets/Romeo_and_Juliet.epub"
    output_mobi_file = "../../assets/Romeo_and_Juliet2.mobi"

    epub_to_mobi(input_epub_file, output_mobi_file)