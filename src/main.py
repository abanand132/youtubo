import urllib.error
from tkinter import *
from tkinter import messagebox
import webbrowser
import installation

# if pytube/plyer module is not installed in the user's device then it will install it
try:
    from pytube import YouTube, Playlist
    import pytube.exceptions
    import plyer
    import youtube_transcript_api
except ModuleNotFoundError:
    if messagebox.askyesno(title="Need to download libraries",
                           message='Software needs to install some modules to work properly.\n\nPress "Yes" to start download'):
        p = installation.main("pytube")
        q = installation.main("plyer")
        r = installation.main("youtube-transcript-api")
        if p and q and r:
            if messagebox.askokcancel(title="Restart Application",
                    message="We installed some required library to run this application.\nSo, you need "
                            "to restart the application to complete the installation process.\n\nThank you"):
                exit()
    else:
        messagebox.showwarning(title="Error", message="The Application won't run until you allow to "
                                                      "download required modules")
        exit()

# including other python files
import search_page
import themes
import playlist_download

# home window creation
home = Tk()
home.title("Youtubo - Youtube Video/Audio Downloader")
home.config(bg='white', pady=20, padx=10)
home.state('zoomed')


# For Space
str1 = "                                          "
space_label = Label(text=f"{str1}", bg='white', font=('arial', 14))
space_label.grid(row=0, column=0)

label1 = Label(text="       ", bg="white")  # 1
label1.grid(row=0, column=1)
label2 = Label(text="", bg="white")  # 2
label2.grid(row=1, column=3)
label3 = Label(text="", bg="white")  # 3
label3.grid(row=3, column=3)
label4 = Label(text="", bg="white")  # 4
label4.grid(row=5, column=2)
label5 = Label(text="", bg="white", pady=15)  # 4
label5.grid(row=7, column=2)
label6 = Label(text="", bg="white")  # 4
label6.grid(row=9, column=2)
label7 = Label(text="", bg="white", pady=20)  # 4
label7.grid(row=11, column=2)

# Create a Label Widget to display the text
img_label = Label(text="YouTubo", bg='#1A2421', foreground="white", font=('Impact', 90))
img_label.grid(row=0, column=2)


str1 = "Paste your video link here 👇"
sub_heading_label = Label(text=f"{str1}", bg="white", foreground='black', font=('Times New Roman', 15))
sub_heading_label.grid(row=2, column=2)

note1 = Label(text="Note : After clicking on 'Search' button, kindly wait for 3-4 secs & \nlet us access the video",
              bg='yellow', font=('arial', 11))
note1.grid(row=12, column=2)

video_link = Label(text="Video Link : ", bg="white", font=('arial', 14))
video_link.grid(row=4, column=1)

playlist_link = Label(text="Playlist Link : ", bg="white", font=('arial', 14))
playlist_link.grid(row=8, column=1)

# Entry Boxes

link_entry = Entry(width=50, borderwidth=1, font=('arial', 14))
link_entry.config(highlightthickness=1, highlightbackground="black", highlightcolor='red')
link_entry.grid(row=4, column=2)
link_entry.focus()

playlist_list = Entry(width=50, borderwidth=1, font=('arial', 14))
playlist_list.config(highlightthickness=1, highlightbackground="black", highlightcolor='red')
playlist_list.grid(row=8, column=2)


# Functions calling
def search_func():
    url = link_entry.get()
    if len(url) > 0:
        try:
            yt = YouTube(url)  # creating youtube object using YouTube class
            stream720 = yt.streams.get_by_itag(22)  # video
            stream360 = yt.streams.get_by_itag(18)  # video
            stream128 = yt.streams.get_by_itag(140)  # audio
            # control goes to next window - search window
            search_page.search(yt, home, stream720, stream360, stream128, theme_integer)

        except pytube.exceptions.VideoPrivate:
            messagebox.showwarning(title="Failed!", message="Sorry You can't download private videos from YouTube."
                                                            "\n\nThank you!")

        except pytube.exceptions.VideoRegionBlocked:
            messagebox.showwarning(title="Failed!", message="Sorry This video is blocked in your region. So, it can't"
                                                            "be downloaded\n\nThank you!")

        except pytube.exceptions.ExtractError:
            messagebox.showwarning(title="Failed!",
                                   message="Due to some technical reason, we can't get this video! "
                                           "\nPlease check the link you pasted."
                                           "\n\nThank you!")

        except pytube.exceptions.VideoUnavailable:
            messagebox.showwarning(title="Failed!", message="Either you pasted wrong link or link may be distorted!")


        except urllib.error.URLError:
            messagebox.showwarning(title="Failed!", message="We can't fetch your video.\n\n"
                                                            "Please check your Internet Connection!")
    else:
        messagebox.showwarning(title='Failed', message="Error! You can't leave link field empty")


# Single video search
search = Button(text="Search Video", font=('arial', 13, 'bold'), bg='black', foreground='white', command=search_func)
search.config(activebackground='green', activeforeground='white')
search.grid(row=6, column=2)


