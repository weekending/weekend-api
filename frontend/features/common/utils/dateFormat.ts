const pad = (n: number) => String(n).padStart(2, "0");

export const isoToYYMMDDHHMMSS = (iso: string) => {
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

export const isoToYYMMDD = (iso: string) => {
  const date = new Date(iso);

  return [
    date.getFullYear(),
    pad(date.getMonth() + 1),
    pad(date.getDate())
  ].join(".");
}

