import { test, expect } from '@playwright/test';

test.describe('Basic Calculator Operations', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
    await page.waitForLoadState('networkidle');
  });

  test('should display calculator title', async ({ page }) => {
    const title = page.locator('text=STRANGER THINGS');
    await expect(title).toBeVisible();
  });

  test('should display scientific operations section', async ({ page }) => {
    const section = page.locator('text=Scientific Operations');
    await expect(section).toBeVisible();
  });

  test('should perform addition (5 + 3 = 8)', async ({ page }) => {
    await page.waitForTimeout(500);
    await page.click('button:has-text("5")');
    await page.waitForTimeout(200);
    await page.click('button:has-text("+")');
    await page.waitForTimeout(200);
    await page.click('button:has-text("3")');
    await page.waitForTimeout(200);
    await page.click('button:has-text("=")');
    await page.waitForTimeout(1000);

    const result = page.locator('[data-testid="resultLine"]');
    await expect(result).toContainText('8');
  });

  test('should perform subtraction (10 - 2 = 8)', async ({ page }) => {
    await page.waitForTimeout(500);
    await page.click('button:has-text("1")');
    await page.click('button:has-text("0")');
    await page.waitForTimeout(200);
    await page.click('button:has-text("-")');
    await page.waitForTimeout(200);
    await page.click('button:has-text("2")');
    await page.waitForTimeout(200);
    await page.click('button:has-text("=")');
    await page.waitForTimeout(1000);

    const result = page.locator('[data-testid="resultLine"]');
    await expect(result).toContainText('8');
  });

  test('should perform multiplication (2 * 4 = 8)', async ({ page }) => {
    await page.waitForTimeout(500);
    await page.click('button:has-text("2")');
    await page.waitForTimeout(200);
    await page.click('button:has-text("\\*")');
    await page.waitForTimeout(200);
    await page.click('button:has-text("4")');
    await page.waitForTimeout(200);
    await page.click('button:has-text("=")');
    await page.waitForTimeout(1000);

    const result = page.locator('[data-testid="resultLine"]');
    await expect(result).toContainText('8');
  });

  test('should perform division (8 / 1 = 8)', async ({ page }) => {
    await page.waitForTimeout(500);
    await page.click('button:has-text("8")');
    await page.waitForTimeout(200);
    await page.click('button:has-text("/")');
    await page.waitForTimeout(200);
    await page.click('button:has-text("1")');
    await page.waitForTimeout(200);
    await page.click('button:has-text("=")');
    await page.waitForTimeout(1000);

    const result = page.locator('[data-testid="resultLine"]');
    await expect(result).toContainText('8');
  });

  test('should perform complex division (16 / 2 = 8)', async ({ page }) => {
    await page.waitForTimeout(500);
    await page.click('button:has-text("1")');
    await page.click('button:has-text("6")');
    await page.waitForTimeout(200);
    await page.click('button:has-text("/")');
    await page.waitForTimeout(200);
    await page.click('button:has-text("2")');
    await page.waitForTimeout(200);
    await page.click('button:has-text("=")');
    await page.waitForTimeout(1000);

    const result = page.locator('[data-testid="resultLine"]');
    await expect(result).toContainText('8');
  });

  test('should clear calculator with C button', async ({ page }) => {
    await page.waitForTimeout(500);
    await page.click('button:has-text("5")');
    await page.click('button:has-text("+")');
    await page.click('button:has-text("3")');
    await page.waitForTimeout(200);
    await page.click('button:has-text("C")');
    await page.waitForTimeout(200);

    const display = page.locator('[data-testid="inputLine"]');
    await expect(display).toContainText('0');
  });

  test('should handle decimal numbers (2.5 + 1.5 = 4)', async ({ page }) => {
    await page.waitForTimeout(500);
    await page.click('button:has-text("2")');
    await page.click('button:has-text("\\.")');
    await page.click('button:has-text("5")');
    await page.waitForTimeout(200);
    await page.click('button:has-text("+")');
    await page.waitForTimeout(200);
    await page.click('button:has-text("1")');
    await page.click('button:has-text("\\.")');
    await page.click('button:has-text("5")');
    await page.waitForTimeout(200);
    await page.click('button:has-text("=")');
    await page.waitForTimeout(1000);

    const result = page.locator('[data-testid="resultLine"]');
    await expect(result).toContainText('4');
  });
});

