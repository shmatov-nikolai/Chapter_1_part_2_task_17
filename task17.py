'''
Write the code which will write excepted data to files below
For example given offices of Google:
1) google_kazakstan.txt
2) google_paris.txt
3)google_uar.txt
4)google_kyrgystan.txt
5)google_san_francisco.txt
6)google_germany.txt
7)google_moscow.txt
8)google_sweden.txt
When the user will say “Hello”
Your code must communicate and give a choice from listed offices. After it
has to receive a complain from user, and write it to file chosen by user.
Hint: Use construction “with open”
'''


def read_write_some_file(key):
    files_name = {1: 'google_kazakstan.txt', 2: "google_paris.txt", 4: "google_kyrgystan.txt", 3: "google_uar.txt"}
    if key not in files_name:
        files_name[key] = input("выбранного файла не существует, создадим новый, введите имя файла с раширением имя_файла.txt:")
    with open(files_name[key], "w") as somefile:
        somefile.write(input('введите текст для записи: '))
        print(f"Ваш текст был записан в файл с именем: {files_name[key]} ")
        
vibor_key = int(input('''
 Выберите файл из списка:
1. google_kazakstan.txt
2. google_paris.txt
3. google_uar.txt
4. google_kyrgystan.txt

введите номер файла:'''))
read_write_some_file(vibor_key)