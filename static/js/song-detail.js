$("#edit-song").click(() => {
  const currentPath = location.pathname;
  location.href = currentPath.endsWith("/") ? currentPath + "edit" : currentPath + "/edit";
});

$("#save-song").click(() => {
  alert("권한이 없습니다.")
});

$("#song-select").click(() => {
  $("#song-status-option").toggle();
});

$(".status-option-item").click(function() {
  $("#song-select .status-item").empty();
  $("#song-select .status-item").append($(this).find(".song-status").clone());
  $("#song-status-option").hide();
});
