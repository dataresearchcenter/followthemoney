# Model Explorer

Explore the default data model shipped with FollowTheMoney. It currently includes [{{ model.schemata | length }} schemata][schemata] and [{{ registry.types | length }} property types][types] that can be selected to generate entities. 

## Schemata

| Name | Label | Abstract | Generated | Matchable | Hidden |
| ---- | ----- | -------- | --------- | --------- | ------ |
{% for schema in model.schemata.values() %}| {{ schema_ref(schema.name) }} | {{ schema.label }} | {{ bool_icon(schema.abstract) }} | {{ bool_icon(schema.generated) }} | {{ bool_icon(schema.matchable) }} | {{ bool_icon(schema.hidden) }} |
{% endfor %}

## Types

| Name | Label | Matchable | Pivot |
| ---- | ----- | --------- | ----- |
{% for type in registry.types %}| {{ type_ref(type.name) }} | {{ type.label }} | {{ bool_icon(type.matchable) }} | {{ bool_icon(type.pivot) }} |
{% endfor %}
