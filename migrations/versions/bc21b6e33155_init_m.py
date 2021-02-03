"""init m

Revision ID: bc21b6e33155
Revises: 
Create Date: 2018-10-30 13:42:08.186888

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc21b6e33155'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('checkclass',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('checkcname', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('examclass',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('examname', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('hospitalconstuct',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('inhospitalarea',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('areaname', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('medicine',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('medicineclass', sa.Integer(), nullable=True),
    sa.Column('medicinename', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('patientinfo',
    sa.Column('id', sa.String(length=64), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('birth', sa.Date(), nullable=True),
    sa.Column('sex', sa.Integer(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('price',
    sa.Column('id', sa.String(length=20), nullable=False),
    sa.Column('optionid', sa.Integer(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usergroup',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bedinfo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('areaid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['areaid'], ['inhospitalarea.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('checkitem',
    sa.Column('id', sa.String(length=128), nullable=False),
    sa.Column('checkitemname', sa.String(length=64), nullable=True),
    sa.Column('itemclass', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['itemclass'], ['checkclass.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('examitem',
    sa.Column('id', sa.String(length=128), nullable=False),
    sa.Column('examitemname', sa.String(length=64), nullable=True),
    sa.Column('itemclass', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['itemclass'], ['checkclass.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('hospitalclass',
    sa.Column('id', sa.String(length=64), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('cid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cid'], ['hospitalconstuct.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('userinfo',
    sa.Column('id', sa.String(length=64), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('sex', sa.Integer(), nullable=True),
    sa.Column('rank', sa.Integer(), nullable=True),
    sa.Column('password', sa.String(length=64), nullable=True),
    sa.Column('groupid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['groupid'], ['usergroup.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('doctorcycle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('doctorid', sa.String(length=64), nullable=True),
    sa.Column('classid', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['classid'], ['hospitalclass.id'], ),
    sa.ForeignKeyConstraint(['doctorid'], ['userinfo.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('expertstimetable',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userinfoid', sa.String(length=64), nullable=True),
    sa.Column('cid', sa.String(length=64), nullable=True),
    sa.Column('date', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['cid'], ['hospitalclass.id'], ),
    sa.ForeignKeyConstraint(['userinfoid'], ['userinfo.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('inpatienttimetable',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userinfoid', sa.String(length=64), nullable=True),
    sa.Column('date', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['userinfoid'], ['userinfo.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('outpatienttimetable',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('doctorcycleid', sa.Integer(), nullable=True),
    sa.Column('date', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['doctorcycleid'], ['doctorcycle.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('opcheckin',
    sa.Column('id', sa.String(length=10), nullable=False),
    sa.Column('patientid', sa.String(length=10), nullable=True),
    sa.Column('doctorid', sa.String(length=10), nullable=True),
    sa.Column('doctime', sa.Integer(), nullable=True),
    sa.Column('experttime', sa.Integer(), nullable=True),
    sa.Column('jips', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['doctime'], ['outpatienttimetable.id'], ),
    sa.ForeignKeyConstraint(['doctorid'], ['userinfo.id'], ),
    sa.ForeignKeyConstraint(['experttime'], ['expertstimetable.id'], ),
    sa.ForeignKeyConstraint(['patientid'], ['patientinfo.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('opcheck',
    sa.Column('id', sa.String(length=10), nullable=False),
    sa.Column('checkitems', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['checkitems'], ['checkitem.id'], ),
    sa.ForeignKeyConstraint(['id'], ['opcheckin.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('opcheckafford',
    sa.Column('id', sa.String(length=10), nullable=False),
    sa.Column('price', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['opcheckin.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('opcheckinafford',
    sa.Column('id', sa.String(length=10), nullable=False),
    sa.Column('price', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['opcheckin.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('opexam',
    sa.Column('id', sa.String(length=10), nullable=False),
    sa.Column('examitems', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['examitems'], ['examitem.id'], ),
    sa.ForeignKeyConstraint(['id'], ['opcheckin.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('opexamafford',
    sa.Column('id', sa.String(length=10), nullable=False),
    sa.Column('price', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['opcheckin.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('oprecipe',
    sa.Column('id', sa.String(length=10), nullable=False),
    sa.Column('medicinenames', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['opcheckin.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('oprecipeafford',
    sa.Column('id', sa.String(length=10), nullable=False),
    sa.Column('price', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['opcheckin.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('oprecipeafford')
    op.drop_table('oprecipe')
    op.drop_table('opexamafford')
    op.drop_table('opexam')
    op.drop_table('opcheckinafford')
    op.drop_table('opcheckafford')
    op.drop_table('opcheck')
    op.drop_table('opcheckin')
    op.drop_table('outpatienttimetable')
    op.drop_table('inpatienttimetable')
    op.drop_table('expertstimetable')
    op.drop_table('doctorcycle')
    op.drop_table('userinfo')
    op.drop_table('hospitalclass')
    op.drop_table('examitem')
    op.drop_table('checkitem')
    op.drop_table('bedinfo')
    op.drop_table('usergroup')
    op.drop_table('price')
    op.drop_table('patientinfo')
    op.drop_table('medicine')
    op.drop_table('inhospitalarea')
    op.drop_table('hospitalconstuct')
    op.drop_table('examclass')
    op.drop_table('checkclass')
    # ### end Alembic commands ###
