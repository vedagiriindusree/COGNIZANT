// 1. Function to fetch user
async function fetchUser(id) {
    try {
        const response = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`);
        const user = await response.json();

        document.getElementById("output").innerHTML = `
            <h3>${user.name}</h3>
            <p>Email: ${user.email}</p>
            <p>Phone: ${user.phone}</p>
        `;
    } catch (error) {
        console.log(error);
    }
}

// 2. Add event listener (PLACE THIS AT THE BOTTOM)
document
    .getElementById("loadUser")
    .addEventListener("click", function () {
        fetchUser(1);
    });
    function fetchAllCourses() {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve([
                "HTML",
                "CSS",
                "JavaScript"
            ]);
        }, 1000);
    });
}
document.getElementById("loadCourses").addEventListener("click", async function () {

    document.getElementById("output").innerHTML = "<p>Loading courses...</p>";

    const courses = await fetchAllCourses();

    let html = "<h2>Available Courses</h2><ul>";

    courses.forEach(course => {
        html += `<li>${course}</li>`;
    });

    html += "</ul>";

    document.getElementById("output").innerHTML = html;
});
async function fetchBothUsers() {
    try {
        const [user1, user2] = await Promise.all([
            fetch("https://jsonplaceholder.typicode.com/users/1").then(res => res.json()),
            fetch("https://jsonplaceholder.typicode.com/users/2").then(res => res.json())
        ]);

        document.getElementById("output").innerHTML = `
            <h2>Both Users Loaded</h2>
            <p>${user1.name}</p>
            <p>${user2.name}</p>
        `;
    } catch (error) {
        console.error(error);
    }
}
document.getElementById("loadBoth").addEventListener("click", fetchBothUsers);
async function apiFetch(url) {
    const response = await fetch(url);

    if (!response.ok) {
        throw new Error(`HTTP Error: ${response.status}`);
    }

    return await response.json();
}
async function loadNotifications() {

    const section = document.getElementById("notifications");

    section.innerHTML = "<p id='loading'>Loading...</p>";

    try {

        const posts = await apiFetch("https://jsonplaceholder.typicode.com/posts?_limit=5");

        let html = "";

        posts.forEach(post => {

            html += `
                <div class="notification-card">
                    <h3>${post.title}</h3>
                    <p>${post.body}</p>
                </div>
            `;

        });

        section.innerHTML = html;

    } catch (error) {

        section.innerHTML = `<p style="color:red">${error.message}</p>`;

    }
}
document
    .getElementById("loadNotifications")
    .addEventListener("click", loadNotifications);

// --------------------
// Task 3 - Axios
// --------------------

// Axios request interceptor
axios.interceptors.request.use(function (config) {
    console.log("API call started:", config.url);
    return config;
});

// Load posts using Axios
document.getElementById("loadAxios").addEventListener("click", async function () {

    document.getElementById("output").innerHTML = "<p>Loading Posts...</p>";

    try {

        const response = await axios.get(
            "https://jsonplaceholder.typicode.com/posts",
            {
                params: {
                    userId: 1
                }
            }
        );

        let html = "<h2>User 1 Posts</h2>";

        response.data.forEach(post => {

            html += `
                <div class="card">
                    <h3>${post.title}</h3>
                    <p>${post.body}</p>
                </div>
            `;

        });

        document.getElementById("output").innerHTML = html;

    } catch (error) {

        document.getElementById("output").innerHTML =
            "<p style='color:red;'>Unable to load posts.</p>";

    }

});