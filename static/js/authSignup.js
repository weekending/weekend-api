$("#signupInputUsername, #signupInputPassword, #signupInputPasswordCheck").on("input", () => {
  const username = $("#signupInputUsername").val();
  const password = $("#signupInputPassword").val();
  const passwordCheck = $("#signupInputPasswordCheck").val();
  if (username && password && passwordCheck && (password === passwordCheck)) {
    $("#signupErrorPassword").hide();
    $("#signupButton").attr("disabled", false);
  } else if (passwordCheck.length > 0 && password !== passwordCheck) {
    $("#signupErrorPassword").text("패스워드가 일치하지 않습니다.");
    $("#signupErrorPassword").show();
    $("#signupButton").attr("disabled", true);
  } else {
    $("#signupButton").attr("disabled", true);
    $("#signupErrorPassword").hide();
  }
});

const singUp = () => {
  $('.signup-error').hide();
  const params = {};
  $('.input-selection').each((i, item) => {
    const key = $(item).attr('name');
    const value = $(item).val();
    if (value) {
      params[key] = value;
    }
  });

  requestSignup(
    params,
    (response) => {
      toggleSignupComplete();
    },
    (response) => {
      result = response.responseJSON;
      if (result.code === "F004") {
        $("#signupErrorEmail").text("중복된 아이디입니다.");
        $("#signupErrorEmail").show();
      } else if (result.code === "F005") {
        $("#signupErrorPassword").text("패스워드가 일치하지 않습니다.");
        $("#signupErrorPassword").show();
      } else {
        alert("회원가입 에러");
      }
    }
  )
}

const toggleSignupComplete = () => {
  $("#screen").toggle();
  $("#signup-complete").toggle();
}

