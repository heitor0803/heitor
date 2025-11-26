function Soma() {
    let a= parseFloat(document.getElementById("val1").value);
    let b = parseFloat( document.getElementById("val2").value)
    let c = document.getElementById("metodo").value;
    switch (c) {
        case "+":
            respostinha = a+b;
            break
        case "-":
            respostinha = a-b;
            break
        case "/":
            respostinha = a/b;
            break
        case "*":
            respostinha = a*b;
            break

    }
    document.getElementById("resultado").innerText = respostinha;

}