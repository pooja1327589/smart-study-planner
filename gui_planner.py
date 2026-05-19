from tkinter import *

window = Tk()

window.title("Smart Study Planner")

window.geometry("500x600")


# ---------------- TITLE ----------------

title = Label(window, text="Smart Study Planner", font=("Arial", 18))
title.pack(pady=10)


# ---------------- SUBJECT ----------------

subject_label = Label(window, text="Subject")
subject_label.pack()

subject_entry = Entry(window, width=30)
subject_entry.pack()


# ---------------- STUDY TIME ----------------

time_label = Label(window, text="Study Time")
time_label.pack()

time_entry = Entry(window, width=30)
time_entry.pack()


# ---------------- DEADLINE ----------------

deadline_label = Label(window, text="Deadline")
deadline_label.pack()

deadline_entry = Entry(window, width=30)
deadline_entry.pack()


# ---------------- TASK DISPLAY BOX ----------------

task_list = Text(window, height=15, width=55)
task_list.pack(pady=10)


# ---------------- ADD TASK FUNCTION ----------------

def add_task():

    subject = subject_entry.get()
    study_time = time_entry.get()
    deadline = deadline_entry.get()

    if subject == "" or study_time == "" or deadline == "":
        task_list.insert(END, "Please fill all fields!\n")
        return

    task = subject + " - " + study_time + " - " + deadline

    task_list.insert(END, task + "\n")

    file = open("tasks.txt", "a")

    file.write(task + "\n")

    file.close()

    # Clear input boxes
    subject_entry.delete(0, END)
    time_entry.delete(0, END)
    deadline_entry.delete(0, END)


# ---------------- CLEAR ALL TASKS FUNCTION ----------------

def clear_tasks():

    task_list.delete(1.0, END)

    file = open("tasks.txt", "w")
    file.close()


# ---------------- COMPLETE LAST TASK FUNCTION ----------------

def complete_task():

    content = task_list.get("1.0", END)

    lines = content.split("\n")

    if len(lines) > 1:

        lines.pop(-2)

        task_list.delete("1.0", END)

        for line in lines:
            if line != "":
                task_list.insert(END, line + "\n")

        file = open("tasks.txt", "w")

        for line in lines:
            if line != "":
                file.write(line + "\n")

        file.close()


# ---------------- BUTTONS ----------------

add_button = Button(window, text="Add Task", width=20, command=add_task)
add_button.pack(pady=5)

complete_button = Button(window, text="Complete Last Task", width=20, command=complete_task)
complete_button.pack(pady=5)

clear_button = Button(window, text="Clear All Tasks", width=20, command=clear_tasks)
clear_button.pack(pady=5)


# ---------------- RUN WINDOW ----------------

window.mainloop()