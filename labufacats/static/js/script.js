let selectedNumber = null;

function selectNumber(number) {
    const numberButton = document.querySelector(`button[data-number="${number}"]`);

    if (numberButton.classList.contains("confirmed")) {
        // O número já foi selecionado e confirmado, não faz nada
        return;
    }

    if (selectedNumber === number) {
        // O número já estava selecionado, então o usuário está confirmando a escolha
        confirmSelection(number);
    } else {
        // O usuário está selecionando um novo número
        selectedNumber = number;
        showSelectedNumber();
    }
}

function confirmSelection(number) {
    const numberButton = document.querySelector(`button[data-number="${number}"]`);
    numberButton.classList.add("confirmed");

    const confirm = window.confirm(`Você selecionou o número ${number}. Confirma a escolha?`);
    if (confirm) {
        // O usuário confirmou a escolha
        // Aqui você pode adicionar a lógica adicional que deseja executar
        saveSelections(); // Salvar as seleções no localStorage

        const selectedNumberElement = document.getElementById("selected-number");
        selectedNumberElement.textContent = ""; // Limpar o conteúdo do elemento
    } else {
        // O usuário cancelou a escolha
        numberButton.classList.remove("confirmed");
        selectedNumber = null;
        showSelectedNumber();
        saveSelections(); // Salvar as seleções no localStorage
    }
}

// Função para salvar os números selecionados e cores no localStorage
function saveSelections() {
    localStorage.setItem("selectedNumber", selectedNumber);
    const confirmedNumbers = document.querySelectorAll(".confirmed");
    const confirmedNumbersArray = Array.from(confirmedNumbers).map(button => button.dataset.number);
    localStorage.setItem("confirmedNumbers", JSON.stringify(confirmedNumbersArray));
}

// Função para carregar os números selecionados e cores do localStorage
function loadSelections() {
    selectedNumber = localStorage.getItem("selectedNumber");
    if (selectedNumber) {
        showSelectedNumber();
    }

    const confirmedNumbersJSON = localStorage.getItem("confirmedNumbers");
    if (confirmedNumbersJSON) {
        const confirmedNumbersArray = JSON.parse(confirmedNumbersJSON);
        confirmedNumbersArray.forEach(number => {
            const numberButton = document.querySelector(`button[data-number="${number}"]`);
            if (numberButton) {
                numberButton.classList.add("confirmed");
            }
        });
    }
}

// Função para limpar todas as seleções e redefinir o armazenamento local
function clearSelections() {
    localStorage.removeItem("selectedNumber");
    localStorage.removeItem("confirmedNumbers");

    // Também é uma boa ideia redefinir a aparência dos botões para remover as classes "confirmed"
    const confirmedButtons = document.querySelectorAll(".confirmed");
    confirmedButtons.forEach(button => {
        button.classList.remove("confirmed");
    });

    // Limpar o número selecionado
    selectedNumber = null;
    const selectedNumberElement = document.getElementById("selected-number");
    selectedNumberElement.textContent = "";

    // Salvar as alterações no localStorage
    saveSelections();
}

class MobileNavbar {
    constructor(mobileMenu, navList, navLinks) {
        this.mobileMenu = document.querySelector(mobileMenu);
        this.navList = document.querySelector(navList);
        this.navLinks = document.querySelectorAll(navLinks);
        this.activeClass = "active";
        this.handleClick = this.handleClick.bind(this);
    }

    animateLinks() {
        this.navLinks.forEach((link, index) => {
            link.style.animation
                ? (link.style.animation = "")
                : (link.style.animation = `navLinkFade 0.5s ease forwards ${
                    index / 7 + 0.3
                }s`);
        });
    }

    handleClick() {
        this.navList.classList.toggle(this.activeClass);
        this.mobileMenu.classList.toggle(this.activeClass);
        this.animateLinks();
    }

    addClickEvent() {
        this.mobileMenu.addEventListener("click", this.handleClick);
    }

    init() {
        if (this.mobileMenu) {
        this.addClickEvent();
        }
        return this;
    }
    }

    const mobileNavbar = new MobileNavbar(
        ".mobile-menu",
        ".nav-list",
        ".nav-list li",
    );
    mobileNavbar.init();
    // Função para fechar automaticamente as mensagens após um determinado tempo
    document.addEventListener('DOMContentLoaded', function() {
        const autoDismissElements = document.querySelectorAll('.auto-dismiss');
        autoDismissElements.forEach(function(element) {
            const autoDismissTime = element.getAttribute('data-auto-dismiss');
            setTimeout(function() {
                element.style.display = 'none';
            }, autoDismissTime);
        });
    });


// Favoritos
function handleStarClick() {
    var starIcon = document.getElementById("star-icon");

    // Se a cor for branca, pergunte se o usuário deseja adicionar aos favoritos
    if (starIcon.style.color === "white") {
        var confirmation = confirm("Você deseja adicionar esse gato aos favoritos?");

        // Se o usuário confirmar, alterar a cor para amarelo
        if (confirmation) {
            starIcon.style.color = "yellow";
        }
    }
    // Se a cor for amarela, pergunte se o usuário deseja remover dos favoritos
    else if (starIcon.style.color === "yellow") {
        var confirmation = confirm("Você deseja remover esse gato dos favoritos?");

        // Se o usuário confirmar, alterar a cor de volta para branca
        if (confirmation) {
            starIcon.style.color = "white";
        }
    }
}

// Adicionar um ouvinte de eventos para o clique no ícone de estrela
document.getElementById("star-icon").addEventListener("click", handleStarClick);

// Chame a função de carregamento assim que a página carregar
window.onload = loadSelections;


