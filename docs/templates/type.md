
| Attribute | Value | Detail |
| ------- | ----- | ----- |
| **name** | `{{ type.name }}` | Used in schema definitions |
{%- if type.group -%}
| **group** | `{{ type.group }}` |  |
{%- endif -%}
| **label** | {{ type.label }} (plural: {{type.plural}}) | |
| **max_length** | {{ type.max_length }} | Space to be allocated in fixed-length database definitions |
| **matchable** | {{ bool_icon(type.matchable) }} | Suitable for use in entity matching |
| **pivot** | {{ bool_icon(type.pivot) }} | Suitable for use as a pivot point for connecting to other entities |
