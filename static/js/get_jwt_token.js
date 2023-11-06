const loginForm = document.getElementById("loginForm");

loginForm.addEventListener("submit", async (event) => {
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
        body: JSON.stringify({ username, password })
    });

    const data = await response.json();

    if (response.ok && data.access && data.refresh) {
        localStorage.setItem("accessToken", data.access);
        localStorage.setItem("refreshToken", data.refresh);
    } else {
        console.error("Authentication failed:", data);
    }
}

const fetchData = async () => {
    try {
        const token = localStorage.getItem("accessToken");
        const response = await fetch("/api/some-endpoint/", {
            method: "GET",
            headers: { "Authorization": `Bearer ${token}` },
        });

        if (!response.ok) throw new Error("Failed to fetch data.");

        // Handle your response data here...
    } catch (error) {
        console.error("Fetch data error:", error.message);
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
