from textwrap import shorten
from typing import Optional
import click
from packer_lib import ZipFiles
# Creates the arguments and options
@click.command()
@click.argument('action')
@click.argument('file', required=False)
@click.option('--password', default=None, help='Password for decrypting ZIP')
def main(action, file, password=""):
    if action == 'shell':
        shell(action, file, password)
    ZipFiles.handleZip(action, file, password)
# Function for managing the shell of packer
def shell(action, file, password):
    running = True
    while running:
        prompt = input("packer>> ")
        if prompt == 'exit':
            exit()
        promptSplit = prompt.split()
        file = promptSplit[1]
        try:
            password = promptSplit[2]
        except:
            password = ""
        action = promptSplit[0]
        
        ZipFiles.handleZip(action, file, password)

# Runs the program
if __name__ == '__main__':
    main()