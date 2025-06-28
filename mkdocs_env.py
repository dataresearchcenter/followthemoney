from followthemoney import model
from followthemoney import registry
from followthemoney.property import Property
from followthemoney.schema import Schema
from followthemoney.types.common import PropertyType


def define_env(env):
    """
    This is the hook for the variables, macros and filters.
    """

    env.variables["model"] = model
    env.variables["registry"] = registry

    @env.macro
    def bool_icon(val: bool) -> str:
        if val:
            return ":material-check:"
        return ":material-close:"

    @env.macro
    def schema_ref(schema: Schema | str) -> str:
        if isinstance(schema, Schema):
            schema = schema.name
        return f"[`{schema}`](/explorer/schemata/{schema})"

    @env.macro
    def type_ref(type_: PropertyType | str) -> str:
        return f"[`{type_}`](/explorer/types/{type_})"

    @env.macro
    def prop_ref(prop: Property | str) -> str:
        if isinstance(prop, Property):
            schema, name = prop.schema.name, prop.name
        else:
            schema, name = prop.split(":")
        return f"[`{prop}`](/explorer/schemata/{schema}#{name})"

    @env.macro
    def select_schema(name: str) -> Schema:
        s = model.get(name)
        assert s is not None, f"Schema not in model: `{name}`"
        return s
