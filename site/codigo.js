let p=[]
let linhas = {
    linha1:[1,2,3],
    linha2:[4,5,6],
    linha3:[7,8,9]

}
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
    p.push(respostinha)
    document.getElementById("resultado").innerText = respostinha;
    


    if (p.length > 9){
        p.splice(0,1)
        linhas["linha1"]= [p[0],p[1],p[2]]
        linhas["linha2"]= [p[3],p[4],p[5]]
        linhas["linha3"]= [p[6],p[7],p[8]]
        document.getElementById("lista").innerText = `${linhas["linha1"]}\n${linhas["linha2"]}\n${linhas["linha3"]}`
    }
    else if (p.length <= 9 ){
        linhas["linha1"]= [p[0],p[1],p[2]]
        linhas["linha2"]= [p[3],p[4],p[5]]
        linhas["linha3"]= [p[6],p[7],p[8]]
        document.getElementById("lista").innerText = `${linhas["linha1"]}\n${linhas["linha2"]}\n${linhas["linha3"]}`
    }
    
}   
