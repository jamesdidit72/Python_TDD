# Test Driven Development
## pytest and unittest
### use pip to install the packages

**TDD**
- Starts with RED (everything failing)
- then GREEN to write the code to pass the test
- BLUE is refactoring - then start again

- `unittest` and `pytest`

#### First steps
- Let's create a file to create out tests
- Then we will create a file to add functionality to pass the tests
- Basic calculator to add basic functions


#### example of tests
```python
import pytest
import unittest

from TDD_simple_calc import SimpleCalc

class Calc_Test(unittest.TestCase):  # helps us test

    calc_test = SimpleCalc()

    def test_add(self):
        # this naming convention is essential as 'test' is the word that we need to use when naming tests so python interpreter can recognise it so it can run
        self.assertEqual(self.calc_test.add(2, 4), 6)  # 2 + 4 = 6

    def test_subtract(self):
        self.assertEqual(self.calc_test.subtract(4, 2), 2)  # 4 - 2 = 2

    def test_multiply(self):
        self.assertEqual(self.calc_test.multiply(2, 2), 4)  # 2 * 2 = 4

    def test_divide(self):
        self.assertEqual(self.calc_test.divide(6, 3), 2)  # 4 / 2 = 2
```
#### how to run:
- right click and click run
- command ` python -m unittest discover -v`
- `python -m unittest`

### Functionality to pass the tests
```python
class SimpleCalc:
    def add(self, val_1, val_2):
        return val_1 + val_2

    def subtract(self, val_1, val_2):
        return val_1 - val_2

    def multiply(self, val_1, val_2):
        return val_1 * val_2

    def divide(self, val_1, val_2):
        return val_1 / val_2
```
#### Run tests again to ensure that all 4 tests pass using:
- command `python -m unittest`
- 