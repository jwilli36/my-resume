

# Save this as resume_extractor.py
# Save this as resume_extractor.py
import pdfplumber
# The BeautifulSoup import is not used in the provided functions,
# but can be left in if you plan to extend the code later.
from bs4 import BeautifulSoup 

def extract_linkedin_data(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ''
        for page in pdf.pages:
            # extract_text attempts to maintain layout better than simple text extraction
            text += page.extract_text() or '' 
    return text

def create_markdown_resume(text):
    # Note: This simple parsing logic might need adjustment based on the PDF's actual layout
    sections = text.strip().split('\n\n')
    with open("resume.md", "w", encoding='utf-8') as file:
            for section in sections:
                lines = section.splitlines()
                if lines:
                    file.write(f"## {lines[0]}\n")
                    for line in lines[1:]:
                        # Basic markdown list formatting
                        file.write(f"- {line.strip()}\n")
                    file.write('\n')

# Main execution part
if __name__ == "__main__":
    PDF_FILE_NAME = 'linkedin_profile.pdf'
    print(f"Attempting to process {PDF_FILE_NAME}...")
    try:
        text_data = extract_linkedin_data(PDF_FILE_NAME)
        create_markdown_resume(text_data)
        print(f"Successfully processed PDF. A markdown file named 'resume.md' has been created.")
    except FileNotFoundError:
        print(f"Error: The file '{PDF_FILE_NAME}' was not found.")
        print("Please ensure your LinkedIn profile PDF is in the same directory.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



