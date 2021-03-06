"""create ingredient table

Revision ID: 47b8f461efad
Revises: 425fd5c6bca6
Create Date: 2022-04-26 16:28:03.713120

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "47b8f461efad"
down_revision = "37bca2ed507f"
branch_labels = None
depends_on = None
#


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.create_table('quantity',
    # sa.Column('quantity_id', sa.Integer(), nullable=False),
    # sa.Column('unit', sa.Enum('QUILO', 'GRAMA', 'LITRO', 'MILILITRO', 'XICARA', name='myenum'), nullable=False),
    # sa.Column('amount', sa.Integer(), nullable=False),
    # sa.PrimaryKeyConstraint('quantity_id')
    # )
    # op.create_table('user',
    # sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False),
    # sa.Column('name', sa.String(), nullable=False),
    # sa.Column('email', sa.String(), nullable=False),
    # sa.Column('password_hash', sa.String(), nullable=False),
    # sa.Column('account_type', sa.String(), nullable=False),
    # sa.PrimaryKeyConstraint('user_id'),
    # sa.UniqueConstraint('email')
    # )
    op.create_table(
        "ingredient",
        sa.Column("ingredient_id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("ingredient_id"),
        sa.UniqueConstraint("title"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("ingredient")
    # op.drop_table('user')
    # op.drop_table('quantity')
    # ### end Alembic commands ###
