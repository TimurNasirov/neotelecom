const radioElements = document.querySelectorAll('.join-us__form-radio label input');

radioElements.forEach(elm => elm.addEventListener('click', changeActiveRadio));

function changeActiveRadio() {
  radioElements.forEach(elm => {
    const label = elm.closest('label');
    label.classList.remove('active');
  });

  this.closest('label').classList.add('active');
}

setTab();

function setTab() {
  let hash = location.hash;
  if (!hash) return;
  hash = hash.substring(1, hash.length);
  const selectedRadioItem = document.getElementById(hash);
  if (!selectedRadioItem) return;
  radioElements.forEach(radio => {
    radio.closest('label').classList.remove('active');
  });
  selectedRadioItem.closest('label').classList.add('active');
  selectedRadioItem.checked = true;
}