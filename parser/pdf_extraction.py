import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()

def get_markdown(pdf_path):
    """
    Process a PDF file using the Datalab API and returns the extracted data response.
    """
    url = "https://www.datalab.to/api/v1/marker"

    form_data = {
        'file': ('test.pdf', open(pdf_path, 'rb'), 'application/pdf'),
        'langs': (None, "English"),
        "force_ocr": (None, False),
        "paginate": (None, False),
        'output_format': (None, 'markdown'),
        "use_llm": (None, False),
        "strip_existing_ocr": (None, False),
        "disable_image_extraction": (None, False)
    }

    headers = {"X-Api-Key": os.getenv("DATALAB_API_KEY")}

    response = requests.post(url, files=form_data, headers=headers)
    if response.status_code == 200:
        data = response.json()
        check_url = data.get("request_check_url")
        if not check_url:
            raise Exception("No request_check_url found in the response.")

        max_polls = 300
        for i in range(max_polls):
            time.sleep(2)
            poll_response = requests.get(check_url, headers=headers)
            poll_data = poll_response.json()

            if poll_data.get("status") == "complete":
                if poll_data.get("success"):
                    return poll_data
                else:
                    raise Exception(f"Error during processing: {poll_data.get('error')}")

        raise Exception("Polling timed out before processing was complete.")
    else:
        raise Exception(f"Failed to initiate PDF processing. Status code: {response.status_code}, Error: {response.text}")

if __name__ == "__main__":
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Process a PDF file using the Datalab API.")
    parser.add_argument("--pdf_path", type=str, help="Path to the PDF file to process.")
    args = parser.parse_args()

    pdf_path = args.pdf_path
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"The file {pdf_path} does not exist.")
    
    print(f"Processing {pdf_path}...")
    try:
        result = get_markdown(pdf_path)
        print("Processing complete. Result:")
        print(result['markdown'][:0:1000])  # Print the first 1000 characters of the markdown result
    except Exception as e:
        print(f"An error occurred: {e}")