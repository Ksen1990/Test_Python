import glob
import tabula
pdf = glob.glob ('*.pdf')
print(pdf)

obj = tabula.read_pdf(pdf[0], pages = 1)
print (obj)

tabula.convert_into(pdf[0],'Lesson8.csv')