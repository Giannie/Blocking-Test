// Function to submit form on button press
function submitForm() {
    $("#block-form").submit();
}

// Select file when div is clicked
function fileSelect() {
    $("#file-input").trigger("click");
}

// Add styling class when file is over div
function dragOverHandler(ev) {
    $("#drop_zone").addClass("drag-over");
    ev.preventDefault();
}

// Add styling class when file enters div
function dragEnterHandler(ev){
    ev.preventDefault();
    $("#drop_zone").addClass("drag-over");
}

// Remove styling when file leaves div
function dragLeaveHandler(ev) {
    ev.preventDefault();
    $("#drop_zone").removeClass("drag-over");
    $("#drop_zone").removeClass("up-success");
}

// Handle uploaded file(s)
function handleFiles(files) {
    var file = files[0]
    var reader = new FileReader()
    // Callback for file reader
    reader.onload = function(event) {
        // Try to read contents and add text to hidden text field.
        try {
            var contents = event.target.result;
            $("#json-text").val(contents);
            JSON.parse(contents);
            $("#drop-text").html("Uploaded: " + file.name);

            // Green styling for success
            $("#drop_zone").addClass("up-success");
            $("#json-submit").removeClass("btn-secondary");

            // Get button ready to submit
            $("#json-submit").text("Submit");
            $("#json-submit").addClass("btn-primary");
            $("#json-submit").click(function() {
                $("#block-form").submit();
            })
        }
        // Catch error and update text div and button
        catch (err) {
            $("#drop-text").html("Invalid JSON, please try again.<br>You can check your json here:<br><a href=\"https://jsonlint.com\">JSONLint</a>");
            $("#json-submit").addClass("btn-primary");
            $("#json-submit").text("Please upload a file");
            $("#json-submit").addClass("btn-secondary");
            $("#json-submit").off("click");
        }
    };
    reader.readAsText(file);
}

// Handle dropped file
function dropHandler(ev) {
    // Remove styling
    $("#drop_zone").removeClass("drag-over");
    $("#drop_zone").removeClass("up-success");

    // Prevent default behavior (Prevent file from being opened)
    ev.preventDefault();
    try {
        if (ev.dataTransfer.items) {
            // Use DataTransferItemList interface to access the file(s)
            for (var i = 0; i < ev.dataTransfer.items.length; i++) {
                // If dropped items aren't files, reject them
                if (ev.dataTransfer.items[i].kind === 'file') {
                    var file = ev.dataTransfer.items[i].getAsFile();
                    console.log('... file[' + i + '].name = ' + file.name);
                    handleFiles([file]);
                }
            }
        }
        else {
            // Use DataTransfer interface to access the file(s)
            for (var i = 0; i < ev.dataTransfer.files.length; i++) {
                console.log('... file[' + i + '].name = ' + ev.dataTransfer.files[i].name);
                handleFiles([file])
            }
        }
    }

    // Catch error and update text div and button
    catch (err) {
        $("#drop-text").html("Invalid JSON, please try again.<br>You can check your json here:<br><a href=\"https://jsonlint.com\">JSONLint</a>");
        $("#json-submit").addClass("btn-primary");
        $("#json-submit").text("Please upload a file");
        $("#json-submit").addClass("btn-secondary");
        $("#json-submit").off("click");
    }
}

// Prepare file when document is ready
$(document).ready(function() {
    $(".legacy").hide(0);
    $("form > br").remove();
    $("#submit").remove();
    $("#file-input").attr("name", "");
    $("#drop_zone").removeAttr("hidden");
});