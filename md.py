import os
import sys
from pathlib import Path

from utils.upload import process_pdf, process_docx
from utils.strings import split_text_into_chunks

# if the user didn't provide a directory, exit
if len(sys.argv) < 3:
    print("Usage: python md.py <directory> <output_filename.md>")
    sys.exit(1)

# get the directory from the command line
directory = sys.argv[1]
output_filename = sys.argv[2]

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
                content = process_pdf(full_path)
            case '.docx':
                content = process_docx(full_path)
            case '.md' | '.txt' | '.html':
                with open(full_path, 'r') as f:
                    content = f.read()
            case _:
                print(
                    f"Invalid extension '{ext}'! Skipping {full_path}.")
        if content:
            content_chunks.extend(split_text_into_chunks(content))

content = '\n\n'.join(content_chunks)

with open(output_filename, 'w') as f:
    f.write(content)
