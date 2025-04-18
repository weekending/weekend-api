const getStatusDisplay = (status) => {
  if (status == "PENDING") {
    return `<div class="song-status pending"><p>대기</p></div>`
  } else if (status == "INPROGRESS") {
    return `<div class="song-status inprogress"><p>연습중</p></div>`
  } else if (status == "CLOSED") {
    return `<div class="song-status closed"><p>종료</p></div>`
  }
}

const circleButtonAction = () => {
  const ids = ['button-register', 'button-pick'];
  if ($("#button-plus").attr("open")) {
    $("#screen").attr("hidden", true)
    for (let i = 0; i < ids.length; i++) {
      element = document.getElementById(ids[i]);
      element.style.bottom = 0;
      element.style.opacity = 0;
    }
    $("#button-plus").removeAttr("open")
  } else {
    $("#screen").removeAttr("hidden", true)
    for (let i = 0; i < ids.length; i++) {
      element = document.getElementById(ids[i]);
      element.style.bottom = 58 * (i + 1) + 'px';
      element.style.opacity = 1;
    }
    $("#button-plus").attr("open", true)
  }
}

requestSongs(
  $.param({}),
  (response) => {
    $("#song-list").empty();
    response.data.forEach(item => {
      $("#song-list").append(
        `<div class="song-item song-item-wrapper flex">
          <div class="flex">
            <div class="song-thumbnail">
              <img src="${item.thumbnail}">
            </div>
            <div class="song-info">
              <div class="song-title">${item.title}</div>
              <div class="song-singer">${item.singer}</div>
            </div>
          </div>
          <div class="song-item-right">${getStatusDisplay(item.status)}
          <div>
        </div>`
      )
    });
  }
);
