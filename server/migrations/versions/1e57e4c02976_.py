"""empty message

Revision ID: 1e57e4c02976
Revises: a448e02bc0b7
Create Date: 2023-06-30 08:56:21.912543

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e57e4c02976'
down_revision = 'a448e02bc0b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('audio2texts', schema=None) as batch_op:
        batch_op.drop_column('audio_data')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('audio2texts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('audio_data', sa.BLOB(), nullable=True))

    # ### end Alembic commands ###