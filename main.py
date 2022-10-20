# This is the main script loaded into index.html
# learned a lot from: https://www.youtube.com/watch?v=RVhVr6x0CgU

import js
import asyncio
from js import document, window, Blob
from pyodide import create_proxy
import os


def corrupt_file(path: str) -> None:
    f = open(path, 'wb') # open the file in binary mode for writing
    for offset in range(1, 3):
        f.seek(offset)
        f.write(bytes('garbage', 'utf-8')) # write anything into the file
    return f


def read_file(file) -> None:
    # debug
    # console.log(file)
    file_name = file.name

    # corrupt the file
    new_file = corrupt_file(file_name)

    # debug, print files in cwd
    print(os.listdir())
    
    # notify the user the file has been corrupted
    output_tag = document.getElementById("output")
    output_tag.style.color = 'green'
    output_tag.innerText = "Please wait."

    # create the new file blob
    corrupt_file_blob = Blob.new([new_file])
    url = window.URL.createObjectURL(corrupt_file_blob)
    window.location.assign(url)
    
    # prompt the user to download the file
    # download_link = document.createElement('a')
    # download_link.download = file_name
    # download_link.innerHTML = 'Download File'
    # download_link.href = window.URL.createObjectURL(file)
    # document.body.append(download_link)


async def process_files(file) -> None:
    # grab the select_file <input> tag
    file_list = document.getElementById('select_file').files
    for f in file_list:
        read_file(f)


def setup() -> None:
    # create a python proxy for the process_file callback function
    select_file_event = create_proxy(process_files)

    # set the listener to the callback
    event = document.getElementById("select_file")
    event.addEventListener("change", select_file_event, False)


# initiate the setup function
setup()