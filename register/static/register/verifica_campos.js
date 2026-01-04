function isSectionEmpty(selector) {
    const section = document.querySelector(selector);
    if (!section) return true;

    const inputs = section.querySelectorAll('input');
    const selects = section.querySelectorAll('select');

    const hasValue = el => el.value !== '' && el.value !== '0';

    return ![...inputs, ...selects].some(hasValue);
}

function toggleSection(selector, checkboxId, elementId) {
    const isEmpty = isSectionEmpty(selector);
    const checkbox = document.getElementById(checkboxId);
    const element = document.getElementById(elementId);

    if (!checkbox || !element) return;

    checkbox.checked = !isEmpty;
    element.classList.toggle('show', !isEmpty);
}

// Lista de verificações
const sections = [
    { selector: '.Verifica_Contato', checkboxId: 'btncheck1', elementId: 'idContato' },
    { selector: '.Verifica_Endereco', checkboxId: 'btncheck2', elementId: 'idEndereco' },
    { selector: '.Verifica_Banco', checkboxId: 'btncheck3', elementId: 'idBanco' },
    { selector: '.Verifica_Cnh', checkboxId: 'btncheck4', elementId: 'idveiculo' }
];

// Executa verificações
sections.forEach(({ selector, checkboxId, elementId }) => {
    try {
        toggleSection(selector, checkboxId, elementId);
    } catch (e) {
        console.warn(`${selector} não existe ou não foi carregada corretamente. Ignorando verificação.`);
    }
});
