const activate = (element) => {
  element.setAttribute('open', true);
  element.classList.add('active');
}

const deactivate = (element) => {
  element.removeAttribute('open');
  element.classList.remove('active');
}

const selectAllSong = () => {
  const totalCheck = document.getElementById('total-check');
  if (totalCheck.getAttribute('open')) {
    deactivate(totalCheck)
    document.querySelectorAll('.song-check').forEach(element => {
      deactivate(element);
    });
  } else {
    activate(totalCheck)
    document.querySelectorAll('.song-check').forEach(element => {
      activate(element);
    });
  }
}

const selectSong = (element) => {
  if (element.getAttribute('open')) {
    deactivate(element);
    const totalCheck = document.getElementById('total-check');
    deactivate(totalCheck)
  } else {
    activate(element);
  }
}

document.querySelectorAll('.song-check').forEach(element => {
  element.addEventListener('click', (e) => selectSong(element))
});
