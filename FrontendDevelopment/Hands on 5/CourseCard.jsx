function CourseCard(props) {
  return (
    <div>
      <h2>{props.name}</h2>

      <p>Code : {props.code}</p>

      <p>Credits : {props.credits}</p>

      <p>Grade : {props.grade}</p>

      <button onClick={props.onEnroll}>
        Enroll
      </button>
      <hr />
    </div>
  );
}

export default CourseCard;