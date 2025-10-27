"""add_initial_roles

Revision ID: fa9771935df1
Revises: a9c9e7816a4c
Create Date: 2025-10-27 19:49:58.545349

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision: str = 'fa9771935df1'
down_revision: Union[str, Sequence[str], None] = 'a9c9e7816a4c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        INSERT INTO role (name, description, created_at, updated_at)
        VALUES
            ('admin', 'Administrator role', NOW(), NOW()),
            ('user', 'Regular user role', NOW(), NOW())
        """
    )


def downgrade() -> None:
    op.execute("DELETE FROM role WHERE name IN ('admin', 'user')")
