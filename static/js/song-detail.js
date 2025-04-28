$("#saveSong").click(() => {
  createSong();
});

$("#updateSong").click(() => {
  updateSong();
});

$("#editSong").click(() => {
  const currentPath = location.pathname;
  location.href = currentPath.endsWith("/") ? currentPath + "edit" : currentPath + "/edit";
});

$("#songSelect").click(() => {
  $("#songStatusOption").toggle();
});

$(".status-option-item").click(function() {
  $("#songSelect .status-item").empty();
  $("#songSelect .status-item").append(
    $(this).find(".song-status").clone(true)
  );
  $("#songStatusOption").hide();
});

const createSong = () => {
  requestCreateSong(
    data = {
      "band_id": getBandId(),
      "title": $("#inputSongTitle").val(),
      "singer": $("#inputSongSinger").val(),
    },
    success = () => {
      location.replace("/songs");
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

const updateSong = () => {
  const songId = window.location.pathname.split("/")[2];
  const status = $("#songSelect .status-item .song-status").data("status");

  requestUpdateSong(
    songId,
    data = {
      "title": $("#inputSongTitle").val(),
      "singer": $("#inputSongSinger").val(),
      "status": status.toUpperCase(),
    },
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
