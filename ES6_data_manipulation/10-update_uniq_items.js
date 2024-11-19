export default function updateUniqueItems(groceries) {
  if (!(groceries instanceof Map)) {
    throw new Error('Cannot process');
  }

  // Iterate over the map and update items with quantity 1
  groceries.forEach((quantity, item) => {
    if (quantity === 1) {
      groceries.set(item, 100);
    }
  });

  return groceries;
}
