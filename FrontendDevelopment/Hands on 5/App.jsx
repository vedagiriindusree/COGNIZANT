import { useState, useEffect } from "react";
import Header from "./components/Header";
import Footer from "./components/Footer";
import CourseCard from "./components/CourseCard";

function App() {

  const [courses, setCourses] = useState([
    {
      id: 1,
      name: "React",
      code: "RE101",
      credits: 3,
      grade: "A"
    },
    {
      id: 2,
      name: "JavaScript",
      code: "JS102",
      credits: 4,
      grade: "A+"
    },
    {
      id: 3,
      name: "Python",
      code: "PY103",
      credits: 3,
      grade: "B+"
    },
    {
      id: 4,
      name: "Java",
      code: "JA104",
      credits: 4,
      grade: "A"
    },
    {
      id: 5,
      name: "HTML & CSS",
      code: "HC105",
      credits: 2,
      grade: "B"
    }
  ]);
  const [searchTerm, setSearchTerm] = useState("");
  const [enrolledCourses, setEnrolledCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const handleEnroll = (course) => {
  setEnrolledCourses([...enrolledCourses, course]);
  };
  useEffect(() => {
  setLoading(true);

  setTimeout(() => {
    setLoading(false);
  }, 2000);
}, []);
  return (
    <>
      <Header
      siteName="Student Portal"
      enrolledCount={enrolledCourses.length}
      />

      <h2>Available Courses</h2>
      {loading && <h3>Loading courses...</h3>}
      <input
      type="text"
      placeholder="Search course..."
      value={searchTerm}
      onChange={(e) => setSearchTerm(e.target.value)}
      />

      {!loading &&
  courses
    .filter((course) =>
      course.name.toLowerCase().includes(searchTerm.toLowerCase())
    )
    .map((course) => (
      <CourseCard
        key={course.id}
        name={course.name}
        code={course.code}
        credits={course.credits}
        grade={course.grade}
        onEnroll={() => handleEnroll(course)}
      />
    ))}

      <Footer />
    </>
  );
}

export default App;