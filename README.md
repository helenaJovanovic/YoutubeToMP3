# YoutubeToMP3

YoutubeToMP3 is a simple GUI interface for youtube-dl library that makes downloading songs from youtube in mp3 format easier. It was written in Python 3.7.4


## Installation

youtube_dl is required if running from source:

```bash
pip install youtube_dl
```
FFmpeg is required to run, you can get the binary for your system here: 

[ffmpeg.org](http://ffmpeg.org/download.html)

In case of Windows you can download the static build here: [http://ffmpeg.zeranoe.com/builds/](http://ffmpeg.zeranoe.com/builds/)
And then extract ffmpeg.exe from the bin folder inside the zip file to the folder where you have the source code or the executable of YoutubeToMP3.
You can also extract the whole folder somewhere more suitable and then add the path to .../bin to the PATH variable.

For Ubuntu based Linux distributions you can do:

```
sudo apt update
sudo apt install ffmpeg
```


## How it works

It's simple. Paste your link and then choose the download destination.

First it will download the video in .webm and then it will convert it to .mp3 in 320 kbps quality and delete the original files.
