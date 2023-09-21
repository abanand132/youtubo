
# Dark mode function of main.py file

def dark_mode_func_main(home, sub_heading_label, link_entry, note1, label1,
                label2, label3, label4, label5, label6, label7, video_link, playlist_link, playlist_list,
                space_label, close, clear_search_video, clear_search_playlist, yt_version, img_label):
    home.config(bg="#1A2421")
    sub_heading_label.config(bg='#1A2421', foreground='white')
    link_entry.config(bg='#1A2421', foreground='white', highlightthickness=1, highlightbackground='cyan',
                      insertbackground='white', highlightcolor='red')
    note1.config(bg="yellow")
    video_link.config(bg='#1A2421', foreground='yellow')
    playlist_link.config(bg='#1A2421', foreground='yellow')
    playlist_list.config(bg="#1A2421", insertbackground="white", foreground='white', highlightthickness=1,
                         highlightbackground='cyan', highlightcolor='red')
    space_label.config(bg='#1A2421')
    label1.config(bg='#1A2421')
    label2.config(bg='#1A2421')
    label3.config(bg='#1A2421')
    label4.config(bg='#1A2421')
    label5.config(bg='#1A2421')
    label6.config(bg='#1A2421')
    label7.config(bg='#1A2421')
    close.config(bg='black', foreground='white')
    close.bind("<Leave>", func=lambda e: close.config(background='black', foreground='white'))
    clear_search_video.config(bg='black', foreground='white')
    clear_search_video.bind("<Leave>", func=lambda e: clear_search_video.config(background='black', foreground='white'))
    clear_search_playlist.config(bg='black', foreground='white')
    clear_search_playlist.bind("<Leave>", func=lambda e: clear_search_playlist.config(background='black', foreground='white'))
    yt_version.config(bg="#1A2421", foreground="white")
    img_label.config(foreground="white", bg="#1A2421")

def back_to_normal_main(home, sub_heading_label, link_entry, note1, label1,
                   label2, label3, label4, label5, label6, label7, video_link, playlist_link, playlist_list,
                        space_label, close, clear_search_video, clear_search_playlist, yt_version, img_label):
    home.config(bg="white")
    # heading_label.config(bg='white', foreground='red')
    sub_heading_label.config(bg='white', foreground='blue')
    link_entry.config(bg='white', foreground='black', highlightthickness=1, highlightbackground="black",
                      highlightcolor='red', insertbackground='black')
    note1.config(bg='yellow')
    video_link.config(bg='white', foreground='black')
    playlist_link.config(bg='white', foreground='black')
    playlist_list.config(bg="white", insertbackground="black", foreground='black', highlightthickness=1,
                         highlightbackground="black", highlightcolor='red')
    space_label.config(bg='white')
    label1.config(bg='white')
    label2.config(bg='white')
    label3.config(bg='white')
    label4.config(bg='white')
    label5.config(bg='white')
    label6.config(bg='white')
    label7.config(bg='white')
    close.config(bg='white', foreground='black')
    clear_search_video.config(bg='white', foreground='black')
    clear_search_playlist.config(bg='white', foreground='black')
    yt_version.config(bg='white', foreground='black')
    img_label.config(foreground="black", bg="white")




# Dark mode function of playlist_download.py file

def dark_mode_func_playlist(heading_label, video_title, video_title_res, owner, total_videos,
            res_one, label1, label2, label3, Browse, home_button, dark_mode_btn,  play_win):
    play_win.config(bg='#1A2421')
    heading_label.config(bg='#1A2421', foreground='white')
    video_title.config(bg='#1A2421', foreground='yellow')
    video_title_res.config(bg='#1A2421', foreground='cyan')
    owner.config(bg='#1A2421', foreground='deep pink')
    total_videos.config(bg='#1A2421', foreground='yellow')
    res_one.config(bg='#1A2421', foreground='yellow')
    Browse.config(bg="black", foreground='white')
    Browse.bind("<Leave>", func=lambda e: Browse.config(background='black', foreground='white'))
    home_button.config(bg='yellow', foreground='black')
    dark_mode_btn.config(bg='#1A2421', foreground='white')
    label1.config(bg='#1A2421')
    label2.config(bg='#1A2421')
    label3.config(bg='#1A2421')



