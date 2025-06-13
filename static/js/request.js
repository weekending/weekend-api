const requestSignup = (data, success, error) => {
  $.ajax({
    url: "/api/auth/signup",
    type: "POST",
    dataType: "JSON",
    contentType: "application/json;",
    data: JSON.stringify(data),
    success: success,
    error: error,
  });
};

const requestLogin = (data, beforeSend, success, error) => {
  $.ajax({
    url: "/api/auth/login",
    type: "POST",
    dataType: "JSON",
    contentType: "application/json;",
    data: JSON.stringify(data),
    beforeSend: beforeSend,
    success: success,
    error: error,
  });
};

const requestSchedules = (query, success) => {
  $.ajax({
    url: "/api/schedules?" + query,
    method: "GET",
    success: success,
    error: function(error) {
      console.error(error);
    },
  });
};

const requestCreateSchedule = (data, success, error) => {
  $.ajax({
    url: "/api/schedules",
    method: "POST",
    dataType: "JSON",
    contentType: "application/json;",
    data: JSON.stringify(data),
    beforeSend: function(xhr) {
      xhr.setRequestHeader("Authorization", "Bearer " + $.cookie("token"));
    },
    success: success,
    error: error,
  });
};

const requestUpdateSchedule = (scheduleId, data, success, error) => {
  $.ajax({
    url: "/api/schedules/" + scheduleId,
    method: "PATCH",
    dataType: "JSON",
    contentType: "application/json;",
    data: JSON.stringify(data),
    beforeSend: function(xhr) {
      xhr.setRequestHeader("Authorization", "Bearer " + $.cookie("token"));
    },
    success: success,
    error: error,
  });
};

const requestAttendSchedule = (scheduleId, success, error) => {
  $.ajax({
    url: "/api/schedules/" + scheduleId + "/attend",
    method: "POST",
    beforeSend: function(xhr) {
      xhr.setRequestHeader("Authorization", "Bearer " + $.cookie("token"));
    },
    success: success,
    error: error,
  });
};

const requestSongs = (query, success) => {
  $.ajax({
    url: "/api/songs?" + query,
    method: "GET",
    success: success,
    error: function(error) {
      console.error(error);
    },
  });
};

const requestCreateSong = (data, success, error) => {
  $.ajax({
    url: "/api/songs",
    method: "POST",
    dataType: "JSON",
    contentType: "application/json;",
    data: JSON.stringify(data),
    beforeSend: function(xhr) {
      xhr.setRequestHeader("Authorization", "Bearer " + $.cookie("token"));
    },
    success: success,
    error: error,
  });
};

const requestUpdateSong = (songId, data, success, error) => {
  $.ajax({
    url: "/api/songs/" + songId,
    method: "PATCH",
    dataType: "JSON",
    contentType: "application/json;",
    data: JSON.stringify(data),
    beforeSend: function(xhr) {
      xhr.setRequestHeader("Authorization", "Bearer " + $.cookie("token"));
    },
    success: success,
    error: error,
  });
};

const requestPostList = (query, success, error) => {
  $.ajax({
    url: "/api/posts?" + query,
    type: "GET",
    success: success,
    error: error,
  });
};

const requestPostCount = (query, success, error) => {
  $.ajax({
    url: "/api/posts/count?" + query,
    type: "GET",
    success: success,
    error: error,
  });
};

const requestPostCommentList = (postId, success, error) => {
  $.ajax({
    url: "/api/posts/" + postId + "/comments",
    type: "GET",
    success: success,
    error: error,
  });
};
