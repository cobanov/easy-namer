
# PyRename

Incremental file renamer written in Python. 


## Usage/Examples

```bash
python pyname.py --path /path/to/folder --prefix <prefix> --suffix <suffix> --digits <zero padding>
```

```bash
Files will be renamed like this:
test_folder/extent.txt    ===>    test_folder/hey_0000_bye.txt
test_folder/toyota.txt    ===>    test_folder/hey_0001_bye.txt
test_folder/dance.txt     ===>    test_folder/hey_0002_bye.txt

Do you want to rename files? (y/n) y
```

## Reference

| Parameter | Type     | Description                | Default |
| :-------- | :------- | :------------------------- | :------ |
| `path`    | `string` | **Required**               |         |
| `prefix`  | `string` | **Optional**               |' '      |
| `suffix`  | `string` | **Optional**               |' '      |
| `digits`  | `string` | **Optional**               | 3       |


## License

[MIT](https://choosealicense.com/licenses/mit/)

