const getComment = (item) => {
  const created_dtm = new Date(item.created_dtm)
  const content = item.is_active
    ? `<div class="font-text-3 comment-content">
        ${item.content}
      </div>`
    : `<div class="font-text-light-3 comment-content">
        ${item.content}
      </div>`;
  return `
    <div class="comment-item" style="margin-left: ${10 * (item.level - 1)}px">
      <div class="font-text-light-4 comment-header">
        <span>${item.user ? item.user.name : '익명'}</span>
        <span>·</span>
        <span>${dateToYYYYMMDD(created_dtm)} ${dateToHHMM(created_dtm)}</span>
      </div>
      ${content}
      <hr>
    </div>
  `
}

const loadPostCommentList = (postId) => {
  requestPostCommentList(
    postId,
    success = (response) => {
      $("#postCommentCount").text(response.data.length);
      const postComment = $("#postComment");
      response.data.forEach(item => {
        postComment.append(getComment(item));
      });
    },
  )
}

$("#inputComment").on("keyup", (e) => {
  const comment = $("#inputComment").val();
  if (comment) {
    $("#commentButton").attr("disabled", false);
  } else {
    $("#commentButton").attr("disabled", true);
  }
});
