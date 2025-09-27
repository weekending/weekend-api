import { create } from "zustand";

interface ScheduleStore {
  month: Date;
  setMonth: (date: Date) => void;
}

export const useScheduleStore = create<ScheduleStore>((set) => ({
  month: new Date(),
  setMonth: (date) => set({ month: date }),
}));
