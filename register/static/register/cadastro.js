window.onload = function () {
    formatarTelefone("input", "id_phone_1");
    formatarTelefone("input", "id_phone_2");
    formatarTelefone("input", "id_phone_3");

    atualizarBotaoContato("id_phone_1", "btn_id_phone_1");
    atualizarBotaoContato("id_phone_2", "btn_id_phone_2");
    atualizarBotaoContato("id_phone_3", "btn_id_phone_3");

    AbrirConjuge()
    configurarCampoDocumento()
};


$(document).ready(function () {
    $('#id_document_type').on('change', configurarCampoDocumento);
});

function configurarCampoDocumento() {
    let tipo_titular = document.getElementById('id_document_type');
    let documento_titular = document.getElementById('id_document_holder');
    let texto_documento_titular = document.getElementById('texto_nomerazao_titular')
    let titular_conta = document.getElementById('id_title_holder')
    let titular_conta_label = document.getElementById('texto_nomerazao_titular')


    if (tipo_titular.value) {
        documento_titular.disabled = false;
        titular_conta.disabled = false;

        if (tipo_titular.value.substr(0, 1) === '1') { // CNPJ
            documento_titular.classList.add('cnpj-cpf');
            documento_titular.placeholder = '00.000.000/0000-00';
            texto_documento_titular.innerHTML = 'CNPJ'
            titular_conta_label.innerHTML = 'Titular Razão Social'
            document.getElementById('id_documento_titular').addEventListener('keyup', validarCNPJ_titular);
            document.getElementById('cnpjlog_titular').innerHTML = 'CNPJ Invalido'

        } else if (tipo_titular.value.substr(0, 1) === '0') { // CPF
            documento_titular.classList.add('cnpj-cpf');
            documento_titular.placeholder = '000.000.000-00';
            texto_documento_titular.innerHTML = 'CPF'
            titular_conta_label.innerHTML = 'Titular Nome Completo'
            document.getElementById('id_documento_titular').addEventListener('keyup', ValidaCPF_titular);
            document.getElementById('cnpjlog_titular').innerHTML = 'CPF Invalido'

        } else { // não é nem CNPJ nem CPF
            documento_titular.classList.remove('cnpj-cpf');
            documento_titular.placeholder = '';
            texto_documento_titular.innerHTML = 'CPF/CNPJ'
            titular_conta_label.innerHTML = 'Nome Completo/Razão Social'
            document.getElementById('id_documento_titular').addEventListener('keyup', function () { });
            document.getElementById('cnpjlog_titular').innerHTML = ''

        }
    } else {
        documento_titular.disabled = true;
        titular_conta.disabled = true;
        documento_titular.value = '';
        documento_titular.classList.remove('cnpj-cpf');
        documento_titular.placeholder = '';
        texto_documento_titular.innerHTML = 'CPF/CNPJ'

        titular_conta_label.innerHTML = 'Nome Completo/Razão Social'
        titular_conta.value = '';

        document.getElementById('cnpjlog_titular').innerHTML = ''
    }

    if (tipo_titular.disabled) {
            titular_conta.disabled = true;
            documento_titular.disabled = true;
            return;
        }


    // Adicione este trecho de código para aplicar a máscara quando o campo já estiver preenchido
    $('.cnpj-cpf').each(function () {
        var tipo = $('#id_tipo_de_documento').val().substr(0, 1);
        var mascara = '';
        if (tipo === '1') {
            mascara = '00.000.000/0000-00';
        } else if (tipo === '0') {
            mascara = '000.000.000-00';
        }
        $(this).mask(mascara);
    });
}



