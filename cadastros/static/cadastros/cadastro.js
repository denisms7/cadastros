window.onload = function () {
    btncontato1()
    btncontato2()
    btncontato3()
    AbrirConjuge()
};


function carregarCNPJ(cnpj) {
    let v_cnpj = cnpj.replace(/[^0-9]/g, '')
    let v_url = 'https://www.receitaws.com.br/v1/cnpj/' + v_cnpj
    const alertPlaceholder = document.getElementById('liveAlertPlaceholder')
    const alert = (message, type) => {
        const wrapper = document.createElement('div')
        wrapper.innerHTML = [
            `<div class="alert alert-${type} alert-dismissible" role="alert">`,
            `   <div>${message}</div>`,
            '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
            '</div>'
        ].join('')
        alertPlaceholder.append(wrapper)
    }

    try {
        if (v_cnpj.length == 14 && validarCNPJ(v_cnpj)) {
            $.ajax({
                url: v_url,
                dataType: 'jsonp',
                crossDomain: true,
                success: function (response) {
                    if (response.status === "OK") {
                        if (response.nome != '') {
                            document.getElementById('id_pessoa_juridica').value = response.nome
                        }
                        if (response.fantasia != '') {
                            document.getElementById('id_nome_fantasia').value = response.fantasia
                        }
                        if (response.cep != '') {
                            document.getElementById('id_cep').value = response.cep
                        }
                        if (response.uf != '') {
                            document.getElementById('id_estado').value = response.uf
                        }
                        if (response.municipio != '') {
                            document.getElementById('id_cidade').value = response.municipio
                        }
                        if (response.bairro != '') {
                            document.getElementById('id_bairro').value = response.bairro
                        }
                        if (response.logradouro != '') {
                            document.getElementById('id_endereco').value = response.logradouro
                        }
                        if (response.numero != '') {
                            document.getElementById('id_numero').value = response.numero
                        }
                        if (response.situacao != '') {
                            document.getElementById('id_cnpj_situacao').value = response.situacao
                        }
                        if (response.porte != '') {
                            document.getElementById('id_cnpj_porte').value = response.porte
                        }
                        if (response.abertura != '') {
                            let dataOriginal = response.abertura
                            let partesData = dataOriginal.split("/");
                            let dataNova = new Date(partesData[2], partesData[1] - 1, partesData[0]);
                            let novaStringData = dataNova.toISOString().slice(0, 10);
                            document.getElementById('id_cnpj_data_abertura').value = novaStringData
                        }
                        if (response.tipo != '') {
                            document.getElementById('id_cnpj_tipo').value = response.tipo
                        }
                        if (response.atividade_principal.length > 0) {
                            let dados_web = response.atividade_principal;
                            let dados = '';
                            for (let i = 0; i < dados_web.length; i++) {
                                dados = dados_web[i].code + ' - ' + dados_web[i].text + '. '
                            }
                            document.getElementById('id_cnpj_atividade_principal').value = dados;
                        }
                        if (response.atividades_secundarias.length > 0) {
                            let dados_web = response.atividades_secundarias;
                            let dados = '';
                            for (let i = 0; i < dados_web.length; i++) {
                                dados = dados_web[i].code + ' - ' + dados_web[i].text + '. '
                            }
                            // document.getElementById('id_cnpj_atividade_principal').value = dados;
                        }
                    } 
                    else {
                        alert('CNPJ n??o encontrado na base de dados', 'primary')
                    }
                },
                error: function (xhr, textStatus, error) {
                    if (xhr.status == 429) {
                        alert('Houve um erro ao receber os dados, aguarde 1 minuto e tente novamente.', 'primary')
                    } else {
                        alert(`${xhr.status} - Status: ${textStatus} - ${error}`, 'warning')
                    }
                }
            });
        } else {
            alert(`O CNPJ ${cnpj} ?? inv??lido!`, 'warning')
        }

    } catch {
        alert('Erro ao enviar dados', 'warning')
    }

}

// Abrir Conjuge
function AbrirConjuge() {
    try {
        const divConjuge = document.getElementById('div_conjuge')
        let estadoCivil = document.getElementById('id_estado_civil')
        teste = false
        if (estadoCivil.value == '1') {
            teste = true
        }
        if (estadoCivil.value == '4') {
            teste = true
        }
        if (teste) {
            divConjuge.classList.add("show");
        }
        else {
            divConjuge.classList.remove("show");
            document.getElementById('conjuge_nome').value = ''
            document.getElementById('conjuge_sobrenome').value = ''
        }
    }
    catch {
        return undefined
    }

}