# Playlist Search
def search_playlist():
    url = playlist_list.get()
    if len(url) > 0:
        try:
            p_obj = Playlist(url)
            playlistTitle = p_obj.title
            noOfVideos = p_obj.length

            playlist_download.playlist(p_obj, playlistTitle, noOfVideos, home, theme_integer)

        except pytube.exceptions.VideoPrivate:
            messagebox.showwarning(title="Failed!", message="Sorry You can't download private videos from YouTube."
                                                            "\n\nThank you!")

        except pytube.exceptions.VideoRegionBlocked:
            messagebox.showwarning(title="Failed!", message="Sorry This video is blocked in your region. So, it can't"
                                                            "be downloaded\n\nThank you!")

        except pytube.exceptions.ExtractError:
            messagebox.showwarning(title="Failed!",
                                   message="Due to some technical reason, we can't extract this video! Or"
                                           "\nPlease check the link you pasted."
                                           "\n\nThank you!")

        except pytube.exceptions.VideoUnavailable:
            messagebox.showwarning(title="Failed!", message="Either you pasted wrong link or link may be distorted!")


        except urllib.error.URLError:
            messagebox.showwarning(title="Failed!", message="We can't fetch your video.\n\n"
                                                            "Please check your Internet Connection!")

        except KeyError:
            messagebox.showwarning(title='Failed',
                                   message="You are entering wrong link.\n\nEither paste playlist link Or"
                                           " link of first video of Playlist")
    else:
        messagebox.showwarning(title='Failed', message="Error! You can't leave link field empty")


# Playlist search button
search1 = Button(text="Search Playlist", font=('arial', 13, 'bold'), bg='black', foreground='white',
                 command=search_playlist)
search1.config(activebackground='green', activeforeground='white')
search1.grid(row=10, column=2)

youtubo_version = 1.2
yt_version = Label(text=f"version - {youtubo_version}", font=('arial', 12))
yt_version.grid(row=13, column=2)


def back_to_normal_func():
    themes.back_to_normal_main(home, sub_heading_label, link_entry, note1, label1,
                               label2, label3, label4, label5, label6, label7, video_link, playlist_link, playlist_list,
                               space_label, close, clear_search_video, clear_search_playlist, yt_version, img_label)
    dark_mode_btn.config(bg='white', foreground='black', command=dark_mode_func, activebackground='white')
    dark_mode_btn.config(text="🔆")
    theme_integer.set(1)


def dark_mode_func():
    themes.dark_mode_func_main(home, sub_heading_label, link_entry, note1, label1,
                               label2, label3, label4, label5, label6, label7, video_link, playlist_link, playlist_list,
                               space_label, close, clear_search_video, clear_search_playlist, yt_version, img_label)
    dark_mode_btn.config(bg='#1A2421', foreground='white', command=back_to_normal_func, activebackground='#1A2421')
    dark_mode_btn.config(text="🌙")
    theme_integer.set(0)


dark_mode_btn = Button(text="🔆", font=('arial', 30), bg='white', foreground='black', borderwidth=0,
                       command=dark_mode_func, activebackground='white')
dark_mode_btn.grid(row=13, column=1)


def close_func():
    home.destroy()


def clear_func1():
    link_entry.delete(0, END)


def clear_func2():
    playlist_list.delete(0, END)


close = Button(text="Close", font=('consolas', 11), bg="white", command=close_func)
close.grid(row=0, column=4)

clear_search_video = Button(text="❌", font=('calibri', 10), bg="white", command=clear_func1, foreground='red')
clear_search_video.grid(row=4, column=4)

clear_search_playlist = Button(text="❌", font=('arial', 10), bg="white", command=clear_func2, foreground='red')
clear_search_playlist.grid(row=8, column=4)


def contact_func():
    if messagebox.askyesno(title="Report an issue",
                           message="YouTubo wants to redirect you to an external website. Proceed ?"):
        # contact_me.bind("<Button>", lambda e: webbrowser.open_new_tab("https://theabhishek.me"))
        webbrowser.open_new_tab("https://github.com/abanand132/youtubo/issues")


contact_me = Button(text='Report Problem', font=('arial', 12), bg='cyan', foreground='black')
contact_me.config(activebackground='black', activeforeground='white', command=contact_func)
contact_me.grid(row=13, column=3)

# set dark mode as default
theme_integer = IntVar()
theme_integer.set(0)

if theme_integer.get() == 0:
    dark_mode_func()


# Hovering

search.bind("<Enter>", func=lambda e: search.config(background='red', foreground='white'))
search.bind("<Leave>", func=lambda e: search.config(background='black', foreground='white'))

search1.bind("<Enter>", func=lambda e: search1.config(background='red', foreground='white'))
search1.bind("<Leave>", func=lambda e: search1.config(background='black', foreground='white'))

close.bind("<Enter>", func=lambda e: close.config(background='#1A2421', foreground='white'))
close.bind("<Leave>", func=lambda e: close.config(background='black', foreground='white'))

clear_search_video.bind("<Enter>", func=lambda e: clear_search_video.config(background='#1A2421', foreground='white'))
clear_search_video.bind("<Leave>", func=lambda e: clear_search_video.config(background='black', foreground='white'))

clear_search_playlist.bind("<Enter>",
                           func=lambda e: clear_search_playlist.config(background='#1A2421', foreground='white'))
clear_search_playlist.bind("<Leave>", func=lambda e: clear_search_playlist.config(background='black', foreground='white'))

contact_me.bind("<Enter>", func=lambda e: contact_me.config(background='#1A2421', foreground='white'))
contact_me.bind("<Leave>", func=lambda e: contact_me.config(background='cyan', foreground='black'))

home.mainloop()
