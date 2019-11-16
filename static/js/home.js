$(document).ready(function() {
    console.log("ready!");
    $("#editorCode").hide();
});

function sendFile() { Console.log("test") }

function run() {
    $.ajax({
        url: "http://127.0.0.1:5000/run",
        type: "GET",
        dataType: "Json"
    }).done(function(data) {

        table = data.table
        lines = data.lines
        errors = data.errors

        showTable(table)
        showCode(lines)
        showErrors(errors)


    }).fail(function(data) {
        window.alert("no funciono");
    });


}

function showErrors(errors) {
    errors.map(x => $("#contentErrors").append("<div>" + "LINEA: " + x[0] + "| DESCRIPCION: " + x[1] + " </div>"));
    $("#contentErrors").widht("100%")
    $("#contentErrors").height("100%")

}

function showCode(lines) {
    $("#editorCode").html("");
    $("#editorCode").show('slow');

    lines.map((x, i = 1) => $("#editorCode").append(" <div> " + " <span class = 'ln'> " + (i + 1) + " </span> " + x + " </div> "))
}

function showTable(table) {
    rows = table.map((x) => x.split(","))
    rows.map(function(x) {
        if (x[0] === "Var") {
            //var
            appendNewRow(x[1], x[2], x[3], null, x[4])
        } else {
            //funcion
            appendNewRow(x[1], x[2], null, x[2], x[3], x[4])
        }
    });
}

function appendNewRow(name, type, val, retorn_val, line, scope) {
    //es una variable

    if (retorn_val === null) {
        retorn_val = '-'
        scope = '-'
    }

    //es una funcion
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



    tr.append(td1, td2, td3, td4, td5, td6); // Append the new elements 
    $("#tableBody").append(tr);


}