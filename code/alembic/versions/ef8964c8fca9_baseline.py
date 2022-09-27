"""baseline

Revision ID: ef8964c8fca9
Revises: d5999952c827
Create Date: 2022-09-27 15:05:22.724884

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "ef8964c8fca9"
down_revision = "d5999952c827"
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
    op.drop_table("account")
