export function toggleMobileMenu(e) {
  const type = e.target.actionType;
  const body = document.querySelector('body');
  const mobileMenu = document.querySelector('.mobile-menu_wrapper');
  switch (type) {
    case 'show':
      body.classList.add('no-scroll');
      mobileMenu.classList.add('active');
      break;
    case 'hide':
      body.classList.remove('no-scroll');
      mobileMenu.classList.remove('active');
      break;
    case 'overlay':
      body.classList.remove('no-scroll');
      mobileMenu.classList.remove('active');
      break;
    default:
      break;
  }
}


export function toggleMobileMenuItem() {
  this.classList.toggle('mobile-menu__item_active')
}