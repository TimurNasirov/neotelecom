import Swiper from 'swiper';

export function bannersSliderInit() {
  const swiperParams = {
    direction: 'horizontal',
    loop: true, // круговое переключение
    slidesPerView: 1,
    preloadImages: true,
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
    autoplay: {
      delay: 5000, // задержка для автоплея
    },
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
  };
  new Swiper('.banner-container', swiperParams);
}

export function actionsSliderInit() {
  new Swiper('.actions-list', {
    slidesPerView: 4,
    spaceBetween: 24,
    autoplay: {
      delay: 3500, // задержка для автоплея
    },
  });
}

export function mobileActionsSliderInit() {
  new Swiper('.mobile-actions-list', {
    slidesPerView: 1,
    spaceBetween: 5,
    autoplay: {
      delay: 3500, // задержка для автоплея
    },
  });
}

export function newsSliderInit(newsListItem) {
  new Swiper(newsListItem, {
    slidesPerView: 3,
    spaceBetween: 24,
    autoplay: {
      delay: 3000, // задержка для автоплея
    },
  });
}

export function mobileNewsSliderInit(newsListItem) {
  new Swiper(newsListItem, {
    slidesPerView: 1,
    spaceBetween: 24,
    autoplay: {
      delay: 3000, // задержка для автоплея
    },
  });
}
