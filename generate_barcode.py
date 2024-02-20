import barcode
from barcode import generate

def generate_barcode(data, barcode_type='code128', output_filename='barcode'):
     
    # Get the appropriate Barcode class
    code = barcode.get_barcode_class(barcode_type)
    barcode_instance = code(data)

    # Save the barcode image to a file
    filename = f"{output_filename}.{barcode_instance.writer.__class__.__name__.lower()}"
    barcode_instance.save(filename, options={'write_text': False})

    print(f"Barcode generated and saved as '{filename}'")

# Example usage:
if __name__ == "__main__":
    data_to_encode = "123456789"  # Example data
    generate_barcode(data_to_encode, barcode_type='code128', output_filename='barcode')