![youTubo_logo](https://github.com/abanand132/youtubo/assets/76703822/ef0beb62-b8a8-411e-9498-938513184077)

### A lightweight, easy to use, Youtube Videos & Audio downloader

It is python based gui software that helps user to download youtube videos (single video or entire playlist) and audio(mp3) with just few clicks.
[(Tutorial Video)](https://drive.google.com/file/d/1zrcVaW5yW-qOwXgCEeojaECO3qARaNAu/view?usp=sharing)

## Contents
- [Important Info](#important-info)
- [Features](#features)
- [Tech Stacks](#tech-stacks)
- [Installations](#installations)
- [Known Issues](#known-issues)


## Important Info
- Operating System : Windows 10 and above
- Current version : 1.2
- Developer : [Abhishek Anand](https://theabhishek.me)

## Features

- User can download a single video or an entire playlist according to their needs
- Multiple Resolutions (360p, 720p etc.) of videos available
- Users can also download just audio (mp3) of a video
- English Subtitles (if available) can be downloaded alongside with the Single video as well as for whole Playlist 
- Application comes with light mode & dark mode
- Progress bar to show the status of video/audio downloading
- Notify users when download completed

## Tech Stacks
- Python3
- [PyTube](https://pytube.io/en/latest/)
- Tkinter (For GUI Interface)

## Installations
- Just go to [Application Folder](https://github.com/abanand132/youtubo/tree/main/application) and download **youtubo.exe** file.
- After successful downloading into your device, just double click and start. You are ready to go. That's it.
- User can also watch tutorial video [(Click Here)](https://drive.google.com/file/d/1zrcVaW5yW-qOwXgCEeojaECO3qARaNAu/view?usp=sharing)
## Known Issues
- If you are facing Microsoft Defender issue  then just click on `more info` and then `run anyway` or watch video given below
  https://github.com/abanand132/youtubo/assets/76703822/ede26d11-94ae-441e-a430-05b45a217aeb
   - If in your system, you don't see `run anyway` then you need to download manually. Follow the steps given below.
      - Download the zip file of entire repo present inside `code` button.
      - Extract the files from zip.
      - Go to `src` and then double click on `main.py`. Application should run after installing some modules.
      - `Python should be installed in your system for this process`
- Downloading playlist of youtube shorts is not available
- 1080p resolution is not available because YouTube used a protocol called DASH in which video file and audio of that video are two separate files. Because of this software needs to download both files separately and merging them alongside takes alot of time. So, that's why It is not available at the moment. Currenlty working on it, if possible then it will be available soon.
<br>
<br>
<b>Thank you for using this app. Your feedback matters so do give your feedback.</b>
