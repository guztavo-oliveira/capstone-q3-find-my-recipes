"""create relationship recipe-ingredient

Revision ID: 0964f96d9e67
Revises: 35f410b9386b
Create Date: 2022-04-28 10:57:24.318743

"""
from alembic import op
import sqlalchemy as sa

#
# revision identifiers, used by Alembic.
revision = "0964f96d9e67"
down_revision = "1c3399e8f064"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "recipe_ingredient", sa.Column("recipe_id", sa.Integer(), nullable=False)
    )
    op.create_foreign_key(
        None, "recipe_ingredient", "recipes", ["recipe_id"], ["recipe_id"]
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "recipe_ingredient", type_="foreignkey")
    op.drop_column("recipe_ingredient", "recipe_id")
    # ### end Alembic commands ###
