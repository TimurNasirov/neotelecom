import "./scss/index.scss";
import changeTab from './js/core/change-tab';
import toggleFooterDropdown from './js/core/toggle-footer-dropdown';
import setBodyScroll from './js/core/set-body-scroll';
import { mask } from './js/core/mask';
// import { checkCityCookie, closeCookiePopup } from './js/core/check-cookie';
import { toggleMobileMenu, toggleMobileMenuItem } from './js/core/mobile-menu';
import { openCallRequestModal } from './main.js'
import Hammer from 'hammerjs';

mask();
// checkCityCookie();
const dataTabButtons = document.querySelectorAll('[data-tab-name]');
const footerDropdownItem = document.querySelectorAll('.mobile-footer__item');
// const cookiePopup = document.querySelector('.cookie-popup');
// cookiePopup.addEventListener('click', closeCookiePopup);

const callBackOpenModal = document.getElementById('callback-modal');

if (callBackOpenModal) {
  callBackOpenModal.addEventListener('click', openCallRequestModal)
}

const mobileMenuWrapper = document.querySelector('.mobile-menu_wrapper');

if (mobileMenuWrapper) {
  mobileMenuWrapper.addEventListener('click', toggleMobileMenu);
  mobileMenuWrapper.actionType = 'overlay';
}

const hammerJS = new Hammer(mobileMenuWrapper);

hammerJS.on('swiperight', (e) => {
  e.target.actionType = 'hide';
  toggleMobileMenu.call(null, e);
});

footerDropdownItem.forEach(itm => itm.addEventListener('click', toggleFooterDropdown))


dataTabButtons.forEach(btn => btn.addEventListener('click', changeTab));

// document.addEventListener('DOMContentLoaded', () => {
//   const preloader = document.getElementById('preloader');
//   preloader.classList.add('hidden');
// });


const mobileMenuItems = document.querySelectorAll('.mobile-menu__item');

mobileMenuItems.forEach(itm => {
  itm.addEventListener('click', toggleMobileMenuItem);
});


const showMobileMenuBtn = document.querySelector('.header__burger-button');
const hideMobileMenuBtn = document.querySelector('.mobile-menu__close-button');
if (showMobileMenuBtn) {
  showMobileMenuBtn.addEventListener('click', toggleMobileMenu);
  showMobileMenuBtn.actionType = 'show';
}

if (hideMobileMenuBtn) {
  hideMobileMenuBtn.addEventListener('click', toggleMobileMenu);
  hideMobileMenuBtn.actionType = 'hide';
}

const popupCloseButtons = document.querySelectorAll('.popup-close');
//
popupCloseButtons.forEach(btn => {
  btn.addEventListener('click', closePopup);
  btn.type = 'button';
});
//
// const popupItems = document.querySelectorAll('.popup_wrapper');
//
// popupItems.forEach(itm => {
//   itm.addEventListener('click', closePopup);
//   itm.type = 'overlay';
// });

function closePopup(e) {
  e.stopPropagation();
  const type = e.target.type;
  switch (type) {
    case 'overlay':
      if (e.target === this) {
        const popup = e.target.closest('.popup_wrapper');
        popup.classList.remove('popup_show');
        setBodyScroll(true);
        break;
      }
    case 'button':
      const popup = e.target.closest('.popup_wrapper');
      popup.classList.remove('popup_show');
      setBodyScroll(true);
      break;
  }

}