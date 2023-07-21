import enum
import logging

from djongo.base import DatabaseWrapper
from djongo.models import JSONField as MJSONField
from djongo.operations import DatabaseOperations
from rest_framework.serializers import JSONField, ModelSerializer
from bson import Decimal128

# from mo_system.bson import AFTSDecimal
# from mo_tasks.common.bson import DecimalField

# logger = logging.getLogger("tasks")


class PatchedDatabaseOperations(DatabaseOperations):
    def adapt_decimalfield_value(self, value, max_digits=None, decimal_places=None):
        if value is None:
            return None
        if isinstance(value, Decimal128):
            return value
        return Decimal128(super().adapt_decimalfield_value(value, max_digits, decimal_places))

    def adapt_unknown_value(self, value):
        if isinstance(value, enum.Enum):
            return value.value
        return super().adapt_unknown_value(value)

    def conditional_expression_supported_in_where_clause(self, expression):
        return False


_old_close = DatabaseWrapper._close


def clean_close(self):
    _old_close(self)
    self.client_connection = None


DatabaseWrapper.ops_class = PatchedDatabaseOperations
DatabaseWrapper._close = clean_close
ModelSerializer.serializer_field_mapping.update({MJSONField: JSONField})
