from tkinter import *
from tkinter import filedialog
import os
from tkinter import messagebox
import urllib.error
from plyer import notification
import themes

# play_win -> name of playlist window

box_print = 1
def desktop_notify(location):
    notification.notify(
        title='Youtubo',
        message='\nVideo downloaded successfully\n\n'
                f'{location}',
        app_icon="",
        timeout=10
    )

def playlist(p, playlistTitle, noOfVideos, home, theme_integer):  # p is the object of the Playlist class
    try:
        play_win = Toplevel()
        play_win.title("Search-result")
        play_win.config(bg='white', pady=20, padx=10)
        home.iconify()
        play_win.state("zoomed")

        def back_to_normal_func():
            themes.back_to_normal_playlist(heading_label, video_title, video_title_res, owner, total_videos,
                 res_one, label1, label2, label3, Browse, home_btn, dark_mode_btn, play_win)
            dark_mode_btn.config(command=dark_mode_func, text="🔆")

        def dark_mode_func():
            themes.dark_mode_func_playlist(heading_label, video_title, video_title_res, owner, total_videos,
                 res_one, label1, label2, label3, Browse, home_btn, dark_mode_btn, play_win)
            dark_mode_btn.config(command=back_to_normal_func, text="🌙")

        def on_progress(stream, chunk, bytes_remaining):
            global box_print
            total_size = stream.filesize
            bytes_downloaded = total_size - bytes_remaining
            percentage_of_completion = bytes_downloaded / total_size * 100
            ani = '⬜' * box_print
            print(f"{ani} {round(percentage_of_completion, 0)}%")
            box_print += 1

        # Labels
        heading_label = Label(play_win, text="File fetched successfully..", font=('Times New Roman', 18), bg='white')
        heading_label.config(padx=30, pady=30)
        heading_label.grid(row=0, column=2)

        # space labels
        str1 = "                                          "
        label1 = Label(play_win, text=f"{str1}", bg="white", pady=15)  # to create space
        label1.grid(row=0, column=0)

        label2 = Label(play_win, text="", bg="white", pady=20)  # to create space
        label2.grid(row=4, column=0)

        label3 = Label(play_win, text="", bg="white")  # to create space
        label3.grid(row=6, column=0)


        # Video Details
        video_title = Label(play_win, text="Title : ", font=('arial', 12), bg='white')
        video_title.grid(row=1, column=1)

        video_title_res = Label(play_win, text=f"{playlistTitle}", font=('arial', 12), bg='white', foreground='blue')
        video_title_res.grid(row=1, column=2)

        owner = Label(play_win, text=f"{p.owner}", font=('arial', 12), bg='white')
        owner.grid(row=1, column=3)

        total_videos = Label(play_win, text=f"No. of Videos : {p.length}", font=('arial', 12), bg='white',
                             foreground='indigo', pady=15)
        total_videos.grid(row=2, column=2)

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
        Browse.grid(row=3, column=3)
        Download_path = StringVar()


        res_one = Label(play_win, text="720p :", font=('arial', 12), bg='white')
        res_one.grid(row=5, column=1)

        def download_func():
            count = 0
            if var.get() == 0:
                play_win.iconify()
                for vid in p.videos:
                    os.system('cls')
                    print(f"Downloading Video {count+1}/{noOfVideos}..")
                    global box_print
                    box_print = 1
                    vid.register_on_progress_callback(on_progress)
                    try:
                        vid.streams.filter(progressive=True)[-1].download(f"{Download_path.get()}")
                        count += 1

                    except urllib.error.URLError:
                        messagebox.showwarning(title="Failed!", message="We can't fetch your video.\n\n"
                                                                        "Please check your Internet Connection!")
                    except:
                        messagebox.showwarning(message="Error !!")
                        play_win.destroy()
                        home.state("zoomed")

                    if noOfVideos == count:
                        desktop_notify(f"{Download_path.get()}\{p.title}")
                        play_win.state("zoomed")

                if count != noOfVideos:
                    messagebox.showwarning(message="Due to some technical issue, we can't able to download"
                                               " all videos")
                    play_win.destroy()
                    home.state("zoomed")
            else:
                messagebox.showwarning(title='Failed', message="You need to select location to download file/files")

        # Buttons

        download_button = Button(play_win, text="Download", foreground="white", font=('arial', 13), bg="green")
        download_button.config(activeforeground='white', activebackground='red', command=download_func)
        download_button.grid(row=5, column=2)


        dark_mode_btn = Button(play_win, text="🌑", font=('arial', 30), bg='white', foreground='black', borderwidth=0,
                               command=dark_mode_func)
        dark_mode_btn.grid(row=7, column=0)


        def home_func():
            play_win.destroy()
            home.state("zoomed")


        home_btn = Button(play_win, text="Home", font=('arial', 10), bg="white", command=home_func)
        home_btn.grid(row=0, column=4)

        # set dark theme as default
        if theme_integer.get() == 0:
            dark_mode_func()


        # Hovering
        Browse.bind("<Enter>", func=lambda e: Browse.config(background='yellow', foreground='black'))
        Browse.bind("<Leave>", func=lambda e: Browse.config(background='black', foreground='white'))

        download_button.bind("<Enter>", func=lambda e: download_button.config(background='yellow', foreground='black',
                                                                            font=('arial', 15)))
        download_button.bind("<Leave>", func=lambda e: download_button.config(background='green', foreground='white',
                                                                            font=('arial', 13)))


    except urllib.error.URLError:
        messagebox.showwarning(title="Failed!", message="We can't fetch your video.\n\n"
                                                        "Please check your Internet Connection!")
        home.state("normal")

    except:
        messagebox.showwarning(title="Failed", message='Unexpected Error! Please try again')

    play_win.grab_set()
