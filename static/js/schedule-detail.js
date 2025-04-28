$("#editSchedule").click(() => {
  const currentPath = location.pathname;
  location.href = currentPath.endsWith("/") ? currentPath + "edit" : currentPath + "/edit";
});

$("#saveSchedule").click(() => {
  updateSchedule();
});

const updateSchedule = () => {
  const scheduleId = window.location.pathname.split("/")[2];
  const data = {
    "title": $("#inputScheduleTitle").val(),
    "date": $("#inputScheduleDate").val(),
    "start_time": $("#inputScheduleStartTime").val(),
    "end_time": $("#inputScheduleEndTime").val(),
    "location": $("#inputScheduleLocation").val(),
    "memo": $("#inputScheduleMemo").val(),
  }
  console.log(scheduleId);
  console.log(data);

  requestUpdateSchedule(
    scheduleId,
    data,
    success = () => {
      location.replace("/schedule/" + scheduleId);
    },
    error = (response) => {
      result = response.responseJSON;
      if (result.code === "F001") {
        alert("권한이 없습니다.");
      } else {
        alert(result.message);
      }
    },
  )
}
