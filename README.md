# Barcode Generator

![Python Version](https://img.shields.io/badge/Python-3.6%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

This Python script allows you to generate barcode images from input data using the 'python-barcode' library. It provides a flexible way to create barcode images of various types and save them to files.

## Table of Contents

- Installation
- Usage
- Supported Barcode Types
- Example
- License

## Installation

1. Make sure you have Python installed on your system. If not, you can download and install it from the official Python website.

2. Install the 'python-barcode' library using pip. Open a terminal or command prompt and run the following command:

       pip install python-barcode
   
4. Download or clone this repository to your local machine.


## Usage

To generate a barcode image, run the 'generate_barcode.py' script with the appropriate parameters:

    python generate_barcode.py <data> [--barcode_type <type>] [--output_filename <filename>]

1. 'data': The data you want to encode in the barcode.
2. '--barcode_type <type>': Optional. The type of barcode to generate. Default is 'code128'. See Supported Barcode Types for available options.
3. '--output_filename <filename>': Optional. The filename to save the generated barcode image (without extension). Default is 'barcode'.

## Supported Barcode Types
The script supports generating barcodes of the following types:

1. Code 128 (default)
2. EAN-13
3. UPC-A

For a complete list of supported types, refer to the 'python-barcode' documentation.

## Example

    python generate_barcode.py 123456789 --barcode_type code128 --output_filename my_barcode

This command will generate a Code 128 barcode image with the data "123456789" and save it as "my_barcode.png" in the current directory.

## License

This project is licensed under the MIT License.

