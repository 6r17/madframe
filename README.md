**madframe** - Functional State-Machine Framework for Python
- ~💢 TypeCheck at runtime~ (coming soon !)
- ☮️ Non intruisive
- 🧰 Functionnal
- 🕐 Event-Based

## Includes

### 🤖 Autofill

Autofill is the process of automaticaly composing a function usage deduced from the prototype naming and a given context.

```python
from madframe.autofill import autofill

context = {"value": "foo"}
def some_function(value):
    print(value)

await autofill(some_function, args=[], context=context) # notice that we don't pass any argument
> "foo"
# autofill undertand it has to retrieve the value from context if you don't specify it

await autofill(some_function, args["bar"], context=context) # we pass an argument
> "bar"
```
💁 **every madframe decorator uses `autofill`**
  
### 🕙 Routine
  
```python
from madframe.bindings import setup

@setup
def initialize():
    return {"some_key": "foo"}

@routine(1)
def print_foo(some_key):
    print(some_key) # -> prints "foo"
```

### 🏗️ Setup

Setup is used to define function to be ran at start-up. Those executions block the start-up and will abort the lauch if they fail.

### 📝 Perpetuate

`perpetuate` is `autofill` but the context is also updated with the result of the function (given it's a `dict`)

### 🚩 Wire

```python
from madframe.bindings import wire

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
