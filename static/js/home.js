const requestSchedule = () => {
  $.ajax({
    url: "/api/schedules",
    method: "GET",
    success: function(response) {
      response.data.forEach(item => {
        $(".schedule-list").append(
          `<div class="schedule-item flex">
            <div class="schedule-info flex">
              <div class="schedule-info-wrapper">
                <div class="schedule-info-dday">${calcDDay(item.day)}</div>
                <div class="schedule-info-date">${formatDate(item.day)} (${item.weekday})</div>
              </div>
            </div>
            <div class="schedule-description">
              <div class="schedule-title">${item.title}</div>
              <div class="schedule-text">${formatTimeTo12Hour(item.start_time)} ~ ${formatTimeTo12Hour(item.end_time)}</div>
              <div class="schedule-text">${item.location}</div>
              <div class="schedule-text">4명 참여</div>
            </div>
          </div>`
        )
      });
    },
    error: function(error) {
      console.error(error);
    }
  });
}

const requestSongs = () => {
  $.ajax({
    url: "/api/songs",
    method: "GET",
    success: function(response) {
      $(".song-list").empty();
      response.data.forEach(item => {
        $(".song-list").append(
          `<div class="song-item flex">
            <div class="song-thumbnail">
              <img src="${item.thumbnail}" width="42px">
            </div>
            <div class="song-info">
              <div class="song-title">${item.title}</div>
              <div class="song-singer">${item.singer}</div>
            </div>
          </div>`
        )
      });
    },
    error: function(error) {
      console.error(error);
    }
  });
}

requestSchedule();
requestSongs();
