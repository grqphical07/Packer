import click
import zipfile
import os


format_size = 15

# Creates the arguments and options
@click.command()
@click.argument('action')
@click.argument('file')
def main(action, file):
    # Extract function
    if action == 'extract':
        with zipfile.ZipFile(file, 'r') as zipObj:
            os.mkdir(file[0:-4])
            zipObj.extractall(file[0:-4])
    # Lists all files in zip file
    elif action == 'list':
        with zipfile.ZipFile(file, 'r') as zipObj:
            files = zipObj.infolist()
            print(f"{'File Name':<15} | {'Date Modified':<25} | {'Compressed Size':<17} | {'Real Size':<5}")
            for elem in files:
                print(f"{elem.filename:<15} | {str(elem.date_time):<25} | {elem.compress_size:<17} | {elem.file_size:<5}")
    elif action == 'archive':
        filename = str(os.path.basename(file))[0:-4] + '.zip'
        if os.path.isdir(file):
            filename = str(os.path.basename(file)) + '.zip'
            with zipfile.ZipFile(filename, 'w') as zipObj:
                for fileA in os.listdir(file):
                    zipObj.write(file +"/"+fileA)
        

if __name__ == '__main__':
    main()