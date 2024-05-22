export default function getStudentsByLocation(name, city) {
  return name.filter((student) => student.location === city);
}
