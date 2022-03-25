 
import pytest
from transactions import transaction


@pytest.fixture
def dbfile(tmpdir):
    ''' create a database file in a temporary file system '''
    return tmpdir.join('test_tracker.db')

@pytest.fixture
def empty_db(dbfile):
    db = transaction(dbfile)
    yield db


@pytest.fixture
def test_db(empty_db):
    trans1 = {'itemNum':'1', 'amount':'20', 'category_t':'rent', 'date':'2022-3-24', 'description':'test'}
    trans2 = {'itemNum':'2', 'amount':'30', 'category_t':'food', 'date':'2021-5-24', 'description':'testa'}
    trans3 = {'itemNum':'3', 'amount':'40', 'category_t':'utilities', 'date':'1492-6-29', 'description':'testb'}
    id1=empty_db.add_transactions(trans1)
    id2=empty_db.add_transactions(trans2)
    id3=empty_db.add_transactions(trans3)
    yield empty_db



#test add_transactions and show_transaction
@pytest.mark.add
def test_add(test_db):
    trans0 = {'itemNum':'4', 'amount':'50', 'category_t':'test1', 'date':'2500-1-10', 'description':'testadd'}
    db = test_db.show_transactions()
  #  yield len(db)
    assert len(db) == 3
    recent = test_db.add_transactions(trans0)

    db = test_db.show_transactions()
    assert len(db) == 4

    assert recent == 4
    assert db[recent-1]['itemNum'] == 4
    assert db[recent-1]['amount']== 50.0
    assert db[recent-1]['category_t']=='test1'
    assert db[recent-1]['date']=='2500-1-10'
    assert db[recent-1]['description']=='testadd'

    # trans0 = {'itemNum':'4', 'amount':'50', 'category':'test1', 'date':'2500-1-10', 'description':'testadd'}
    # tran0 = test_db.show_transactions()
    # rowid = test_db.add_transactions(tran0)
    # trans1 = test_db.show_transactions()
    # assert len(trans1) == len(trans0) + 1
    # tran1 = test_db.select_one(rowid)
    # assert tran1['name']==tran0['name']
    # assert tran1['desc']==tran0['desc']

@pytest.fixture
def test_db2(empty_db):
    trans0 = {'itemNum':'1', 'amount':'50', 'category_t':'test1', 'date':'2500-1-10', 'description':'testadd'}
    trans1 = {'itemNum':'2', 'amount':'40', 'category_t':'test2', 'date':'2500-1-10', 'description':'testadd'}
    trans2 = {'itemNum':'3', 'amount':'10', 'category_t':'test3', 'date':'2500-3-10', 'description':'testadd'}
    recent = empty_db.add_transactions(trans0)
    recent = empty_db.add_transactions(trans1)
    recent = empty_db.add_transactions(trans2)
    yield empty_db

#tests summarize transactions by date function
@pytest.mark.sum_by_date 
def test_sum_by_date(test_db2):
    recent = test_db2.summarize_by_date("2500-1-10")
    assert len(recent) == 2
    
