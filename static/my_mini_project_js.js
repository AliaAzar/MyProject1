console.log('Я працюю');
const routes = [
    { path: '/signUp_pg', handler: signupHandler },
    { path: '/login_pg', handler: loginHandler },
    { path: '/question1_pg', handler: question1Handler },
    { path: '/question2_pg', handler: question2Handler },
    { path: '/question3_pg', handler: question3Handler },
    { path: '/question4_pg', handler: question4Handler },
    { path: '/question5_pg', handler: question5Handler },
    { path: '/question6_pg', handler: question6Handler },
    { path: '/question7_pg', handler: question7Handler },
    { path: '/question8_pg', handler: question8Handler },
    { path: '/question9_pg', handler: question9Handler },
    { path: '/question10_pg', handler: question10Handler },
    { path: '/results_pg', handler: resultsHandler },
    { path: '/results-comparison_pg', handler: resultsComparisonHandler }
];

function RequestToServer(form, url) {
    const formData = new FormData(form);
    console.log('Я RequestToServer');
    return new Promise((resolve, reject) => {
        fetch(url, {
            method: "POST",
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            resolve(data);
        });
    });
};


function loginHandler() {
    const Form = document.querySelector('#login-form');
    const res = document.getElementById('result');
    const urlLogin = '/login';
    console.log('Я loginHandler');
    Form.addEventListener('submit', (event) => {
        event.preventDefault();
        RequestToServer(event.target, urlLogin)
        .then(response => {
        res.innerHTML = `<p>${response.message}</p>
        <a href=${response.url1}>${response.message2}</a>`});
    });
};

function signupHandler() {
    const Form = document.querySelector('#signUp-form');
    const res = document.getElementById('result');
    const urlSignup = '/signUp';
    console.log('Я signupHandler');
    Form.addEventListener('submit', (event) => {
        event.preventDefault();
        RequestToServer(event.target, urlSignup)
        .then(response => {
        res.innerHTML = `<p>${response.message}</p>
        <a href="/question1_pg">${response.message2}</a>`});
    });
}

function question1Handler() {
    const Form = document.querySelector('#question1-form');
    const res = document.getElementById('result');
    const urlQuestion1 = '/question1';
    console.log('Я question1Handler');
    Form.addEventListener('submit', (event) => {
        event.preventDefault();
        RequestToServer(event.target, urlQuestion1)
        .then(response => {
        res.innerHTML = `<a href="/question2_pg">${response.message}</a>`});
    });
};

function question2Handler() {
    const Form = document.querySelector('#question2-form');
    const res = document.getElementById('result');
    const urlQuestion2 = '/question2';
    console.log('Я question2Handler');
    Form.addEventListener('submit', (event) => {
        event.preventDefault();
        RequestToServer(event.target, urlQuestion2)
        .then(response => {
        res.innerHTML = `<a href="/question3_pg">${response.message}</a>`});
    });
};

function question3Handler() {
    const Form = document.querySelector('#question3-form');
    const res = document.getElementById('result');
    const urlQuestion3 = '/question3';
    console.log('Я question3Handler');
    Form.addEventListener('submit', (event) => {
        event.preventDefault();
        RequestToServer(event.target, urlQuestion3)
        .then(response => {
        res.innerHTML = `<a href="/question4_pg">${response.message}</a>`});
    });
};

function question4Handler() {
    const Form = document.querySelector('#question4-form');
    const res = document.getElementById('result');
    const urlQuestion4 = '/question4';
    console.log('Я question4Handler');
    Form.addEventListener('submit', (event) => {
        event.preventDefault();
        RequestToServer(event.target, urlQuestion4)
        .then(response => {
        res.innerHTML = `<a href="/question5_pg">${response.message}</a>`});
    });
};

function question5Handler() {
    const Form = document.querySelector('#question5-form');
    const res = document.getElementById('result');
    const urlQuestion5 = '/question5';
    console.log('Я question5Handler');
    Form.addEventListener('submit', (event) => {
        event.preventDefault();
        RequestToServer(event.target, urlQuestion5)
        .then(response => {
        res.innerHTML = `<a href="/question6_pg">${response.message}</a>`});
    });
};

function question6Handler() {
    const Form = document.querySelector('#question6-form');
    const res = document.getElementById('result');
    const urlQuestion6 = '/question6';
    console.log('Я question6Handler');
    Form.addEventListener('submit', (event) => {
        event.preventDefault();
        RequestToServer(event.target, urlQuestion6)
        .then(response => {
        res.innerHTML = `<a href="/question7_pg">${response.message}</a>`});
    });
};

function question7Handler() {
    const Form = document.querySelector('#question7-form');
    const res = document.getElementById('result');
    const urlQuestion7 = '/question7';
    console.log('Я question7Handler');
    Form.addEventListener('submit', (event) => {
        event.preventDefault();
        RequestToServer(event.target, urlQuestion7)
        .then(response => {
        res.innerHTML = `<a href="/question8_pg">${response.message}</a>`});
    });
};

function question8Handler() {
    const Form = document.querySelector('#question8-form');
    const res = document.getElementById('result');
    const urlQuestion8 = '/question8';
    console.log('Я question8Handler');
    Form.addEventListener('submit', (event) => {
        event.preventDefault();
        RequestToServer(event.target, urlQuestion8)
        .then(response => {
        res.innerHTML = `<a href="/question9_pg">${response.message}</a>`});
    });
};

function question9Handler() {
    const Form = document.querySelector('#question9-form');
    const res = document.getElementById('result');
    const urlQuestion9 = '/question9';
    console.log('Я question1Handler');
    Form.addEventListener('submit', (event) => {
        event.preventDefault();
        RequestToServer(event.target, urlQuestion9)
        .then(response => {
        res.innerHTML = `<a href="/question1_pg">${response.message}</a>`});
    });
};

function question10Handler() {
    const Form = document.querySelector('#question10-form');
    const res = document.getElementById('result');
    const urlQuestion10 = '/question10';
    console.log('Я question10Handler');
    Form.addEventListener('submit', (event) => {
        event.preventDefault();
        RequestToServer(event.target, urlQuestion10)
        .then(response => {
        res.innerHTML = `<a href="/results_pg">${response.message}</a>`});
    });
};

function resultsHandler() {
    const Form = document.querySelector('#results-form');
    const res = document.getElementById('result');
    const urlResults = '/results';
    console.log('Я resultsHandler');
    Form.addEventListener('submit', (event) => {
        event.preventDefault();
        RequestToServer(event.target, urlResults)
        .then(response => {
        res.innerHTML = `${response.innerHTML1}`});
    });
};

function resultsComparisonHandler() {
    const Form = document.querySelector('#results-comparison-form');
    const res = document.getElementById('result');
    const urlResultsComparison = '/results_comparison';
    console.log('Я resultsComparisonHandler');
    Form.addEventListener('submit', (event) => {
        event.preventDefault();
        RequestToServer(event.target, urlResultsComparison)
        .then(response => {
        res.innerHTML = `${response.innerHTML1}`});
    });
};



function handleRoutes() {
    const currentPath = window.location.pathname;
    console.log('Я  handleRoutes');
    const routeData = routes.find(route => route.path === currentPath);
    routeData.handler();
};

document.addEventListener("DOMContentLoaded", function() {
    handleRoutes();
});
