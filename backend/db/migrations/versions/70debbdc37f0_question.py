"""question

Revision ID: 70debbdc37f0
Revises: 8852459e778b
Create Date: 2023-04-09 10:36:01.864718

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70debbdc37f0'
down_revision = '8852459e778b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_questions_id'), 'questions', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_questions_id'), table_name='questions')
    op.drop_table('questions')
    # ### end Alembic commands ###
