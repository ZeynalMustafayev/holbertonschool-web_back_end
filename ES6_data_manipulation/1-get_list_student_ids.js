export default function getListStudentIds(getListStudents) {
  if (typeof getListStudents !== 'object') {
    return [];
  }
  return getListStudents.map((student) => student.id);
}
