"""empty message

Revision ID: a8302c0a9694
Revises: 49950fc41364
Create Date: 2017-11-29 20:51:52.192186

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a8302c0a9694'
down_revision = '49950fc41364'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post_tags', sa.Column('tag_id', sa.Integer(), nullable=True))
    op.drop_constraint('post_tags_ibfk_2', 'post_tags', type_='foreignkey')
    op.create_foreign_key(None, 'post_tags', 'tag', ['tag_id'], ['id'])
    op.drop_column('post_tags', 'teg_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post_tags', sa.Column('teg_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'post_tags', type_='foreignkey')
    op.create_foreign_key('post_tags_ibfk_2', 'post_tags', 'tag', ['teg_id'], ['id'])
    op.drop_column('post_tags', 'tag_id')
    # ### end Alembic commands ###
