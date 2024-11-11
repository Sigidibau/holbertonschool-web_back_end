export function taskFirst() {
    const task = 'I prefer const when I can.'; // Use const here since the value of task doesn't change.
    return task;
  }
  
  export function getLast() {
    return ' is okay';
  }
  
  export function taskNext() {
    let combination = 'But sometimes let'; // Use let here since the combination value will change (concatenation).
    combination += getLast(); // The value of combination changes after this line.
  
    return combination;
  }