function carregarCNPJ(cnpj) {
    let v_cnpj = cnpj.replace(/[^0-9]/g, '')
    let v_url = 'https://www.receitaws.com.br/v1/cnpj/' + v_cnpj

    try {
        if (v_cnpj.length == 14 && validarCNPJ(v_cnpj)) {
            $.ajax({
                url: v_url,
                dataType: 'jsonp',
                crossDomain: true,
                success: function (response) {
                    console.log('Response status:', response.status);
                    if (response.status === "OK") {
                        const setValueIfExists = (id, value) => {
                            const element = document.getElementById(id);
                            if (element && value != '') {
                                element.value = value;
                            }
                        };

                        setValueIfExists('id_legal', response.nome);
                        setValueIfExists('id_fantasy', response.fantasia);
                        setValueIfExists('id_cep', response.cep);
                        setValueIfExists('id_state', response.uf);
                        setValueIfExists('id_city', response.municipio);
                        setValueIfExists('id_neighborhood', response.bairro);
                        setValueIfExists('id_address', response.logradouro);
                        setValueIfExists('id_number', response.numero);
                        setValueIfExists('id_cnpj_situation', response.situacao);
                        setValueIfExists('id_cnpj_carrying', response.porte);
                        setValueIfExists('id_cnpj_type_activity', response.tipo);

                        if (response.abertura != '') {
                            let dataOriginal = response.abertura
                            let partesData = dataOriginal.split("/");
                            let dataNova = new Date(partesData[2], partesData[1] - 1, partesData[0]);
                            let novaStringData = dataNova.toISOString().slice(0, 10);
                            setValueIfExists('id_cnpj_date', novaStringData);
                        }

                        if (response.atividade_principal && response.atividade_principal.length > 0) {
                            let dados_web = response.atividade_principal;
                            let dados = '';
                            for (let i = 0; i < dados_web.length; i++) {
                                dados += dados_web[i].code + ' - ' + dados_web[i].text + '. ';
                            }
                            setValueIfExists('cnpj_activity', dados);
                        }

                        if (response.atividades_secundarias && response.atividades_secundarias.length > 0) {
                            let dados_web = response.atividades_secundarias;
                            let dados = '';
                            for (let i = 0; i < dados_web.length; i++) {
                                dados += dados_web[i].code + ' - ' + dados_web[i].text + '. ';
                            }
                            setValueIfExists('id_cnpj_atividade_secundaria', dados);
                        }
                        console.log('Chamando fireAlert de sucesso');
                        if (typeof window.fireAlert === 'function') {
                            window.fireAlert('Dados do CNPJ carregados com sucesso!', 'success');
                        } else {
                            console.error('fireAlert não está disponível');
                        }
                    }
                    else {
                        window.fireAlert('CNPJ não encontrado na base de dados', 'primary')
                    }
                },
                error: function (xhr, textStatus, error) {
                    if (xhr.status == 429) {
                        window.fireAlert('Houve um erro ao receber os dados, aguarde 1 minuto e tente novamente.', 'primary')
                    } else {
                        window.fireAlert(`${xhr.status} - Status: ${textStatus} - ${error}`, 'warning')
                    }
                }
            });
        } else {
            window.fireAlert(`O CNPJ ${cnpj} é inválido!`, 'warning')
        }

    } catch {
        window.fireAlert('Erro ao enviar dados', 'warning')
    }

}

// Abrir Conjuge
function AbrirConjuge() {
    try {
        const divConjuge = document.getElementById('div_conjuge')
        let estadoCivil = document.getElementById('id_spouse_status')
        teste = false
        if (estadoCivil.value == '1') {
            teste = true
        }
        if (estadoCivil.value == '4') {
            teste = true
        }
        
        if (teste) {
            divConjuge.classList.add("show");
            document.getElementById('id_spouse_name').setAttribute('required', 'required');
            document.getElementById('id_spouse_last_name').setAttribute('required', 'required');
        }
        else {
            divConjuge.classList.remove("show");
            document.getElementById('id_spouse_name').value = ''
            document.getElementById('id_spouse_last_name').value = ''
            document.getElementById('id_spouse_name').removeAttribute('required');
            document.getElementById('id_spouse_last_name').removeAttribute('required');
        }
    }
    catch {
        return undefined
    }

}





// FORMATAR BOTAO TELEFONE
function atualizarBotaoContato(inputId, botaoId) {
    let fone = document.getElementById(inputId).value
    let foneTipo = parseInt(document.getElementById(inputId + "_type").value)
    let botao = document.getElementById(botaoId)

    if (foneTipo === 1) {
        botao.innerHTML = '<i class="bi bi-telephone-inbound"></i>';
        botao.href = "tel:" + fone.replace(/\D/g, '');
        botao.classList.remove("disabled");
        botao.classList.add("btn-outline-primary");
        botao.classList.remove("btn-outline-success");

    } else if (foneTipo === 2) {
        botao.innerHTML = '<i class="bi bi-whatsapp"></i>';
        botao.href = "https://wa.me/" + fone.replace(/\D/g, '');
        botao.classList.remove("disabled");
        botao.classList.remove("btn-outline-primary");
        botao.classList.add("btn-outline-success");

    } else if (foneTipo === 3) {
        botao.innerHTML = '<i class="bi bi-telegram"></i>';
        botao.href = "https://t.me/" + fone.replace(/\D/g, '');
        botao.classList.remove("disabled");
        botao.classList.add("btn-outline-primary");
        botao.classList.remove("btn-outline-success");

    } else {
        botao.innerHTML = '<i class="bi bi-dash"></i>';
        botao.classList.add("disabled");
        botao.classList.add("btn-outline-primary");
        botao.classList.remove("btn-outline-success");
    }
}


