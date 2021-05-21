import tkinter as tk

main_window = tk.Tk()  # creates the window
main_window.geometry('640x480+250-120')  # window size by pixel and placement

# Creates all the rows and columns of the window grid
main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.columnconfigure(2, weight=1)
main_window.columnconfigure(3, weight=1)
main_window.rowconfigure(0, weight=1)
main_window.rowconfigure(1, weight=1)
main_window.rowconfigure(2, weight=1)
main_window.rowconfigure(3, weight=1)

# Creates labels for each cell in the grid
label_1 = tk.Label(main_window, text='Label 1')
label_1.grid(row=0, column=0)
label_2 = tk.Label(main_window, text='Label 2')
label_2.grid(row=0, column=1)
label_3 = tk.Label(main_window, text='Label 3')
label_3.grid(row=0, column=2)
label_4 = tk.Label(main_window, text='Label 4')
label_4.grid(row=1, column=0)
label_5 = tk.Label(main_window, text='Label 5')
label_5.grid(row=1, column=1)
label_6 = tk.Label(main_window, text='Label 6')
label_6.grid(row=1, column=2)
# label_7 = tk.Label(main_window, text='Label 7')
# label_7.grid(row=1, column=2)
# label_8 = tk.Label(main_window, text='Label 8')
# label_8.grid(row=1, column=3)
# label_5 = tk.Label(main_window, text='Label 9')
# label_5.grid(row=2, column=0)
# label_6 = tk.Label(main_window, text='Label 10')
# label_6.grid(row=2, column=1)
# label_7 = tk.Label(main_window, text='Label 11')
# label_7.grid(row=2, column=2)
# label_8 = tk.Label(main_window, text='Label 12')
# label_8.grid(row=2, column=3)
# label_5 = tk.Label(main_window, text='Label 13')
# label_5.grid(row=3, column=0)
# label_6 = tk.Label(main_window, text='Label 14')
# label_6.grid(row=3, column=1)
# label_7 = tk.Label(main_window, text='Label 15')
# label_7.grid(row=3, column=2)
# label_8 = tk.Label(main_window, text='Label 16')
# label_8.grid(row=3, column=3)

skill_frame = tk.LabelFrame(main_window, text='LABEL FRAME')  # Creates the label frame
skill_frame.grid(row=0, column=3)

skill_frame.rowconfigure(0, weight=1)
skill_frame.rowconfigure(1, weight=1)

skill_label = tk.Label(skill_frame, text='SKILL')  # creates the label
skill_label.grid(row=0)
label_test = tk.Label(skill_frame, text='TEST')  # creates the label
label_test.grid(row=1)



main_window.mainloop()
