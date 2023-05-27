**madframe** - Functional Event Framework for Python
- ~💢 TypeCheck at runtime~ (coming soon !)
- ☮️ Non intruisive
- 💪 Modular

### Over 10 different [bindings](./madframe/bindings.py')

```python
from madframe import routine

@routine(1)
def print_hello():
    print('hello world')
```

  
### Autofill
  
```python
from madframe import setup

@setup
def initialize():
    return {"some_key": "foo"}

@routine(1)
def print_foo(some_key):
    print(some_key) # -> will print foo 
```

### Wire

```python
from madframe import wire

something_is_done_when, do_something_when = wire()

fetch = do_something_when(fetch_data)
something_is_done_when(analyze_data)

fetch # is equivalent of `analyze_data(fetch_data)`
```

[![Package test](https://github.com/6r17/madframe/actions/workflows/test.yml/badge.svg)](https://github.com/6r17/madframe/actions/workflows/test.yml)
[![pypi](https://img.shields.io/pypi/v/madframe)](https://pypi.org/project/madframe/)
![python: >3.9](https://img.shields.io/badge/python-%3E3.9-informational)
### Installation

```bash
pip3 install madframe
```

### Context