document.getElementById("id_phone_1_type").addEventListener("input", function () {
    atualizarBotaoContato("id_phone_1", "btn_id_phone_1");
});

document.getElementById("id_phone_2_type").addEventListener("input", function () {
    atualizarBotaoContato("id_phone_2", "btn_id_phone_2");
});

document.getElementById("id_phone_3_type").addEventListener("input", function () {
    atualizarBotaoContato("id_phone_3", "btn_id_phone_3");
});









// FORMATAR TELEFONE
function formatarTelefone(event, inputId) {
    var valor = document.getElementById(inputId).value;
    var retorno = valor.replace(/\D/g, "");
    retorno = retorno.replace(/^0/, "");
    if (retorno.length > 10) {
        retorno = retorno.replace(/^(\d\d)(\d{5})(\d{4}).*/, "($1) $2-$3");
    } else if (retorno.length > 5) {
        if (retorno.length === 6 && event.code === "Backspace") {
            // Necessário pois, senão o "-" fica sempre voltando ao dar backspace
            return;
        }
        retorno = retorno.replace(/^(\d\d)(\d{4})(\d{0,4}).*/, "($1) $2-$3");
    } else if (retorno.length > 2) {
        retorno = retorno.replace(/^(\d\d)(\d{0,5})/, "($1) $2");
    } else {
        if (retorno.length !== 0) {
            retorno = retorno.replace(/^(\d*)/, "($1");
        }
    }
    document.getElementById(inputId).value = retorno;
}

document.getElementById("id_phone_1").addEventListener("input", function (event) {
    formatarTelefone(event, "id_phone_1");
});

document.getElementById("id_phone_2").addEventListener("input", function (event) {
    formatarTelefone(event, "id_phone_2");
});

document.getElementById("id_phone_3").addEventListener("input", function (event) {
    formatarTelefone(event, "id_phone_3");
});






// Buscar CEP
function limpa_formulário_cep() {
    //Limpa valores do formulário de cep.
    document.getElementById('id_address').value = ("");
    document.getElementById('id_neighborhood').value = ("");
    document.getElementById('id_city').value = ("");
    document.getElementById('id_state').value = ("");
    document.getElementById('ceplog').classList.remove('d-block')
}

function meu_callback(conteudo) {
    if (!("erro" in conteudo)) {
        //Atualiza os campos com os valores.
        document.getElementById('id_address').value = (conteudo.logradouro);
        document.getElementById('id_neighborhood').value = (conteudo.bairro);
        document.getElementById('id_city').value = (conteudo.localidade);
        document.getElementById('id_state').value = (conteudo.uf);
        document.getElementById('ceplog').classList.remove('d-block')
        window.fireAlert('CEP encontrado com sucesso!', 'success')
    } //end if.
    else {
        //CEP não Encontrado.
        limpa_formulário_cep();
        document.getElementById('ceplog').classList.add('d-block')
        window.fireAlert('CEP não encontrado.', 'warning')
    }
}


function pesquisacep(valor) {
    //Nova variável "cep" somente com dígitos.
    var cep = valor.replace(/\D/g, '');
    //Verifica se campo cep possui valor informado.
    if (cep != "") {
        //Expressão regular para validar o CEP.
        var validacep = /^[0-9]{8}$/;
        //Valida o formato do CEP.
        if (validacep.test(cep)) {
            //Preenche os campos com "..." enquanto consulta webservice.
            document.getElementById('id_address').value = "...";
            document.getElementById('id_neighborhood').value = "...";
            document.getElementById('id_city').value = "...";
            document.getElementById('id_state').value = "...";
            //Cria um elemento javascript.
            var script = document.createElement('script');
            //Sincroniza com o callback.
            script.src = 'https://viacep.com.br/ws/' + cep + '/json/?callback=meu_callback';
            //Insere script no documento e carrega o conteúdo.
            document.body.appendChild(script);
        } //end if.
        else {
            //cep é inválido.
            limpa_formulário_cep();
            document.getElementById('ceplog').classList.add('d-block')
            window.fireAlert('Formato de CEP inválido.', 'danger')
        }
    } //end if.
    else {
        //cep sem valor, limpa formulário.
        limpa_formulário_cep();
        document.getElementById('ceplog').classList.remove('d-block')
    }
};




