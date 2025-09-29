const pad = (n: number) => String(n).padStart(2, "0");

/**
 * 2025-01-15T12:34:56 => 2025.01.15 12:34:56
 */
export const isoToYYMMDDHHMMSS = (iso: string): string => {
  const date = new Date(iso);

  return [
    date.getFullYear(),
    pad(date.getMonth() + 1),
    pad(date.getDate())
  ].join(".") + " " + [
    pad(date.getHours()),
    pad(date.getMinutes()),
    pad(date.getSeconds())
  ].join(":");
}

/**
 * 2025-01-15T12:34:56 => 2025.01.15
 */
export const isoToYYMMDD = (iso: string): string => {
  const date = new Date(iso);

  return [
    date.getFullYear(),
    pad(date.getMonth() + 1),
    pad(date.getDate())
  ].join(".");
}

/**
 * 2025-01-15T12:34:56 => 2025-01-15
 */
export const dateToYYMMDD = (date: Date): string => {
  return [
    date.getFullYear(),
    pad(date.getMonth() + 1),
    pad(date.getDate())
  ].join("-");
}

/**
 * 2025-01-15 => 01.15
 */
export const formatDay = (date: string): string => {
  const [_, month, day] = date.split("-");
  return `${month}.${day}`;
}

/**
 * 16:00:00 => 오후 4:00
 */
export const formatTime24to12 = (timeStr: string): string => {
  const [hours, minutes, seconds] = timeStr.split(":").map(Number);
  const date = new Date();
  date.setHours(hours, minutes, seconds);
  return date.toLocaleTimeString([], { hour: "numeric", minute: "2-digit", hour12: true });
}

