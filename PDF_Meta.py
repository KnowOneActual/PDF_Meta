import pdfrw

def display_pdf_metadata(pdf_file):
  """Displays the metadata in a PDF file.

  Args:
    pdf_file: The path to the PDF file.
  """

  pdf_reader = pdfrw.PdfReader(pdf_file)
  pdf_metadata = pdf_reader.Info

  print("PDF Metadata:")
  for key, value in pdf_metadata.items():
    print(f"{key}: {value}")

if __name__ == "__main__":
  # Get the PDF file path from the user.
  pdf_file = input("Enter the path to the PDF file: ")

  # Display the PDF metadata.
  display_pdf_metadata(pdf_file)
