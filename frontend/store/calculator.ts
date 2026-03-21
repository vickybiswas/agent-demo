import { create } from 'zustand';

export interface CalculatorStore {
  display: string;
  previousValue: number | null;
  operation: string | null;
  newInput: boolean;
  isLoading: boolean;
  error: string | null;
  isUpsideDown: boolean;

  setDisplay: (value: string) => void;
  handleNumber: (num: number) => void;
  handleDecimal: () => void;
  handleOperation: (op: string) => void;
  handleEquals: () => void;
  handleClear: () => void;
  handleDelete: () => void;
  toggleUpsideDown: () => void;
  setLoading: (loading: boolean) => void;
  setError: (error: string | null) => void;
  clearDisplay: () => void;
}

export const useCalculator = create<CalculatorStore>((set, get) => ({
  display: '0',
  previousValue: null,
  operation: null,
  newInput: true,
  isLoading: false,
  error: null,
  isUpsideDown: false,

  setDisplay: (value: string) => {
    set({ display: value, error: null });
  },

  handleNumber: (num: number) => {
    const { display, newInput } = get();

    if (newInput) {
      set({
        display: String(num),
        newInput: false,
        error: null,
      });
    } else {
      if (display === '0') {
        set({ display: String(num), error: null });
      } else if (display.length < 16) {
        set({ display: display + num, error: null });
      }
    }
  },

  handleDecimal: () => {
    const { display, newInput } = get();

    if (newInput) {
      set({ display: '0.', newInput: false, error: null });
    } else if (!display.includes('.')) {
      set({ display: display + '.', error: null });
    }
  },

  handleOperation: (op: string) => {
    const { display, previousValue, operation, newInput } = get();
    const currentValue = parseFloat(display);

    if (!newInput && previousValue !== null && operation) {
      // Chain operations - calculate the result of previous operation
      const prevNum = previousValue;
      const currentNum = currentValue;

      let result: number;
      switch (operation) {
        case '+':
          result = prevNum + currentNum;
          break;
        case '-':
          result = prevNum - currentNum;
          break;
        case '*':
          result = prevNum * currentNum;
          break;
        case '/':
          if (currentNum === 0) {
            set({ display: 'E', error: 'Division by zero' });
            return;
          }
          result = prevNum / currentNum;
          break;
        default:
          result = currentNum;
      }

      set({
        display: String(result),
        previousValue: result,
        operation: op,
        newInput: true,
        error: null,
      });
    } else {
      set({
        previousValue: currentValue,
        operation: op,
        newInput: true,
        error: null,
      });
    }
  },

  handleEquals: async () => {
    const { display, previousValue, operation } = get();
    const currentValue = parseFloat(display);

    if (previousValue === null || operation === null) {
      return;
    }

    // Show loading state
    set({ isLoading: true });

    try {
      // Call backend API
      const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8004';
      const response = await fetch(
        `${apiUrl}/${operation}?num1=${previousValue}&num2=${currentValue}`
      );

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      const result = data.result;

      set({
        display: String(result),
        previousValue: null,
        operation: null,
        newInput: true,
        isLoading: false,
        error: null,
      });
    } catch (error) {
      const errorMsg = error instanceof Error ? error.message : 'Unknown error';
      set({
        display: 'E',
        previousValue: null,
        operation: null,
        newInput: true,
        isLoading: false,
        error: errorMsg,
      });
    }
  },

  handleClear: () => {
    set({
      display: '0',
      previousValue: null,
      operation: null,
      newInput: true,
      error: null,
    });
  },

  handleDelete: () => {
    const { display, newInput } = get();

    if (newInput || display === '0') {
      return;
    }

    const newDisplay = display.slice(0, -1) || '0';
    set({ display: newDisplay, error: null });
  },

  toggleUpsideDown: () => {
    set((state) => ({ isUpsideDown: !state.isUpsideDown }));
  },

  setLoading: (loading: boolean) => {
    set({ isLoading: loading });
  },

  setError: (error: string | null) => {
    set({ error });
  },

  clearDisplay: () => {
    set({
      display: '0',
      previousValue: null,
      operation: null,
      newInput: true,
      error: null,
    });
  },
}));
