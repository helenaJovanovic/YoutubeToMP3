# YoutubeToMP3

A GUI wrapper for an existing library called youtube-dl. Only personal use is allowed and distribution of mp3s downloaded is illegal. 
Written in Python 3.7.4


## Installation

youtube_dl is required if running from source:

```bash
pip install youtube_dl
```
FFmpeg is required to run, you can get the binary for your system here: 

[ffmpeg.org](http://ffmpeg.org/download.html)

In case of Windows you can download the static build here: [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)
and then extract ffmpeg.exe from the bin folder to the folder where you have the source code or the YoutubeToMP3 executable.
You can also extract the whole folder somewhere more suitable and then add that path to the PATH variable.

For Ubuntu based Linux distributions you can do:

```
sudo apt update
sudo apt install ffmpeg
```


## How it works

It's simple. Paste your link and then choose the download destination.

First it will download the video in .webm and then it will convert it to .mp3 in 320 kbps quality and delete the original files.


<br />
<br />

#### Ffmpeg source code:
https://github.com/FFmpeg/FFmpeg/commit/6d886b6586
