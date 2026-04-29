import argparse
import requests

def download_file(url, local_filename):
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename

parser = argparse.ArgumentParser()

#Add command line arguments
parser.add_argument("URL", help="Url of the file to download")
parser.add_argument("Output", help="Ny which name do you want to save your file?")

# Parse the arguments
args = parser.parse_args()

# Use the arguments in your code
print(args.URL)
print(args.Output)

download_file(args.URL, args.Output)