export default function toggleFooterDropdown(e) {
  const allFooterDropdownItems = document.querySelectorAll('.mobile-footer__item');
  allFooterDropdownItems.forEach(itm => itm.classList.remove('mobile-footer__item_active'))
  if (e.target.classList.contains('mobile-footer__item-title')) {
    e.target.closest('.mobile-footer__item').classList.add('mobile-footer__item_active');
  }
}