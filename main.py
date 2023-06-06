from handlers import PDFHandler


def main():
    rockyou_file_path = 'data/rockyou.txt'
    rockyou_fs_r = open(rockyou_file_path, 'r', encoding='latin-1')

    target_file_path = 'data/protected.pdf'
    pdf_handler = PDFHandler(target_file_path)
    pdf_handler.open_pdf()

    for password_guess in rockyou_fs_r:
        if pdf_handler.unlock_pdf(password_guess.strip()):
            return
    print('c: Missing matches in rockyou.txt')


if __name__ == '__main__':
    main()
