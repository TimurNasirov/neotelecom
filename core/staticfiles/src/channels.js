import setBodyScroll from './js/core/set-body-scroll';

const filterChannelsField = document.querySelector('#search-channel');
const allChannelsGrid = document.querySelectorAll('.single-channel_grid');

filterChannelsField.addEventListener('keyup', filterChannels);

function filterChannels() {
  const searchString = this.value.toLowerCase();
  const allChannels = document.querySelectorAll('.single-channel');
  allChannels.forEach(channel => {
    channel.classList.add('single-channel_disabled');
    const slug = channel.getAttribute('data-channel-slug').toLowerCase();
    const name = channel.getAttribute('data-channel-name').toLowerCase();
    if (slug.includes(searchString) || name.includes(searchString)) {
      channel.classList.remove('single-channel_disabled');
    }
  })
}

allChannelsGrid.forEach(channel => {
  channel.addEventListener('click', showChannelModal);
});

function showChannelModal(e) {
  if (this.classList.contains('single-channel_disabled')) return;
  if (e.target === this || e.target.classList.contains('single-channel__img')) {
    const modal = this.querySelector('.popup_wrapper');
    modal.classList.add('popup_show');
    setBodyScroll(false);
  }
}

const changeListTypeButtons = document.querySelectorAll('.channels-controls__type-button');

changeListTypeButtons.forEach(btn => {
  btn.addEventListener('click', changeListType);
});

function changeListType() {
  const listType = this.getAttribute('data-list-type-btn');
  const allLists = document.querySelectorAll('.channels__list');
  allLists.forEach(list => {
    list.classList.remove('channels__list_show');
    if (list.getAttribute('data-list-type') === listType) list.classList.add('channels__list_show');
  });
  changeListTypeButtons.forEach(btn => {
    btn.classList.remove('channels-controls__type-button_active');
  });
  this.classList.add('channels-controls__type-button_active');
}