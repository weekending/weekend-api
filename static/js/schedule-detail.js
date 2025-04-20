$("#edit-schedule").click(() => {
  const currentPath = location.pathname;
  location.href = currentPath.endsWith("/") ? currentPath + "edit" : currentPath + "/edit";
});

$("#save-schedule").click(() => {
  alert("권한이 없습니다.")
});
