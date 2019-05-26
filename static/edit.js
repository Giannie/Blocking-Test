function addRowSingle(subject) {
    if (!subject) {
        subject = "";
    }
    var html = "<tr><td><input class=\"subject\" type=\"text\" value=\"" + subject + "\"></td>"
    var block_array = ["A", "B", "C", "D"];
    block_array.forEach(function(item, index) {
        html += "<td><input type=\"checkbox\" class=\"block\" name=\"" + item + "\"></td>";
    })
    html += "<td><button onclick=\"deleteRow(this)\">Delete</button></td></tr>";
    $("#single-table-body").append(html);
}

function addRowDouble(subject) {
    if (!subject) {
        subject = "";
    }
    var html = "<tr><td><input class=\"subject\" type=\"text\" value=\"" + subject + "\"></td>"
    var block_array = ["AB", "AC", "AD", "BC", "BD", "CD"];
    block_array.forEach(function(item, index) {
        html += "<td><input type=\"checkbox\" class=\"block\" name=\"" + item + "\"></td>";
    })
    html += "<td><button onclick=\"deleteRow(this)\">Delete</button></td></tr>";
    $("#double-table-body").append(html);
}

function deleteRow(b) {
    console.log()
    b.parentNode.parentNode.parentNode.removeChild(b.parentNode.parentNode);
}

function createJson() {
    var dict = {};
    $("tbody > tr").each(function() {
        var subject = $(".subject", this).val();
        dict[subject] = [];
        $(".block", this).each(function() {
            if (this.checked) {
                dict[subject].push(this.name);
            }
        })
    })
    return dict;
}

function submitJson() {
    var blocking_str = JSON.stringify(createJson());
    $form = $("<form></form>");
    $form.attr("action", "/test");
    $form.attr("method", "post");
    $form.attr("hidden", "hidden");
    $input = $("<input type=\"text\">")
    $input.attr("name", "json-text");
    $input.val(blocking_str);
    $form.append($input);
    $(document.body).append($form);
    $form.submit()
}

function downloadJson() {
    // Read array from hidden data field.
    var regex = /\]\,/gi;
    var dict = createJson();
    var json_str = JSON.stringify(dict).replace(regex, "],\n").replace("{", "{\n").replace("}", "\n}");

    var jsonFile = new Blob([json_str], {type:"text/json"});

    // Create link tag and download
    var link = document.createElement("a");
    link.href = window.URL.createObjectURL(jsonFile);
    link.download =  "blocking.json";
    document.body.appendChild(link);
    link.click();
}

function clearEmpties() {
    $("tbody > tr").each(function() {
        var blocks = $(".block", this);
        for (var i = 0; i < blocks.length; i++) {
            if (blocks[i].checked) {
                return true;
            }
        }
        this.parentNode.removeChild(this);
    })
}

$(document).ready(function() {
    clearEmpties();
});
