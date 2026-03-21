import { test, expect } from '@playwright/test';

test.describe('Backend Integration & CORS', () => {
  test('should verify backend is accessible via API', async ({ page }) => {
    const response = await page.request.get('http://localhost:8004/health');
    expect(response.status()).toBeLessThan(500);
  });

  test('should have CORS headers in response', async ({ page }) => {
    const response = await page.request.get(
      'http://localhost:8004/add?num1=5&num2=3',
      {
        headers: {
          'Origin': 'http://localhost:3004',
        },
      }
    );

    const headers = response.headers();
    expect(headers['access-control-allow-origin']).toBeDefined();
  });

  test('should fetch data from backend', async ({ page }) => {
    const response = await page.request.get('http://localhost:8004/add?num1=5&num2=3');
    expect(response.status()).toBe(200);

    const data = await response.json();
    expect(data).toHaveProperty('result');
    expect(data.result).toBe(8);
  });

  test('should verify all operations are available', async ({ page }) => {
    const operations = [
      { endpoint: 'add', num1: 10, num2: 5, expected: 15 },
      { endpoint: 'subtract', num1: 10, num2: 5, expected: 5 },
      { endpoint: 'multiply', num1: 10, num2: 5, expected: 50 },
      { endpoint: 'divide', num1: 10, num2: 5, expected: 2 },
    ];

    for (const op of operations) {
      const response = await page.request.get(
        `http://localhost:8004/${op.endpoint}?num1=${op.num1}&num2=${op.num2}`
      );
      expect(response.status()).toBe(200);

      const data = await response.json();
      expect(data.result).toBe(op.expected);
    }
  });

  test('should handle backend errors gracefully', async ({ page }) => {
    // Try to reach a non-existent endpoint
    const response = await page.request.get('http://localhost:8004/invalid', {
      failOnStatusCode: false,
    });
    expect(response.status()).toBeGreaterThanOrEqual(400);
  });
});
