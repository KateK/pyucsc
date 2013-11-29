import example3 as example

def test_search():
    host=0
    host=example.host
    assert host!=0, "there is no connection to host"
    dbname=0
    dbname=example.dbname
    assert dbname!=0, "there is no database name."
    return dbname

def test_read(dbname):
    db=0
    db=example.db 
    assert db!=0, "there is no connection to database"
    a=0
    a=example.a
    assert a!=0, "there is no data for chromosome - choose chromosome!"
    return a

def test_longest_genes(a):
    z=0
    z=example.z
    assert z!=0
    nn=0
    nn=example.nn
    assert nn!=0, "there is no id"
    Id=0
    Id=example.Id
    assert Id!=0, "create an Id-list"
    
    
z=test_search()
a=test_read(z)
test_longest_genes(a)
