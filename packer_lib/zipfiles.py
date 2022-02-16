import zipfile
import os
import click

def extract(file, password=""):
    """Extracts the given archive with the given password if needed"""
    with zipfile.ZipFile(file, 'r') as zipObj:
            os.mkdir(file[0:-4])
            zipObj.extractall(file[0:-4], pwd=bytes(password, 'utf-8'))
def list(file):
    """Lists all files in a given zip file with extra data"""
    with zipfile.ZipFile(file, 'r') as zipObj:
            files = zipObj.infolist()
            print(f"{'File Name':<15} | {'Date Modified':<25} | {'Compressed Size':<17} | {'Real Size':<5}")
            for elem in files:
                dateTime = elem.date_time
                year = dateTime[0]
                month = dateTime[1]
                day = dateTime[3]
                hour = dateTime[4]
                minute = dateTime[5]
                if minute < 10:
                    minute = f"0{minute}"
                formattedDatetime = f"{month}/{day}/{year} {hour}:{minute}"
                print(f"{elem.filename:<15} | {formattedDatetime:<25} | {elem.compress_size:<17} | {elem.file_size:<5}")
def archive(file):
    """Creates a zipfile out of the given file/directory"""
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
def setpwd(file, password):
    """Sets the password for the given zipfile"""
    
    with zipfile.ZipFile(file, 'w') as zipObj:
        zipObj.setpassword(bytes(password, 'utf-8'))

def handleZip(action, file, password=""):
    if file != None:
        if not os.path.exists(file):
            print(f"ERROR: '{file}' does not exist")
            return
    if password == None:
        password = ""
    # Extract function
    if action == 'extract':
        if file == None:
            print("ERROR: No File Specified")
        extract(file, password)
    # Lists all files in zip file
    elif action == 'list':
        if file == None:
            print("ERROR: No File Specified")
        list(file)
    # Creates a ZIP file out of a file or folder specified
    elif action == 'archive':
        if file == None:
            print("ERROR: No File Specified")
        archive(file)
    # Sets the password for the given ZIP file
    elif action == 'setpwd':
        if file == None:
            print("ERROR: No File Specified")
        setPwd = click.prompt("Please Enter Password", hide_input=True, confirmation_prompt=True, )
        setpwd(file, setPwd)

