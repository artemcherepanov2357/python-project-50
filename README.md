### Hexlet tests and linter status:
[![Actions Status](https://github.com/artemcherepanov2357/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/artemcherepanov2357/python-project-50/actions)

## Usage Example

[![Demo](https://asciinema.org/a/n9boKSPyMVRlPbvl1IjaS6nPI.svg)](https://asciinema.org/a/n9boKSPyMVRlPbvl1IjaS6nPI)

### As a CLI utility
```bash
gendiff file1.json file2.json
```

Output:
```
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

### As a library
```python
from gendiff import generate_diff

diff = generate_diff('file1.json', 'file2.json')
print(diff)
```