import csv
import cgi, cgitb
# import sys

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
# f_html.write('<script src = "rowcount.js"></script>')
# f_html.write('<script src="submit_javascript.js"></script>')
f_html.write('</head>')

f_html.write('<style>body {background-color: white;text-align: center;   color: black;}table, th, td {    border: 1px solid black;    border-collapse: collapse;}</style>')

f_html.write('<form method = "post" id = "form_id">')

f_html.write('<div id = "dvData">')
f_html.write('<table id = "tblCustomers">')
for row in reader:
    for column in row:
        f_html.write('<th>' + column + '</th>')
    break
i = 1
for row in reader: # Read a single row from the CSV file
  f_html.write('<tr>')# Create a new row in the table
  for column in row: # For each column..
    if column == 'INPUT':
        f_html.write('<td id = "' + str(i) + '"><input TYPE="TEXT" NAME="name" id ="inputbox" SIZE="20"></td>')
        # print i
        i+=1
        # print i
    else:
        f_html.write('<td id = "' + str(i) + '">' + column + '</td>')
        i+=1
  f_html.write('</tr>')

f_html.write('</table>')
# f_html.write('<script> ')
# f_html.write('<pre>"Hello"</pre>')
# f_html.write('<pre id = "json"></pre>')
# f_html.write('<pre>"Here"</pre>')
# f_html.write('<script> function myfunction(){document.getElementById("form_id").submit();var myRows = [];var $headers = $("th");var $rows = $("tbody tr").each(function(index) {$cells = $(this).find("td");myRows[index] = {};$cells.each(function(cellIndex) {myRows[index][$($headers[cellIndex]).html()] = $(this).html();});});var myObj = {};myObj.myrows = myRows;document.getElementById("json").innerHTML = JSON.stringify(myObj);}</script>')
# f_html.write()
# f_html.write('<input type="button" name = "submitbutton" value="Submit" onclick = "CountRows()"/>')
f_html.write('<input type="button" name = "submitbutton" value="Submit" onclick = "download_csv()"/>')
f_html.write('<input type = "button" name = "downloadbutton" value = "Download" onclick = "exportTableToCSV()"/>')
# f_html.write('<div class="button"><a href="#" id ="export" role="button">Click On This Here Link To Export The Table Data into a CSV File                </a></div>')
f_html.write('<script src = "download_csv.js"></script>')
f_html.write('<script src = "downloadcsv.js"></script>')
f_html.write('<script src = "rowcount.js"></script>')
f_html.write('<p id = "demo"></p>')

# f_html.write('<script type="text/javascript">function CountRows() {   var totalRowCount = 0;    var rowCount = 0;    var table = document.getElementById("tblCustomers");    var rows = table.getElementsByTagName("tr")    for (var i = 0; i < rows.length; i++) {        totalRowCount++;        if (rows[i].getElementsByTagName("td").length > 0) {            rowCount++;        }    }    var message = "Total Row Count: " + totalRowCount;    message += "\nRow Count: " + rowCount;    console.log(message);}</script>')
f_html.write('</form>')