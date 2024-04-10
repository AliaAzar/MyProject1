console.log('Я працюю');
const routes = [
    { path: '/signUp_pg', handler: signupHandler },
    { path: '/login_pg', handler: loginHandler },
    { path: '/favourite_food_pg', handler: favouriteFoodHandler },
    { path: '/check_favourite_food_pg', handler: checkFavouriteFoodHandler }
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
    const res2 = document.getElementById('result2');
    const urlSignup = '/signUp';
    console.log('Я signupHandler');
    Form.addEventListener('submit', (event) => {
        event.preventDefault();
        RequestToServer(event.target, urlSignup)
        .then(response => {
        res.innerHTML = `<p>${response.message}</p>
        <a href="/favourite_food_pg">${response.message2}</a>`});
    });
}

function favouriteFoodHandler() {
    const Form = document.querySelector('#favourite-food-form');
    const res = document.getElementById('result');
    const urlFavouriteFood = '/favourite_food';
    console.log('Я favouriteFoodHandler');
    Form.addEventListener('submit', (event) => {
    event.preventDefault();
    RequestToServer(event.target, urlFavouriteFood)
    .then(response => {
    res.innerHTML = response.innerHTML1});
    });
};

function checkFavouriteFoodHandler() {
    const Form = document.querySelector('#check-favourite-food-form');
    const res = document.getElementById('result');
    const urlCheckFavouriteFood = '/check_favourite_food';
    console.log('Я checkFavouriteFoodHandler');
    Form.addEventListener('submit', (event) => {
    event.preventDefault();
    RequestToServer(event.target, urlCheckFavouriteFood)
    .then(response => {
    res.innerHTML = `<p>${response.message}</p>
    <a href="/favourite_food_pg">Записати улюблені страви</a>`});
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
