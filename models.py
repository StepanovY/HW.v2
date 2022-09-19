from typing import Iterable, Any

from marshmallow import fields, Schema, validates_schema, ValidationError

VALID_CMD_PARAMS: Iterable[str] = (
    'filter',
    'map',
    'unique',
    'sort',
    'limit',
    'regex',
)


class RequestParams(Schema):
    cmd = fields.Str(required=True)
    value = fields.Str(required=True)

    @validates_schema
    def validate_cmd_params(self, values: dict[str, str], *args: Any, **kwargs: Any) -> dict[str, str]:
        if values['cmd'] not in VALID_CMD_PARAMS:
            raise ValidationError('Некоректный параметр "cmd"')

        return values


class BatchRequestParams(Schema):
    queries = fields.Nested(RequestParams, many=True)
