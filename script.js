const input = document.querySelector('#text');
const button = document.querySelector('#button');

button.onclick = () => {
    let phrasesListElement = document.querySelector('#phrases_list');
    if (phrasesListElement) {
        phrasesListElement.remove();
    };
    
    let phrasesElements = document.querySelectorAll('.phrase');

    for (let phraseElement of phrasesElements) {
        phraseElement.nextElementSibling.nextElementSibling.remove();
        phraseElement.nextElementSibling.remove();
        phraseElement.remove();
    };
}

input.onkeyup = (event) => {
    if (event.key == 13 || event.key == 'Enter') {
        eel.parse(input.value);
        input.value = '';
    }
};


function render_phrases(lang, phrases) {
    let phraseListHTML = '<p id="phrases_list"><b>ЗАГРУЖЕННЫЕ ФРАЗЫ:</b></p>';
    document.body.insertAdjacentHTML('beforeend', phraseListHTML);

    if (lang == 'en') {
        for (let phrase of phrases) {
            let blockHTML = `
                        <p class="phrase">${phrase[0]}</p>
                        <audio controls src="${phrase[1]}" preload="none"></audio>
                        <br>`;
            document.body.insertAdjacentHTML('beforeend', blockHTML);
        };
    } else {
        for (let phrase of phrases) {
            let blockHTML = `
                        <p class="phrase">${phrase[0]}</p>
                        <a href="${phrase[1]}" target="_blank">ССЫЛКА НА ПЛЕЕР</a>
                        <br>`;
            document.body.insertAdjacentHTML('beforeend', blockHTML);
        };
    };
};

eel.expose(render_phrases);
