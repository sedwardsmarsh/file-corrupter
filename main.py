# This is the main script loaded into index.html
# learned a lot from: https://www.youtube.com/watch?v=RVhVr6x0CgU

import js
from js import document, FileReader
from pyodide import create_proxy
import corrupter


def read_file(file) -> None:
    # debug
    # console.log(file)

    # corrupt the file
    corrupter.corrupt_file(file.name)
    
    # notify the user the file has been corrupted
    element = document.getElementById("output")
    element.style.color = 'green'
    element.innerText = "Done corrupting file!\nPlease wait for download"
    
    # prompt the user to download the file
    # document.getElementById("output").append(element)


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