# Packer
---
Packer is a lightweight command line tool to manage zip files. It is written in 100 percent python and also includes a library for working with zip files

## How To Use

You can call packer by using *packer ACTION FILE*
- ACTION: extract, archive, list (What you want to do)
- FILE: the file you wish to manipulate

### **Optional Arguments**

--password: Password used for decrypting ZIP files

## Using the library

The library is contained in /packer_lib/ and includes a file called zipfiles
To use just call:
```python  
    from packer_lib import ZipFiles
```
### **Modules**

- extract(file, password): Extracts the given file with the given password
- archive(file): Creates a ZIP file from the given file or directory
- list(file, password): Lists all of the files inside of the given file
- setpwd(file, password): Will set the given file's password to *password*
