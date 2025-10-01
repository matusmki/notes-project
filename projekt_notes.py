def new_window():
    import os
    os.system('cls')

FILE_NAME = "project_nts.txt"
counter = 1

start = """📁  Simple Notes Manager
=========================
1️⃣  List Notes
2️⃣  Add a Note
3️⃣  Delete a Note
4️⃣  Exit"""


def type_zero():
    while True:
        try:
            zero = int(input("Press 0 to continue: "))
            if zero != 0:
                continue
            else:
                break
        except ValueError:
            print("Must be 0")


def add_notes():
    with open("project_nts.txt", "r", encoding="utf-8") as subor:
        lines = [line.strip() for line in subor.readlines() if line.strip()]

    if len(lines) == 0:
        print("Any notes yet")
        return

    print("📝 List of notes📝 :")
    for i in range(0, len(lines), 3):
        note = lines[i:i+3]
        print(f"\n📝 NOTE NUMBER {(i // 3) + 1}")
        for riadok in note:
            print(riadok)

        
def existing_notes():
    with open("project_nts.txt","r") as another_file:
        amount_of_lines = another_file.readlines()
        if len(amount_of_lines) == 0:
            print("No notes to delete")


def delete_notes():
    with open("project_nts.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        number = int(input("Enter the number of note to delete: "))
        index = (number -1) * 3
        if index < 0 or index + 2 >= len(lines):
            print("❌ Invalid number of note.")
            return
        del lines[index:index+3]
        with open("project_nts.txt", "w", encoding="utf-8") as f:
            f.writelines(lines)



def question_analyzer(question):
    if question == 4:
        print("Goodbye👋")
        return False
    
    elif question == 1:
        new_window()
        print("✅ Welcome to List Notes!✅\n===========================")
        add_notes()

    elif question == 2:
        new_window()
        print("📝 Add New Note📝\n=================\n")
        date = input("Note date: ")
        note_input = input("Note: ")
        is_important = input("Is note important: ")
        print()
        with open("project_nts.txt","a", encoding = "utf-8") as file:
            file.write(f"Date: {date}\n")
            file.write(f"Note: {note_input}\n")
            file.write(f"Is note important: {is_important}\n")

    else:
        new_window()
        print("🗑️  Delete Note🗑️\n==================")
        existing_notes()
        delete_notes()
    menu = input("Press Enter to return to main menu: ")
    return True


while True:
    new_window()
    print(start)
    try:
        question = int(input("Choose an option (1-4): "))
        if question not in range(1, 5):
            continue
    except ValueError:
        print("Must be number (1-4)\nTry again")
        if not type_zero():
            continue
    if not question_analyzer(question):
        break
    else:
        continue