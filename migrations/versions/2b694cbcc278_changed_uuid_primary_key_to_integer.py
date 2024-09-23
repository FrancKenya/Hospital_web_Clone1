"""Changed UUID primary key to Integer

Revision ID: 2b694cbcc278
Revises: 232d6ee19a18
Create Date: 2024-09-23 14:37:30.840998

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b694cbcc278'
down_revision = '232d6ee19a18'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('bookings', schema=None) as batch_op:
        batch_op.add_column(sa.Column('patient_age', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('patient_gender', sa.String(length=10), nullable=False))
        batch_op.add_column(sa.Column('appointment_time', sa.DateTime(), nullable=False))
        batch_op.add_column(sa.Column('branch_id', sa.String(length=60), nullable=False))
        batch_op.alter_column('service_id',
               existing_type=sa.VARCHAR(length=60),
               type_=sa.Integer(),
               existing_nullable=False)
        batch_op.alter_column('id',
               existing_type=sa.VARCHAR(length=60),
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True)
        batch_op.create_foreign_key(None, 'branches', ['branch_id'], ['id'])

    with op.batch_alter_table('branches', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.VARCHAR(length=60),
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True)
        batch_op.alter_column('location',
               existing_type=sa.TEXT(),
               type_=sa.String(length=255),
               existing_nullable=False)

    with op.batch_alter_table('services', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.VARCHAR(length=60),
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True)
        batch_op.alter_column('branch_id',
               existing_type=sa.VARCHAR(length=60),
               type_=sa.Integer(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('services', schema=None) as batch_op:
        batch_op.alter_column('branch_id',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(length=60),
               existing_nullable=False)
        batch_op.alter_column('id',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(length=60),
               existing_nullable=False,
               autoincrement=True)

    with op.batch_alter_table('branches', schema=None) as batch_op:
        batch_op.alter_column('location',
               existing_type=sa.String(length=255),
               type_=sa.TEXT(),
               existing_nullable=False)
        batch_op.alter_column('id',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(length=60),
               existing_nullable=False,
               autoincrement=True)

    with op.batch_alter_table('bookings', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('id',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(length=60),
               existing_nullable=False,
               autoincrement=True)
        batch_op.alter_column('service_id',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(length=60),
               existing_nullable=False)
        batch_op.drop_column('branch_id')
        batch_op.drop_column('appointment_time')
        batch_op.drop_column('patient_gender')
        batch_op.drop_column('patient_age')

    # ### end Alembic commands ###
