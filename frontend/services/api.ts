const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8004';

export interface ApiResponse {
  result: number;
  operation?: string;
}

export async function calculateAdd(num1: number, num2: number): Promise<number> {
  const response = await fetch(`${API_URL}/add?num1=${num1}&num2=${num2}`);
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }
  const data: ApiResponse = await response.json();
  return data.result;
}

export async function calculateSubtract(
  num1: number,
  num2: number
): Promise<number> {
  const response = await fetch(
    `${API_URL}/subtract?num1=${num1}&num2=${num2}`
  );
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }
  const data: ApiResponse = await response.json();
  return data.result;
}

export async function calculateMultiply(
  num1: number,
  num2: number
): Promise<number> {
  const response = await fetch(
    `${API_URL}/multiply?num1=${num1}&num2=${num2}`
  );
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }
  const data: ApiResponse = await response.json();
  return data.result;
}

export async function calculateDivide(
  num1: number,
  num2: number
): Promise<number> {
  const response = await fetch(`${API_URL}/divide?num1=${num1}&num2=${num2}`);
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }
  const data: ApiResponse = await response.json();
  return data.result;
}

export async function calculate(
  operation: string,
  num1: number,
  num2: number
): Promise<number> {
  switch (operation) {
    case 'add':
      return calculateAdd(num1, num2);
    case 'subtract':
      return calculateSubtract(num1, num2);
    case 'multiply':
      return calculateMultiply(num1, num2);
    case 'divide':
      return calculateDivide(num1, num2);
    default:
      throw new Error(`Unknown operation: ${operation}`);
  }
}
