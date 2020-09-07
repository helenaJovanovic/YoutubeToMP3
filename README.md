# YoutubeToMP3

YoutubeToMP3 is a simple Python GUI interface for youtube-dl library that makes downloading songs from youtube in mp3 format easier. 


## Installation

youtube_dl is required if running from source:

```bash
pip install youtube_dl
```
FFmpeg is required to run, you can get the binary for your system here: 

[ffmpeg.org](http://ffmpeg.org/download.html)


(You can copy the binary into the folder with the program, or install it elsewhere and add it to the PATH variable)

## How it works

It's simple. Paste your link and then choose the download destination.

First it will download the video in .webm and .mp4 and then it will convert it to .mp3 in 320 kbps quality and delete the original files.
