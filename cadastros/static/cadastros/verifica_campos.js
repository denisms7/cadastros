function Verifica(var_classe) {
    var verificaCamposDiv = document.querySelector(var_classe);
    var inputs = verificaCamposDiv.getElementsByTagName('input');
    var selects = verificaCamposDiv.getElementsByTagName('select');
    var todosVazios = true;

    for (var i = 0; i < inputs.length; i++) {
        if (inputs[i].value !== '' && inputs[i].value !== '0') {
            todosVazios = false;
            break;
        }
    }

    if (todosVazios) {
        for (var j = 0; j < selects.length; j++) {
            if (selects[j].value !== '' && selects[j].value !== '0') {
                todosVazios = false;
                break;
            }
        }
    }
    return todosVazios
}

function verificarCampos(classe, btncheckId, elementId) {
    if (Verifica(classe)) {
        // Todos os campos estão vazios dentro da div
        document.getElementById(btncheckId).checked = false;
        document.getElementById(elementId).classList.remove('show');
    } else {
        // Existem campos preenchidos dentro da div
        document.getElementById(btncheckId).checked = true;
        document.getElementById(elementId).classList.add('show');
    }
}

verificarCampos('.Verifica_Contato', 'btncheck1', 'idContato');
verificarCampos('.Verifica_Endereco', 'btncheck2', 'idEndereco');
verificarCampos('.Verifica_Banco', 'btncheck3', 'idBanco');
try {
    verificarCampos('.Verifica_Cnh', 'btncheck4', 'idveiculo');
} catch {
    console.log('#Error Verifica_Cnh')
}

