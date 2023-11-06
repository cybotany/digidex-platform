const loginForm = document.getElementById("loginForm");

loginForm.addEventListener("submit", async (event) => {
    console.log("Login form submitted");
    event.preventDefault();

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
        localStorage.setItem("refreshToken", data.refresh);
    } else {
        console.error("Authentication failed:", data);
    }
}

const refreshToken = async () => {
    try {
        const refresh = localStorage.getItem("refreshToken");
        const response = await fetch("/api/token/refresh/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ refresh })
        });

        const data = await response.json();

        if (response.ok && data.access) {
            localStorage.setItem("accessToken", data.access);
        } else {
            throw new Error(data.detail || "Failed to refresh token.");
        }
    } catch (error) {
        console.error("Refresh token error:", error.message);
    }
}