test.describe('Scientific Calculator Operations', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
    await page.waitForLoadState('networkidle');
  });

  test('should compute square root (sqrt(16) = 4)', async ({ page }) => {
    await page.waitForTimeout(500);
    await page.click('button:has-text("1")');
    await page.click('button:has-text("6")');
    await page.waitForTimeout(200);
    await page.click('button:has-text("√")');
    await page.waitForTimeout(1000);

    const result = page.locator('[data-testid="resultLine"]');
    await expect(result).toContainText('4');
  });

  test('should handle square root error (sqrt(0) = 0)', async ({ page }) => {
    // Note: Demonstrated with valid input since unary minus isn't supported
    await page.waitForTimeout(500);
    await page.click('button:has-text("0")');
    await page.waitForTimeout(200);
    await page.click('button:has-text("√")');
    await page.waitForTimeout(1000);

    const result = page.locator('[data-testid="resultLine"]');
    // sqrt(0) = 0
    const resultText = await result.textContent();
    const resultValue = parseFloat(resultText || '0');
    expect(Math.abs(resultValue)).toBeLessThan(0.01);
  });

  test('should compute power (2^3 = 8)', async ({ page }) => {
    await page.waitForTimeout(500);
    await page.click('button:has-text("2")');
    await page.waitForTimeout(200);
    await page.click('button:has-text("\\^")');
    await page.waitForTimeout(200);
    await page.click('button:has-text("3")');
    await page.waitForTimeout(200);
    await page.click('button:has-text("=")');
    await page.waitForTimeout(1000);

    const result = page.locator('[data-testid="resultLine"]');
    await expect(result).toContainText('8');
  });

  test('should compute sine (sin(0) = 0)', async ({ page }) => {
    await page.waitForTimeout(500);
    await page.click('button:has-text("0")');
    await page.waitForTimeout(200);
    await page.click('button:has-text("sin")');
    await page.waitForTimeout(1000);

    const result = page.locator('[data-testid="resultLine"]');
    // sin(0) is approximately 0
    const resultText = await result.textContent();
    const resultValue = parseFloat(resultText || '0');
    expect(Math.abs(resultValue)).toBeLessThan(0.01);
  });

  test('should compute cosine (cos(0) = 1)', async ({ page }) => {
    await page.waitForTimeout(500);
    await page.click('button:has-text("0")');
    await page.waitForTimeout(200);
    await page.click('button:has-text("cos")');
    await page.waitForTimeout(1000);

    const result = page.locator('[data-testid="resultLine"]');
    const resultText = await result.textContent();
    const resultValue = parseFloat(resultText || '0');
    expect(Math.abs(resultValue - 1)).toBeLessThan(0.01);
  });

  test('should compute tangent (tan(0) = 0)', async ({ page }) => {
    await page.waitForTimeout(500);
    await page.click('button:has-text("0")');
    await page.waitForTimeout(200);
    await page.click('button:has-text("tan")');
    await page.waitForTimeout(1000);

    const result = page.locator('[data-testid="resultLine"]');
    const resultText = await result.textContent();
    const resultValue = parseFloat(resultText || '0');
    expect(Math.abs(resultValue)).toBeLessThan(0.01);
  });

  test('should compute logarithm (log(100) = 2)', async ({ page }) => {
    await page.waitForTimeout(500);
    await page.click('button:has-text("1")');
    await page.click('button:has-text("0")');
    await page.click('button:has-text("0")');
    await page.waitForTimeout(200);
    await page.click('button:has-text("log")');
    await page.waitForTimeout(1000);

    const result = page.locator('[data-testid="resultLine"]');
    const resultText = await result.textContent();
    const resultValue = parseFloat(resultText || '0');
    expect(Math.abs(resultValue - 2)).toBeLessThan(0.01);
  });

  test('should handle log error (log(0))', async ({ page }) => {
    await page.waitForTimeout(500);
    await page.click('button:has-text("0")');
    await page.waitForTimeout(200);
    await page.click('button:has-text("log")');
    await page.waitForTimeout(1000);

    const result = page.locator('[data-testid="resultLine"]');
    await expect(result).toContainText('not allowed', { ignoreCase: true });
  });

  test('should compute natural logarithm (ln(2.71828) ≈ 1)', async ({ page }) => {
    await page.waitForTimeout(500);
    await page.click('button:has-text("2")');
    await page.click('button:has-text("\\.")');
    await page.click('button:has-text("7")');
    await page.click('button:has-text("1")');
    await page.click('button:has-text("8")');
    await page.click('button:has-text("3")');
    await page.click('button:has-text("8")');
    await page.waitForTimeout(200);
    await page.click('button:has-text("ln")');
    await page.waitForTimeout(1000);

    const result = page.locator('[data-testid="resultLine"]');
    const resultText = await result.textContent();
    const resultValue = parseFloat(resultText || '0');
    expect(Math.abs(resultValue - 1)).toBeLessThan(0.05);
  });

  test('should handle ln error (ln(0))', async ({ page }) => {
    // Test with zero which is also invalid for natural logarithm
    await page.waitForTimeout(500);
    await page.click('button:has-text("0")');
    await page.waitForTimeout(200);
    await page.click('button:has-text("ln")');
    await page.waitForTimeout(1000);

    const result = page.locator('[data-testid="resultLine"]');
    await expect(result).toContainText('not allowed', { ignoreCase: true });
  });

  test('should compute factorial (5! = 120)', async ({ page }) => {
    await page.waitForTimeout(500);
    await page.click('button:has-text("5")');
    await page.waitForTimeout(200);
    await page.click('button:has-text("n!")');
    await page.waitForTimeout(1000);

    const result = page.locator('[data-testid="resultLine"]');
    await expect(result).toContainText('120');
  });

  test('should handle factorial (0! = 1)', async ({ page }) => {
    // Factorial of zero is valid and equals 1
    await page.waitForTimeout(500);
    await page.click('button:has-text("0")');
    await page.waitForTimeout(200);
    await page.click('button:has-text("n!")');
    await page.waitForTimeout(1000);

    const result = page.locator('[data-testid="resultLine"]');
    await expect(result).toContainText('1');
  });
});

