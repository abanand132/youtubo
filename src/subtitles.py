from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import *
from youtube_transcript_api.formatters import SRTFormatter
from tkinter import messagebox
from plyer import notification

def desktop_notify(message):
    notification.notify(
        title='Youtubo',
        message=f'\nError\n\n{message}',
        app_icon="",
        timeout=10
    )
def download_subtitle(yt, download_path, title):
    """
    :param yt: YouTube object
    :param download_path: location where to download the subtitle file. Generally video & subtile location are same
    :param title : video title
    :return: None
    """
    video = yt.video_id
    try:
        caption = YouTubeTranscriptApi.get_transcript(video_id=video, languages=['en', 'en-IN', 'en-US', 'en-UK'])

        srt_format = SRTFormatter()
        sub = srt_format.format_transcript(caption)

        with open(f"{download_path}\{title}.srt", 'w') as file:
            pass
        file.close()

        with open(f"{download_path}\{title}.srt", 'w') as file:
            file.write(sub)
        file.close()

    except TranscriptsDisabled:
        message = "Subtitle is not available for this video\nTry downloading without subtitles"
        desktop_notify(message)
        messagebox.showerror(title="Error", message=f"{message}")

    except NoTranscriptFound:
        message = "No English subtitle is found!\nTry downloading without subtitles"
        messagebox.showerror(title="Error", message=f"{message}")
