const todayClass = (year, month, day, today) => {
  if (
    day === today.getDate() &&
    month === today.getMonth() &&
    year === today.getFullYear()
  ) return "today"
  return ""
}

const sundayClass = (year, month, day) => {
  const date = new Date(year, month, day)
  if (date.getDay() === 0) return "red"
  return ""
}

const renderCalendar = (date) => {
  const year = date.getFullYear();
  const month = date.getMonth();
  const firstDay = new Date(year, month, 1).getDay();
  const lastDate = new Date(year, month + 1, 0).getDate();

  $("#month-title").text(`${year}년 ${month + 1}월`);
  const calendarDays = $("#calendarDays");
  $("#calendarDays").empty();
  for (let i = 0; i < firstDay; i++) {
    calendarDays.append(
      `<div class="day-item">
        <div class="day"></div>
        <div class="day-schedule"></div>
      </div>`
    );
  }

  const today = new Date();
  for (let day = 1; day <= lastDate; day++) {
    calendarDays.append(
      `<div class="day-item">
        <div class="day ${todayClass(year, month, day, today)} ${sundayClass(year, month, day)}">${day}</div>
        <div class="day-schedule" data-date=${dayToYYYYMMDD(year, month, day)}></div>
      </div>`
    );
  }

  requestSchedule(
    $.param(
      {"from": dateToYYYYMMDD(new Date(year, month, 1)), "to": dateToYYYYMMDD(new Date(year, month + 1, 0))}
    ),
    (response) => {
      $("#schedule-list").empty();
      let scheduleDate = null;
      response.data.forEach(item => {
        if (scheduleDate !== item.day) {
          $("#schedule-list").append(
            `<div class="schedule-date">
              <div class="circle"></div>
              <p>${formatDate(item.day)} (${item.weekday})</p>
            </div>`
          )
          scheduleDate = item.day;
        }
        $("#schedule-list").append(
          `<div class="schedule-description line" data-id="${item.id}">
            <div class="schedule-title">${item.title}</div>
            <div class="schedule-text">${formatTimeTo12Hour(item.start_time)} ~ ${formatTimeTo12Hour(item.end_time)}</div>
            <div class="schedule-text">${item.location}</div>
            <div class="schedule-text">${item.users.length}명 참여</div>
          </div>`
        )
        $("#schedule-list").on("click", ".schedule-description", function () {
          location.href = "/schedule/" + $(this).data("id");
        });
        $(`.day-schedule[data-date="${item.day}"]`).append(`<div class="event"></div>`);
      });
    }
  );
}

const currentDate = new Date();

renderCalendar(currentDate);

$("#prev-month").click(() => {
  currentDate.setMonth(currentDate.getMonth() - 1);
  renderCalendar(currentDate);
})

$("#next-month").click(() => {
  currentDate.setMonth(currentDate.getMonth() + 1);
  renderCalendar(currentDate);
})
