import pyucsc as ucsc

z= ucsc.search_database('Mammal','Human')
host=z.connect_ucsc()
cursor=host.cursor()
dbname=z.download_db_name(cursor)
db=ucsc.read_from_database().connect(dbname) 
cursor=db.cursor()
a=ucsc.read_from_database().download(cursor,'chr1')
z=ucsc.longest_genes(3,a)
nn=z.index()
Id=z.Id_list(nn)
records=z.save(Id,"gb")
for l in records:
	print l.id
