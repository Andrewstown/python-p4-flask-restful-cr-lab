"""empty message

Revision ID: f6a2da181497
Revises: 3e451751636f
Create Date: 2023-03-15 17:53:02.886551

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f6a2da181497'
down_revision = '3e451751636f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plants', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('image', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('price', sa.Float(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plants', schema=None) as batch_op:
        batch_op.drop_column('price')
        batch_op.drop_column('image')
        batch_op.drop_column('name')

    # ### end Alembic commands ###
