export default function cleanSet(set, startString) {
  // Filter the set to find values that start with the startString
  const filteredValues = [...set]
    .filter((value) => value.startsWith(startString))
    .map((value) => value.slice(startString.length)); // Remove startString from each matching value

  // Join the filtered values into a single string separated by hyphens
  return filteredValues.join('-');
}
