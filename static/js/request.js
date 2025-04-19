const requestSchedule = (query, successFunc) => {
  $.ajax({
    url: "/api/schedules?" + query,
    method: "GET",
    success: successFunc,
    error: function(error) {
      console.error(error);
    }
  });
}

const requestSongs = (query, successFunc) => {
  $.ajax({
    url: "/api/songs?" + query,
    method: "GET",
    success: successFunc,
    error: function(error) {
      console.error(error);
    }
  });
}
