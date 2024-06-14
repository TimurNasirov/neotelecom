export default function setBodyScroll(type) {
  const body = document.querySelector('body');
  if (type) {
    body.classList.remove('no-scroll');
  } else {
    body.classList.add('no-scroll');
  }
}