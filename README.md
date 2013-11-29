pyucsc
======
###### UCSC Genome Browser - http://genome.ucsc.edu/cgi-bin/hgTables?command=start ######

What do you need?

1. Download Biopython, MySQLdb and re package.
2. You have to add file "pyucsc.py" to folder with your script. 
3. Self.baza is a dictionary of organisms that you can use(for that organisms is avaliable refGene table in UCSC).

What for?

1. This tool allows to search things in "Table Browser" especially longest genes on the chromosome. 
2. Class search_database - useful to connect to host and search database of organism that you've selected.
3. Class read_from_database - useful to connect to database of selected organism and it returns records from refGene table of your organism.
4. Class longest_genes - returns "n" longest genes from chromosome that you've selected (it saves sequence to file in selected format and to biopython object).


What is in?

1. pyucsc.py is file with script.
2. example.py is an example file that shows how to use pyucsc.py.
3. tests.py is testing file - you can check your function call(in import change "example3" to your file name).  
