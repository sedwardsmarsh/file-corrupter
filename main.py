# mostly borrowed from: https://www.youtube.com/watch?v=RVhVr6x0CgU
import asyncio
import js
from js import document, FileReader
from pyodide import create_proxy


async def process_file(file) -> None:
    file_list = document.getElementById('uploadButton').files

    for f in fileList:
        # reader is a pyodide.JsProxy
        reader = FileReader.new()

        # create a python proxy for the callback function
        onload_event = create_proxy(read_complete)

        reader.onload = onload_event
        # reader.readAsText(f)
        # trying this method of reading the file since we want to read 
        # arbitrary files, not only text.
        reader.readAsArrayBuffer(f)


def main() -> None:
    # create a python proxy for the callback function
    file_event = create_proxy(process_file)

    # set the listener to the callback
    e = document.getElementById("uploadButton")
    e.addEventListener("click", file_event, False)