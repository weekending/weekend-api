export default function ErrorMessage({ message }: { message: string }) {
  return message ? <div className="text-red-500">{message}</div> : null;
}
