const todayClass = (year, month, day, today) => {
  if (
    day === today.getDate() &&
    month === today.getMonth() &&
    year === today.getFullYear()
  ) return "today";
  return "";
}

const sundayClass = (year, month, day) => {
  const date = new Date(year, month, day);
  if (date.getDay() === 0 || date.getDay() === 6 ) return "holiday";
  return "";
}

const fillDays = (calendarDay, year, month, firstDay, lastDate) => {
  for (let i = 0; i < firstDay; i++) {
    calendarDay.append(
      `<div class="day-item">
        <div class="day"></div>
        <div class="day-schedule"></div>
      </div>`
    );
  }

  const today = new Date();
  for (let day = 1; day <= lastDate; day++) {
    calendarDay.append(
      `<div class="day-item font-text-2">
        <div class="day ${todayClass(year, month, day, today)} ${sundayClass(year, month, day)}">${day}</div>
        <div class="day-schedule" data-date=${dayToYYYYMMDD(year, month, day)}></div>
      </div>`
    );
  }
}

const renderScheduleList = (scheduleList, year, month) => {
  requestSchedules(
    data = $.param(
      {
        "band_id": getBandId(),
        "from": dateToYYYYMMDD(new Date(year, month, 1)),
        "to": dateToYYYYMMDD(new Date(year, month + 1, 0)),
      }
    ),
    success = (response) => {
      let scheduleDate = null;
      response.data.forEach(item => {
        const day = item.day.split("-")[2];
        scheduleList.append(
          `<li class="schedule-li flex">
            <div class="schedule-date font-title-5">${day}</div>
            <div class="schedule-item schedule-item-detail" data-id="${item.id}">
              <div class="schedule-title font-title-4">
                <p>${item.title}</p>
              </div>
              <div class="schedule-description font-text-light-3">
                <div class="schedule-text">${formatTimeTo12Hour(item.start_time)} ~ ${formatTimeTo12Hour(item.end_time)}</div>
                <div class="schedule-text">${item.location}</div>
              </div>
            </div>
          </li>`
        );
        $(`.day-schedule[data-date="${item.day}"]`).append(`<div class="event"></div>`);
      });
      scheduleList.on("click", ".schedule-item", function() {
        location.href = "/schedules/" + $(this).data("id");
      });
    }
  );
}

const renderCalendar = (date) => {
  const year = date.getFullYear();
  const month = date.getMonth();
  const firstDay = new Date(year, month, 1).getDay();
  const lastDate = new Date(year, month + 1, 0).getDate();

  $("#monthTitle").text(`${year}년 ${month + 1}월`);
  const calendarDay = $("#calendarDay");
  const scheduleList = $("#scheduleList");

  calendarDay.empty();
  scheduleList.empty();

  fillDays(calendarDay, year, month, firstDay, lastDate);
  renderScheduleList(scheduleList, year, month);
}

const currentDate = new Date();

renderCalendar(currentDate);

$("#prevMonth").click(() => {
  currentDate.setMonth(currentDate.getMonth() - 1);
  renderCalendar(currentDate);
})

$("#nextMonth").click(() => {
  currentDate.setMonth(currentDate.getMonth() + 1);
  renderCalendar(currentDate);
})
