// ------------------- Validações -------------------

function TestaCPF(cpf) {
    cpf = cpf.replace(/[^\d]+/g, "");
    if (cpf.length !== 11 || /^(\d)\1+$/.test(cpf)) return false;

    let soma = 0;
    for (let i = 0; i < 9; i++) soma += parseInt(cpf.charAt(i)) * (10 - i);
    let resto = (soma * 10) % 11;
    if (resto === 10 || resto === 11) resto = 0;
    if (resto !== parseInt(cpf.charAt(9))) return false;

    soma = 0;
    for (let i = 0; i < 10; i++) soma += parseInt(cpf.charAt(i)) * (11 - i);
    resto = (soma * 10) % 11;
    if (resto === 10 || resto === 11) resto = 0;

    return resto === parseInt(cpf.charAt(10));
}

function validarCNPJ(cnpj) {
    cnpj = cnpj.replace(/[^\d]+/g, "");
    if (cnpj.length !== 14 || /^(\d)\1+$/.test(cnpj)) return false;

    let tamanho = cnpj.length - 2;
    let numeros = cnpj.substring(0, tamanho);
    let digitos = cnpj.substring(tamanho);
    let soma = 0;
    let pos = tamanho - 7;

    for (let i = tamanho; i >= 1; i--) {
        soma += numeros.charAt(tamanho - i) * pos--;
        if (pos < 2) pos = 9;
    }

    let resultado = soma % 11 < 2 ? 0 : 11 - (soma % 11);
    if (resultado !== parseInt(digitos.charAt(0))) return false;

    tamanho = tamanho + 1;
    numeros = cnpj.substring(0, tamanho);
    soma = 0;
    pos = tamanho - 7;

    for (let i = tamanho; i >= 1; i--) {
        soma += numeros.charAt(tamanho - i) * pos--;
        if (pos < 2) pos = 9;
    }

    resultado = soma % 11 < 2 ? 0 : 11 - (soma % 11);
    return resultado === parseInt(digitos.charAt(1));
}

// ------------------- Utils -------------------

function toggleLog(inputId, logId, validator) {
    const input = document.getElementById(inputId);
    const log = document.getElementById(logId);

    if (!input || !log) return;

    const isValid = validator(input.value);
    log.textContent = isValid ? "Válido" : "Inválido";
    log.style.color = isValid ? "green" : "red";
}

function formatarTelefone(_, inputId) {
    const input = document.getElementById(inputId);
    if (!input) return;

    let v = input.value.replace(/\D/g, "").replace(/^0/, "");

    if (v.length > 10) {
        v = v.replace(/^(\d{2})(\d{5})(\d{4}).*/, "($1) $2-$3");
    } else if (v.length > 5) {
        v = v.replace(/^(\d{2})(\d{4})(\d{0,4}).*/, "($1) $2-$3");
    } else if (v.length > 2) {
        v = v.replace(/^(\d{2})(\d{0,5})/, "($1) $2");
    } else if (v.length) {
        v = v.replace(/^(\d*)/, "($1");
    }

    input.value = v;
}

function atualizarBotaoContato(inputId, botaoId) {
    const input = document.getElementById(inputId);
    const botao = document.getElementById(botaoId);

    if (!input || !botao) return;

    botao.onclick = () => {
        const tel = input.value.replace(/\D/g, "");
        if (tel.length >= 10) {
            window.open(`https://wa.me/55${tel}`, "_blank");
        }
    };
}

// ------------------- Documento -------------------

function configurarCampoDocumento() {
    const tipoSelect = document.getElementById("id_tipo_de_documento");
    const docInput = document.getElementById("id_documento_titular");
    const nomeRazaoInput = document.getElementById("id_nome_razao_titular");

    if (!tipoSelect || !docInput || !nomeRazaoInput) return;

    const aplicarValidacao = () => {
        const tipo = tipoSelect.value;
        const logId = "doc_titular_log";

        // Se o select estiver desabilitado, desabilita também os outros
        if (tipoSelect.disabled) {
            docInput.disabled = true;
            nomeRazaoInput.disabled = true;
            return;
        } else {
            docInput.disabled = false;
            nomeRazaoInput.disabled = false;
        }

        // Substitui input para resetar eventos/máscaras
        const novoInput = docInput.cloneNode(true);
        docInput.parentNode.replaceChild(novoInput, docInput);

        if (tipo === "1") { // CNPJ
            $(novoInput).mask("00.000.000/0000-00");
            novoInput.addEventListener("keyup", () =>
                toggleLog(novoInput.id, logId, validarCNPJ)
            );
        } else if (tipo === "2") { // CPF
            $(novoInput).mask("000.000.000-00");
            novoInput.addEventListener("keyup", () =>
                toggleLog(novoInput.id, logId, TestaCPF)
            );
        }
    };

    tipoSelect.addEventListener("change", aplicarValidacao);
    aplicarValidacao();
}

// ------------------- Cônjuge -------------------

function AbrirConjuge() {
    const select = document.getElementById("id_estado_civil");
    const campo = document.getElementById("id_nome_do_conjuge");
    if (!select || !campo) return;

    const toggle = () => {
        const show = ["2", "3", "5"].includes(select.value);
        campo.style.display = show ? "block" : "none";
    };

    select.addEventListener("change", toggle);
    toggle();
}

// ------------------- Init -------------------

window.addEventListener("load", () => {
    // Telefones
    ["1", "2", "3"].forEach(num => {
        formatarTelefone(null, `id_fone_${num}`);
        atualizarBotaoContato(`id_fone_${num}`, `btn_id_fone_${num}`);
    });

    // Documento
    configurarCampoDocumento();

    // Cônjuge
    AbrirConjuge();

    // Logs iniciais
    toggleLog("id_cnpj", "cnpjlog", validarCNPJ);
    toggleLog("id_cpf", "cpflog", TestaCPF);
});
