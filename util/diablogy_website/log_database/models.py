import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

class ExampleModel(DjangoCassandraModel):
    example_id    = columns.UUID(primary_key=True, default=uuid.uuid4)
    example_type  = columns.Integer(index=True)
    created_at    = columns.DateTime()
    description   = columns.Text(required=False)

# Create your models here.
