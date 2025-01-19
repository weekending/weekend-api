const requestRegister = () => {
  title = document.getElementById('input-title').value;
  singer = document.getElementById('input-singer').value;
  if (title === '') {
    alert('곡을 입력해 주세요!')
    return;
  } else if (singer === '') {
    alert('가수를 입력해 주세요!')
    return;
  }
  fetch('/api/songs', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({title: title, singer: singer}),
  })
  .then(response => {
    if (!response.ok) {
      throw new Error('등록에 실패했습니다ㅠㅠ 다시 시도해주세요.');
    }
    return response.json();
  })
  .then(data => {
    location.replace('/');
  })
  .catch(error => {
    alert('등록 에러');
  });
}