function validarCNPJ_x() {
    let vcnpj = document.getElementById('id_cnpj')
    const cnpjlog = document.getElementById('cnpjlog')
    let teste = validarCNPJ(vcnpj.value)
    if (vcnpj.value.length == 0) {
        teste = true
    }
    if (teste) {
        cnpjlog.classList.add("d-none");
        cnpjlog.classList.remove("d-block");
    } else {
        cnpjlog.classList.remove("d-none");
        cnpjlog.classList.add("d-block");
    }
}


function validarCNPJ_titular() {
    let vcnpj = document.getElementById('id_documento_titular')
    const cnpjlog = document.getElementById('cnpjlog_titular')
    let teste = validarCNPJ(vcnpj.value)
    if (vcnpj.value.length == 0) {
        teste = true
    }
    if (teste) {
        cnpjlog.classList.add("d-none");
        cnpjlog.classList.remove("d-block");
    } else {
        cnpjlog.classList.remove("d-none");
        cnpjlog.classList.add("d-block");
    }
}


function validarCNPJ(cnpj) {
    cnpj = cnpj.replace(/[^\d]+/g, '');
    if (cnpj == '') return false;
    if (cnpj.length != 14)
        return false;
    // Elimina CNPJs invalidos conhecidos
    if (cnpj == "00000000000000" ||
        cnpj == "11111111111111" ||
        cnpj == "22222222222222" ||
        cnpj == "33333333333333" ||
        cnpj == "44444444444444" ||
        cnpj == "55555555555555" ||
        cnpj == "66666666666666" ||
        cnpj == "77777777777777" ||
        cnpj == "88888888888888" ||
        cnpj == "99999999999999")
        return false;
    // Valida DVs
    tamanho = cnpj.length - 2
    numeros = cnpj.substring(0, tamanho);
    digitos = cnpj.substring(tamanho);
    soma = 0;
    pos = tamanho - 7;
    for (i = tamanho; i >= 1; i--) {
        soma += numeros.charAt(tamanho - i) * pos--;
        if (pos < 2)
            pos = 9;
    }
    resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;
    if (resultado != digitos.charAt(0))
        return false;

    tamanho = tamanho + 1;
    numeros = cnpj.substring(0, tamanho);
    soma = 0;
    pos = tamanho - 7;
    for (i = tamanho; i >= 1; i--) {
        soma += numeros.charAt(tamanho - i) * pos--;
        if (pos < 2)
            pos = 9;
    }
    resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;
    if (resultado != digitos.charAt(1))
        return false;

    return true;

}


// CPF
function TestaCPF(strCPF) {
    var Soma;
    var Resto;
    Soma = 0;
    if (strCPF == "00000000000") return false;
    if (strCPF == "11111111111") return false;
    if (strCPF == "22222222222") return false;
    if (strCPF == "33333333333") return false;
    if (strCPF == "44444444444") return false;
    if (strCPF == "55555555555") return false;
    if (strCPF == "66666666666") return false;
    if (strCPF == "77777777777") return false;
    if (strCPF == "88888888888") return false;
    if (strCPF == "99999999999") return false;
    for (i = 1; i <= 9; i++) Soma = Soma + parseInt(strCPF.substring(i - 1, i)) * (11 - i);
    Resto = (Soma * 10) % 11;
    if ((Resto == 10) || (Resto == 11)) Resto = 0;
    if (Resto != parseInt(strCPF.substring(9, 10))) return false;
    Soma = 0;
    for (i = 1; i <= 10; i++) Soma = Soma + parseInt(strCPF.substring(i - 1, i)) * (12 - i);
    Resto = (Soma * 10) % 11;
    if ((Resto == 10) || (Resto == 11)) Resto = 0;
    if (Resto != parseInt(strCPF.substring(10, 11))) return false;
    return true;
}

function ValidaCPF() {
    let formCpf = document.getElementById('id_cpf')
    const cpflog = document.getElementById('cpflog')
    teste = TestaCPF(formCpf.value.replace(/[^\d]/g, ''))
    if (formCpf.value.length == 0) {
        teste = true
    }
    if (teste) {
        cpflog.classList.add("d-none");
        cpflog.classList.remove("d-block");
    } else {
        cpflog.classList.remove("d-none");
        cpflog.classList.add("d-block");
    }
}


function ValidaCPF_titular() {
    let formCpf = document.getElementById('id_documento_titular')
    const cpflog = document.getElementById('cnpjlog_titular')
    teste = TestaCPF(formCpf.value.replace(/[^\d]/g, ''))
    if (formCpf.value.length == 0) {
        teste = true
    }
    if (teste) {
        cpflog.classList.add("d-none");
        cpflog.classList.remove("d-block");
    } else {
        cpflog.classList.remove("d-none");
        cpflog.classList.add("d-block");
    }
}



