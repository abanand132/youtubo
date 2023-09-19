from tkinter import *
from tkinter import filedialog
import os
from tkinter import messagebox
import urllib.error
import themes


def playlist_less(p, home):  # p is the object of the Playlist class
    try:
        play_win = Toplevel()
        play_win.title("Search-result")
        play_win.config(bg='white', pady=20, padx=10)
        # play_win.minsize(width=600, height=400)
        home.iconify()
        play_win.state("zoomed")


        # Labels
        heading_label = Label(play_win, text="File fetched successfully..", font=('arial', 14), bg='white')
        heading_label.grid(row=0, column=1)

        # Video Details
        label1 = Label(play_win, text="", bg="white")  # to create space
        label1.grid(row=1, column=0)

        video_title = Label(play_win, text="Title : ", font=('arial', 12), bg='white')
        video_title.grid(row=2, column=0)

        video_title_res = Label(play_win, text=f"{p.title}", font=('arial', 12), bg='white', foreground='blue')
        video_title_res.grid(row=2, column=1)

        owner = Label(play_win, text=f"Channel : {p.owner}", font=('arial', 12), bg='white')
        owner.grid(row=3, column=1)

        total_videos = Label(play_win, text=f"No. of Videos : {p.length}", font=('arial', 12), bg='white',
                             foreground='indigo')
        total_videos.grid(row=4, column=1)

        # Selection of Location in File Manager
        var = IntVar()  # to tell the user that they need to select a location before downloading file
        var.set(1)

        def browse():
            # set directory
            download_dir = filedialog.askdirectory(initialdir="/")
            Download_path.set(download_dir)
            x = Download_path.get()
            if len(x) != 0:
                var.set(0)
                Browse.config(text=f"{x[0:20]}..", font=('arial', 10))

        # Buttons
        Browse = Button(play_win, text="Select File Location", font=('arial', 13), bg='black',
                        foreground='white', command=browse)
        Browse.config(activebackground='red', activeforeground='white')
        Browse.grid(row=6, column=2)
        Download_path = StringVar()

        for video in p.videos:
            print(video.title)
            x = video.streams.get_by_itag(22)
            print(x)

        # Calculating total size of playlist
        def show_size_func():
            show_size.destroy()
            total_size = 0
            for video in p.videos:
                x = video.streams.get_by_itag(22)
                total_size = total_size + x.filesize
            total_size_720 = round(total_size/(1024*1024), 2)
            file_size_res_one = Label(play_win, text=f"File Size : {total_size_720}MB", font=('arial', 12), bg='white')
            file_size_res_one.grid(row=7, column=2)
            show_size.destroy()

        label2 = Label(play_win, text="", bg="white")  # to create space
        label2.grid(row=5, column=1)

        download_heading = Label(play_win, text="Download Options", font=('arial', 12), bg='white', foreground='red')
        download_heading.grid(row=6, column=1)

        res_one = Label(play_win, text="720p :", font=('arial', 12), bg='white',pady=20)
        res_one.grid(row=7, column=0)

        def advance_download():
            if var.get() == 0:
                os.mkdir(f"{Download_path.get()}\{p.title}")  # creating folder in the file manager
                video_no = 0
                if (video_no <= 50):
                    for video in p.videos:
                        x = video.streams.get_by_itag(22)
                        x.download(f"{Download_path.get()}\{p.title}")
                        video_no += 1
                    download_status = Label(play_win, text=f"Part-1 Download Completed", bg='black', foreground='white')
                    download_status.config(font=('arial', 20))
                    download_status.grid(row=3, column=1)

                elif video_no > 50:
                    pass

                # write code for videos present at more than 50 video number







        def res_720():
            count = 0
            if var.get() == 0:
                os.mkdir(f"{Download_path.get()}\{p.title}")

                for video in p.videos:  # p is the object of PlayList
                    x = video.streams.get_by_itag(22)
                    x.download(f"{Download_path.get()}\{p.title}")
                    count += 1

                    if p.length == count:
                        download_status = Label(play_win, text=f"100% Download Completed", bg='black', foreground='white')
                        download_status.config(font=('arial', 20))
                        download_status.grid(row=3, column=1)
                    else:
                        download_status = Label(play_win, text=f"Download Incomplete", bg='black',
                                                foreground='white')
                        download_status.config(font=('arial', 20))
                        download_status.grid(row=3, column=1)
            else:
                messagebox.showwarning(title='Failed', message="You need to select location to download file/files")

        # Buttons

        download_button = Button(play_win, text="Download", foreground="white", font=('arial', 13), bg="green")
        download_button.config(activeforeground='white', activebackground='red')
        download_button.grid(row=7, column=1)

        if p.length <= 50:
            download_button.config(command=res_720)
        else:
            download_button.config(command=advance_download)
        show_size = Button(play_win, text="click to see size", bg="white", font=('arial', 10), command=show_size_func)
        show_size.grid(row=7, column=2)

        def back_to_normal_func():
            dark_mode_page.back_to_normal_playlist(heading_label, video_title, video_title_res, owner, total_videos,
            download_heading, res_one, label1, label2, label3, Browse, home_button, dark_mode_btn,
                                                   show_size, play_win)
            dark_mode_btn.config(command=dark_mode_func)

        def dark_mode_func():
            dark_mode_page.dark_mode_func_playlist(heading_label, video_title, video_title_res, owner, total_videos,
            download_heading, res_one, label1, label2, label3, Browse, home_button, dark_mode_btn,
                                                   show_size, play_win)
            dark_mode_btn.config(command=back_to_normal_func)

        dark_mode_btn = Button(play_win, text="🌑", font=('arial', 30), bg='white', foreground='black', borderwidth=0,
                               command=dark_mode_func)
        dark_mode_btn.grid(row=0, column=0)

        label3 = Label(play_win, text="", bg="white")  # to create space
        label3.grid(row=8, column=0)

        def home_func():
            play_win.destroy()
            home.state("zoomed")

        home_button = Button(play_win, text="Close", font=('arial', 10), bg="white", command=home_func)
        home_button.grid(row=0, column=2)

        # Hovering

        Browse.bind("<Enter>", func=lambda e: Browse.config(background='yellow', foreground='black'))
        Browse.bind("<Leave>", func=lambda e: Browse.config(background='black', foreground='white'))

        download_button.bind("<Enter>", func=lambda e: download_button.config(background='yellow', foreground='black',
                                                                            font=('arial', 15)))
        download_button.bind("<Leave>", func=lambda e: download_button.config(background='green', foreground='white',
                                                                            font=('arial', 13)))


        play_win.grab_set()

    except urllib.error.URLError:
        messagebox.showwarning(title="Failed!", message="We can't fetch your video.\n\n"
                                                        "Please check your Internet Connection!")
        home.state("normal")
    # except:
    #     messagebox.showwarning(title="Failed", message='Unexpected Error! Please try again')

def playlist_more(p, home):
    pass





