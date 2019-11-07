$(document).ready(function() {
    console.log("ready!");
});

function sendFile() { Console.log("test") }

function showResult() {
    let query = "all";

    $.ajax({
        // url: "api/formManagment/" + query, poner api de mia creada con python
        type: "get",
        dataType: "json"
    }).done(function(data) {

        data.forEach(obj => appendNewRow(obj.type, obj.name, obj.val, obj.retorn_val, obj.line, obj.scope));

    }).fail(function(data) {
        window.alert("no funciono");
    });
}

function appendNewRow(type, name, val, retorn_val, line, scope) {
    if (retorn_val === null) {
        retorn_val = '-'
    }
    if (val === null) {
        val = '-'
    }
    let tr = $("<tr></tr>"); // Create with jQuery
    let td1 = $("<td></td>").text(type);
    let td2 = $("<td></td>").text(name);
    let td3 = $("<td></td>").text(val);
    let td4 = $("<td></td>").text(retorn_val);
    let td5 = $("<td></td>").text(line);
    let td6 = $("<td></td>").text(scope);


    tr.append(td1, td2, td3, td4, td5, tf6); // Append the new elements 
    $("#tableBody").append(tr);


}