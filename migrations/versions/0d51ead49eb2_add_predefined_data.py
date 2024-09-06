"""Add predefined data

Revision ID: 0d51ead49eb2
Revises: 
Create Date: 2024-09-06 16:43:12.293865

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "0d51ead49eb2"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Insertar datos predefinidos en la tabla Country
    op.bulk_insert(sa.table("country", sa.column("name", sa.String)), [{"name": "Espanya"}])

    # Insertar datos predefinidos en la tabla Region
    op.bulk_insert(
        sa.table("region", sa.column("name", sa.String), sa.column("country_name", sa.String)),
        [{"name": "Catalunya", "country_name": "Espanya"}],
    )

    # Insertar datos predefinidos en la tabla Province
    op.bulk_insert(
        sa.table("province", sa.column("name", sa.String), sa.column("region_name", sa.String)),
        [
            {"name": "Barcelona", "region_name": "Catalunya"},
            {"name": "Girona", "region_name": "Catalunya"},
            {"name": "Tarragona", "region_name": "Catalunya"},
            {"name": "Lleida", "region_name": "Catalunya"},
        ],
    )


def downgrade():
    # Eliminar datos predefinidos en la tabla Province
    op.execute('DELETE FROM province WHERE name IN ("Barcelona", "Girona", "Tarragona", "Lleida")')

    # Eliminar datos predefinidos en la tabla Region
    op.execute('DELETE FROM region WHERE name IN ("Catalunya")')

    # Eliminar datos predefinidos en la tabla Country
    op.execute('DELETE FROM country WHERE name IN ("Espanya")')
