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

const circleButtonAction = () => {
  const ids = ['button-register', 'button-pick', 'button-schedule'];
  if (document.getElementById('button-plus').getAttribute('open')) {
    document.getElementById('screen').setAttribute('hidden', true);
    for (let i = 0; i < ids.length; i++) {
      element = document.getElementById(ids[i]);
      element.style.bottom = 0;
      element.style.opacity = 0;
    }
    document.getElementById('button-plus').removeAttribute('open');
  } else {
    document.getElementById('screen').removeAttribute('hidden');
    for (let i = 0; i < ids.length; i++) {
      element = document.getElementById(ids[i]);
      element.style.bottom = 58 * (i + 1) + 'px';
      element.style.opacity = 1;
    }
    document.getElementById('button-plus').setAttribute('open', true);
  }
}
