import urllib.error
import webbrowser
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import os
import time
import themes
from plyer import notification
import subtitles

box_print = 1

def desktop_notify(location):
    notification.notify(
        title='Youtubo',
        message='\nVideo downloaded successfully\n\n'
                f'{location}',
        app_icon="",
        timeout=10
    )

def search(yt, home, stream720, stream360, stream128, theme_integer):

    # handling error if desired resolution is not available
    video_res = yt.streams.filter(progressive=True)
    audio_stream_list = yt.streams.filter(mime_type="audio/mp4")

    if stream720 is None:
        stream720 = video_res[-1]

    if stream360 is None:
        stream360 = video_res[-2]

    if stream128 is None:
        stream128 = audio_stream_list[-1]

    try:
        var = IntVar()  # to tell the user that they need to select a location before downloading file
        var.set(1)

        search_window = Toplevel()
        search_window.title("Search-result")
        search_window.config(bg='white', pady=20, padx=10)
        search_window.state("zoomed")

        home.iconify()

        def back_to_normal_func():
            themes.back_to_normal_search(search_window, space_label, heading_label, video_title, video_title_res,
                    file_size_res360, file_size_res720, file_size_res128, Browse, note,
                    audio_one, label2, label3, label4, label5, label6, label7, res_one, res_two, home_button)
            dark_mode.config(command=dark_mode_func1, foreground='black', bg='white', text="🔆")

        def dark_mode_func1():
            themes.dark_mode_func_search(search_window, space_label, heading_label, video_title, video_title_res,
            file_size_res360, file_size_res720, file_size_res128, Browse, note, audio_one,
            label2, label3, label4, label5, label6, label7, res_one, res_two, home_button)

            dark_mode.config(command=back_to_normal_func, foreground='white', bg='#1A2421', text="🌙")

        # Function to select location in file manager
        def browse():
            # set directory
            download_dir = filedialog.askdirectory(initialdir="/")
            Download_path.set(download_dir)
            x = Download_path.get()
            if len(x) != 0:
                var.set(0)
                Browse.config(text=f"{x[0:20]}..", font=('arial', 10))

        # Buttons
        Browse = Button(search_window, text="Select File Location", font=('arial', 13, 'bold'), bg='black',
                        foreground='white', command=browse)
        Browse.grid(row=4, column=3)
        Download_path = StringVar()  # StringVar


        # Labels
        str1 = "                                            "
        space_label = Label(search_window, text=f'{str1}', bg='white', font=('arial', 12))
        space_label.grid(row=0, column=0)

        heading_label = Label(search_window, text="File fetched successfully..", font=('Times New Roman', 18), bg='white')
        heading_label.grid(row=0, column=2)

        # Video Details
        label2 = Label(search_window, text="", bg="white")  # to create space
        label2.grid(row=1, column=1)

        video_title = Label(search_window, text="Title : ", font=('arial', 12), bg='white')
        video_title.grid(row=2, column=1)

        title = yt.title  # title of the video

        if len(title) > 80:
            title = title[0:81]
        video_title_res = Label(search_window, text=f"{title}", font=('arial', 12), bg='white')
        video_title_res.config(foreground='black')
        video_title_res.grid(row=2, column=2)

        # modifying title as it may contain special characters which may not supported by windows
        title = yt.title
        newstr = ""
        for i in title:
            if i.isalnum() or i == " " or i == '-' or i == "_" or i == "'":
                newstr += i
        title = newstr
        # print(title)

        size720 = round(stream720.filesize_mb, 2)
        file_size_res720 = Label(search_window, text=f"File Size : {size720} MB", font=('arial', 12), bg="white")
        file_size_res720.grid(row=9, column=3)

        size360 = round(stream360.filesize_mb, 2)
        file_size_res360 = Label(search_window, text=f"File Size : {size360} MB", font=('arial', 12), bg="white")
        file_size_res360.grid(row=8, column=3)

        size128 = round(stream128.filesize_mb, 2)
        file_size_res128 = Label(search_window, text=f"File Size : {size128} MB", font=('arial', 12), bg="white")
        file_size_res128.grid(row=6, column=3)

        label3 = Label(search_window, text="", bg="white")  # to create space
        label3.grid(row=3, column=1)


        label4 = Label(search_window, text="", bg="white", pady=20)  # to create space
        label4.grid(row=5, column=2)

        audio_one = Label(search_window, text='128K (audio) : ', bg="white", font=('arial', 13))
        audio_one.grid(row=6, column=1)

        label5 = Label(search_window, text="", bg="white")  # to create space
        label5.grid(row=7, column=2)

        res_one = Label(search_window, text="720p : ", bg="white", font=('arial', 13), pady=20)
        res_one.grid(row=9, column=1)

        res_two = Label(search_window, text="360p : ", bg="white", font=('arial', 13))
        res_two.grid(row=8, column=1)


        def res_720():
            if var.get() == 0:
                # It gives 1 if check box is ticked otherwise it gives 0  -- subtitle download
                if checked_state.get():
                    subtitles.download_subtitle(yt, Download_path.get(), title)
                os.system('cls')  # clearing cmd/terminal
                search_window.iconify()
                global box_print
                box_print = 1
                print("Downloading...\n")
                try:
                    stream720.download(output_path=Download_path.get(), filename=f"{title}.mp4")
                    time.sleep(2)
                    search_window.state("zoomed")
                    desktop_notify(Download_path.get())
                    messagebox.showinfo(title="Video Downloaded",
                                        message="Video downloaded successfully..\n Thank you")
                except:
                    search_window.state("zoomed")
                    messagebox.showwarning(title="Issue", message="Error! Something unexpected occurred")
            else:
                messagebox.showwarning(title='Failed',
                                message="You need to select location to download file/files")

        def res_360():
            if var.get() == 0:
                # It gives 1 if check box is ticked otherwise it gives 0  -- subtitle download
                if checked_state.get():
                    subtitles.download_subtitle(yt, Download_path.get(), title)
                os.system('cls')  # clearing terminal/cmd
                search_window.iconify()
                global box_print
                box_print = 1
                print("Downloading...\n")
                try:
                    stream360.download(output_path=Download_path.get(), filename=f"{title}.mp4")
                    time.sleep(2)
                    search_window.state("zoomed")
                    desktop_notify(Download_path.get())
                    messagebox.showinfo(title="Video Downloaded",
                                        message="Video downloaded successfully..\n Thank you")
                except:
                    search_window.state("zoomed")
                    messagebox.showwarning(title="Issue", message="Error! Something unexpected occurred")
            else:
                messagebox.showwarning(title='Failed',
                                    message="You need to select location to download file/files")

        def audio():
            if var.get() == 0:
                os.system('cls')  # clearing cmd/terminal
                search_window.iconify()
                global box_print
                box_print = 1
                print("Downloading...\n")
                try:
                    outfile = stream128.download(output_path=Download_path.get(), filename=f"{title}.mp4")
                    base, ext = os.path.splitext(outfile)
                    new_file = base + '.mp3'
                    os.rename(outfile, new_file)
                    time.sleep(2)
                    search_window.state("zoomed")
                    desktop_notify(Download_path.get())
                    messagebox.showinfo(title="Audio Downloaded",
                                        message="Audio downloaded successfully..\n Thank you")
                except:
                    search_window.state("zoomed")
                    messagebox.showwarning(title="Issue", message="Error! Something unexpected occurred")
            else:
                messagebox.showwarning(title='Failed',
                                    message="You need to select location to download file/files")

        # Buttons
        audio_button = Button(search_window, text="Download", foreground="white", font=('arial', 13), bg="green")
        audio_button.config(command=audio, activeforeground='white', activebackground='red')
        audio_button.grid(row=6, column=2)

        res_720_button = Button(search_window, text="Download", foreground="white", font=('arial', 13), bg="green")
        res_720_button.config(command=res_720, activeforeground='white', activebackground='red')
        res_720_button.grid(row=9, column=2)

        res_360_button = Button(search_window, text="Download", foreground="white", font=('arial', 13), bg="green")
        res_360_button.config(command=res_360, activeforeground='white', activebackground='red')
        res_360_button.grid(row=8, column=2)


        # space labels
        label6 = Label(search_window, text="", bg="white")  # to create space
        label6.grid(row=10, column=1)

        label7 = Label(search_window, text="", bg="white")  # to create space
        label7.grid(row=12, column=1)



        # variable to hold on to checked state, 0 is off, 1 is on.
        checked_state = IntVar()
        isSubtitle = Checkbutton(search_window, text="Download Subtitle", variable=checked_state)
        isSubtitle.config(font=('consolas', 11), bg='#dbde40', foreground='black')
        isSubtitle.grid(row=11, column=1)


        note = Label(search_window, text='On clicking "Download" button, entire application\n will be '
                                         'minimized. Download progress will be displayed on \n'
                                         'the console that opens along with the software. Do not\n'
                                         'try to open the application during downloading as it\n'
                                         'may cause error')
        note.config(bg="white", foreground='blue')
        note.grid(row=13, column=2)

        def home_func():
            search_window.destroy()
            home.state("zoomed")

        home_button = Button(search_window, text="Home", font=('arial', 10), bg="white", command=home_func)
        home_button.grid(row=0, column=4)

        def report_issue():
            if messagebox.askyesno(title="Report an issue",
                                   message="YouTubo wants to redirect you to an external website. Proceed ?"):
                webbrowser.open_new_tab("https://github.com/abanand132/youtubo/issues")

        report_problem = Button(search_window, text="Report bug", font=('arial', 12, 'bold'), bg="cyan")
        report_problem.config(foreground='black', activebackground='black', activeforeground='white', command=report_issue)
        report_problem.grid(row=13, column=4)


        dark_mode = Button(search_window, text="🔆", font=('arial', 30), bg='white', foreground='black', borderwidth=0,
                           command=dark_mode_func1)
        dark_mode.grid(row=13, column=0)

        # set dark theme as default
        if theme_integer.get() == 0:
            dark_mode_func1()


        def on_progress(stream, chunk, bytes_remaining):
            global box_print
            total_size = stream.filesize
            bytes_downloaded = total_size - bytes_remaining
            percentage_of_completion = bytes_downloaded / total_size * 100
            ani = '⬜' * box_print
            # os.system('cls')
            print(f"{ani} {round(percentage_of_completion, 0)}%")
            box_print += 1

        yt.register_on_progress_callback(on_progress)


        # Hovering design

        res_720_button.bind("<Enter>", func=lambda e: res_720_button.config(background='yellow', foreground='black',
                                                                            font=('arial', 15)))
        res_720_button.bind("<Leave>", func=lambda e: res_720_button.config(background='green', foreground='white',
                                                                            font=('arial', 13)))

        res_360_button.bind("<Enter>", func=lambda e: res_360_button.config(background='yellow', foreground='black',
                                                                            font=('arial', 15)))
        res_360_button.bind("<Leave>", func=lambda e: res_360_button.config(background='green', foreground='white',
                                                                            font=('arial', 13)))


        audio_button.bind("<Enter>", func=lambda e: audio_button.config(background='yellow', foreground='black',
                                                                            font=('arial', 15)))
        audio_button.bind("<Leave>", func=lambda e: audio_button.config(background='green', foreground='white',
                                                                            font=('arial', 13)))

        Browse.bind("<Enter>", func=lambda e: Browse.config(background='yellow', foreground='black'))
        Browse.bind("<Leave>", func=lambda e: Browse.config(background='black', foreground='white'))

        note.bind("<Enter>", func=lambda e: note.config(background='yellow', foreground='black'))
        note.bind("<Leave>", func=lambda e: note.config(background='#1A2421', foreground='white'))

        home_button.bind("<Enter>", func=lambda e: home_button.config(background='#1A2421', foreground='white'))
        home_button.bind("<Leave>", func=lambda e: home_button.config(background='white', foreground='black'))



    except urllib.error.URLError:
        messagebox.showwarning(title="Failed!", message="We can't fetch your video.\n\n"
                                                        "Please check your Internet Connection!")
        home.state("zoomed")

    except:
        messagebox.showwarning(title="Failed", message='Unexpected Error! Please try again')

    search_window.grab_set()
