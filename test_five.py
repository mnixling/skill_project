import tkinter as tk
import pickle



main_window = tk.Tk() # creates main window
main_window.geometry('450x550+250-120') # creates size of window

skill_input_text = tk.StringVar() # ?What does this mean?
time_input = tk.StringVar()
row_counter = 0
column_counter = 0
#Make 4x4 grid
main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.rowconfigure(0, weight=1)
main_window.rowconfigure(1, weight=1)
# add input box
add_skill_entry = tk.Entry(main_window, bg="gray", textvariable=skill_input_text)
add_skill_entry.grid(column=0, row=0, sticky="s")
# add input box
time_tracker = tk.Entry(main_window, bg="gray", textvariable=time_input)
time_tracker.grid(column=0, row=1, sticky="n")
# display skill and graph
frame1 = tk.Frame(main_window, bg="white", height="300", width="300")
frame1.grid_propagate(0)
frame1.grid(row=0, column=1, rowspan=2)

skill_dictionary = {}
#print(skill_dictionary == {})

# add input from skill_input to frame: the characters, background, and a rectangle. And, adding time to the rectangle parameter.
def add_to_frame():
    global row_counter
    global column_counter
    entry_text = skill_input_text.get()
    skill_input_text.set("")
    time = skill_dictionary['ducks'][0]  # accessing the key value for time at its index of 0 for time = x0
    time_input.set("")
	
    for key in skill_dictionary.keys():
        x0 = time
        y0 = skill_dictionary[key][0]
        print(f'y0 is {y0}')
        x1 = skill_dictionary[key][1]
        y1 = skill_dictionary[key][2]

        if skill_dictionary == {}:  # first time through enter
          # if column_counter in (0, 1, 2, 3):
          print('FISH')
          frame1.rowconfigure(row_counter, weight=1)
          frame1.columnconfigure(column_counter, weight=1)
          new_label = tk.Canvas(frame1, width=150, height=50)
          new_label.create_rectangle(x0, y0, x1, y1, fill="red")
          new_label.create_text(30, 27, text=entry_text)
          skill_dictionary[entry_text] = []
          skill_dictionary.setdefault(entry_text, []).append(time)

          new_label.grid(row=row_counter, column=column_counter, padx=5, pady=10)
          column_counter += 1
          skill_dictionary.setdefault(entry_text, []).append(column_counter)
          skill_dictionary.setdefault(entry_text, []).append(row_counter)
          if column_counter == 3:
              column_counter = 0
              row_counter += 1

        else:
          print('TESTY')
          frame1.rowconfigure(row_counter, weight=1)
          frame1.columnconfigure(column_counter, weight=1)
          new_label = tk.Canvas(frame1, width=150, height=50)
          print(f'xo is {x0}')  # this printed
          new_label.create_rectangle(x0, y0, x1, y1, fill="red") # this did not crash
          new_label.create_text(30, 27, text=entry_text)
          skill_dictionary[entry_text] = []
          skill_dictionary.setdefault(entry_text, []).append(time)

          new_label.grid(row=row_counter, column=column_counter, padx=5, pady=10)
          column_counter += 1
          skill_dictionary.setdefault(entry_text, []).append(column_counter)
          skill_dictionary.setdefault(entry_text, []).append(row_counter)
          if column_counter == 3:
              column_counter = 0
              row_counter += 1



# add time button
# add_time_button = tk.Button(main_window, text="ADD TIME", command=add_to_frame)
# add_time_button.grid(column=0, row=2, sticky="n")

# add skill button
# add_skill_button = tk.Button(main_window, text="ADD SKILL", command=add_to_frame)
# add_skill_button.grid(column=0, row=1, sticky="n")

# submit button for both
submit_button = tk.Button(main_window, text="Submit", command=add_to_frame)
submit_button.grid(column=0, row=1, sticky="s")


#print(skill_dictionary)
skill_dictionary_pickeled = pickle.dumps(skill_dictionary)
skill_dictionary_unpickle = pickle.loads(skill_dictionary_pickeled)

#with open('mypickle.pickle', 'wb') as f_out:
#  print('Pickling file')
#  pickle.dump(skill_dictionary, f_out, protocol=pickle.HIGHEST_PROTOCOL)
#  print('file pickled')

with open('mypickle.pickle', 'rb') as pickle_file:
  print('opening file')
  content = pickle.load(pickle_file)
  skill_dictionary = content
  print(skill_dictionary['ducks'][0])
  
  #for key, value in content.items():
   # print(key, value)
  
add_to_frame()  # dictionary changed size during iteration
	
#add_to_frame()
#for key, value in skill_dictionary_unpickle.items():
#   print(key, value[0])

# print(f'skill diction includes:'
#       f'skill name{skill_dictionary.keys()}'
#       f'skill ')


#  you have to cd to directory pyinstaller --onefile -w 'test_four.py'
main_window.mainloop() # makes it so the main window opens (and stays open?)