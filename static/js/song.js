const getStatusDisplay = (status) => {
  if (status == "PENDING") {
    return `<div class="song-status pending"><p>대기</p></div>`
  } else if (status == "INPROGRESS") {
    return `<div class="song-status inprogress"><p>연습중</p></div>`
  } else if (status == "CLOSED") {
    return `<div class="song-status closed"><p>종료</p></div>`
  }
}

const registerSong = () => {
  hideButton();
  location.href='/songs/register';
}

requestSongs(
  $.param({}),
  (response) => {
    const songLint = $("#song-list")
    songLint.empty();
    response.data.forEach(item => {
      songLint.append(
        `<div class="song-item song-item-wrapper flex" data-id="${item.id}">
          <div class="flex">
            <div class="song-thumbnail">
              <img src="${item.thumbnail}">
            </div>
            <div class="song-info">
              <div class="song-title font-title-4">${item.title}</div>
              <div class="font-text-light-2">${item.singer}</div>
            </div>
          </div>
          <div class="song-item-right">${getStatusDisplay(item.status)}
          <div>
        </div>`
      );
    });
    songLint.on("click", ".song-item", function() {
      location.href = "/songs/" + $(this).data("id");
    });
  }
);
