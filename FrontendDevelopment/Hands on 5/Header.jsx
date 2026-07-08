import { Link } from "react-router-dom";

function Header(props) {
  return (
    <header>
      <h1>{props.siteName}</h1>

      <nav>
        <Link to="/">Home</Link> |{" "}
        <Link to="/courses">Courses</Link> |{" "}
        <Link to="/profile">Profile</Link>
      </nav>

      <h3>Enrolled Courses: {props.enrolledCount}</h3>

      <hr />
    </header>
  );
}

export default Header;