$.cookie("bandId", 1);

requestSchedules(
  data = $.param({"band_id": getBandId(), "from": dateToYYYYMMDD(new Date())}),
  success = (response) => {
    response.data.forEach((item, i) => {
      $("#dDayList").append(
        `<div class="schedule-item flex">
          <div class="schedule-info flex">
            <div class="schedule-info-wrapper">
              <div class="schedule-info-dday">${calcDDay(item.day)}</div>
              <div class="font-subtitle-2">${formatDate(item.day)} (${item.weekday})</div>
            </div>
          </div>
          <div class="schedule-description">
            <div class="schedule-title font-title-4">${item.title}</div>
            <div class="schedule-text font-text-light-3">${formatTimeTo12Hour(item.start_time)} ~ ${formatTimeTo12Hour(item.end_time)}</div>
            <div class="schedule-text font-text-light-3">${item.location}</div>
            <div class="schedule-text font-text-light-3">${item.users.length}명 참여</div>
          </div>
        </div>`
      );
      if (i === 0) {
        $("#scheduleScroll").append('<button class="active"></button>')
      } else {
        $("#scheduleScroll").append('<button></button>')
      }
    });
  }
);

requestSongs(
  data = $.param({"band_id": getBandId(), "status": "INPROGRESS"}),
  success = (response) => {
    $("#songList").empty();
    const maxCount = 5;
    for (let i = 0; i < maxCount && i < response.data.length; i++) {
      item = response.data[i];
      $("#songList").append(
        `<div class="song-item flex">
          <div class="song-thumbnail">
            <img src="${item.thumbnail}">
          </div>
          <div class="song-info">
            <div class="song-title font-title-4">${item.title}</div>
            <div class="font-text-light-2">${item.singer}</div>
          </div>
        </div>`
      );
    };
  }
);
