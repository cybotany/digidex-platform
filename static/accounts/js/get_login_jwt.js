const loginForm = document.getElementById("loginForm");

loginForm.addEventListener("submit", async (event) => {
    console.log("Login form submitted");

    const formData = new FormData(loginForm);
    const username = formData.get('username');
    const password = formData.get('password');

    await login(username, password);
});

const login = async (username, password) => {
    const response = await fetch("/api/token/", {
        method: "POST", 
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
        credentials: 'include'
    });

    const data = await response.json();

    if (response.ok && data.access && data.refresh) {
        localStorage.setItem("accessToken", data.access);
    } else {
        console.error("Authentication failed:", data);
    }
}
