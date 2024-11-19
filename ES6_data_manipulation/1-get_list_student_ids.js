export default function getListStudentIds(students) {
  // Check if the input is an array
  if (!Array.isArray(students)) {
    return [];  // Return an empty array if input is not an array
  }
  
  // Use map to extract the ids
  return students.map(student => student.id);
}