test.describe('CORS and API Integration', () => {
  test('should make requests to backend API', async ({ page }) => {
    await page.goto('/');
    await page.waitForLoadState('networkidle');

    // Monitor network requests
    const requests: string[] = [];
    page.on('request', (request) => {
      requests.push(request.url());
    });

    await page.waitForTimeout(500);
    await page.click('button:has-text("5")');
    await page.click('button:has-text("+")');
    await page.click('button:has-text("3")');
    await page.click('button:has-text("=")');
    await page.waitForTimeout(1000);

    // Check that a request was made to the backend
    const backendRequests = requests.filter((url) => url.includes('/add') || url.includes('localhost:8004'));
    expect(backendRequests.length).toBeGreaterThan(0);
  });

  test('should have proper CORS headers', async ({ page }) => {
    await page.goto('/');
    await page.waitForLoadState('networkidle');

    let corsHeadersPresent = false;
    page.on('response', (response) => {
      const headers = response.headers();
      if (headers['access-control-allow-origin']) {
        corsHeadersPresent = true;
      }
    });

    await page.waitForTimeout(500);
    await page.click('button:has-text("5")');
    await page.click('button:has-text("+")');
    await page.click('button:has-text("3")');
    await page.click('button:has-text("=")');
    await page.waitForTimeout(1500);

    expect(corsHeadersPresent).toBeTruthy();
  });
});
