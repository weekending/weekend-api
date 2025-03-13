const setCookie = (cookieName, value) => {
  document.cookie = cookieName + "=" + value + ";path=/";
};

const requestLogin = () => {
  const email = document.getElementById("input-user-email").value
  const password = document.getElementById("input-password").value
  if (email === '') {
    alert('이메일을 입력해주세요')
    return;
  } else if (password === '') {
    alert('비밀번호를 입력해주세요!')
    return;
  }

  $.ajax({
    url: "/auth/login",
    type: "POST",
    dataType: "JSON",
    contentType: "application/json;",
    data: JSON.stringify({"email": email, "password": password}),
    beforeSend: () => {
      $('.exception-message').text("");
    },
    success: (data) => {
      setCookie("token", data.data.token);
      location.replace("/docs");
    },
    error: (data) => {
      $('.exception-message').text(data.responseJSON["detail"]);
    },
  });
};

const onkeyupLogin = () => {
	if (window.event.keyCode === 13) {
    requestLogin();
  }
};
