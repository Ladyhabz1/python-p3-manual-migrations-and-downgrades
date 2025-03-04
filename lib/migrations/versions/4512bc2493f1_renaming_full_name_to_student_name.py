"""Renaming full_name to student_name

Revision ID: 4512bc2493f1
Revises: 791279dd0760
Create Date: 2025-03-04 10:16:22.775483

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4512bc2493f1'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade():
     op.rename_table('students', 'scholars')


def downgrade():
     op.rename_table('scholars', 'students')