// FORMATAR TELEFONE
function mascaraFone1(event) {
    var valor = document.getElementById("id_fone_1").attributes[0].ownerElement['value'];
    var retorno = valor.replace(/\D/g, "");
    retorno = retorno.replace(/^0/, "");
    if (retorno.length > 10) {
        retorno = retorno.replace(/^(\d\d)(\d{5})(\d{4}).*/, "($1) $2-$3");
    } else if (retorno.length > 5) {
        if (retorno.length == 6 && event.code == "Backspace") {
            // necess??rio pois sen??o o "-" fica sempre voltando ao dar backspace
            return;
        }
        retorno = retorno.replace(/^(\d\d)(\d{4})(\d{0,4}).*/, "($1) $2-$3");
    } else if (retorno.length > 2) {
        retorno = retorno.replace(/^(\d\d)(\d{0,5})/, "($1) $2");
    } else {
        if (retorno.length != 0) {
            retorno = retorno.replace(/^(\d*)/, "($1");
        }
    }
    document.getElementById("id_fone_1").attributes[0].ownerElement['value'] = retorno;
}


function mascaraFone2(event) {
    var valor = document.getElementById("id_fone_2").attributes[0].ownerElement['value'];
    var retorno = valor.replace(/\D/g, "");
    retorno = retorno.replace(/^0/, "");
    if (retorno.length > 10) {
        retorno = retorno.replace(/^(\d\d)(\d{5})(\d{4}).*/, "($1) $2-$3");
    } else if (retorno.length > 5) {
        if (retorno.length == 6 && event.code == "Backspace") {
            // necess??rio pois sen??o o "-" fica sempre voltando ao dar backspace
            return;
        }
        retorno = retorno.replace(/^(\d\d)(\d{4})(\d{0,4}).*/, "($1) $2-$3");
    } else if (retorno.length > 2) {
        retorno = retorno.replace(/^(\d\d)(\d{0,5})/, "($1) $2");
    } else {
        if (retorno.length != 0) {
            retorno = retorno.replace(/^(\d*)/, "($1");
        }
    }
    document.getElementById("id_fone_2").attributes[0].ownerElement['value'] = retorno;
}


function mascaraFone3(event) {
    var valor = document.getElementById("id_fone_3").attributes[0].ownerElement['value'];
    var retorno = valor.replace(/\D/g, "");
    retorno = retorno.replace(/^0/, "");
    if (retorno.length > 10) {
        retorno = retorno.replace(/^(\d\d)(\d{5})(\d{4}).*/, "($1) $2-$3");
    } else if (retorno.length > 5) {
        if (retorno.length == 6 && event.code == "Backspace") {
            // necess??rio pois sen??o o "-" fica sempre voltando ao dar backspace
            return;
        }
        retorno = retorno.replace(/^(\d\d)(\d{4})(\d{0,4}).*/, "($1) $2-$3");
    } else if (retorno.length > 2) {
        retorno = retorno.replace(/^(\d\d)(\d{0,5})/, "($1) $2");
    } else {
        if (retorno.length != 0) {
            retorno = retorno.replace(/^(\d*)/, "($1");
        }
    }
    document.getElementById("id_fone_3").attributes[0].ownerElement['value'] = retorno;
}




// Buscar CEP
function limpa_formul??rio_cep() {
    //Limpa valores do formul??rio de cep.
    document.getElementById('id_endereco').value = ("");
    document.getElementById('id_bairro').value = ("");
    document.getElementById('id_cidade').value = ("");
    document.getElementById('id_estado').value = ("");
    document.getElementById('ceplog').classList.remove('d-block')
}

function meu_callback(conteudo) {
    if (!("erro" in conteudo)) {
        //Atualiza os campos com os valores.
        document.getElementById('id_endereco').value = (conteudo.logradouro);
        document.getElementById('id_bairro').value = (conteudo.bairro);
        document.getElementById('id_cidade').value = (conteudo.localidade);
        document.getElementById('id_estado').value = (conteudo.uf);
        document.getElementById('ceplog').classList.remove('d-block')
    } //end if.
    else {
        //CEP n??o Encontrado.
        limpa_formul??rio_cep();
        //alert("CEP n??o encontrado.");
        document.getElementById('ceplog').classList.add('d-block')
    }
}


function pesquisacep(valor) {
    //Nova vari??vel "cep" somente com d??gitos.
    var cep = valor.replace(/\D/g, '');
    //Verifica se campo cep possui valor informado.
    if (cep != "") {
        //Express??o regular para validar o CEP.
        var validacep = /^[0-9]{8}$/;
        //Valida o formato do CEP.
        if (validacep.test(cep)) {
            //Preenche os campos com "..." enquanto consulta webservice.
            document.getElementById('id_endereco').value = "...";
            document.getElementById('id_bairro').value = "...";
            document.getElementById('id_cidade').value = "...";
            document.getElementById('id_estado').value = "...";
            //Cria um elemento javascript.
            var script = document.createElement('script');
            //Sincroniza com o callback.
            script.src = 'https://viacep.com.br/ws/' + cep + '/json/?callback=meu_callback';
            //Insere script no documento e carrega o conte??do.
            document.body.appendChild(script);
        } //end if.
        else {
            //cep ?? inv??lido.
            limpa_formul??rio_cep();
            document.getElementById('ceplog').classList.add('d-block')
            // alert("Formato de CEP inv??lido.");
        }
    } //end if.
    else {
        //cep sem valor, limpa formul??rio.
        limpa_formul??rio_cep();
        document.getElementById('ceplog').classList.remove('d-block')
    }
};



