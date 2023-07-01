"""empty message

Revision ID: 83b81cb97b4a
Revises: f48c84581f1d
Create Date: 2023-07-01 15:00:42.534930

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83b81cb97b4a'
down_revision = 'f48c84581f1d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('audio2texts', schema=None) as batch_op:
        batch_op.drop_column('translation_text')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('audio2texts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('translation_text', sa.TEXT(), nullable=True))

    # ### end Alembic commands ###
