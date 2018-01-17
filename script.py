import pandas
from bs4 import BeautifulSoup
import csv
source = 'searchresults.xls'

def read_excel_xml(path):
### Converts Excel XML to a [[[list]]] """
    file = open(path).read();
    soup = BeautifulSoup(file,'lxml');
    workbook = []
    for sheet in soup.find_all('worksheet'):
        sheet_as_list = []
        for row in sheet.findAll('row'):
            row_as_list = []
            for cell in row.findAll('cell'):
                row_as_list.append(cell.data.text)
            sheet_as_list.append(row_as_list)
        workbook.append(sheet_as_list)
    return workbook


workbooks = read_excel_xml(source)

print(workbooks);
thefile = open('test.csv', 'w')
for wbook in workbooks:
    for wsheet in wbook:
        for row in wsheet:
                print(row);
                thefile.write("%s," % row)
        thefile.write("\n");
###data = map(literal_eval, datau)
thefile.close();
#tldcsvfile = open('tldsearchresults.csv', "w")
#tldcsvwriter = csv.writer(tldcsvfile, delimiter=',')

#with open('tldsearchresults.csv', 'w') as myfile:
#    wr = csv.writer(myfile, quoting=csv.QUOTE_MINIMAL)
#    wr.writerows(data)



##for row in data[0][]:
##     tldcsvwriter.writerow((row[0],row[1],row[2],row[4], row[5],row[6])) ### zeroed out the qty due to poor inventory feed.

###df = pd.DataFrame(data[0][1:],columns = data[0][0])

