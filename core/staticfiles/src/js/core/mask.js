import IMask from 'imask';

const MASK_SELECTOR = 'input[name=phone]';
const MASK_PHONE = '+{996}(#00)00-00-00';

export function mask(selector = MASK_SELECTOR, maskField = MASK_PHONE) {
  const elements = document.querySelectorAll(selector);
  elements.forEach(input => {
    const mask = new IMask(input, { mask: maskField, definitions: {'#': /[1-9]/ }})
  });
}
