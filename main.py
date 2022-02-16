import click
import zipfile
import os

# Creates the arguments and options
@click.command()
@click.argument('action')
@click.argument('file')
@click.option('--password', default=None, help='Password for decrypting ZIP')
def main(action, file, password):
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
        

if __name__ == '__main__':
    main()