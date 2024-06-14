const answers = document.querySelectorAll('.handbook-questions__item');

answers.forEach(answer => answer.addEventListener('click', toggleDropdown));

function toggleDropdown() {
  this.classList.toggle('handbook-questions__item_active')
}