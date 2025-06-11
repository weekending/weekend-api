const getPostItem = (item) => {
  const created_dtm = new Date(item.created_dtm)
  const comments = item.comment_count
  return `
    <li>
      <a href="/community/posts/${item.id}">
        <div class="post-title-header">
          ${item.is_new ? '<span class="post-new font-text-4">New</span>' : ''}
          <span class="font-title-5 post-title">${item.title}</span>
          ${comments > 0 ? '<span class="post-comment-count font-text-3">[' + comments + ']</span>' : ''}
        </div>
        <div class="post-below font-text-light-3">
          <span>${item.category.name}</span>
          <span>·</span>
          <span>${item.user ? item.user.name : '익명'}</span>
          <span>·</span>
          <span>${dateToYYYYMMDD(created_dtm)}</span>
        </div>
      </a>
    </li>
  `;
}

const getPrev = (page, initialPage) => {
  if (page > 5) {
    return `<span class="previous">
      <a href="/community?page=${initialPage - 5}">&lt; Prev</a>
    </span>`
  } else {
    return `<span class="previous disable">&lt; Prev</span>`
  }
}

const getNext = (page, initialPage, pageSize, maxCount) => {
  if (pageSize * (initialPage + 4) < maxCount) {
    return `<span class="next">
      <a href="/community?page=${initialPage + 5}">Next &gt;</a>
    </span>`
  } else {
    return `<span class="next disable">Next &gt;</span>`
  }
}

const loadPost = (categoryId, page) => {
  requestPostList(
    $.param({"category_id": categoryId, "page": page}),
    success = (response) => {
      const postList = $("#postList");
      response.data.forEach(item => {
        postList.append(getPostItem(item));
      });
    },
  )
};

const loadPagination = (categoryId, page) => {
  requestPostCount(
    $.param({"category_id": categoryId}),
    success = (response) => {
      const postPagination = $("#postPagination");
      const pageSize = 15
      const initialPage = page - (page - 1) % 5
      const maxPage = Math.floor((response.data.count - 1) / pageSize) + 1;
      postPagination.append(getPrev(page, initialPage));
      for (let i = initialPage; i <= initialPage + 4 && i <= maxPage; i++) {
        if (i === page) {
          postPagination.append(
            `<span class="current font-bold-4">${i}</span>`
          )
        } else {
          postPagination.append(
            `<a href="/community?category_id=${categoryId}&page=${i}">
              <span class="pagination-page">${i}</span>
            </a>`
          )
        }
      }
      postPagination.append(
        getNext(page, initialPage, pageSize, response.data.count)
      );
    }
  )
}
