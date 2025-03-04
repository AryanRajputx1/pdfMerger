PDF Merger

Overview

This project is a simple Python script that merges multiple PDF files into a single PDF. It uses the PyPDF2 library to perform the merging operation.

Prerequisites

Ensure you have Python installed on your system. You will also need the PyPDF2 library. If you haven't installed it yet, you can do so using pip:

pip install PyPDF2

Usage

Place the PDF files you want to merge in the project directory.

Update the pdffiles list in main.py with the names of the PDF files.

Run the script:

python main.py

The merged PDF will be saved as merged.pdf in the project directory.

Script Details

The script follows these steps:

Defines a list of PDF files to be merged.

Uses PyPDF2.PdfMerger() to merge them.

Saves the output as merged.pdf.

Repository Structure

pdfMerger/
│-- main.py
│-- README.md
│-- 1.pdf
│-- 2.pdf

Contributing

Feel free to contribute by adding new features or improving the script. Fork the repository, make your changes, and submit a pull request.

License

This project is open-source and available under the MIT License.
