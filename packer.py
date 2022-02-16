import click
from packer_lib import zipfiles
# Creates the arguments and options
@click.command()
@click.argument('action')
@click.argument('file')
@click.option('--password', default=None, help='Password for decrypting ZIP')
def main(action, file, password):
    zipfiles.handleZip(action, file, password)
if __name__ == '__main__':
    main()