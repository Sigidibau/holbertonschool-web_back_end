export default function cleanSet(set, startString) {
  const filteredValues = [...set]
    .filter((value) => value.startsWith(startString))
    .map((value) => value.slice(startString.length));

  return filteredValues.join('-');
}
