import os
import click

def rename(path, prefix, suffix, digits):
    for count, filename in enumerate(os.listdir(path)):
            file_path = f'{path}/{filename}'
            ext = filename.split('.')[-1]
            if prefix and not suffix:
                os.rename(file_path, f'{path}/{prefix}_{count:0{digits}d}.{ext}')
            
            elif suffix and not prefix:
                os.rename(file_path, f'{path}/{count:0{digits}d}_{suffix}.{ext}')
            
            elif prefix and suffix:
                os.rename(file_path, f'{path}/{prefix}_{count:0{digits}d}_{suffix}.{ext}')
            
            elif not prefix and not suffix:
                os.rename(file_path, f'{path}/{count:0{digits}d}.{ext}')

def preview(path, prefix, suffix, digits):
    print('Files rename like this:')
    for count, filename in enumerate(os.listdir(path)[:3]):
        file_path = f'{path}/{filename}'
        ext = filename.split('.')[-1]
        if prefix and not suffix:
            print(file_path, '===>', f'{path}/{prefix}_{count:0{digits}d}.{ext}')
        
        elif suffix and not prefix:
            print(file_path, '===>', f'{path}/{count:0{digits}d}_{suffix}.{ext}')
        
        elif prefix and suffix:
            print(file_path, '===>', f'{path}/{prefix}_{count:0{digits}d}_{suffix}.{ext}')
        
        elif not prefix and not suffix:
            print(file_path, '===>', f'{path}/{count:0{digits}d}.{ext}')

    choice = input('Do you want to rename files? (y/n)')
    return choice


@click.command()
@click.option("--path", help="path to folder with files")
@click.option("--prefix", default='', help="prefix for files")
@click.option("--suffix", default='', help="suffix for files")
@click.option("--digits", default=3, help="Number of digits")
def main(path, prefix, suffix, digits):

    if os.path.exists(path):
        if preview(path, prefix, suffix, digits) == 'y':
            rename(path, prefix, suffix, digits)
        else:
            print('Aborted')
    else:
        print('Folder does not exist')

if __name__ == '__main__':
    main()