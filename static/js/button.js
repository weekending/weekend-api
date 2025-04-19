const circleButtonAction = () => {
  if ($("#button-plus").attr("open")) {
    $("#screen").attr("hidden", true)
    $(".button-item").each((i, item) => {
      $(item).css("bottom", 0)
      $(item).css("opacity", 0)
    });
    $("#button-plus").removeAttr("open")
  } else {
    $("#screen").removeAttr("hidden")
    $(".button-item").each((i, item) => {
      $(item).css("bottom", 60 * (i + 1))
      $(item).css("opacity", 1)
    });
    $("#button-plus").attr("open", true)
  }
}