function btncontato1() {
    let fone_1 = document.getElementById("id_fone_1").value
    let fone_1_tipo = document.getElementById("id_fone_1_tipo").value
    let botao = document.getElementById("btn_id_fone_1")
    if (fone_1_tipo === '1') {
        botao.innerHTML = '<i class="bi bi-telephone-inbound"></i>'
        botao.href = "tel:" + fone_1.replace(/\D/g, '') + "";
        botao.classList.remove("disabled")
        botao.classList.add("btn-outline-dark")
        botao.classList.remove("btn-outline-success")
    } else if (fone_1_tipo === '2') {
        botao.innerHTML = '<i class="bi bi-whatsapp"></i>'
        botao.href = "https://wa.me/" + fone_1.replace(/\D/g, '') + "";
        botao.classList.remove("disabled")
        botao.classList.remove("btn-outline-dark")
        botao.classList.add("btn-outline-success")
    } else if (fone_1_tipo === '3') {
        botao.innerHTML = '<i class="bi bi-telegram"></i>'
        botao.href = "https://t.me/" + fone_1.replace(/\D/g, '') + "";
        botao.classList.remove("disabled")
        botao.classList.add("btn-outline-dark")
        botao.classList.remove("btn-outline-success")
    } else {
        botao.innerHTML = '<i class="bi bi-dash"></i>'
        botao.classList.add("disabled")
        botao.classList.add("btn-outline-dark")
        botao.classList.remove("btn-outline-success")
    }
}

function btncontato2() {
    let fone_1 = document.getElementById("id_fone_2").value
    let fone_1_tipo = document.getElementById("id_fone_2_tipo").value
    let botao = document.getElementById("btn_id_fone_2")
    if (fone_1_tipo === '1') {
        botao.innerHTML = '<i class="bi bi-telephone-inbound"></i>'
        botao.href = "tel:" + fone_1.replace(/\D/g, '') + "";
        botao.classList.remove("disabled")
        botao.classList.add("btn-outline-dark")
        botao.classList.remove("btn-outline-success")
    } else if (fone_1_tipo === '2') {
        botao.innerHTML = '<i class="bi bi-whatsapp"></i>'
        botao.href = "https://wa.me/" + fone_1.replace(/\D/g, '') + "";
        botao.classList.remove("disabled")
        botao.classList.remove("btn-outline-dark")
        botao.classList.add("btn-outline-success")
    } else if (fone_1_tipo === '3') {
        botao.innerHTML = '<i class="bi bi-telegram"></i>'
        botao.href = "https://t.me/" + fone_1.replace(/\D/g, '') + "";
        botao.classList.remove("disabled")
        botao.classList.add("btn-outline-dark")
        botao.classList.remove("btn-outline-success")
    } else {
        botao.innerHTML = '<i class="bi bi-dash"></i>'
        botao.classList.add("disabled")
        botao.classList.add("btn-outline-dark")
        botao.classList.remove("btn-outline-success")
    }
}

function btncontato3() {
    let fone_1 = document.getElementById("id_fone_3").value
    let fone_1_tipo = document.getElementById("id_fone_3_tipo").value
    let botao = document.getElementById("btn_id_fone_3")
    if (fone_1_tipo === '1') {
        botao.innerHTML = '<i class="bi bi-telephone-inbound"></i>'
        botao.href = "tel:" + fone_1.replace(/\D/g, '') + "";
        botao.classList.remove("disabled")
        botao.classList.add("btn-outline-dark")
        botao.classList.remove("btn-outline-success")
    } else if (fone_1_tipo === '2') {
        botao.innerHTML = '<i class="bi bi-whatsapp"></i>'
        botao.href = "https://wa.me/" + fone_1.replace(/\D/g, '') + "";
        botao.classList.remove("disabled")
        botao.classList.remove("btn-outline-dark")
        botao.classList.add("btn-outline-success")
    } else if (fone_1_tipo === '3') {
        botao.innerHTML = '<i class="bi bi-telegram"></i>'
        botao.href = "https://t.me/" + fone_1.replace(/\D/g, '') + "";
        botao.classList.remove("disabled")
        botao.classList.add("btn-outline-dark")
        botao.classList.remove("btn-outline-success")
    } else {
        botao.innerHTML = '<i class="bi bi-dash"></i>'
        botao.classList.add("disabled")
        botao.classList.add("btn-outline-dark")
        botao.classList.remove("btn-outline-success")
    }
}


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

