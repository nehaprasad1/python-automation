
#to extract table from pdf we need to import  camelot-py library 
#use : pip install camelot-py
# before this we need to installl two dependencies by usigng command : pip install tk and  pip insstall ghostscript
import camelot

tables = camelot.read_pdf('food.pdf', page='1')
print(tables)

tables.export('food.csv', f='csv', compress=True)
tables[0].to_csv('foo.csv')  # to a csv file
print(tables[0].df)  # to a df
