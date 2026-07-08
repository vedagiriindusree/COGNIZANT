const courses = [
{
    id: 1,
    name: "HTML5",
    code: "CS101",
    credits: 3,
    description: "Learn the fundamentals of HTML."
},
{
    id: 2,
    name: "CSS3",
    code: "CS102",
    credits: 4,
    description: "Learn how to style web pages."
},
{
    id: 3,
    name: "JavaScript",
    code: "CS103",
    credits: 4,
    description: "Learn JavaScript programming basics."
},
{
    id: 4,
    name: "Data Structures",
    code: "CS201",
    credits: 4,
    description: "Learn Data Structures."
},
{
    id: 5,
    name: "Algorithms",
    code: "CS202",
    credits: 5,
    description: "Learn Algorithms."
}
];

// ES6 map()
const formattedCourses = courses.map(course =>
`${course.code} - ${course.name} (${course.credits} Credits)`
);

console.log(formattedCourses);

// ES6 filter()
const fourCreditCourses = courses.filter(course =>
    course.credits === 4
);

console.log(fourCreditCourses);

// ES6 reduce()
const totalCredits = courses.reduce(
    (total, course) => total + course.credits,
    0
);

console.log(totalCredits);

// DOM Selection
const grid = document.querySelector(".course-grid");
const total = document.querySelector("#total-credits");

// Display Courses
function displayCourses(courseList) {

    grid.innerHTML = "";

    courseList.forEach(course => {

        const card = document.createElement("article");

        card.classList.add("course-card");

        card.innerHTML = `
            <h3>${course.name}</h3>
            <p>${course.description}</p>
            <span>Credits : ${course.credits}</span>
        `;

        // Click Event
        card.addEventListener("click", () => {

            alert(
`Course Name : ${course.name}
Credits : ${course.credits}
Course Code : ${course.code}`
            );

        });

        grid.appendChild(card);

    });

}

// Initial Display
displayCourses(courses);

total.textContent = `Total Credits : ${totalCredits}`;

// Search
const search = document.querySelector("#search-course");

search.addEventListener("input", () => {

    const keyword = search.value.toLowerCase();

    const filtered = courses.filter(course =>
        course.name.toLowerCase().includes(keyword)
    );

    displayCourses(filtered);

    const filteredCredits = filtered.reduce(
        (sum, course) => sum + course.credits,
        0
    );

    total.textContent = `Total Credits : ${filteredCredits}`;

});

// Sort
const sortBtn = document.querySelector("#sort-btn");

sortBtn.addEventListener("click", () => {

    courses.sort((a, b) => b.credits - a.credits);

    displayCourses(courses);

    total.textContent = `Total Credits : ${totalCredits}`;

});