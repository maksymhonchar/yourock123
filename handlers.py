import datetime

import PyPDF2


class PDFHandler:

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.pdf_reader: PyPDF2.PdfReader = None

    def open_pdf(self) -> None:
        try:
            with open(self.file_path, 'rb') as file:
                self.pdf_reader = PyPDF2.PdfReader(file)
        except FileNotFoundError as e:
            error_msg = f"File not found: {e}"
            raise FileNotFoundError(error_msg)
        
    def unlock_pdf(self, password: str) -> bool:
        if self.pdf_reader.is_encrypted:
            return self._unlock_encrypted_pdf(password)
        else:
            self._log("File is not encrypted.")
            return True

    def _unlock_encrypted_pdf(self, password: str) -> bool:
        success_decryption_results = {
            1: 'USER_PASSWORD',
            2: 'OWNER_PASSWORD'
        }
        decryption_result = self.pdf_reader.decrypt(password)
        if decryption_result in success_decryption_results:
            self._log(f"File decrypted successfully. [{password}]")
            return True
        else:
            self._log(f"Password is not correct. [{password}].")
            return False

    def _log(self, message: str) -> None:
        current_time_fmt = "%Y-%m-%d %H:%M:%S"
        current_time = datetime.datetime.now().strftime(current_time_fmt)
        print(f"[{current_time}] [{self.file_path}]\t{message}")
