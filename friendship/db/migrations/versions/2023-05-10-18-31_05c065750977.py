"""added friend

Revision ID: 05c065750977
Revises: 
Create Date: 2023-05-10 18:31:41.486410

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "05c065750977"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "category",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=200), nullable=False),
        sa.Column("reminder_frequency", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "dummy_model",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=200), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "friend",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=200), nullable=False),
        sa.Column("last_contacted", sa.Date(), nullable=False),
        sa.Column("category", sa.Integer(), nullable=True),
        sa.Column("friendship_score", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["category"], ["category.id"], name="fk_friend_category_id_category"
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("friend")
    op.drop_table("dummy_model")
    op.drop_table("category")
    # ### end Alembic commands ###