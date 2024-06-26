"""Changed 'translation' to 'translator' in PlayTranslations table

Revision ID: 4f8d56e07d4f
Revises: 64af634f4b33
Create Date: 2023-11-03 14:49:38.493561

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4f8d56e07d4f'
down_revision = '64af634f4b33'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('playtranslations', sa.Column('translator', sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    op.drop_column('playtranslations', 'translation')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('playtranslations', sa.Column('translation', mysql.VARCHAR(length=255), nullable=True))
    op.drop_column('playtranslations', 'translator')
    # ### end Alembic commands ###
