export const useFilters = (element: any, current: Ref<string[]>, audience: Ref<string[]>, genre: Ref<string[]>) => {
  const isCurrent = current.value.length === 0 || element.dataset.groups.includes("true");
  const selectedAudience =
    audience.value.length === 0 || audience.value.some((filter) => element.dataset.groups.includes(filter));
  const selectedGenres =
    genre.value.length === 0 || genre.value.some((filter) => element.dataset.groups.includes(filter));

  return isCurrent && selectedAudience && selectedGenres;
};
