from app.modules.file_organizer import organize_folder


folder = input("Enter full folder path: ")
result = organize_folder(folder)
print(result)
