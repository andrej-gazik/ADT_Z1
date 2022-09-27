"""Add Tables

Revision ID: 2b9c9a7d7426
Revises: 66cfb7e86829
Create Date: 2022-09-27 15:21:34.233485

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "2b9c9a7d7426"
down_revision = "66cfb7e86829"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "test",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("description", sa.Unicode(200)),
    )


def downgrade() -> None:
    pass
