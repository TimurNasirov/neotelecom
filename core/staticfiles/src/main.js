import {
  bannersSliderInit,
  actionsSliderInit,
  mobileActionsSliderInit,
  newsSliderInit,
  mobileNewsSliderInit
} from './js/core/swiper-init';
import setBodyScroll from './js/core/set-body-scroll';

const callRequestBtn = document.getElementById('call-request');
const callRequestForm = document.getElementById('call-request-form');

if (callRequestBtn) {
  callRequestBtn.addEventListener('click', openCallRequestModal);
}
callRequestForm.addEventListener('submit', submitCallRequestForm);

bannersSliderInit();

actionsSliderInit();
mobileActionsSliderInit();

const allNewsLists = document.querySelectorAll('.news-list');
const allMobileNewsLists = document.querySelectorAll('.mobile-news-list');

allNewsLists.forEach(itm => newsSliderInit(itm));
allMobileNewsLists.forEach(itm => mobileNewsSliderInit(itm));

export function openCallRequestModal() {
  const callRequestPopup = document.querySelector('.popup_wrapper_call');
  callRequestPopup.classList.add('popup_show');
  setBodyScroll(false);
}

function submitCallRequestForm(e) {
  e.preventDefault();
  const headers = new Headers();
  headers.append('Content-Type', 'application/x-www-form-urlencoded');

  this.submit_callback.setAttribute('disabled', true);

  const body = {
    name: this.name.value,
    phone: this.phone.value,
  };
  const formData = new URLSearchParams();
  Object.keys(body).forEach(key => formData.append(key, body[key]));

  const postData = {
    method: 'POST',
    headers: headers,
    body: formData,
  };

  fetch('/api/v1/callback_form/', postData)
      .then(res => res.json())
      .then(res => {
        console.log(res.success);
        if (res.success) {
          successCallRequestForm();
        } else {
          alert('Возникла ошибка! Попробуйте позже.');
        }
      })
}

function successCallRequestForm() {
  const popupFooter = document.querySelector('.popup_call .popup__footer');
  popupFooter.classList.add('popup__footer_show');
  setTimeout(() => {
    popupFooter.classList.remove('popup__footer_show');
  }, 30 * 1000);
}