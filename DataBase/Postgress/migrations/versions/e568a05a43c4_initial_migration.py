"""Initial migration

Revision ID: e568a05a43c4
Revises: 
Create Date: 2024-11-25 23:08:54.267413

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e568a05a43c4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Employee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('designation', sa.Text(), nullable=False),
    sa.Column('scale', sa.Integer(), nullable=False),
    sa.Column('working_year_in_company', sa.Integer(), nullable=False),
    sa.Column('salary', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Employee')
    # ### end Alembic commands ###
