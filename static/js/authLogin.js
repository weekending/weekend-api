const login = () => {
  $(".login-error").hide();
  const params = {};
  $(".input-selection").each((i, item) => {
    const key = $(item).attr("name");
    const value = $(item).val();
    if (value) {
      params[key] = value;
    }
  });

  requestLogin(
    params,
    () => {
      $("#loginErrorPassword").hide();
    },
    (response) => {
      $.cookie("token", response.data.token);
      location.href = "/";
    },
    (response) => {
      $("#loginButton").attr("disabled", true);
      result = response.responseJSON;
      if (result.code === "F006") {
        $("#loginErrorPassword").text("아이디 혹은 비밀번호가 일치하지 않습니다.");
        $("#loginErrorPassword").show();
      } else {
        alert("로그인 에러");
      }
    },
  )
}

$(".input-selection").on("keyup", (e) => {
  if (e.keyCode !== 13) {
    const username = $("#loginInputUsername").val();
    const password = $("#loginInputPassword").val();
    if (username && password) {
      $("#loginButton").attr("disabled", false);
    } else {
      $("#loginButton").attr("disabled", true);
    }
  } else if (!$("#loginButton").prop("disabled")) {
    login();
  }
});
