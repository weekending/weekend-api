const requestSignup = (data, successFunc, errorFunc) => {
  $.ajax({
    url: "/api/auth/signup",
    type: "POST",
    dataType: "JSON",
    contentType: "application/json;",
    data: JSON.stringify(data),
    success: successFunc,
    error: errorFunc,
  });
};

const requestLogin = (data, beforeSendFunc, successFunc, errorFunc) => {
  $.ajax({
    url: "/api/auth/login",
    type: "POST",
    dataType: "JSON",
    contentType: "application/json;",
    data: JSON.stringify(data),
    beforeSend: beforeSendFunc,
    success: successFunc,
    error: errorFunc,
  });
};

const requestSchedule = (query, successFunc) => {
  $.ajax({
    url: "/api/schedules?" + query,
    method: "GET",
    headers: {"Authorization": "Bearer ${$.cookie('token')}"},
    success: successFunc,
    error: function(error) {
      console.error(error);
    }
  });
};

const requestSongs = (query, successFunc) => {
  $.ajax({
    url: "/api/songs?" + query,
    method: "GET",
    success: successFunc,
    error: function(error) {
      console.error(error);
    }
  });
};
