export function openTicketPopup(url: string): void {
  const screenWidth = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
  const screenHeight = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;

  const popupWidth = 810; // Set the desired width
  const popupHeight = screenHeight; // Make it 100% tall

  const left = (screenWidth - popupWidth) / 2;
  const top = 0;

  const features = `width=${popupWidth},height=${popupHeight},left=${left},top=${top},resizable=yes`;

  window.open(url, "Popup", features);
}
