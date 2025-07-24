### Hexlet tests and linter status:
[![Actions Status](https://github.com/artemcherepanov2357/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/artemcherepanov2357/python-project-50/actions)

## Пример использования

### Как CLI-утилита
```bash
gendiff file1.json file2.json
```

Вывод:
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

### Как библиотека
```python
from gendiff import generate_diff

diff = generate_diff('file1.json', 'file2.json')
print(diff)
```