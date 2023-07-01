"""empty message

Revision ID: a448e02bc0b7
Revises: a258e6776e01
Create Date: 2023-06-30 08:52:44.496281

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a448e02bc0b7'
down_revision = 'a258e6776e01'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('audios', schema=None) as batch_op:
        batch_op.add_column(sa.Column('audio_data', sa.LargeBinary(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('audios', schema=None) as batch_op:
        batch_op.drop_column('audio_data')

    # ### end Alembic commands ###