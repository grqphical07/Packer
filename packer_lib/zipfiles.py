import zipfile
import os
import click

def handleZip(action, file, password):
    if password == None:
        password = ""
    # Extract function
    if action == 'extract':
        with zipfile.ZipFile(file, 'r') as zipObj:
            os.mkdir(file[0:-4])
            zipObj.extractall(file[0:-4], pwd=bytes(password, 'utf-8'))
    # Lists all files in zip file
    elif action == 'list':
        with zipfile.ZipFile(file, 'r') as zipObj:
            files = zipObj.infolist(pwd=bytes(password, 'utf-8'))
            print(f"{'File Name':<15} | {'Date Modified':<25} | {'Compressed Size':<17} | {'Real Size':<5}")
            for elem in files:
                print(f"{elem.filename:<15} | {str(elem.date_time):<25} | {elem.compress_size:<17} | {elem.file_size:<5}")
    # Creates a ZIP file out of a file or folder specified
    elif action == 'archive':
        filename = str(os.path.basename(file))[0:-4] + '.zip'
        if os.path.isdir(file):
            filename = str(os.path.basename(file)) + '.zip'
            with zipfile.ZipFile(filename, 'w') as zipObj:
                for fileA in os.listdir(file):
                    zipObj.write(file +"/"+file)
        else:
            filename = str(file)[0:-4]
            with zipfile.ZipFile(filename + '.zip', 'w') as zipObj:
                zipObj.write(file)
    # Sets the password for the given ZIP file
    elif action == 'setpwd':
        setPwd = click.prompt("Please Enter Password:", hide_input=True, confirmation_prompt=True, )
        with zipfile.ZipFile(file, 'w') as zipObj:
            zipObj.setpassword(bytes(setPwd, 'utf-8'))
    elif action == 'shell':
        shell(action, file, password)
def shell(action, file, password):
    running = True
    while running:
        prompt = input("packer>> ")
        if action == 'exit':
            running = False
        promptSplit = prompt.split()
        file = promptSplit[1]
        try:
            password = promptSplit[2]
        except:
            password = ""
        action = promptSplit[0]
        
        handleZip(action, file, password)