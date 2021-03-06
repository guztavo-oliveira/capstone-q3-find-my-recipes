"""create table feed

Revision ID: 6eacc178a403
Revises: 7ec17968871c
Create Date: 2022-04-27 11:29:39.812168

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '6eacc178a403'
down_revision = '499b5ea1e61a'
branch_labels = None
depends_on = None


def upgrade():

    op.create_table('feed',
    sa.Column('feed_id', sa.BigInteger(), nullable=False),
    sa.Column('icon', sa.String(), nullable=True),
    sa.Column('user_name', sa.String(), nullable=False),
    sa.Column('publication_date', sa.DateTime(), nullable=True),
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('feed_id')
    )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('feed')

    # ### end Alembic commands ###
