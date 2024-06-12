export const getTranslation = (item: any, propertyName: string) => {
  return item.translation?.[propertyName] ?? item[propertyName];
};
