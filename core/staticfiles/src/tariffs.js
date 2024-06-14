setTab();

function setTab() {
  let hash = location.hash;
  if (!hash) return;
  hash = hash.substring(1, hash.length);
  const selectedTab = document.querySelector(`[data-tab-item="${hash}"]`);
  const selectedTabButton = document.querySelector(`[data-tab-name="${hash}"]`);

  if (!selectedTab) return;
  const tabsParentElem = document.querySelector('.tab-container');
  const dataTabButtons = tabsParentElem.querySelectorAll('[data-tab-name]');
  const allTabs = tabsParentElem.querySelectorAll('[data-tab-item]');

  dataTabButtons.forEach(btn => {
    btn.classList.remove('tab-selector-item_active');
  });

  allTabs.forEach((tab) => {
    tab.classList.remove('tab-item_active');
  });

  selectedTab.classList.add('tab-item_active');
  selectedTabButton.classList.add('tab-selector-item_active')
}