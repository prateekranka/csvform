import csv
import cgi, cgitb
# import sys

# if len(sys.argv) < 2:
#   print "Usage: ./csv-html.py <your CSV file> <your HTML File.html>"
#   print
#   print
#   exit(0)

# Open the CSV file for reading
# reader = csv.reader(open(sys.argv[1]))
datadict_path = 'C:\Users\USER\Downloads\RIT\Deliverables\\'
reader = csv.reader(open(datadict_path + 'Data Dictionary_Inv.csv'))

# Create the HTML file
# f_html = open(sys.argv[2],"w");
f_html = open('Inventory_new.html',"w")

f_html.write('<title>Inventory Data Dictionary</title>')

f_html.write('<head>')
f_html.write('<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>')
f_html.write('<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>')
# f_html.write('<script src="submit_javascript.js"></script>')
f_html.write('</head>')

f_html.write('<style>body {background-color: white;text-align: center;   color: black;}table, th, td {    border: 1px solid black;    border-collapse: collapse;}</style>')

f_html.write('<form method = "post" id = "form_id">')

f_html.write('<table>')
for row in reader:
    # print "Start of row"
    # print row
    # print "End of row"
    for column in row:
        f_html.write('<th>' + column + '</th>')
        # print column
    break

for row in reader: # Read a single row from the CSV file
  f_html.write('<tr>')# Create a new row in the table
  for column in row: # For each column..
    if column == 'INPUT':
        f_html.write('<td>' + '<INPUT TYPE="TEXT" NAME="name" id = "inout" SIZE="20">' + '</td>')
    else:
        f_html.write('<td>' + column + '</td>')
  f_html.write('</tr>')


f_html.write('</table>')
# f_html.write('<script> ')
f_html.write('<pre>"Hello"</pre>')
f_html.write('<pre id = "json"></pre>')
f_html.write('<pre>"Here"</pre>')
f_html.write('<script> function myfunction(){document.getElementById("form_id").submit();var myRows = [];var $headers = $("th");var $rows = $("tbody tr").each(function(index) {$cells = $(this).find("td");myRows[index] = {};$cells.each(function(cellIndex) {myRows[index][$($headers[cellIndex]).html()] = $(this).html();});});var myObj = {};myObj.myrows = myRows;document.getElementById("json").innerHTML = JSON.stringify(myObj);}</script>')
# f_html.write()
f_html.write('<button type="button" name = "submitbutton" onclick = "myfunction()">Submit</button>')
f_html.write('</form>')

