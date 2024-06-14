export default function changeTab(e) {
  const { target } = e;
  const tabsParentElem = target.closest('.tab-container');
  const dataTabButtons = tabsParentElem.querySelectorAll('[data-tab-name]');
  const allTabs = tabsParentElem.querySelectorAll('[data-tab-item]');

  const selectedTabName = target.getAttribute('data-tab-name');
  const selectedTab = tabsParentElem.querySelector(`[data-tab-item="${selectedTabName}"]`);
  let tabsCounter = 0;
  allTabs.forEach((tab, i, arr) => {
    tabsCounter++;
    tab.classList.remove('tab-item_active');
    if (tabsCounter === arr.length) {
      selectedTab.classList.add('tab-item_active');
    }
  })

  dataTabButtons.forEach(btn => {
    btn.classList.remove('tab-selector-item_active');
  });


  target.classList.add('tab-selector-item_active');
};