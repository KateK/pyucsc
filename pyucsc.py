#coding: utf-8

import MySQLdb
from Bio import SeqIO
from Bio import Entrez
import re


class search_database: 
	def __init__(self,clade,genome):
		self.c = clade
		self.g = genome
		self.baza={frozenset(['Mammal', 'Human']):"hg19",frozenset(['Mammal', 'Chimp']):"panTro4",frozenset(['Mammal', 'Orangutan']):"ponAbe2",frozenset(['Mammal', 'Rhesus']):"rheMac3", frozenset(['Mammal', 'Baboon']):"papAnu2",frozenset(['Mammal', 'Marmoset']):"calJac3", frozenset(['Mammal', 'Mouse']):"mm10", frozenset(['Mammal', 'Rat']):"rn4", frozenset(['Mammal', 'Guinea pig']):"cavPor3", frozenset(['Mammal', 'Rabbit']):"oryCun2", frozenset(['Mammal', 'Pig']):"susScr3", frozenset(['Mammal', 'Sheep']):"oviAri3", frozenset(['Mammal', 'Cow']):"bosTau7", frozenset(['Mammal', 'Horse']):"equCab2", frozenset(['Mammal', 'Cat']):"felCat5", frozenset(['Mammal', 'Ferret']):"musFur1", frozenset(['Mammal', 'Dog']):"canFam3", frozenset(['Mammal', 'Elephant']):"loxAfr3", frozenset(['Mammal', 'Opossum']):"monDom5", frozenset(['Mammal', 'Tasmanian devil']):"sarHar1", frozenset(['Mammal', 'Platypus']):"ornAna1", frozenset(['Vertebrate', 'Chicken']):"galGal4", frozenset(['Vertebrate', 'Zebra finch']):"taeGut1", frozenset(['Vertebrate', 'X.tropicalis']):"xenTro3", frozenset(['Vertebrate', 'Fugu']):"fr3", frozenset(['Vertebrate', 'Nile tilapia']):"oreNil2", frozenset(['Vertebrate', 'Stickleback']):"gasAcu1", frozenset(['Vertebrate', 'Medaka']):"oryLat2", frozenset(['Vertebrate', 'Zebrafish']):"danRer7", frozenset(['Deuterostome', 'C. intestinalis']):"ci2", frozenset(['Deuterostome', 'S. purpurantus']):"ci2", frozenset(['Insect', 'D. melanogaster']):"dm3", frozenset(['Nematode', 'C. elegans']):"ce6"}
		print self.baza
		
	def connect_ucsc(self):
		self.key=frozenset([self.c, self.g])
		db = MySQLdb.connect(host="genome-mysql.cse.ucsc.edu", 	user="genomep", passwd="password",db = "hgcentral" )
		return db
		
	def download_db_name(self, cursor):
		cursor.execute("SHOW databases")
		z=cursor.fetchall()
		s = re.sub("\d+", "", self.baza[self.key])
		for i in range(len(z)):
			for l in range(1,101):
				if z[i][0] == s+str(l):
					data=z[i][0]
		return data
	
class read_from_database:
	def connect(self,databasename):
		dbname=databasename
		db = MySQLdb.connect(host="genome-mysql.cse.ucsc.edu", 	user="genomep", passwd="password",db = dbname )
		return db


	def download(self, cursor, nameOFchromosome):
		nameOFchromosome = "\""+ nameOFchromosome + "\""
		cursor.execute("SELECT * FROM refGene WHERE chrom LIKE "+ nameOFchromosome)
		a = cursor.fetchall()	
		assert len(a)!=0, "there is no data for chromosome - are you sure that this chromosome is correct for that organism?"
		return a



class longest_genes:
	def __init__(self, numberOFgene, table):
		self.a = table
		self.n = numberOFgene

	def index(self):
		lenlist=[]
		names=[]
#Returns list of n longest genes.
		for row in self.a:
			lenlist.append(row[5]-row[4])
			names.append(row[1])
	
		indeks=[]
		top = sorted(lenlist,reverse=True)[:self.n]
		for i in top:
			t=lenlist.index(i)
			indeks.append(t)
			lenlist[t]=0


		nn=[]
		for l in indeks:
			nn.append(names[l])

		z=zip(nn,top)

		return nn

	def Id_list(self,nn):
#Return an id list.
		war=""
		for i in range(len(nn)):
			war+=nn[i]+"[accn] OR "
		war=war.strip(' OR ')
		handle = Entrez.esearch(db="nucleotide", term=war)
		record = Entrez.read(handle)
		Id = record["IdList"]

		return Id

	def save(self,Id,format):
		SeqRecords=[]
		for n in xrange(len(Id)):
			handle = Entrez.efetch(db="nucleotide", id=Id[n], rettype=format, retmode="text")
			handle=handle.read()
			file = open(Id[n]+"."+format,"w")
			file.write(handle)
			file.close()
			SeqRecord=SeqIO.parse(open(Id[n]+"."+format), format)
			for record in SeqRecord:
				SeqRecords.append(record)

		return SeqRecords











