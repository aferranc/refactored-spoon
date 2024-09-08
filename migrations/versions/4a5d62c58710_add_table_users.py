"""Add table Users

Revision ID: 4a5d62c58710
Revises: 0d51ead49eb2
Create Date: 2024-09-08 08:31:38.769617

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "4a5d62c58710"
down_revision = "0d51ead49eb2"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("username", sa.String(80), nullable=False),
        sa.Column("password", sa.Unicode(120)),
    )


def downgrade():
    op.drop_table("users")