def back_to_normal_playlist(heading_label, video_title, video_title_res, owner, total_videos,
            res_one, label1, label2, label3, Browse, home_button, dark_mode_btn, play_win):
    play_win.config(bg='white')
    heading_label.config(bg='white', foreground='black')
    video_title.config(bg='white', foreground='black')
    video_title_res.config(bg='white', foreground='blue')
    owner.config(bg='white', foreground='black')
    total_videos.config(bg='white', foreground='indigo')
    res_one.config(bg='white', foreground='black')
    Browse.config(bg="black", foreground='white')
    Browse.bind("<Leave>", func=lambda e: Browse.config(background='black', foreground='white'))
    home_button.config(bg='white', foreground='black')
    dark_mode_btn.config(bg='white', foreground='black')
    label1.config(bg='white')
    label2.config(bg='white')
    label3.config(bg='white')


# Dark mode functions of search_page.py file


def dark_mode_func_search(search_window, space_label, heading_label, video_title, video_title_res, file_size_res360, file_size_res720,
    file_size_res128, Browse, note, audio_one, label2, label3, label4, label5, label6, label7, res_one,
                          res_two, home_button):

    search_window.config(bg='#1A2421')
    space_label.config(bg="#1A2421", foreground='white')
    heading_label.config(bg="#1A2421", foreground='white')
    video_title.config(bg='#1A2421', foreground='yellow')
    video_title_res.config(bg="#1A2421", foreground='cyan')
    file_size_res360.config(bg='#1A2421', foreground='white')
    file_size_res720.config(bg='#1A2421', foreground='white')
    file_size_res128.config(bg='#1A2421', foreground='white')
    Browse.config(bg="black", foreground='white')
    Browse.bind("<Leave>", func=lambda e: Browse.config(background='black', foreground='white'))
    note.config(bg='#1A2421', foreground='white')
    note.bind("<Leave>", func=lambda e: note.config(background='#1A2421', foreground='white'))
    audio_one.config(bg='#1A2421', foreground='yellow')
    label2.config(bg="#1A2421")
    label3.config(bg="#1A2421")
    label4.config(bg="#1A2421")
    label5.config(bg="#1A2421")
    label6.config(bg="#1A2421")
    label7.config(bg="#1A2421")

    res_one.config(bg='#1A2421', foreground='yellow')
    res_two.config(bg='#1A2421', foreground='yellow')
    home_button.config(bg="black", foreground='white')
    home_button.bind("<Leave>", func=lambda e: home_button.config(bg='black', foreground="white"))



def back_to_normal_search(search_window, space_label, heading_label, video_title, video_title_res, file_size_res360, file_size_res720,
    file_size_res128, Browse, note, audio_one, label2, label3, label4, label5, label6, label7, res_one,
                          res_two, home_button):
    search_window.config(bg='white')
    space_label.config(bg="white", foreground='black')
    heading_label.config(bg="white", foreground='black')
    video_title.config(bg='white', foreground='black')
    video_title_res.config(bg="white", foreground='blue')
    file_size_res360.config(bg='white', foreground='black')
    file_size_res720.config(bg='white', foreground='black')
    file_size_res128.config(bg='white', foreground='black')
    Browse.config(bg="black", foreground='white')
    Browse.bind("<Leave>", func=lambda e: Browse.config(background='black', foreground='white'))
    note.config(bg='white', foreground='blue')
    note.bind("<Leave>", func=lambda e: note.config(background='white', foreground='blue'))
    audio_one.config(bg='white', foreground='black')
    label2.config(bg="white")
    label3.config(bg="white")
    label4.config(bg="white")
    label5.config(bg="white")
    label6.config(bg="white")
    label7.config(bg="white")
    res_one.config(bg='white', foreground='black')
    res_two.config(bg='white', foreground='black')
    home_button.config(bg="white", foreground='black')
