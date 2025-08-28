"""
A Simple Note-Taking Application For TI84 Plus CE PYTHON Calculators
by PaxLak 
Version 0.1 (08/28/2025)
"""
from ti_system import recall_list, store_list, disp_clr # type: ignore

notes = recall_list("NOTES")

def disp_notes():
    disp_clr()
    if not notes:
        print("No notes available.")
        input("Press Enter to continue...")
    else:
        page = 0
        while True:
            disp_clr()
            start = page * 3
            end = start + 3
            current_notes = notes[start:end]
            for idx, note in enumerate(current_notes, start=1):
                print(str(start + idx) + ". " + str(note))
            print("\n+ Next Page  - Prev Page  0 Back")
            action = input("Choose: ")
            if action == '+':
                if end < len(notes):
                    page += 1
            elif action == '-':
                if page > 0:
                    page -= 1
            elif action == '0':
                break

while True:
    disp_clr()
    print("1. View Notes")
    print("2. Add Note")
    print("3. Delete Note")
    print("4. Exit")
    choice = input("Choose an option (1-4): ")
    if choice == '1':
        disp_clr()
        disp_notes()
    elif choice == '2':
        disp_clr()
        note = input("Enter your note: ")
        if note:
            notes.append(note)
            store_list("NOTES", notes)
            print("Note added!")
        else:
            print("No note entered.")
        input("Press Enter to continue...")
    elif choice == '3':
        disp_clr()
        if not notes:
            print("No notes to delete.")
            input("Press Enter to continue...")
        else:
            disp_notes()
            try:
                idx = int(input("Enter note number to delete (0 to cancel): "))
                if idx == 0:
                    continue
                if 1 <= idx <= len(notes):
                    del notes[idx - 1]
                    store_list("NOTES", notes)
                    print("Note deleted!")
                else:
                    print("Invalid note number.")
            except ValueError:
                print("Invalid input.")
            input("Press Enter to continue...")
    elif choice == '4':
        disp_clr()
        print("Exiting...")
        break
    else:
        disp_clr()
        print("Invalid choice!")
        input("Press Enter to continue...")