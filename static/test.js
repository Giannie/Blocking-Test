// Function to generate and download a csv file
function downloadCSV() {
    // Read array from hidden data field.
    var regex = /\'/gi;
    var data_array = JSON.parse($("#json-data").text().replace(regex, "\""));

    // Generate csv file
    var csv_string = data_array.join("\n");
    var csvFile = new Blob([csv_string], {type:"text/csv"});

    // Create link tag and download
    var link = document.createElement("a");
    link.href = window.URL.createObjectURL(csvFile);
    link.download =  "bad_combos.csv";
    document.body.appendChild(link);
    link.click();
}
// Some taken from https://datatables.net/examples/styling/bootstrap4
$(document).ready(function() {
    $("#download-button").removeAttr("hidden");
    $('.table-cell').text(function() {
        $(this).css("text-align", "center");
    });
    $('#resp-table').DataTable();
} );