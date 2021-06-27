import pathlib
import re
from datetime import datetime


def main():
    path = input('Enter the folder path: ')
    path = pathlib.Path(path).absolute()
    if not path.is_dir():
        print('This is not a folder path')
        return

    confirm = input(f'Are you sure you want to sort {path}? [y/N]: ')
    if confirm.strip().lower() != 'y':
        return

    items = list(path.iterdir())
    item_count = len(items)
    for n, item in enumerate(items, 1):
        print(f'{n / item_count:.1%}', end=' ')

        if item.is_dir() and re.fullmatch(r'\d{4}-\d{2}', item.name):
            print(f'Skipping {item.name}')
            continue

        print(f'Moving {item.name}')
        time = datetime.fromtimestamp(item.lstat().st_mtime)
        newpath = item.parent / time.strftime('%Y-%m')
        newpath.mkdir(exist_ok=True)
        item.rename(newpath / item.name)

    print('Done!')


if __name__ == '__main__':
    main()