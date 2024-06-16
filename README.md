A simple Python script that copies the key analyzed by Serato to the comment of a song
This script is used for writing into XML files for streaming services, as these are not written by other external programs.

## Usage
Clone the repository into a desired folder and execute `python3 serato-key-copier.py`. Next, enter the folder where Serato stores the metadata. It is usually something like `music/serato/metadata`. You can then choose either the Open Key or the Camelot format.

## What does the script do?
Serato analyzes the music for its key and BPM. However, in Serato Lite, the key is not shown even though the analyzed key is stored in the metadata. This script simply copies the key data stored in the metadata and writes it at the beginning of the description.

The problem with other third-party programs is that they can only write to MP3 files and not to XML files that store information for songs from streaming services such as SoundCloud.
