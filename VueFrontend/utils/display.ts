// Filter things based on display size
export function getDisplaySize(width: number) {
  if (width < 576) {
    return "xs"; // Extra small
  } else if (width < 768) {
    return "sm"; // Small
  } else if (width < 992) {
    return "md"; // Medium
  } else if (width < 1200) {
    return "lg"; // Large
  } else if (width < 1400) {
    return "xl"; // Extra large
  } else {
    return "xxl"; // Extra extra large
  }
}
