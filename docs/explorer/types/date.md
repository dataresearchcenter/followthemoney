# Date

Dates are given in a basic ISO 8601 date or date-time format, `YYYY-MM-DD` or `YYYY-MM-DDTHH:MM:SS`. In source data, we find varying degrees of precision: some events may be defined as a full timestamp (`2021-08-25T09:26:11`), while for many we only know a year (`2021`) or month (`2021-08`). Such *date prefixes* are carried through and used to specify date precision as well as the actual value.

### Usage

```python
from followthemoney import registry

assert registry.validate('2023-01-14')
assert not registry.validate('2023-20-14')

# Helpers:
assert registry.to_datetime('2023-01-14').year == '2023'
```