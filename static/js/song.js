const getStatusDisplay = (status) => {
  if (status == "PENDING") {
    return `<div class="song-status pending"><p>대기</p></div>`
  } else if (status == "INPROGRESS") {
    return `<div class="song-status inprogress"><p>연습중</p></div>`
  } else if (status == "CLOSED") {
    return `<div class="song-status closed"><p>종료</p></div>`
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
