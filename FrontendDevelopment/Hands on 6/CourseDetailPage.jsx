import { useParams } from "react-router-dom";

function CourseDetailPage() {
  const { id } = useParams();

  return (
    <div style={{ padding: "20px" }}>
      <h1>Course Details</h1>

      <h2>Course ID : {id}</h2>
    </div>
  );
}

export default CourseDetailPage;