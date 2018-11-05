function exportTableToCSV(filename) {
    var csv = [];
    var rows = document.querySelectorAll("table tr");
    console.log('Rows length = ' + rows.length)
    var cols = document.getElementById('tblCustomers').getElementsByTagName('td'), colslen = cols.length, i = 0;
    var input = "";
//    for (var i = 0; i < rows.length; i++) {
//        var row = [], cols = rows[i].querySelectorAll("td, th");
//        console.log('Columns length = ' + cols.length)
////        for (var j = 0; j < cols.length; j++)
//        var j = 0
//        while (++j<cols.length){
//            console.log("Outside if = " + j)
//            if (j%8 == 0){
//                console.log("Inside if = " + j)
////                row.push(cols[j].children.inputbox.value)
//                  row.push(document.getElementById(j+1).children.inputbox.value)
//            }
//            else
//                row.push(cols[j].innerText);
//        }
        console.log("Before loop = " + input)
    	while(++i < colslen){
        console.log("i = " + i);
        if (i%9==0){
            input += document.getElementById(i).children.inputbox.value + '\n';
//            input += '\n';
            console.log("Inside IF Input = " + input);
//            console.log(input.getElementById("inputbox").value);
//              console.log(input.getElementsByTagName("input").children.value);
        }
        else {
            input += document.getElementById(i).innerHTML;
            console.log("Else Input =" + input)
            console.log(document.getElementById(i).innerHTML);
        }
//        csv.push(input.join(","));
          input += ","
        }


    // Download CSV file
    downloadCSV(input +="\n", "project.csv");
}

function downloadCSV(csv, filename) {
    var csvFile;
    var downloadLink;

    // CSV file
    csvFile = new Blob([csv], {type: "text/csv"});

    // Download link
    downloadLink = document.createElement("a");

    // File name
    downloadLink.download = filename;

    // Create a link to the file
    downloadLink.href = window.URL.createObjectURL(csvFile);

    // Hide download link
    downloadLink.style.display = "none";

    // Add the link to DOM
    document.body.appendChild(downloadLink);

    // Click download link
    downloadLink.click();
}