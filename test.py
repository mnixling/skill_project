import tkinter

main_window = tkinter.Tk()
main_window.geometry('640x480+320-120')
main_window.configure(bg='black')

skill_name = tkinter.StringVar()


def s_entry():
    skill = skill_name.get()
    skill_name.set('')
    test_label = tkinter.Label(main_window, text=skill)
    test_label.grid(rowspan=3, columnspan=3)


main_label = tkinter.Label(main_window, text='Skill Tracker', bg='black', fg='green', font='bold')
main_label.grid(row=0, column=0, columnspan=5)
skill_label = tkinter.Label(main_window, text='Skill', bg='black', fg='green')
skill_label.grid(row=1, column=4, sticky='w')
skill_entry = tkinter.Entry(main_window, textvariable=skill_name)
skill_entry.grid(row=1, column=4)
add_skill_button = tkinter.Button(main_window, text='Add Skill', bg='black', fg='green', command=s_entry)
add_skill_button.grid(row=2, column=4)




main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.columnconfigure(2, weight=1)
main_window.columnconfigure(3, weight=1)
main_window.columnconfigure(4, weight=1)
main_window.rowconfigure(0)#, weight=1)
main_window.rowconfigure(1)#, weight=10)
main_window.rowconfigure(2)#, weight=1)
main_window.rowconfigure(3)#, weight=3)
main_window.rowconfigure(4)#, weight=3)





main_window.mainloop()