import os
import sys
from pathlib import Path

from athenadb import AthenaDBSync
from utils.upload import process_pdf, process_docx
from utils.strings import split_text_into_chunks

# if the user didn't provide a directory, exit
if len(sys.argv) < 3:
    print("Usage: python bulk_upload_quickchat.py <directory> <namespace>")
    sys.exit(1)

# get the directory from the command line
directory = sys.argv[1]
athena_namespace = sys.argv[2]

athena = AthenaDBSync(os.getenv('ATHENA_DB'))

content_chunks: list[str] = []

# walk the given directory
for root, dirs, files in os.walk(directory):
    for file in files:
        # get the full path using pathlib
        full_path = Path(root) / file
        # get the extension
        ext = full_path.suffix
        print(f'Processing {full_path}')
        content = None
        match ext:
            case '.pdf':
                content = process_pdf(athena, full_path)
            case '.docx':
                content = process_docx(athena, full_path)
            case '.md' | '.txt' | '.html':
                with open(full_path, 'r') as f:
                    content = f.read()
            case _:
                print(
                    f"Invalid extension '{ext}'! Skipping {full_path}.")
        if content:
            content_chunks.extend(split_text_into_chunks(content))


# upload the chunks to athena
for i, chunk in enumerate(content_chunks):
    if i < 52:
        continue
    print(
        f'Uploading chunk {i+1}/{len(content_chunks)} with length {len(chunk)}')
    try:
        athena.insert(input=chunk, namespace=athena_namespace)
    except Exception as e:
        print(f'Error uploading chunk {i+1}: {e}')
