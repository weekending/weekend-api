const switchTab = (event) => {
  const target = event.target.dataset.section;
  document.querySelectorAll('.song-section').forEach(element => {
    if (element.id === target) {
      element.removeAttribute('hidden');
    } else {
      element.setAttribute('hidden', true);
    }
  });
  document.querySelectorAll('.nav-item').forEach(element => {
    element.classList.remove('nav-item-active')
  });
  event.target.classList.add('nav-item-active')
}

document.querySelectorAll('.nav-item').forEach(element => {
  element.addEventListener('click', (e) => switchTab(e))
});
