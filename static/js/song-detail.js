$("#editSong").click(() => {
  const currentPath = location.pathname;
  location.href = currentPath.endsWith("/") ? currentPath + "edit" : currentPath + "/edit";
});

$("#saveSong").click(() => {
  updateSong();
});

$("#songSelect").click(() => {
  $("#songStatusOption").toggle();
});

$(".status-option-item").click(function() {
  $("#songSelect .status-item").empty();
  $("#songSelect .status-item").append($(this).find(".song-status").clone(true));
  $("#songStatusOption").hide();
});

const updateSong = () => {
  const songId = window.location.pathname.split("/")[2];
  const status = $("#songSelect .status-item .song-status").data("status");
  const data = {
    "title": $("#inputSongTitle").val(),
    "singer": $("#inputSongSinger").val(),
    "status": status.toUpperCase(),
  }

  requestUpdateSong(
    songId,
    data,
    success = () => {
      location.replace("/songs/" + songId);
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
