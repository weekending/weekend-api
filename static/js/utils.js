const calcDDay = (dateStr) => {
  const targetDate = new Date(dateStr);
  const today = new Date()
  today.setHours(0, 0, 0, 0);
  targetDate.setHours(0, 0, 0, 0);
  const diffDays = Math.ceil((targetDate - today) / (1000 * 60 * 60 * 24));

  if (diffDays > 0) {
    return `D-${diffDays}`;
  } else {
    return "D-day";
  }
}

const formatDate = (dateStr) => {
  const [, month, day] = dateStr.split("-");
  return `${month}.${day}`;
}

function formatTimeTo12Hour(timeStr) {
  const [hourStr, minuteStr] = timeStr.split(":");
  let hour = parseInt(hourStr, 10);
  const minute = parseInt(minuteStr, 10);
  const period = hour >= 12 ? "PM" : "AM";
  hour = hour % 12;
  if (hour === 0) hour = 12;
  return `${hour}:${minute.toString().padStart(2, "0")} ${period}`;
}
